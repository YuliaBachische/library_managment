# handlers.py
from library.library import Library


def handle_add_book(library: Library):
    """
    Обрабатывает добавление книги в библиотеку.

    Запрашивает у пользователя название, автора и год издания книги.
    Проверяет корректность введенных данных и добавляет книгу в библиотеку.
    Выводит сообщение об успешном добавлении или ошибке.

    Аргументы:
        library (Library): Объект библиотеки для добавления книги.
    """
    title = input("Введите название книги: ").strip()
    author = input("Введите автора книги: ").strip()
    year_input = input("Введите год издания книги: ").strip()
    year = int(year_input) if year_input.isdigit() else year_input

    error = library.add_book(title, author, year)
    if error:
        print(f"Ошибка при добавлении книги: {error}")
    else:
        print(f"Книга '{title}' успешно добавлена.")


def handle_remove_book(library: Library):
    """
    Обрабатывает удаление книги из библиотеки.

    Запрашивает у пользователя ID книги для удаления.
    Проверяет корректность ID и удаляет книгу из библиотеки.
    Выводит сообщение об успешном удалении или ошибке.

    Аргументы:
        library (Library): Объект библиотеки для удаления книги.
    """
    book_id_input = input("Введите ID книги для удаления: ").strip()
    book_id = int(book_id_input) if book_id_input.isdigit() else book_id_input
    error = library.remove_book(book_id)
    if error:
        print(f"Ошибка при удалении книги: {error}")
    else:
        print(f"Книга с ID {book_id} успешно удалена.")


def handle_search_books(library: Library):
    """
    Обрабатывает поиск книг в библиотеке.

    Запрашивает у пользователя критерии поиска (название, автора, год).
    Выполняет поиск книг по заданным критериям и выводит результат.

    Аргументы:
        library (Library): Объект библиотеки для выполнения поиска.
    """
    print("Введите критерии поиска (оставьте поле пустым, если не используется):")
    title = input("Название: ").strip() or None
    author = input("Автор: ").strip() or None
    year = input("Год: ").strip() or None
    criteria = {key: value for key, value in {"title": title, "author": author, "year": year}.items() if value}

    results = library.search_books(**criteria)
    if results:
        print("Найденные книги:")
        for book in results:
            print(book.to_dict())
    else:
        print("Книги не найдены по заданным критериям.")


def handle_display_books(library: Library):
    """
    Отображает все книги в библиотеке.

    Если библиотека пуста, выводит соответствующее сообщение.

    Аргументы:
        library (Library): Объект библиотеки для отображения книг.
    """
    books = library.display_books()
    if books:
        print("Список книг в библиотеке:")
        for book in books:
            print(book)
    else:
        print("Библиотека пуста.")


def handle_update_status(library: Library):
    """
    Обрабатывает обновление статуса книги в библиотеке.

    Запрашивает у пользователя ID книги и новый статус.
    Проверяет корректность данных и обновляет статус книги.
    Выводит сообщение об успешном обновлении или ошибке.

    Аргументы:
        library (Library): Объект библиотеки для обновления статуса книги.
    """
    book_id_input = input("Введите ID книги: ").strip()
    book_id = int(book_id_input) if book_id_input.isdigit() else book_id_input
    new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip().lower()
    error = library.update_status(book_id, new_status)
    if error:
        print(f"Ошибка при обновлении статуса книги: {error}")
    else:
        print(f"Статус книги с ID {book_id} успешно обновлен.")

