import unittest
from library.book import Book


class TestBook(unittest.TestCase):
    """
    Набор тестов для проверки класса Book.
    """

    def test_create_book_default_status(self):
        """
        Тест создания книги с использованием значения по умолчанию для статуса.
        """
        print("Тест 'test_create_book_default_status' начинается")
        book = Book(2, "Другой заголовок", "Другой автор", 2021)
        self.assertEqual(book.id, 2)
        self.assertEqual(book.title, "Другой заголовок")
        self.assertEqual(book.author, "Другой автор")
        self.assertEqual(book.year, 2021)
        self.assertEqual(book.status, "в наличии")
        print("Тест 'test_create_book_default_status' завершен успешно")

    def test_to_dict(self):
        """
        Тест метода to_dict, преобразующего объект книги в словарь.
        """
        print("Тест 'test_to_dict' начинается")
        book = Book(3, "Заголовок", "Автор", 2019)
        expected_dict = {
            "id": 3,
            "title": "Заголовок",
            "author": "Автор",
            "year": 2019,
            "status": "в наличии"
        }
        self.assertEqual(book.to_dict(), expected_dict)
        print("Тест 'test_to_dict' завершен успешно")

    def test_from_dict(self):
        """
        Тест метода from_dict, создающего объект книги из словаря.
        """
        print("Тест 'test_from_dict' начинается")
        data = {
            "id": 4,
            "title": "Словарь заголовок",
            "author": "Словарь автор",
            "year": 2020,
            "status": "в наличии"
        }
        book = Book.from_dict(data)
        self.assertEqual(book.id, 4)
        self.assertEqual(book.title, "Словарь заголовок")
        self.assertEqual(book.author, "Словарь автор")
        self.assertEqual(book.year, 2020)
        self.assertEqual(book.status, "в наличии")
        print("Тест 'test_from_dict' завершен успешно")


if __name__ == "__main__":
    unittest.main()
