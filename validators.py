from datetime import datetime
from typing import List, Optional
from library.book import Book


def validate_book_data(title: str, author: str, year: int, books: List[Book]) -> Optional[str]:
    """
    Проверяет данные книги на корректность.

    Возвращает строку с описанием ошибки, если данные некорректны,
    или None, если все проверки пройдены.
    """
    if not title.strip() and not author.strip() and not year:
        return "Укажите название книги, автора и год издания."

    if not title.strip() or not author.strip() or not year:
        return "Все поля (название, автор, год) должны быть заполнены."

    current_year = datetime.now().year

    if not isinstance(year, int) or year <= 0 or year < 1000 or year > current_year:
        return "Год издания должен быть 4-значным положительным числом и не превышать текущий год."

    if len(title) < 2 or len(title) > 200:
        return "Название книги должно содержать от 2 до 200 символов."

    if len(author) < 2 or len(author) > 100:
        return "Имя автора должно содержать от 2 до 100 символов."

    if any(char.isdigit() for char in author):
        return "Имя автора не должно содержать цифры."

    invalid_chars = set("!@#$%^&*()_+=[]{}|;:'\",<>?/\\")
    if any(char in invalid_chars for char in title) or any(char in invalid_chars for char in author):
        return "Название книги или имя автора содержит недопустимые символы."

    if any(book.title.lower() == title.lower() and book.author.lower() == author.lower() for book in books):
        return "Книга с таким названием и автором уже существует в библиотеке."

    return None


def validate_status(status: str) -> Optional[str]:
    """
    Проверяет статус книги на корректность.

    Возвращает строку с описанием ошибки, если данные некорректны,
    или None, если все проверки пройдены.
    """
    if status not in ["в наличии", "выдана"]:
        return "Статус книги должен быть 'в наличии' или 'выдана'."

    return None
