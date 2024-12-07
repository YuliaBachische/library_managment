from typing import Dict


class Book:
    """
    Представляет книгу в библиотеке.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги ("в наличии" или "выдана").
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        """
        Инициализирует новый экземпляр книги.

        Аргументы:
            id (int): Уникальный идентификатор.
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания.
            status (str, optional): Статус книги. По умолчанию "в наличии".
        """
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict:
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: Dict) -> 'Book':
        """Создает экземпляр книги из словаря."""
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])
