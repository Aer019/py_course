Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
123+123
246
li = [1,2,2,3,4,5]
li
[1, 2, 2, 3, 4, 5]
print(li)
[1, 2, 2, 3, 4, 5]
di = {1:11, 2:22}
di
{1: 11, 2: 22}
del di
try:
    print(di)
except NameError:
    print('asdads')

    
asdads
print(di)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(di)
NameError: name 'di' is not defined


try:
    print(di)
except NameError:
    print('asdads')
    raise

asdads
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    print(di)
NameError: name 'di' is not defined
try:
    asdasd
except:
    print(asdasd)
except NameError:
    print(123)
    
SyntaxError: default 'except:' must be last

































# Car
# vin volume body_type
class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f'Car({sel.vin}, {self.volume}, {self.body_type})'

    

lada1 = Car('1231312', 1.67, 'hatchback')
lada1
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    lada1
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "<pyshell#51>", line 7, in __repr__
    return f'Car({sel.vin}, {self.volume}, {self.body_type})'
NameError: name 'sel' is not defined. Did you mean: 'self'?
class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f'Car({self.vin}, {self.volume}, {self.body_type})'

    
lada1 = Car('1231312', 1.67, 'hatchback')
lada1
Car(1231312, 1.67, hatchback)
lada1.__dict__
{'vin': '1231312', 'volume': 1.67, 'body_type': 'hatchback'}
di = lada1.__dict__
di
{'vin': '1231312', 'volume': 1.67, 'body_type': 'hatchback'}
di.get('vin')
'1231312'
di.get('volume')
1.67
type(di)
<class 'dict'>


lada2 = Car('12312312', 1.9, 'sedan')
lada2
Car(12312312, 1.9, sedan)
li = [lada1, lada2]
li
[Car(1231312, 1.67, hatchback), Car(12312312, 1.9, sedan)]
for car_inst in li:
    print(car_inst.vin)
    print(car_inst.volume)
    print(car_inst.body_type)

    
1231312
1.67
hatchback
12312312
1.9
sedan
for car_inst in li:
    for k, v in car_inst.__dict__.items():
        print(k, ':', v)

        
vin : 1231312
volume : 1.67
body_type : hatchback
vin : 12312312
volume : 1.9
body_type : sedan


class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f'Car({self.vin}, {self.volume}, {self.body_type})'

    
lada2
Car(12312312, 1.9, sedan)
lada2.body_type = 'coupe'
lada2
Car(12312312, 1.9, coupe)
lada2.new_var = 43535353
lada2
Car(12312312, 1.9, coupe)
lada2.__dict__
{'vin': '12312312', 'volume': 1.9, 'body_type': 'coupe', 'new_var': 43535353}
Car.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Car.__init__ at 0x000001C02EE01D00>, '__repr__': <function Car.__repr__ at 0x000001C02EE01DA0>, '__static_attributes__': ('body_type', 'vin', 'volume'), '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None})
Car.__bases__
(<class 'object'>,)
class S:
    pass

fg = S()


class Car:
    def __init__(self, vin, volume, body_type):
        self.vin = vin
        self.volume = volume
        self.body_type = body_type
    def __repr__(self):
        return f'Car({self.vin}, {self.volume}, {self.body_type})'
    def move(self):
        print('move')
    def turn(self, direc):
        print('turn', direc)
    def stop(self):
        print('stop')

        
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270, max_speed=300):
        super().__init__(self, vin, volume, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
     def __repr__(self):
         super().__repr__()
        return f'SportCar({self.speed_limit}, {self.max_speed})'
    
SyntaxError: unindent does not match any outer indentation level
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270, max_speed=300):
        super().__init__(self, vin, volume, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
         super().__repr__()
        return f'SportCar({self.speed_limit}, {self.max_speed})'
    
SyntaxError: unindent does not match any outer indentation level
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270, max_speed=300):
        super().__init__(self, vin, volume, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        super().__repr__()
        return f'SportCar({self.speed_limit}, {self.max_speed})'
    def race(self):
        print(f'race with {self.max_speed} km\h')

        
renault = SportCar('12312313', 3.5, 'coupe')
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    renault = SportCar('12312313', 3.5, 'coupe')
  File "<pyshell#116>", line 3, in __init__
    super().__init__(self, vin, volume, body_type)
TypeError: Car.__init__() takes 4 positional arguments but 5 were given


class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270, max_speed=300):
        super().__init__(self, vin, volume, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        return super().__repr__() + f'SportCar({self.speed_limit}, {self.max_speed})'
    def race(self):
        print(f'race with {self.max_speed} km\h')

        
renault = SportCar('12312313', 3.5, 'coupe')
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    renault = SportCar('12312313', 3.5, 'coupe')
  File "<pyshell#121>", line 3, in __init__
    super().__init__(self, vin, volume, body_type)
TypeError: Car.__init__() takes 4 positional arguments but 5 were given
class SportCar(Car):
    def __init__(self, vin, volume, body_type, speed_limit=270, max_speed=300):
        super().__init__(vin, volume, body_type)
        self.speed_limit = speed_limit
        self.max_speed = max_speed
    def __repr__(self):
        return super().__repr__() + f'SportCar({self.speed_limit}, {self.max_speed})'
    def race(self):
        print(f'race with {self.max_speed} km\h')

        
renault = SportCar('12312313', 3.5, 'coupe')
renault
Car(12312313, 3.5, coupe)SportCar(270, 300)
\


class Dog:
    def say(self, msg):
        print(msg)

        
class Cat:
    def say(self, msg):
        print(msg)

        
class Bird:
    def say(self, msg):
        print(msg)

        
d, c, b = Dog(), Cat(), Bird()
d.say('dog'), c.say('cat'), b.say('kria')
dog
cat
kria
(None, None, None)


# Stack

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack
[1, 2, 3]
del stack[-1]
stack
[1, 2]
del stack[-1]
del stack[-1]
stack
[]


class Stack:
    def __init__(self):
        self.__stack = []
        print('stack создан успешно')
    def push(self, value):
        self.__stack.append(value)
        print(value, 'добавлено успешно')
    def pop(self):
        print(self.__stack.pop(), 'успешно удалено.')

        
s1 = Stack()
stack создан успешно
s1.push(4)
4 добавлено успешно
s1.push(44)
44 добавлено успешно
s1.push(3)
3 добавлено успешно
s1.push(2)
2 добавлено успешно
s1.__dict__
{'_Stack__stack': [4, 44, 3, 2]}
s1.pop()
2 успешно удалено.
s1.pop()
3 успешно удалено.
s1.pop()
44 успешно удалено.
s1.pop
<bound method Stack.pop of <__main__.Stack object at 0x000001C02ECDF620>>
s1.pop()
4 успешно удалено.
s1.__dict__
{'_Stack__stack': []}
class Stack:
    def __init__(self):
        self.__stack = []
        print('stack создан успешно')
    def push(self, value):
        self.__stack.append(value)
        print(value, 'добавлено успешно')
    def pop(self):
        print(self.__stack.pop(), 'успешно удалено.')
    def state(self):
        print('Текущее состояние стека')
        print(self.__stack)

        
s1 = Stack()
stack создан успешно
s1.state
<bound method Stack.state of <__main__.Stack object at 0x000001C02ECDF770>>
s1.push(555)
555 добавлено успешно
s1.state
<bound method Stack.state of <__main__.Stack object at 0x000001C02ECDF770>>
s1.state()
Текущее состояние стека
[555]
s1.pop()
555 успешно удалено.
s1.state()
Текущее состояние стека
[]


class Stack:
    def __init__(self):
        self.__stack = []
        print('stack создан успешно')
    def push(self, value):
        self.__stack.append(value)
        print(value, 'добавлено успешно')
    def pop(self):
        try:
            print(self.__stack.pop(), 'успешно удалено.')
        except:
            print('стек уже пустой.')
    def state(self):
        print('Текущее состояние стека')
        print(self.__stack)

        
s1 = Stack()
stack создан успешно
s1.state()
Текущее состояние стека
[]
s1.pop()
стек уже пустой.


class AddStackValuse(Stack):
    def __init__(self):
        super().__init__()
        self.__suma = 0
    def push(self, value):
        super().push(value)
        self.__summa += value
    def get_summa(self):
        print(self.__summa)

        
s2 = AddStackValuse()
stack создан успешно
s2.get_summa()
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    s2.get_summa()
  File "<pyshell#206>", line 9, in get_summa
    print(self.__summa)
AttributeError: 'AddStackValuse' object has no attribute '_AddStackValuse__summa'. Did you mean: '_AddStackValuse__suma'?
class AddStackValuse(Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push(self, value):
        super().push(value)
        self.__summa += value
    def get_summa(self):
        print(self.__summa)


s2 = AddStackValuse()
stack создан успешно
s2.get_summa()
0


a = 10
b = 15
a+b
25
c, d = 3.13, 5.7
c
3.13
d
5.7
c + d
8.83
c.__add__(d)
8.83



class Dog:
    def __init__(self, number):
        self.number = number
    def __add__(self, dog_inst):
        return self.number + dog_inst.number

    
d1, d2 = Dog(4), Dog(6)
d1.__add__(d2)
10
d1 + d2
10


class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary

        
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary

    
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary

    
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __sub__(self, naxt_dog):
        return self.salary - next_dog.salary
    def __len__(self):
        return self.age

    
class Dog:
    def __init__(self, name, age, color, salary):
        self.name = name
        self.age = age
        self.color = color
        self.salary = salary
    def __add__(self, next_dog):
        return self.salary + next_dog.salary
    def __sub__(self, naxt_dog):
        return self.salary - next_dog.salary
    def __len__(self):
        return self.age
    def __eq__(self, next_dog):
        return self.name == next_dog.name
    def __eq__(self, next_dog):
        return self.name != next_dog.name

    
d1, d2 = Dog('jo', 4, 'red', 100), Dog('Jojo', 1, 'blue', 1000)
d1 + d2
1100
d1 == d2
True
d1 != d2
False
d1
<__main__.Dog object at 0x000001C02ECDF380>
d1()
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    d1()
TypeError: 'Dog' object is not callable
>>> print(d1)
<__main__.Dog object at 0x000001C02ECDF380>
>>> class Dog:
...     def __init__(self, name, age, color, salary):
...         self.name = name
...         self.age = age
...         self.color = color
...         self.salary = salary
...     def __add__(self, next_dog):
...         return self.salary + next_dog.salary
...     def __sub__(self, naxt_dog):
...         return self.salary - next_dog.salary
...     def __len__(self):
...         return self.age
...     def __eq__(self, next_dog):
...         return self.name == next_dog.name
...     def __ne__(self, next_dog):
...         return self.name != next_dog.name
... 
...     
>>> d1, d2 = Dog('jo', 4, 'red', 100), Dog('Jojo', 1, 'blue', 1000)
>>> d1 == d2
False
>>> d1 != d2
True
>>> 
>>> 
>>> return
SyntaxError: 'return' outside function
>>> if True:
...     123
... 
...     
123
>>> 
>>> 
>>> x= 0
>>> for i in range(10):
...     for j in range(1, 10, 1):
...         x +=1
... 
...         
>>> print(x)
90
