from library.library import Library
from handlers import (handle_add_book, handle_remove_book, handle_search_books, handle_display_books,
                      handle_update_status)


def main():
    library = Library("library.json")

    commands = {
        "1": handle_add_book,
        "2": handle_remove_book,
        "3": handle_search_books,
        "4": handle_display_books,
        "5": handle_update_status,
    }

    while True:
        print("\nДоступные команды:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        command = input("Введите номер команды: ").strip()

        if command == "6":
            print("Выход из программы.")
            break
        elif command in commands:
            commands[command](library)
        else:
            print("Неверная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
