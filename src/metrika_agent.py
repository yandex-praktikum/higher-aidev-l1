"""
Шаблон для итогового проекта: агент с 4 tools.

TODO: Реализуйте агента на LangGraph с tools: search_docs, search_tickets, check_service_status, create_ticket.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Literal

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

DOCS_DIR = Path(os.getenv('METRIKA_DOCS_PATH', 'data/docs'))

# Учебные данные из практики 03
TICKETS: list[dict[str, Any]] = [
    {
        'id': 'TICK-1001',
        'title': 'Нет данных в отчётах после установки счётчика',
        'status': 'open',
        'component': 'collection',
        'summary': 'Клиент установил код вчера, отчёты пустые.',
    },
    {
        'id': 'TICK-1002',
        'title': 'Вебвизор не записывает визиты',
        'status': 'open',
        'component': 'webvisor',
        'summary': 'Несколько клиентов за час: вебвизор пустой.',
    },
    {
        'id': 'TICK-1003',
        'title': 'Цели не срабатывают на кнопку',
        'status': 'resolved',
        'component': 'goals',
        'summary': 'Решено: неверный селектор CSS. Проверка _ym_debug=2.',
    },
    {
        'id': 'TICK-1004',
        'title': 'Расхождение с Директом по конверсиям',
        'status': 'open',
        'component': 'reports',
        'summary': 'Разная атрибуция и окна конверсии.',
    },
    {
        'id': 'TICK-1005',
        'title': 'Экспорт отчёта падает по таймауту',
        'status': 'open',
        'component': 'export',
        'summary': 'Массовые жалобы на экспорт за последний час.',
    },
]

COMPONENTS: dict[str, dict[str, str]] = {
    'collection': {'status': 'operational', 'detail': 'Сбор хитов штатно.'},
    'webvisor': {'status': 'degraded', 'detail': 'Пустые записи Вебвизора в части регионов.'},
    'goals': {'status': 'operational', 'detail': 'Цели в норме.'},
    'reports': {'status': 'operational', 'detail': 'Отчёты штатно.'},
    'export': {'status': 'down', 'detail': 'Экспорт недоступен: инцидент.'},
    'api': {'status': 'operational', 'detail': 'API в пределах SLO.'},
}

_CREATED: list[dict[str, Any]] = []


@tool
def search_docs(query: str, top_k: int = 3) -> str:
    """
    Ищет в справке Метрики (snapshot).
    
    Когда вызывать: how-to по установке счётчика, коду, целям, Вебвизору.
    Когда НЕ вызывать: статус сервиса, поиск тикетов, создание тикета.
    """
    # TODO: Реализуйте поиск через MetrikaRAG
    # 1. Используйте MetrikaRAG.index_docs(DOCS_DIR, RagConfig(top_k=top_k))
    # 2. Вызовите rag.retrieve(query, top_k=top_k)
    # 3. Верните JSON с results (path, title, excerpt)
    raise NotImplementedError('Реализуйте tool search_docs')


@tool
def search_tickets(query: str, status: Literal['open', 'resolved', 'any'] = 'open') -> str:
    """
    Ищет похожие учебные тикеты.
    
    Когда вызывать: понять массовость жалобы.
    Когда НЕ вызывать: чистый how-to из документации.
    """
    # TODO: Реализуйте поиск по TICKETS + _CREATED
    # Простой token matching, сортировка по score
    raise NotImplementedError('Реализуйте tool search_tickets')


@tool
def check_service_status(component: str) -> str:
    """
    Учебный статус компонента: collection|webvisor|goals|reports|export|api.
    
    Когда вызывать: подозрение на массовый сбой.
    Когда НЕ вызывать: единичный how-to про установку кода.
    """
    # TODO: Реализуйте проверку статуса через COMPONENTS
    # Верните JSON с component, status, detail
    raise NotImplementedError('Реализуйте tool check_service_status')


@tool
def create_ticket(title: str, component: str, details: str) -> str:
    """
    Создаёт учебный тикет (только запись).
    
    Blast radius минимальный. Звать только если решения нет.
    """
    # TODO: Реализуйте создание тикета
    # Добавьте в _CREATED, верните JSON с created ticket
    raise NotImplementedError('Реализуйте tool create_ticket')


ALL_TOOLS = [search_docs, search_tickets, check_service_status, create_ticket]

SYSTEM_PROMPT = """Ты — агент L1-поддержки Яндекс Метрики.
Работай Thought → Action → Observation. Сначала инструмент, потом ответ клиенту.

How-to про установку/код/цели/Вебвизор — сначала search_docs по справке.
Массовый сбой, таймауты, «у всех», «уже час» — check_service_status и/или search_tickets.
Если status=down/degraded или много open-тикетов — не советуй сразу «почините у себя».
create_ticket — только если решения нет.

Корпус документации учебный. Отвечай кратко по-русски после Observation.
"""


def build_llm() -> ChatOpenAI:
    """Создает LLM client для агента."""
    api_key = os.getenv('LLM_API_KEY', '')
    base_url = os.getenv('LLM_BASE_URL', 'https://api.eliza.yandex.net/raw/openrouter/v1')
    model = os.getenv('LLM_MODEL', 'openai/gpt-oss-20b')
    
    if not api_key or 'ваш_' in api_key:
        raise RuntimeError('Задайте LLM_API_KEY')
    
    return ChatOpenAI(
        api_key=api_key,
        base_url=base_url,
        model=model,
        temperature=0,
        max_tokens=1500,
    )


def build_agent(llm=None):
    """Создает ReAct агента с 4 tools."""
    # TODO: Реализуйте создание агента
    # return create_react_agent(model=llm or build_llm(), tools=ALL_TOOLS, prompt=SYSTEM_PROMPT)
    raise NotImplementedError('Реализуйте функцию build_agent')


def extract_trace(messages) -> list[dict]:
    """Извлекает trace из messages агента."""
    # TODO: Реализуйте извлечение trace
    # trace = [{'event': 'action', 'tool': ..., 'args': ...}, {'event': 'observation', 'content': ...}, ...]
    raise NotImplementedError('Реализуйте функцию extract_trace')


def run_agent(question: str, agent=None) -> dict:
    """
    Запускает агента и возвращает ответ + trace.
    
    Returns:
        {'answer': str, 'trace': list[dict], 'messages': list}
    """
    # TODO: Реализуйте запуск агента
    # 1. graph = agent or build_agent()
    # 2. result = graph.invoke({'messages': [{'role': 'user', 'content': question}]})
    # 3. Извлеките final answer из messages
    # 4. Извлеките trace через extract_trace()
    # 5. Верните {'answer': final_text, 'trace': trace, 'messages': messages}
    raise NotImplementedError('Реализуйте функцию run_agent')


if __name__ == '__main__':
    import sys
    
    q = ' '.join(sys.argv[1:]) or 'Куда поставить код счётчика Яндекс Метрики?'
    out = run_agent(q)
    print(out['answer'])
    print('--- TRACE ---')
    print(json.dumps(out['trace'], ensure_ascii=False, indent=2))
