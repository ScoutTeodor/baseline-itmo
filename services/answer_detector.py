import re


def has_answer_options(query: str) -> bool:
    """Определяет наличие пронумерованных вариантов ответа в вопросе"""
    pattern = r'\n\d+\.\s.+'
    return bool(re.search(pattern, query))
