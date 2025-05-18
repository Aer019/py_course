def change(func):
    print('декоратор скушал имя функции.')
    def inner(inner_number):
        print('вместо оригинала запущена inner функция.')
        return func(inner_number*2)
    return inner


@change
def sub_five(number):
    print('И только тут сработал оригинал')
    return number - 5


@change
def add_five(number):
    print('И только тут сработал оригинал')
    return number + 5

print(add_five(6))
print(sub_five(6))