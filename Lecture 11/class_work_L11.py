Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}"

    
User.get_u_counter()
'User.user_counter = 0'

u1 = User('Vasia', 77)
User.get_u_counter()
'User.user_counter = 1'
u2 = User('Vasia', 77)
u3 = User('Vasia', 77)
User.get_u_counter()
'User.user_counter = 3'
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}"
    @classmethod
    def job(cls):
        return cls.user_counter ** 2 / 2

    
u1 = User('Vasia', 77)
User.get_u_counter()
'User.user_counter = 1'
User.job()
0.5
class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = n
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}"
    @classmethod
    def job(cls):
        return cls.user_counter ** 2 / 2
    @classmethod
    def ch_u_count(cls, new_value):
        cls.user_counter = new_value

        
User.get_u_counter()
'User.user_counter = 0'
User.ch_u_count(7777)
User.get_u_counter()
'User.user_counter = 7777'


User.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'user_counter': 7777, '__init__': <function User.__init__ at 0x000002A7FD702480>, '__repr__': <function User.__repr__ at 0x000002A7FD702B60>, 'get_u_counter': <classmethod(<function User.get_u_counter at 0x000002A7FD702C00>)>, 'job': <classmethod(<function User.job at 0x000002A7FD702CA0>)>, 'ch_u_count': <classmethod(<function User.ch_u_count at 0x000002A7FD702D40>)>, '__static_attributes__': ('age', 'name'), '__dict__': <attribute '__dict__' of 'User' objects>, '__weakref__': <attribute '__weakref__' of 'User' objects>, '__doc__': None})
help(User)
Help on class User in module __main__:

class User(builtins.object)
 |  User(n, a)
 |
 |  Methods defined here:
 |
 |  __init__(self, n, a)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  ch_u_count(new_value)
 |
 |  get_u_counter()
 |
 |  job()
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  user_counter = 7777



class User:
    user_counter = 0
    def __init__(self, n, a):
        self.name = User.name_checker(n)
        self.age = a
        User.user_counter += 1
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    @classmethod
    def get_u_counter(cls):
        return f"User.user_counter = {cls.user_counter}"
    @classmethod
    def job(cls):
        return cls.user_counter ** 2 / 2
    @classmethod
    def ch_u_count(cls, new_value):
        cls.user_counter = new_value
    @staticmethod
    def name_checker(user_name):
        if len(user_name) < 3:
            return user_name * 4
        return user_name

    
u1 = User('Ag', 5)
u1
User(AgAgAgAg, 5)
u2 = User('Kate', 5666)
u2
User(Kate, 5666)


name = "Fa"
name = User.name_checker(name)
name
'FaFaFaFa'
u1 = User(name, 44)
u1
User(FaFaFaFa, 44)


# Export
# python data --> txt, csv, xml
import ABC, abstractmethod
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    import ABC, abstractmethod
ModuleNotFoundError: No module named 'ABC'

class ExportTXT(Export):
    def __init__(self, data):
        self.data = data
    def preparation(self):
        return self.data.upper()
    def export_prep_data(self):
        return 'export txt' + self.preparation()

    
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    class ExportTXT(Export):
NameError: name 'Export' is not defined
txt = ExportTXT('asdasd')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    txt = ExportTXT('asdasd')
NameError: name 'ExportTXT' is not defined




# 3 classes
# A(object)
# B(A)
# C(B)
# class var, inst var, method
class A:
    a = 1
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B(A):
    b = 2
    def __init__(self):
        self.bb = 22
    def fun_a(self):
        return "fun_b"

    
class C(B):
    c = 3
    def __init__(self):
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
class B(A):
    b = 2
    def __init__(self):
        self.bb = 22
    def fun_b(self):
        return "fun_b"

    
class C(B):
    c = 3
    def __init__(self):
        self.cc = 33
    def fun_c(self):
        return "fun_c"

    
c_inst = C()
c_inst.cc
33
c_inst.c
3
c_inst.fun_c()
'fun_c'
c_inst.b
2
c_inst.bb
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    c_inst.bb
AttributeError: 'C' object has no attribute 'bb'
c_inst.fun_b()
'fun_b'
c_inst,a
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    c_inst,a
NameError: name 'a' is not defined
c_inst.a
1


c_inst.fun_a()
'fun_a'
c.mro()
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    c.mro()
NameError: name 'c' is not defined
C.mro()
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
A.mro()
[<class '__main__.A'>, <class 'object'>]


# A B -->C(a,b)
class A:
    a = 1
    variable = 100
    def __init__(self):
        self.aa = 11
    def fun_a(self):
        return "fun_a"

    
class B:
    b = 1
    variable = 333
    def __init__(self):
        self.bb = 11
    def fun_b(self):
        return "fun_b"

    
class C(A,B):
    pass

c_inst = C()
c_inst.a
1
c_inst.b
1
c_inst.variable
100
C.mro()
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]



class A:
    def start(self):
        print("A - start")
    def job(self):
        self.start()

        
class B(A):
    def start(self):
        print("B - start")

        
B.mro()
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
a_inst = A()
b_inst = B()
a_inst.start()
A - start
a_inst.job()
A - start


b_inst.start()
B - start
b_inst.job()
B - start


bb = B()
print(bb)
<__main__.B object at 0x000002A7FD714190>



class A:
    def __str__(self):
        return "A - str"

    
try:
    1/0
except:
    print(0)
else:
    print('OK')
finally:
    print('BUM')

    
0
BUM


class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"

    
def user_input():
    n, a = input('name '), int(input('age '))
    if len(n) < 2:
        pass ## вызвать исключение Ошибка
    if a < 0:
        pass ## вызвать исключение
    return User(n, a)

def user_input():
    n, a = input('name '), int(input('age '))
    if len(n) < 2:
        raise ZeroDivisionError
    if a < 0:
        raise ZeroDivisionError
    return User(n, a)

user_input()
name f
age 55
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    user_input()
  File "<pyshell#190>", line 4, in user_input
    raise ZeroDivisionError
ZeroDivisionError
class UserNameError(Exception):
    def __init__(self, u_name, message="имя пользователя меньше двух символов запрещено!"):
        self.u_name = u_name
        self.message = message

        
raise UserNameError('A')
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    raise UserNameError('A')
UserNameError: A
class UserAgeError(Exception):
    def __init__(self, u_age, message="age пользователя меньше 0 запрещено!"):
        self.u_age = u_name
        self.message = message
    def __repr__(self):
        return f"{self.u_age} --> {self.message}"

    
raise UserAgeError(-1)
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    raise UserAgeError(-1)
  File "<pyshell#201>", line 3, in __init__
    self.u_age = u_name
NameError: name 'u_name' is not defined. Did you mean: 'u_age'?
class UserAgeError(Exception):
    def __init__(self, u_age, message="age пользователя меньше 0 запрещено!"):
        self.u_age = u_age
        self.message = message
    def __repr__(self):
        return f"{self.u_age} --> {self.message}"

    
raise UserAgeError(-1)
Traceback (most recent call last):
  File "<pyshell#205>", line 1, in <module>
    raise UserAgeError(-1)
UserAgeError: -1


def user_input():
    n, a = input('name '), int(input('age '))
    if len(n) < 2:
        pass ## вызвать исключение Ошибка
    if a < 0:
        pass ## вызвать исключение
    return User(n, a)

user_input()
name f
age 123123
User(f, 123123)




# Q exce
# exception - -QueEmptyError

class Que:
    def __init__(self):
        self.__que = []
        print('Очередь создана')
    def put(self, number):
        self.__que.append(number)
        print('значение успешно добавлено')
    def get(self):
        if len(self.__que) < 1:
            raise EmptyQueError

        
class Que:
    def __init__(self):
        self.__que = []
        print('Очередь создана')
    def put(self, number):
        self.__que.append(number)
        print('значение успешно добавлено')
    def get(self):
        if len(self.__que) < 1:
            raise EmptyQueError
        del self._que [0]
        print('значение успешно удалено')

        
class EmptyQueError(Exception):
    ''''''
    pass

q1 = Que()
Очередь создана
for i in range(5):
    q1.put(i)

    
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
q1.__dict__
{'_Que__que': [0, 1, 2, 3, 4]}
q1.get()
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    q1.get()
  File "<pyshell#230>", line 11, in get
    del self._que [0]
AttributeError: 'Que' object has no attribute '_que'


class Que:
    def __init__(self):
        self.__que = []
        print('Очередь создана')
    def put(self, number):
        self.__que.append(number)
...         print('значение успешно добавлено')
...     def get(self):
...         if len(self.__que) < 1:
...             raise EmptyQueError
...         del self.__que [0]
...         print('значение успешно удалено')
... 
...         
>>> class EmptyQueError(Exception):
...     ''''''
...     pass
... 
>>> q1 = Que()
... Очередь создана
... for i in range(5):
...     q1.put(i)
...     
SyntaxError: multiple statements found while compiling a single statement
>>> q1 = Que()
Очередь создана
>>> for i in range(5):
...     q1.put(i)
... 
...     
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
значение успешно добавлено
>>> q1.get()
значение успешно удалено
>>> q1.get()
значение успешно удалено
>>> q1.get()
значение успешно удалено
>>> q1.get()
значение успешно удалено
>>> q1.get()
значение успешно удалено
>>> q1.get()
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    q1.get()
  File "<pyshell#244>", line 10, in get
    raise EmptyQueError
EmptyQueError
