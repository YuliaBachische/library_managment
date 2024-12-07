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

    def test_add_book(self):
        """
        Тестирует добавление книги в библиотеку.

        Убедитесь, что количество книг увеличивается после добавления.
        """
        print("Тест 'test_add_book' начинается")
        self.library.add_book("Название книги", "Имя автора", 2024)
        self.assertEqual(len(self.library.books), 1)
        print("Тест 'test_add_book' завершен успешно")

    def test_empty_fields(self):
        """
        Тест проверки поведения функции при пустых полях.
        """
        print("Тест 'test_empty_fields' начинается")
        error = self.library.validate_book_data("", "", 0)
        self.assertEqual(error, "Укажите название книги, автора и год издания.")
        print("Тест 'test_empty_fields' завершен успешно")

    def test_partial_empty_fields(self):
        """
        Тест проверки поведения функции при частично заполненных полях.
        """
        print("Тест 'test_partial_empty_fields' начинается")
        error = self.library.validate_book_data("", "Author", 2024)
        self.assertEqual(error, "Все поля (название, автор, год) должны быть заполнены.")
        print("Тест 'test_partial_empty_fields' завершен успешно")

    def test_invalid_year(self):
        """
        Тест проверки поведения функции при некорректном годе издания.
        """
        print("Тест 'test_invalid_year' начинается")
        error = self.library.validate_book_data("Title", "Author", 999)
        self.assertEqual(error, "Год издания должен быть 4-значным положительным числом и не превышать текущий год.")

        error = self.library.validate_book_data("Title", "Author", 2025)
        self.assertEqual(error, "Год издания должен быть 4-значным положительным числом и не превышать текущий год.")
        print("Тест 'test_invalid_year' завершен успешно")

    def test_title_length(self):
        """
        Тест проверки поведения функции при некорректной длине названия книги.
        """
        print("Тест 'test_title_length' начинается")
        error = self.library.validate_book_data("A", "Author", 2024)
        self.assertEqual(error, "Название книги должно содержать от 2 до 200 символов.")

        long_title = "A" * 201
        error = self.library.validate_book_data(long_title, "Author", 2024)
        self.assertEqual(error, "Название книги должно содержать от 2 до 200 символов.")
        print("Тест 'test_title_length' завершен успешно")

    def test_author_length(self):
        """
        Тест проверки поведения функции при некорректной длине имени автора.
        """
        print("Тест 'test_author_length' начинается")
        error = self.library.validate_book_data("Title", "A", 2024)
        self.assertEqual(error, "Имя автора должно содержать от 2 до 100 символов.")

        long_author = "A" * 101
        error = self.library.validate_book_data("Title", long_author, 2024)
        self.assertEqual(error, "Имя автора должно содержать от 2 до 100 символов.")
        print("Тест 'test_author_length' завершен успешно")

    def test_author_contains_digits(self):
        """
        Тест проверки поведения функции при наличии цифр в имени автора.
        """
        print("Тест 'test_author_contains_digits' начинается")
        error = self.library.validate_book_data("Title", "Author1", 2024)
        self.assertEqual(error, "Имя автора не должно содержать цифры.")
        print("Тест 'test_author_contains_digits' завершен успешно")

    def test_invalid_characters(self):
        """
        Тест проверки поведения функции при наличии недопустимых символов в названии книги или имени автора.
        """
        print("Тест 'test_invalid_characters' начинается")
        error = self.library.validate_book_data("Title@", "Author", 2024)
        self.assertEqual(error, "Название книги или имя автора содержит недопустимые символы.")

        error = self.library.validate_book_data("Title", "Auth@r", 2024)
        self.assertEqual(error, "Название книги или имя автора содержит недопустимые символы.")
        print("Тест 'test_invalid_characters' завершен успешно")

    def test_duplicate_book(self):
        """
        Тест проверки поведения функции при добавлении книги с дублирующимися названием и автором.
        """
        print("Тест 'test_duplicate_book' начинается")
        self.library.books = [Book(1, "Title", "Author", 2024)]
        error = self.library.validate_book_data("Title", "Author", 2024)
        self.assertEqual(error, "Книга с таким названием и автором уже существует в библиотеке.")
        print("Тест 'test_duplicate_book' завершен успешно")

    def test_valid_book(self):
        """
        Тест проверки поведения функции при корректных данных книги.
        """
        print("Тест 'test_valid_book' начинается")
        error = self.library.validate_book_data("Valid Title", "Valid Author", 2024)
        self.assertIsNone(error)
        print("Тест 'test_valid_book' завершен успешно")

    def test_remove_book(self):
        """
        Тестирует удаление книги из библиотеки.
        """
        print("Тест 'test_remove_book' начинается")
        self.library.add_book("Название книги", "Имя автора", 2024)
        book_id = self.library.books[0].id
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)
        print("Тест 'test_remove_book' завершен успешно")

    def test_search_books(self):
        """
        Тестирует поиск книги по заданным критериям.
        """
        print("Тест 'test_search_books' начинается")
        self.library.add_book("Название книги", "Имя автора", 2024)
        results = self.library.search_books(title="Название книги")
        if results:
            for book in results:
                print(book.to_dict())
        self.assertEqual(len(results), 1)
        print("Тест 'test_search_books' завершен успешно")

    def test_search_books_with_all_empty_criteria(self):
        """
        Проверяет, что метод не выполняется при пустых критериях.
        """
        print("Тест 'test_search_books_with_empty_criteria' начинается")
        results = self.library.search_books(title="", author="", year=None)
        self.assertEqual(results, [])
        print("Тест 'test_search_books_with_empty_criteria' завершен успешно")

    def test_update_status(self):
        """
        Тестирует обновление статуса книги.
        """
        print("Тест 'test_update_status' начинается")
        self.library.add_book("Название книги", "Имя автора", 2024)
        book_id = self.library.books[0].id
        self.library.update_status(book_id, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")
        print("Тест 'test_update_status' завершен успешно")



if __name__ == "__main__":
    unittest.main()
