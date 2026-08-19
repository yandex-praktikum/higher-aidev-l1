"""
Шаблон для итогового проекта: context budget из практики 01.

TODO: Реализуйте управление бюджетом контекста (ContextBudget, build_context, inspect_context).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ContextBudget:
    """
    Бюджет слотов контекста.
    
    Каждый слот может содержать:
    - system_instruction: инструкция для модели
    - memory_retrieval: релевантные записи из памяти сессий
    - rag_context: документация из справки
    - current_question: текущий вопрос клиента
    """
    system_instruction: int = 400   # макс. токенов для system
    memory_retrieval: int = 1200    # макс. токенов для memory
    rag_context: int = 2500         # макс. токенов для RAG
    current_question: int = 200     # макс. токенов для question


def build_context(
    system_instruction: str = '',
    memory_retrieval: str = '',
    rag_context: str = '',
    current_question: str = '',
) -> dict[str, str]:
    """
    Собирает контекст из 4 слотов.
    
    Args:
        system_instruction: Инструкция для агента
        memory_retrieval: Записи из памяти сессий
        rag_context: Документация из справки
        current_question: Текущий вопрос
    
    Returns:
        dict с 4 слотами
    """
    # TODO: Реализуйте сборку контекста
    raise NotImplementedError('Реализуйте функцию build_context')


def inspect_context(context: dict[str, str]) -> dict:
    """
    Инспекция контекста: считает токены в каждом слоте.
    
    Args:
        context: Контекст для анализа
    
    Returns:
        {
            'system_instruction_tokens': int,
            'memory_retrieval_tokens': int,
            'rag_context_tokens': int,
            'current_question_tokens': int,
            'total_tokens': int
        }
    """
    # TODO: Реализуйте инспекцию
    raise NotImplementedError('Реализуйте функцию inspect_context')
