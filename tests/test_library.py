import unittest

from library.book import Book
from library.library import Library


class TestLibrary(unittest.TestCase):
    """
    Набор тестов для проверки функции validate_book_data в классе Library.

    Функция validate_book_data проверяет корректность данных книги и возвращает описание ошибки или None, если данные корректны.
    """

    def setUp(self):
        """
        Метод setUp вызывается перед каждым тестом для инициализации объекта библиотеки.
        """
        self.library = Library("../test_library.json")
        self.library.books = []  # Очищаем список книг для тестов

    def test_add_book_successful(self):
        """
        Тестирует добавление книги в библиотеку.

        Убедитесь, что количество книг увеличивается после добавления.
        """
        error = self.library.add_book("Название книги", "Имя автора", 2024)
        self.assertIsNone(error)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Название книги")

    def test_add_book_empty_fields(self):
        """
        Тест проверки поведения функции при пустых полях.
        """
        error = self.library.add_book("", "", 0)
        self.assertEqual(error, "Укажите название книги, автора и год издания.")
        self.assertEqual(len(self.library.books), 0)

    def test_add_book_partial_empty_fields(self):
        """
        Тест проверки поведения функции при частично заполненных полях.
        """
        error = self.library.add_book("", "автор", 2023)
        self.assertEqual(error, "Все поля (название, автор, год) должны быть заполнены.")
        self.assertEqual(len(self.library.books), 0)

    def test_add_book_invalid_year(self):
        """
        Тест проверки поведения функции при некорректном годе издания.
        """
        error = self.library.add_book("Title", "Author", 999)
        self.assertEqual(error, "Год издания должен быть 4-значным положительным числом и не превышать текущий год.")
        error = self.library.add_book("Title", "Author", 2025)
        self.assertEqual(error, "Год издания должен быть 4-значным положительным числом и не превышать текущий год.")
        self.assertEqual(len(self.library.books), 0)

    def test_title_length(self):
        """
        Тест проверки поведения функции при некорректной длине названия книги.
        """
        error = self.library.add_book("A", "Author", 2024)
        self.assertEqual(error, "Название книги должно содержать от 2 до 200 символов.")
        self.assertEqual(len(self.library.books), 0)
        long_title = "A" * 201
        error = self.library.add_book(long_title, "Author", 2024)
        self.assertEqual(error, "Название книги должно содержать от 2 до 200 символов.")
        self.assertEqual(len(self.library.books), 0)

    def test_author_length(self):
        """
        Тест проверки поведения функции при некорректной длине имени автора.
        """
        error = self.library.add_book("Title", "A", 2024)
        self.assertEqual(error, "Имя автора должно содержать от 2 до 100 символов.")
        self.assertEqual(len(self.library.books), 0)
        long_author = "A" * 101
        error = self.library.add_book("Title", long_author, 2024)
        self.assertEqual(error, "Имя автора должно содержать от 2 до 100 символов.")
        self.assertEqual(len(self.library.books), 0)

    def test_author_contains_digits(self):
        """
        Тест проверки поведения функции при наличии цифр в имени автора.
        """
        error = self.library.add_book("Title", "Author1", 2024)
        self.assertEqual(error, "Имя автора не должно содержать цифры.")
        self.assertEqual(len(self.library.books), 0)

    def test_invalid_characters_in_book_or_author(self):
        """
        Тест проверки поведения функции при наличии недопустимых символов в названии книги или имени автора.
        """
        error = self.library.add_book("Title@", "Author", 2024)
        self.assertEqual(error, "Название книги или имя автора содержит недопустимые символы.")
        self.assertEqual(len(self.library.books), 0)
        error = self.library.add_book("Title", "Auth@r", 2024)
        self.assertEqual(error, "Название книги или имя автора содержит недопустимые символы.")
        self.assertEqual(len(self.library.books), 0)

    def test_duplicate_book(self):
        """
        Тест проверки поведения функции при добавлении книги с дублирующимися названием и автором.
        """
        self.library.books = [Book(1, "Title", "Author", 2024)]
        error = self.library.add_book("Title", "Author", 2024)
        self.assertEqual(error, "Книга с таким названием и автором уже существует в библиотеке.")

    def test_remove_book_successful(self):
        """
        Тестирует удаление книги из библиотеки.
        """
        self.library.add_book("Название книги", "Имя автора", 2024)
        book_id = self.library.books[0].id
        error = self.library.remove_book(book_id)
        self.assertIsNone(error)
        self.assertEqual(len(self.library.books), 0)

    def test_remove_book_invalid_id(self):
        """
        Проверяет поведение метода удаления книги при использовании несуществующего ID.
        """
        error = self.library.remove_book(999)
        self.assertEqual(error, "Ошибка: книги с заданным ID не существует.")

    def test_search_books(self):
        """
        Тестирует поиск книги по заданным критериям.
        """
        self.library.add_book("Название книги", "Имя автора", 2024)
        results = self.library.search_books(title="Название книги")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Название книги")
        self.assertEqual(results[0].author, "Имя автора")
        self.assertEqual(results[0].year, 2024)

    def test_search_books_no_results(self):
        """
        Проверяет, что метод не выполняется при пустых критериях.
        """
        self.library.add_book("Название книги", "Имя автора", 2024)
        results = self.library.search_books(title="Несуществующая книга")
        self.assertEqual(len(results), 0)

    def test_update_status_successful(self):
        """
        Проверяет успешное обновление статуса книги.
        """
        self.library.add_book("Название книги", "Имя автора", 2024)
        book_id = self.library.books[0].id
        error = self.library.update_status(book_id, "выдана")
        self.assertIsNone(error)
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_update_status_invalid_id(self):
        """
        Проверяет поведение метода при попытке обновления статуса книги с несуществующим ID.
        """
        error = self.library.update_status(999, "выдана")
        self.assertEqual(error, "Ошибка: книги с заданным ID не существует.")

    def test_update_status_invalid_status(self):
        """
        Проверяет поведение метода при вводе некорректного статуса.
        """
        self.library.add_book("Название книги", "Имя автора", 2024)
        book_id = self.library.books[0].id
        error = self.library.update_status(book_id, "недоступно")
        self.assertEqual(error, "Статус книги должен быть 'в наличии' или 'выдана'.")

    def test_display_books_empty_library(self):
        """
        Проверяет корректный вывод, когда библиотека пуста.
        """
        books = self.library.display_books()
        self.assertEqual(books, [])

    def test_display_books_with_books(self):
        """
        Проверяет корректный вывод списка книг, если библиотека содержит данные.
        """
        self.library.add_book("Название книги", "Имя автора", 2024)
        books = [book.to_dict() for book in self.library.books]
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], "Название книги")


if __name__ == "__main__":
    unittest.main()
