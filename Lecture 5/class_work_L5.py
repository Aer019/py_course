Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1 + 3
4
print(12)
12
type(3)
<class 'int'>
3 < 5
True
666 > 55
True
True or False
True
False or False
False
input()
sadasd
'sadasd'
int("123123")
123123
li = [1,2,3,4]
li
[1, 2, 3, 4]
li[1]
2

li[0]
1
li.pop()
4




# sign up
# name phone username
# 10 users
# per day
name = input('Name:')
Name:Vasia
phone = input('Phone:')
Phone:123312312312
username = input('Username:')
Username:saddasdas

def sing_up():
    name = input('Name:')
    phone = input('Phone:')
    username = input('Username:')
    user = [name, phone, username]
    print('User:', user, 'was created.')

    
sign_up
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    sign_up
NameError: name 'sign_up' is not defined. Did you mean: 'sing_up'?
sing_up
<function sing_up at 0x0000025D83E4F6A0>
print
<built-in function print>

sing_up()
Name:Stefan
Phone:2132131
Username:stef12345
User: ['Stefan', '2132131', 'stef12345'] was created.
sing_up()
Name:Petya
Phone:123312
Username:Petr1
User: ['Petya', '123312', 'Petr1'] was created.
User
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    User
NameError: name 'User' is not defined
user
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    user
NameError: name 'user' is not defined
username
'saddasdas'





def hel lo():
    
SyntaxError: expected '('
def hello:
    
SyntaxError: expected '('
def hello
SyntaxError: expected '('
def hello():
    print('hello')

    
hello
<function hello at 0x0000025D83E4DC60>
hello()
hello
def bye():
    print('Bye')

    
bye
<function bye at 0x0000025D83E5D3A0>
bye()
Bye
for i in range(5):
    hello()
    bye()

    
hello
Bye
hello
Bye
hello
Bye
hello
Bye
hello
Bye



def sing_up():
    name = input('Name:')
    phone = input('Phone:')
    username = input('Username:')
    user = [name, phone, username]
    print('User:', user, 'was created.')

    
print('Привет юзер')
Привет юзер
1+3
4
5+5
10
if 1 == 1:
    sing_up()

    
Name:Jack
Phone:12312
Username:JackRipper
User: ['Jack', '12312', 'JackRipper'] was created.


hello
<function hello at 0x0000025D83E4DC60>
type(hello)
<class 'function'>
hello = 10
type(hello)
<class 'int'>


print = 100
print()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print()
TypeError: 'int' object is not callable
print
100

================================================ RESTART: Shell ================================================

print()

# cm --> m
# 178 --> 1.78

def converter_cm_to_m():
    pass


def hello_user(user_name):
    print(f'Welcome, {username}')

    
hello_user()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    hello_user()
TypeError: hello_user() missing 1 required positional argument: 'user_name'
hello_user('Vasia')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    hello_user('Vasia')
  File "<pyshell#97>", line 2, in hello_user
    print(f'Welcome, {username}')
NameError: name 'username' is not defined. Did you mean: 'user_name'?
def hello_user(user_name):
    print(f'Welcome, {user_name}')

    
hello_user('Vasia')
Welcome, Vasia

def converter_cm_to_m(cm):
    cmm = cm % 100 # 78
    mm = cm  // 100 # 1
    print(mm, cmm, sep='.')

    
converter_cm_to_m(178)
1.78
converter_cm_to_m(215)
2.15
converter_cm_to_m(165)
1.65
converter_cm_to_m(78)
0.78

cmm
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    cmm
NameError: name 'cmm' is not defined
mm
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    mm
NameError: name 'mm' is not defined
cm
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    cm
NameError: name 'cm' is not defined


def fun(num1, st1, li1):
    print(num1, st1, li1)
    bbbb = 100000
    print(bbbb)

    
num1
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    num1
NameError: name 'num1' is not defined
bbbb
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    bbbb
NameError: name 'bbbb' is not defined
fun(1, 'sdsds', [1,2,3,4])
1 sdsds [1, 2, 3, 4]
100000
bbbb
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    bbbb
NameError: name 'bbbb' is not defined


# simple
def hello(name, phone):
    print('Name:', name)
    print('phone:', phone)

    
hello('Vasia', 1231231)
Name: Vasia
phone: 1231231
hello(1231231, 'Vasia')
Name: 1231231
phone: Vasia
def hello(str(name), int(phone)):
    
SyntaxError: invalid syntax
int(phone)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    int(phone)
NameError: name 'phone' is not defined. Did you mean: 'None'?



# while exit +- funcs

def add(a, b):
    print(f"{a} + {b} = {a+b}")

    
def sub(a, b):
    print(f"{a} - {b} = {a-b}")

    
def mul(a, b):
    print(f"{a} * {b} = {a*b}")

    
oper = input('exit + -')
exit + --
while oper !='exit':
    num1, num2 = int(input('n1: ')), int(input('n2: '))
    if oper == '+':
        add(num1, num2)
    elif oper == '-':
        sub(num1, num2)
    elif oper == '*':
        mul(num1, num2)
    else:
        print('No!')
    oper = input('exit + -')

    
n1: 5
n2: 2
5 - 2 = 3
exit + -+
n1: 5
n2: 2
5 + 2 = 7
exit + -*
n1: 2
n2: 2
2 * 2 = 4
exit + -exit


def add(a, b):
    print(f"{a} + {b} = {a+b}")

    

def sub(a, b):
    print(f"{a} - {b} = {a-b}")


def mul(a, b):
    print(f"{a} * {b} = {a*b}")

    
def main():
    oper = input('exit + -')
    while oper !='exit':
        num1, num2 = int(input('n1: ')), int(input('n2: '))
        if oper == '+':
            add(num1, num2)
        elif oper == '-':
            sub(num1, num2)
        elif oper == '*':
            mul(num1, num2)
        else:
            print('No!')
        oper = input('exit + -')

        
main()
exit + -*
n1: 4
n2: 4
4 * 4 = 16
exit + -exit




def add(a, b):
    print(f"{a} + {b} = {a+b}")

    
name = input('name:')
name:Vasya
name
'Vasya'
suma = add(4,5)
4 + 5 = 9
summa
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    summa
NameError: name 'summa' is not defined. Did you mean: 'suma'?
suma
print(suma)
None
def add(a, b):
    print(f"{a} + {b} = {a+b}")
    return a+b

summa = ad(4,5)
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    summa = ad(4,5)
NameError: name 'ad' is not defined
summa = add(4,5)
4 + 5 = 9
summa
9




def add(a, b):
    print(f"{a} + {b} = {a+b}")
    return a+b

def sub(a, b):
    print(f"{a} - {b} = {a-b}")
    return a-b

def mul(a, b):
    print(f"{a} * {b} = {a*b}")
    return a*b

def main():
    oper = input('exit + -')
    while oper !='exit':
        num1, num2 = int(input('n1: ')), int(input('n2: '))
        if oper == '+':
            result = add(num1, num2)
            print('result from return:', result)
        elif oper == '-':
            result = sub(num1, num2)
            print('result from return:', result)
        elif oper == '*':
            result = mul(num1, num2)
            print('result from return:', result)
        else:
            print('No!')
        oper = input('exit + -')

        
main()
exit + -+
n1: 3
n2: 5
3 + 5 = 8
result from return: 8
exit + -exit
result
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    result
NameError: name 'result' is not defined


pass
def shallow():
    pass

shallow()
res = shallow()
print(res)
None


def converter_cm_to_m(cm):
    cmm = cm % 100 # 78
    mm = cm  // 100 # 1
    return f'{mm}.{cmm{}def converter_cm_to_m(cm):
    cmm = cm % 100 # 78
    mm = cm  // 100 # 1
print(mm, cmm, sep='.')
SyntaxError: invalid syntax. Perhaps you forgot a comma?

def converter_cm_to_m(cm):
    cmm = cm % 100 # 78
    mm = cm  // 100 # 1
    return f'{mm}.{cmm}'

res = converter_cm_to_m(190)
res
'1.90'


def converter_cm_to_m(cm):
    """Эта функция для понимаия"""
    cmm = cm % 100 # 78
    mm = cm  // 100 # 1
    return f'{mm}.{cmm}'

help(converter_cm_to_m)
Help on function converter_cm_to_m in module __main__:

converter_cm_to_m(cm)
    Эта функция для понимаия


def converter_cm_to_m(cm):
    """Эта функция для понимаия"""
    if cm < 100:
        return False
    
    cmm = cm % 100 # 78
    mm = cm  // 100 # 1
    return f'{mm}.{cmm}'


converter_cm_to_m(100)
'1.0'
converter_cm_to_m(10)
False
converter_cm_to_m(101)
'1.1'
converter_cm_to_m(110)
'1.10'
101/100
1.01
110/100
1.1



def fun(listik):
    listik[0] = 19999

    
li
Traceback (most recent call last):
  File "<pyshell#252>", line 1, in <module>
    li
NameError: name 'li' is not defined
li = [1,2,3,4]
li
[1, 2, 3, 4]
fun(li)
li
[19999, 2, 3, 4]


isinstance
<built-in function isinstance>
help(isinstance)
Help on built-in function isinstance in module builtins:

isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.

isinstance(10, int)
True
isinstance(li, list)
True
li
[19999, 2, 3, 4]


total = 0
def add_to_total(n):
    total = total + n

    
add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#269>", line 2, in add_to_total
    total = total + n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
def add_to_total(n):
    total = total + n

add_to_total(5)
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    add_to_total(5)
  File "<pyshell#272>", line 2, in add_to_total
    total = total + n
UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
print(total)
0
def add_to_total(n):
    result = total + n
    print(result)

    
add(5)
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    add(5)
TypeError: add() missing 1 required positional argument: 'b'
add_to_total(5)
5
# !5 !6 !3
1 * 2 * 3
6
for i in range(50)
SyntaxError: expected ':'
for i in range(10):
    mult = i*i

    
mult
81


def factorial(n):
    if n < 0:
        return
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    
    for i in range(2, n+1):
        result *= i
        
    return result

factorial(9)
362880
factorial(1)
1
factorial(-9)
factorial()
Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    factorial()
TypeError: factorial() missing 1 required positional argument: 'n'
def main():
    oper = input('exit +')
    while oper != 'exit':
        result = factorial(int(input('factorial to number:'))
        print('factorial is:', result)
                           
SyntaxError: '(' was never closed
def main():
    oper = input('exit +')
    while oper != 'exit':
        result = factorial(int(input('factorial to number:')))
        print('factorial is:', result)
        oper = input('exit +')

        
main(10)
Traceback (most recent call last):
  File "<pyshell#308>", line 1, in <module>
    main(10)
TypeError: main() takes 0 positional arguments but 1 was given
factorial(10)
3628800
main()
exit ++
factorial to number:10
factorial is: 3628800
exit +exit




def recurs(n):
    if n >= 20:
        return 1
    return n + recurs(n + 4)

recurs(5)
45
recurs(1)
46

>>> 
>>> def factorial(n):
...     if n == 0:
...         return 1
...     return n * factorial(n-1)
... 
>>> factorial(10)
3628800
>>> 
>>> 
>>> f1, f2 = 1, 1
>>> f1
1
>>> f2
1
>>> f1, f2 = f2, f1 + f2
>>> f1
1
>>> f2
2
>>> f1, f2 = f2, f1 + f2
>>> f2
3
>>> f1, f2 = f2, f1 + f2
>>> f2
5
>>> f1, f2 = f2, f1 + f2
>>> f2
8
>>> def febo(n):
...     f1, f2 = 1, 1
...     if n == 1 or n == 2
...     
SyntaxError: expected ':'
>>> n = 3
>>> for i in range(2, n):
...     pass
... 
>>> f1, f2 = 1, 1
>>> for i in range(2,n):
...     f1, f2 = f2, f1 + f2
... 
...     
>>> f2
2
>>> f1, f2 = 1, 1
>>> for i in range(2,n):
...     f1, f2 = f2, f1 + f2
... 
...     
>>> f2
2
>>> n = 4
>>> for i in range(2,n):
...     f1, f2 = f2, f1 + f2
... 
...     
>>> f2
5
