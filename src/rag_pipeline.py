"""
Шаблон для итогового проекта: RAG с классовой архитектурой.

TODO: Реализуйте класс MetrikaRAG с методами index_docs(), retrieve(), generate().
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

# Цена в курсе: 0,1 ₽ за 1000 токенов (вход + выход).
PRICE_PER_1K_RUB = 0.1

# Путь до выгрузки документации Яндекс Метрики
DEFAULT_DOCS_DIR = Path(os.getenv('METRIKA_DOCS_PATH', 'data/docs'))

# Тестовые вопросы для smoke test
GOLDEN_QA = [
    {
        'id': 'q1',
        'question': 'Куда поставить код счётчика Яндекс Метрики?',
        'relevant_paths': [
            'ru/troubleshooting/install-tag.md',
            'ru/general/creating-counter.md',
            'ru/quick-start.md',
            'ru/code/install',
        ],
    },
    {
        'id': 'q2',
        'question': 'Как проверить, что счётчик установлен корректно?',
        'relevant_paths': [
            'ru/general/check-counter.md',
            'ru/troubleshooting/install-tag.md',
            'ru/quick-start.md',
        ],
    },
    {
        'id': 'q3',
        'question': 'Что такое Вебвизор?',
        'relevant_paths': ['ru/webvisor', 'ru/general/counter-webvisor.md'],
    },
    {
        'id': 'q4',
        'question': 'Как создать цель в Метрике?',
        'relevant_paths': [
            'ru/general/goal',
            'ru/general/choose-goal.md',
            'ru/simple-goal',
            'ru/integrated-goal',
            'ru/general/goals.md',
        ],
    },
    {
        'id': 'q5',
        'question': 'Почему в отчётах нет данных после установки счётчика?',
        'relevant_paths': [
            'ru/troubleshooting',
            'ru/general/check-counter.md',
            'ru/general/sources-qanda.md',
        ],
    },
]


def precision_at_k(retrieved_paths: list[str], relevant_paths: set[str], k: int) -> float:
    """
    Precision@k для оценки качества retrieval.
    
    Найденный путь засчитывается, если он:
    - точно совпадает с relevant_path, ИЛИ
    - является его префиксом (ru/webvisor → ru/webvisor/info.md)
    
    Args:
        retrieved_paths: Список путей из sources (например, ['ru/webvisor/info.md', 'ru/quick-start.md'])
        relevant_paths: Множество релевантных путей (например, {'ru/webvisor', 'ru/general/counter-webvisor.md'})
        k: Количество top результатов для оценки
    
    Returns:
        float в [0, 1] — доля релевантных среди top-k
    """
    top_k = retrieved_paths[:k]
    if not top_k:
        return 0.0
    
    def is_hit(path: str) -> bool:
        """Проверяет, что path релевантен (точное совпадение или префикс)."""
        return any(
            path == r or path.startswith(r.rstrip('/') + '/')
            for r in relevant_paths
        )
    
    hits = sum(1 for p in top_k if is_hit(p))
    return hits / min(k, len(top_k))


@dataclass
class RagConfig:
    """Конфигурация RAG pipeline."""
    chunk_size: int = 4000
    top_k: int = 3


class MetrikaRAG:
    """RAG для справки Яндекс Метрики (BM25 + metadata boost)."""
    
    def __init__(self, docs_dir: Path = DEFAULT_DOCS_DIR, config: RagConfig | None = None):
        """
        Args:
            docs_dir: Путь до документации (metrica-docs-snapshot/docs)
            config: Конфигурация (chunk_size, top_k)
        """
        self.docs_dir = docs_dir
        self.config = config or RagConfig()
        # TODO: Инициализируйте структуры для хранения chunks и BM25 индекса
        raise NotImplementedError('Реализуйте __init__')
    
    @classmethod
    def index_docs(cls, docs_dir: Path, config: RagConfig | None = None) -> 'MetrikaRAG':
        """
        Офлайн-индексация документации.
        
        1. Рекурсивно читает все *.md файлы из docs_dir
        2. Разбивает на чанки (по абзацам, max chunk_size символов)
        3. Строит BM25 индекс
        
        Args:
            docs_dir: Путь до документации
            config: Конфигурация
        
        Returns:
            Проиндексированный MetrikaRAG
        """
        # TODO: Реализуйте индексацию
        raise NotImplementedError('Реализуйте метод index_docs')
    
    def retrieve(self, query: str, top_k: int | None = None) -> list[dict]:
        """
        Поиск top-k релевантных чанков.
        
        1. BM25 ранжирование по тексту чанка
        2. Бонус за совпадение токенов query с path и title
        3. Дедупликация по path (берем лучший чанк на документ)
        
        Args:
            query: Вопрос пользователя
            top_k: Количество результатов (default: self.config.top_k)
        
        Returns:
            list[dict] с полями: path, title, text, score
        """
        # TODO: Реализуйте retrieval
        raise NotImplementedError('Реализуйте метод retrieve')
    
    def generate(self, query: str, top_k: int | None = None) -> dict:
        """
        Полный RAG: Retrieval + Augmentation + Generation.
        
        1. retrieve(query, top_k) → chunks
        2. Собрать промпт: system + CONTEXT (chunks) + QUESTION
        3. Вызвать LLM (OpenAI-совместимый клиент)
        4. Вернуть answer, sources (пути), cost_rub
        
        Args:
            query: Вопрос пользователя
            top_k: Количество источников
        
        Returns:
            {
                'answer': str,           # Ответ модели
                'sources': list[str],    # Пути файлов (top-k)
                'cost_rub': float        # Стоимость запроса
            }
        """
        # TODO: Реализуйте generation
        raise NotImplementedError('Реализуйте метод generate')
