def funny():
    print('fun' * 100)


if __name__ == '__main__':
    print('fun.py - запущен по F5 или вручную')
    print()
    funny()
else:
    print('fun.py - запущен через импорт в другой модуль')
    