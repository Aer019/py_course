# CRUD
# Create - Add
# Read - Show
# Delete


def Add(data):
    print(data, 'was created!')


def Show(data):
    print('Show data:!')
    print(data)


def Delete(data):
    print(data, 'was removed!')


if __name__ == '__main__':
    print('sport_data_logic.py - запущен по F5 или вручную')
    print()
    test_data = 'asdasdasd'
    Add(test_data)
    Show(test_data)
    Delete(test_data)
else:
    print('sport_data_logic.py - запущен через импорт в другой модуль')
