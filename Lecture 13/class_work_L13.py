Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = [1,2,3,4]
li += [1,2,3,4]
li
[1, 2, 3, 4, 1, 2, 3, 4]
li * 5
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
st =
SyntaxError: invalid syntax
st = 'stsara'
print(st)
stsara
Summa = 0
for i in li
SyntaxError: expected ':'
for i in li:
    Summa += i

    
summa
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    summa
NameError: name 'summa' is not defined. Did you mean: 'Summa'?
Summa
20



class A:
    def __init__(self, f, b):
        self.f = f
        self.b = b
    def __str__(self):
        return f'A({self.f}, {self.b})'

    
a = A(123, 2353)
a
<__main__.A object at 0x000001FAFCEFECF0>
print(a)
A(123, 2353)





class Singleton:
    pass

s1 = Singleton()
s2 = Singleton()
s1
<__main__.Singleton object at 0x000001FAFCEFEE40>
s2
<__main__.Singleton object at 0x000001FAFCF17C50>
class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('У данного класса может быть только 1 экземпляр')

        
s1 = Singleton()
s1
<__main__.Singleton object at 0x000001FAFCEFEF90>
s2 = Singleton()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s2 = Singleton()
  File "<pyshell#45>", line 7, in __init__
    raise Exception('У данного класса может быть только 1 экземпляр')
Exception: У данного класса может быть только 1 экземпляр
Singleton.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '_Singleton__instance': <__main__.Singleton object at 0x000001FAFCEFEF90>, '__init__': <function Singleton.__init__ at 0x000001FAFD008860>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Singleton' objects>, '__weakref__': <attribute '__weakref__' of 'Singleton' objects>, '__doc__': None})


# Database
# может быть один конекшн
class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise Exception('У данного класса может быть только 1 экземпляр')
    def __repr__(self):
        return f'Соединение с БД {self.database_name}'

    
DatabaseConnection._DatabaseConnection_instance
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    DatabaseConnection._DatabaseConnection_instance
AttributeError: type object 'DatabaseConnection' has no attribute '_DatabaseConnection_instance'. Did you mean: '_DatabaseConnection__instance'?
DatabaseConnection._DatabaseConnection__instance
print(DatabaseConnection._DatabaseConnection__instance)
None
class MultipleDatabaseConnectionError(Exception)
SyntaxError: expected ':'
class MultipleDatabaseConnectionError(Exception):
    pass

class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise MultipleDatabaseConnectionError
    def __repr__(self):
        return f'Соединение с БД {self.database_name}'

    
conn = DatabaseConnection('account_info.db')
conn
Соединение с БД account_info.db
conn1 = DatabaseConnection ('accowqunt_info.db')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    conn1 = DatabaseConnection ('accowqunt_info.db')
  File "<pyshell#66>", line 8, in __init__
    raise MultipleDatabaseConnectionError
MultipleDatabaseConnectionError



# Creator Sub
# Creator - list = [Sub1, Sub2]
# Creator - createpost
# Creator - notifyall


class Creator:
    def __init__(self):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)

        
creator1 = Creator('MyChannel')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    creator1 = Creator('MyChannel')
TypeError: Creator.__init__() takes 1 positional argument but 2 were given
class Creator:
    def __init__(self,name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)

        
creator1 = Creator('MyChannel')
class Creator:
    def __init__(self,name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)

        
creator1 = Creator('MyChannel')
creator1.show_followers()
[]
creator1.follow('Petya')
creator1.follow('Jan')
creator1.show_followers()
['Petya', 'Jan']
class Creator:
    def __init__(self,name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def create_post(self, message):
        print(self.creator_name, 'опубликовал это сообщение:')
        print(message)
        print()

        
creator1 = Creator('MyChannel')
creator1.create_post('Hello')
MyChannel опубликовал это сообщение:
Hello

class Follower:
    def __init__(self, name):
        self.follower_name = name
    def react(self):
        print(self.follower_name, 'лайкает сообщение')
    def __str__(self):
        return f'follower({self.follower_name})
    
SyntaxError: unterminated f-string literal (detected at line 7)
class Follower:
    def __init__(self, name):
        self.follower_name = name
    def react(self):
        print(self.follower_name, 'лайкает сообщение')
    def __str__(self):
        return f'follower({self.follower_name})
    
SyntaxError: unterminated f-string literal (detected at line 7)
class Follower:
    def __init__(self, name):
        self.follower_name = name
    def react(self):
        print(self.follower_name, 'лайкает сообщение')
    def __str__(self):
        return f'follower({self.follower_name})'
    def __repr__(self):
        return f'follower({self.follower_name})'

    
class Creator:
    def __init__(self,name):
        self.sub_list = []
        self.creator_name = name
    def follow(self, follower):
        self.sub_list.append(follower)
    def show_followers(self):
        print(self.sub_list)
    def notify_all(self):
        for follower in self.sub_list:
            follower.react()
    def create_post(self, message):
        print(self.creator_name, 'опубликовал это сообщение:')
        print(message)
        print()
        self.notify_all()

        
creator1 = Creator('MyChannel')
f1 = Follower('Petya')
f2 = Follower('Dimas')
f3 = Follower('Kolyan')
creator1.show_followers
<bound method Creator.show_followers of <__main__.Creator object at 0x000001FAFCEFF380>>
creator1.create_post('run run run')
MyChannel опубликовал это сообщение:
run run run

creator1.follow(f1)
creator1.show_followers()
[follower(Petya)]
creator1.create_post('run run run')
MyChannel опубликовал это сообщение:
run run run

Petya лайкает сообщение
creator1.follow(f3)
creator1.create_post('run run run')
MyChannel опубликовал это сообщение:
run run run

Petya лайкает сообщение
Kolyan лайкает сообщение
creator1.follow(f2)
creator1.create_post('run run run')
MyChannel опубликовал это сообщение:
run run run

Petya лайкает сообщение
Kolyan лайкает сообщение
Dimas лайкает сообщение


def add_five(number):
    return number + 5

add_five(4)
9


def change(func):
    def inner(inner_number):
        pass
    return inner

@change
def add_five(number):
    return number + 5

add_five(5)
def change(func):
    def inner(inner_number):
        return func(inner_number*2)
    return inner

@change
def add_five(number):
    return number + 5

add_five(5)
15


def change(func):
    print('декоратор скушал имя функции.')
    def inner(inner_number):
        print('вместо оригинала запущена inner функция.')
        return func(inner_number*2)
    return inner


@change
def add_five(number):
    print('Примеры разборов ДЗ лекция 13')
    return number + 5

декоратор скушал имя функции.
add_five
<function change.<locals>.inner at 0x000001FAFD009760>
add_five(3)
вместо оригинала запущена inner функция.
Примеры разборов ДЗ лекция 13
11
def sub_five(number):
    print('И только тут сработал оригинал')
    return number - 5

sub_five(5)
И только тут сработал оригинал
0


@change
def sub_five(number):
    print('И только тут сработал оригинал')
    return number - 5

декоратор скушал имя функции.


@change
def add_five(number):
    print('И только тут сработал оригинал')
    return number + 5

декоратор скушал имя функции.





# file + try + exce +fin

import os
os.getcwd()
'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313'
fstream = open('my_first_txt_file.txt', 'w')
>>> try:
...     fstream.write('1 Привет мир!\n')
...     fstream.write('2 Привет мир!\n')
...     fstream.write('3 Привет мир!\n')
...     fstream.write('4 Привет мир!\n')
...     fstream.write('5 Привет мир!\n')
...     fstream.write('6 Привет мир!\n')
... except:
...     print('up')
... finally:
...     fstream.close()
... 
...     
14
14
14
14
14
14
>>> 
>>> 
>>> fstream.write('1 Привет мир!\n')
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    fstream.write('1 Привет мир!\n')
ValueError: I/O operation on closed file.
>>> 
>>> 
>>> os.getcwd()
'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python313'
>>> 
>>> 
>>> with open('my_second_txt_file.txt', 'w') as fstream:
...     fstream.write('1 Привет мир!\n')
...     fstream.write('2 Привет мир!\n')
...     fstream.write('3 Привет мир!\n')
...     fstream.write('4 Привет мир!\n')
...     fstream.write('5 Привет мир!\n')
...     fstream.write('6 Привет мир!\n')
... 
14
14
14
14
14
14
