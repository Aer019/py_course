teams = {}


def add_team():
    """Данная функция добавляет новую команду в словарь teams, запрашивая у пользователя данные."""
    name = input("Введите название команды: ")
    if name in teams:
        print("Команда уже существует.")
        return
    city = input("Введите город команды: ")
    year = input("Введите год основания команды: ")
    players = input("Введите игроков (через запятую): ").split(',')

    teams[name] = {
        'город': city,
        'год основания': year,
        'игроки': [player for player in players]
    }
    print(f"Команда {name} успешно добавлена.")



def show_teams():
    """Данная функция выводит список всех сохранённых команд с подробной информацией."""
    if not teams:
        print("Нет сохранённых команд.")
        return
    for name, info in teams.items():
        print(f"\nНазвание: {name}")
        print(f"Город: {info['город']}")
        print(f"Год основания: {info['год основания']}")
        print(f"Игроки: {', '.join(info['игроки'])}")



def delete_team():
    """Данная функция удаляет команду из словаря по имени."""
    name = input("Введите название команды для удаления: ")
    if name in teams:
        del teams[name]
        print(f"Команда '{name}' удалена.")
    else:
        print("Команда не найдена.")



def edit_team():
    """Данная функция позволяет внести изменения в уже существующую команду."""
    name = input("Введите название команды для редактирования: ")
    if name not in teams:
        print("Команда не найдена.")
        return

    print("\nЧто вы хотите изменить?")
    print("1. Название")
    print("2. Город")
    print("3. Год основания")
    print("4. Игроков")
    choice_for_edit = input("Выбор (1-4): ")

    if choice_for_edit == '1':
        new_name = input("Введите новое название: ")
        if new_name in teams:
            print("Команда c таким названием уже существует.")
        else:
            teams[new_name] = teams.pop(name)
            print("Название команды изменено.")
    elif choice_for_edit == '2':
        new_city = input("Введите новый город: ")
        teams[name]['город'] = new_city
        print("Город обновлён.")
    elif choice_for_edit == '3':
        new_year = input("Введите новый год основания: ")
        teams[name]['год основания'] = new_year
        print("Год основания обновлён.")
    elif choice_for_edit == '4':
        new_players = input("Введите новый список игроков (через запятую): ").split(',')
        teams[name]['игроки'] = [player for player in new_players]
        print("Список игроков обновлён.")
    else:
        print("Неверный выбор.")
