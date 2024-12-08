import json
from typing import List, Optional

from validators import validate_book_data, validate_status, validate_book_id
from .book import Book


class Library:
    """
    Управляет коллекцией книг в библиотеке.

    """

    def __init__(self, data_file: str):
        """
        Инициализирует библиотеку с указанным файлом данных.

        Аргументы:
            data_file (str): Путь к файлу, содержащему данные о книгах.
            books (List[Book]): Список книг в библиотеке.
        """
        self.data_file = data_file
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        """Загружает книги из JSON-файла."""
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                return [Book.from_dict(book) for book in json.load(file)]
        except FileNotFoundError:
            return []

    def save_books(self):
        """Сохраняет текущий список книг в JSON-файл."""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def get_book_by_id(self, book_id: int) -> Book:
        """Возвращает книгу по её ID или None, если книга не найдена."""
        return next((book for book in self.books if book.id == book_id))

    def add_book(self, title: str, author: str, year: int) -> Optional[str]:
        """Добавляет новую книгу в библиотеку, если данные корректны."""
        validation_error = validate_book_data(title, author, year, self.books)
        if validation_error:
            return validation_error
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        return None

    def remove_book(self, book_id: int) -> Optional[str]:
        """Удаляет книгу из библиотеки по её ID. Возвращает True, если удаление успешно, иначе False."""
        validation_error = validate_book_id(book_id, self.books)
        if validation_error:
            return validation_error
        else:
            book = self.get_book_by_id(book_id)
            self.books.remove(book)
            self.save_books()
            return None

    def search_books(self, **criteria) -> List[Book]:
        """Ищет книги, соответствующие заданным критериям."""
        if not any(criteria.values()):
            return []

        results = self.books
        for key, value in criteria.items():
            if value is not None:
                results = [book for book in results if str(getattr(book, key)).lower() == str(value).lower()]

        return results

    def update_status(self, book_id: int, new_status: str) -> Optional[str]:
        """Обновляет статус книги по её ID. Возвращает True, если обновление успешно, иначе False."""
        validation_error = validate_book_id(book_id, self.books)
        if validation_error:
            return validation_error
        else:
            book = self.get_book_by_id(book_id)
            status_error = validate_status(new_status)
            if status_error:
                return status_error
            else:
                book.status = new_status
                self.save_books()
                return None

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            return []
        else:
            for book in self.books:
                return book.to_dict()
