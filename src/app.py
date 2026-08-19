"""
Шаблон для итогового проекта: главная склейка app.py.

TODO: Реализуйте функции guardrail() и handle() согласно заданию.
"""

from __future__ import annotations


def guardrail(answer: str, trace: list[dict]) -> str:
    """
    Защита от вины клиента при инциденте.
    
    Если в trace был status=down и ответ содержит 
    «переустановите код», «почините у себя», «ошибка на вашей стороне» —
    заменить на сообщение про инцидент и эскалацию.
    
    Args:
        answer: Ответ агента клиенту
        trace: Список действий агента (action/observation)
    
    Returns:
        Безопасный ответ (исправленный или оригинальный)
    """
    # TODO: Реализуйте логику guardrail
    # 1. Проверьте trace на наличие observation с "status": "down"
    # 2. Если saw_down=True и answer матчит паттерн обвинения клиента → замените ответ
    raise NotImplementedError('Реализуйте функцию guardrail')


def handle(question: str) -> dict:
    """
    Главный entry point: context budget → agent → guardrail.
    
    Args:
        question: Вопрос клиента
    
    Returns:
        {
            'answer': str,           # Ответ клиенту (после guardrail)
            'trace': list[dict],     # Действия агента
            'budget_report': dict    # Инспекция контекста
        }
    """
    # TODO: Реализуйте полную склейку:
    # 1. build_context() → ctx
    # 2. inspect_context(ctx) → budget_report
    # 3. run_agent(question) → agent_out
    # 4. guardrail(agent_out['answer'], agent_out['trace']) → safe_answer
    # 5. return {'answer': safe_answer, 'trace': agent_out['trace'], 'budget_report': budget_report}
    raise NotImplementedError('Реализуйте функцию handle')


if __name__ == '__main__':
    import json
    import sys
    
    q = ' '.join(sys.argv[1:]) or 'У многих падает экспорт отчётов час. Что делать?'
    print(json.dumps(handle(q), ensure_ascii=False, indent=2)[:4000])
