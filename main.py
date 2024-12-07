from library.library import Library


def main():
    """
    Главная функция для взаимодействия с пользователем и выполнения команд управления библиотекой.
    """
    library = Library("library.json")

    while True:
        print("\nДоступные команды:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        command = input("Введите номер команды: ").strip()

        if command == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            year_input = input("Введите год издания книги: ").strip()

            if year_input.isdigit():
                year = int(year_input)
            else:
                year = year_input

            library.add_book(title, author, year)

        elif command == "2":
            book_id_input = input("Введите ID книги для удаления: ").strip()
            if book_id_input.isdigit():
                book_id = int(book_id_input)
            else:
                book_id = book_id_input
            library.remove_book(book_id)

        elif command == "3":
            print("Введите критерии поиска (оставьте поле пустым, если не используется):")
            title = input("Название: ").strip() or None
            author = input("Автор: ").strip() or None
            year = input("Год: ").strip() or None

            criteria = {key: value for key, value in {"title": title, "author": author, "year": year}.items() if value}
            results = library.search_books(**criteria)

            if results:
                for book in results:
                    print(book.to_dict())

        elif command == "4":
            library.display_books()

        elif command == "5":
            book_id_input = input("Введите ID книги: ")
            if book_id_input.isdigit():
                book_id = int(book_id_input)
            else:
                book_id = book_id_input
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip().lower()
            library.update_status(book_id, new_status)

        elif command == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
