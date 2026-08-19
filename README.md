# L1-агент для Яндекс Метрики

Итоговый проект по промпт-инженерингу: агент с context budget, RAG и guardrail.

## Установка

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export LLM_API_KEY=your_key
export LLM_BASE_URL=https://api.eliza.yandex.net/raw/openrouter/v1
export LLM_MODEL=openai/gpt-oss-20b
export METRIKA_DOCS_PATH=data/docs
```

## Запуск

```bash
# Автотесты
pytest tests/test_final.py -v

# Вручную
python src/app.py "У многих падает экспорт отчётов час. Что делать?"
```

## Структура

- `src/context_pipeline.py` — управление бюджетом контекста (из практики 01)
- `src/rag_pipeline.py` — класс `MetrikaRAG` с BM25 индексом, retrieval, generation (расширенная версия практики 02)
- `src/metrika_agent.py` — LangGraph ReAct с 4 tools
- `src/app.py` — главная склейка: context → agent → guardrail
- `tests/test_final.py` — автотесты
- `report.md` — архитектура + trade-offs
