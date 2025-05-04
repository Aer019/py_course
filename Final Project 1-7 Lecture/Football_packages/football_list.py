from Football_packages.functions import add_team, show_teams, delete_team, edit_team


def menu():
    """Данная функция запускает меню с набором действий для пользователя"""
    while True:
        print("\n--- Меню программы ---")
        print("1. Добавить команду")
        print("2. Показать команды")
        print("3. Удалить команду")
        print("4. Изменить данные команды")
        print("5. Выход")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            add_team()
        elif choice == '2':
            show_teams()
        elif choice == '3':
            delete_team()
        elif choice == '4':
            edit_team()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Ошибка. Необходимо ввести цифру от 1 до 5.")
