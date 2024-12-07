import json
from datetime import datetime
from typing import List
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

    def validate_book_data(self, title: str, author: str, year: int) -> str:
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

        if any(book.title.lower() == title.lower() and book.author.lower() == author.lower() for book in self.books):
            return "Книга с таким названием и автором уже существует в библиотеке."

        return None

    def add_book(self, title: str, author: str, year: int):
        """Добавляет новую книгу в библиотеку, если данные корректны."""
        validation_error = self.validate_book_data(title, author, year)
        if validation_error:
            print(validation_error)
            return
        new_id = max((book.id for book in self.books), default=0) + 1
        new_book = Book(new_id, title, author, year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга добавлена: {new_book.to_dict()}")

    def is_valid_book_id(self, book_id: int):
        """Проверяет, что ID книги является числом."""
        if not isinstance(book_id, int):
            print("Ошибка: ID книги должен быть числом.")
            return

    def remove_book(self, book_id: int):
        """Удаляет книгу из библиотеки по её ID."""
        self.is_valid_book_id(book_id)
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с id {book_id} удалена.")
                return
        print(f"Книга с id {book_id} не найдена.")

    def search_books(self, **criteria) -> List[Book]:
        """Ищет книги, соответствующие заданным критериям."""
        if not any(criteria.values()):
            print("Поиск невозможен. Укажите хотя бы один критерий.")
            return []

        results = self.books
        for key, value in criteria.items():
            # Преобразуем значение к строке и сравниваем в нижнем регистре
            if value is not None:  # Проверка, что значение не None
                results = [book for book in results if str(getattr(book, key)).lower() == str(value).lower()]
            else:
                results = [book for book in results if getattr(book, key) is None]

        if not results:
            print("Книга с заданными параметрами не найдена.")

        return results

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
            return
        else:
            for book in self.books:
                print(book.to_dict())

    def update_status(self, book_id: int, new_status: str):
        """Обновляет статус книги по её ID."""
        self.is_valid_book_id(book_id)
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print(f"Статус книги с id {book_id} обновлен на '{new_status}'.")
                else:
                    print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")
                return
        print(f"Книга с id {book_id} не найдена.")



