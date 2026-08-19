"""
Автотесты для итогового проекта L1-агент.

ОБЯЗАТЕЛЬНЫЕ переменные окружения:
    export LLM_API_KEY=your_yandex_llm_key
    export LLM_BASE_URL=https://api.eliza.yandex.net/raw/openrouter/v1
    export LLM_MODEL=openai/gpt-oss-20b
    export METRIKA_DOCS_PATH=/absolute/path/to/metrica-docs-snapshot/docs

Запуск:
    pytest tests/test_final.py -v
"""

import json
import os
import re
from pathlib import Path

import pytest

from src.app import guardrail, handle
from src.context_pipeline import ContextBudget, build_context, inspect_context, trim_to_budget
from src.rag_pipeline import GOLDEN_QA, MetrikaRAG, RagConfig, precision_at_k


DOCS = Path(os.getenv('METRIKA_DOCS_PATH', 'data/docs'))


def test_docs_present():
    """Документация распакована."""
    assert DOCS.exists() and any(DOCS.rglob('*.md')), 'Распакуйте metrica-docs-snapshot.zip'


def test_context_budget_still_works():
    """Context budget работает: build, trim, inspect."""
    ctx = build_context(
        system_instructions='sys',
        memory_retrieval='mem',
        tool_results='tools',
        conversation_history='h' * 5000,
        budget=ContextBudget(conversation_history=100),
    )
    report = inspect_context(ctx)
    assert report['heaviest_component'] in {
        'conversation_history',
        'system_instructions',
        'memory_retrieval',
        'tool_results',
    }
    
    tight = ContextBudget(
        system_instructions=40,
        memory_retrieval=40,
        tool_results=40,
        conversation_history=80,
    )
    trimmed = trim_to_budget(
        build_context(
            system_instructions='x' * 400,
            memory_retrieval='y' * 400,
            tool_results='z' * 400,
            conversation_history='h' * 2000,
            budget=ContextBudget(
                system_instructions=2000,
                memory_retrieval=2000,
                tool_results=2000,
                conversation_history=2000,
            ),
        ),
        tight,
    )
    assert inspect_context(trimmed)['total_input_tokens'] <= tight.total_input_limit


def test_rag_precision_smoke():
    """RAG: mean precision@3 >= 0.4 на GOLDEN_QA."""
    rag = MetrikaRAG.index_docs(DOCS, RagConfig(top_k=3))
    scores = [
        precision_at_k(
            [h['path'] for h in rag.retrieve(case['question'], top_k=3)],
            set(case['relevant_paths']),
            k=3,
        )
        for case in GOLDEN_QA
    ]
    mean_p = sum(scores) / len(scores)
    assert mean_p >= 0.4, f'Mean precision@3 = {mean_p:.3f}, требуется >= 0.4'


def test_guardrail_blocks_blame_client_when_down():
    """Guardrail блокирует вину клиента при status=down."""
    trace = [
        {
            'event': 'observation',
            'tool': 'check_service_status',
            'content': json.dumps({'component': 'export', 'status': 'down'}),
        }
    ]
    bad = 'Переустановите код у себя — ошибка на вашей стороне.'
    fixed = guardrail(bad, trace)
    assert 'инцидент' in fixed.lower() or 'status=down' in fixed.lower() or 'эскал' in fixed.lower()
    assert 'переустановите код у себя' not in fixed.lower()


def _require_live():
    key = os.getenv('LLM_API_KEY') or ''
    model = os.getenv('LLM_MODEL') or ''
    assert key and model and 'ваш_' not in key, 'Нужны LLM_API_KEY и LLM_MODEL для зачёта'


def _tools(out: dict) -> set[str]:
    return {s.get('tool') for s in out['trace'] if s.get('event') == 'action'}


def test_case_howto_counter_uses_docs():
    """Кейс A: how-to — search_docs + ответ про код/страницу."""
    _require_live()
    out = handle(
        'По документации: куда поставить код счётчика Яндекс Метрики? '
        'Сначала найди фрагмент через search_docs, потом ответь кратко.'
    )
    assert out['answer'] and 'budget_report' in out
    assert 'search_docs' in _tools(out), f'search_docs не вызван, tools: {_tools(out)}'
    text = out['answer'].lower()
    assert any(w in text for w in ('код', 'счетчик', 'счётчик', 'страниц', 'head'))


def test_case_export_incident_not_blame_client():
    """Кейс B: инцидент экспорта — status/tickets; нельзя винить клиента при down."""
    _require_live()
    out = handle('У многих клиентов час падает экспорт отчётов. Что проверить?')
    assert out['answer']
    tools_used = _tools(out)
    assert tools_used & {'check_service_status', 'search_tickets', 'search_docs'}, \
        f'Нет нужных tools, использованы: {tools_used}'
    text = out['answer'].lower()
    blame = re.search(r'переустановите код|ошибка на вашей стороне|почините у себя', text)
    if blame:
        assert 'инцидент' in text or 'status=down' in text or 'эскал' in text


def test_trace_format():
    """Trace имеет правильный формат."""
    _require_live()
    out = handle('Что такое Вебвизор?')
    assert isinstance(out['trace'], list)
    for step in out['trace']:
        assert step.get('event') in {'action', 'observation'}
        if step['event'] == 'action':
            assert 'tool' in step


def test_budget_report_format():
    """budget_report имеет правильный формат."""
    _require_live()
    out = handle('Как создать цель?')
    report = out['budget_report']
    assert 'total_input_tokens' in report
    assert 'per_component_tokens' in report
    assert 'heaviest_component' in report


def test_all_tools_registered():
    """Все 4 tools зарегистрированы в агенте."""
    from src.metrika_agent import ALL_TOOLS
    
    tool_names = {t.name for t in ALL_TOOLS}
    assert tool_names == {'search_docs', 'search_tickets', 'check_service_status', 'create_ticket'}
