Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
while counter1 > 0 or counter2 >0:
if counter1 > 0:
print("первый", counter1)
else:
print("первый отвалился")

if counter2 > 0:
print("второй", counter2)
else:
print("второй отвалился")

counter1 -= 1
counter2 -= 1
SyntaxError: expected an indented block after 'while' statement on line 1
while counter1 > 0 or counter2 >0:
    if counter1 > 0:
        print("первый", counter1)
    else:
        print("первый отвалился")

    if counter2 > 0:
        print("второй", counter2)
    else:
        print("второй отвалился")

    counter1 -= 1
    counter2 -= 1

    
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    while counter1 > 0 or counter2 >0:
NameError: name 'counter1' is not defined
counter1 = 6
counter2 = 3
while counter1 > 0 or counter2 >0:
    if counter1 > 0:
        print("первый", counter1)
    else:
        print("первый отвалился")

    if counter2 > 0:
        print("второй", counter2)
    else:
        print("второй отвалился")

    counter1 -= 1
    counter2 -= 1

    
первый 6
второй 3
первый 5
второй 2
первый 4
второй 1
первый 3
второй отвалился
первый 2
второй отвалился
первый 1
второй отвалился


5 > 2
True
3 < 5
True
True or False
True
False or False
False


True
True
not True
False
not False
True
3 > 2
True
not 3 > 2
False
if 3 > 2:
    print(3)
else:
    print(2)

    
3
if 3 > 2:
    print(2)
else:
    print(3)

    
2

if not 3 > 2:
    print(3)
else:
    print(2)

    
2



not not not False
True




number1 = int(input("Введи число:"))
Введи число:12
number2 = int(input('Введи число:'))
Введи число:6
operation = input("+ - * / exit")
+ - * / exit+
operation
'+'
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("Не понимаю...")

    
18
while operation != "exit":
    number1 = int(input("Введи число:"))
    Введи число:12
    number2 = int(input('Введи число:'))
    Введи число:6
    operation = input("+ - * / exit")
    + - * / exit+
    operation
    '+'
    if operation == "+":
        print(number1 + number2)
    elif operation == "-":
        print(number1 - number2)
    elif operation == "*":
        print(number1 * number2)
    elif operation == "/":
        print(number1 / number2)
    else:
        print("Не понимаю...")
        
SyntaxError: invalid syntax


while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input('Введи число:'))
    operation = input("+ - * / exit")
    + - * / exit+
    operation
    '+'
    if operation == "+":
        print(number1 + number2)
    elif operation == "-":
        print(number1 - number2)
    elif operation == "*":
        print(number1 * number2)
    elif operation == "/":
        print(number1 / number2)
    else:
        print("Не понимаю...")
        
SyntaxError: invalid syntax


while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input('Введи число:'))
    operation = input("+ - * / exit")
    if operation == "+":
        print(number1 + number2)
    elif operation == "-":
        print(number1 - number2)
    elif operation == "*":
        print(number1 * number2)
    elif operation == "/":
        print(number1 / number2)
    else:
        print("Не понимаю...")

        
Введи число:4
Введи число:5
+ - * / exit+
9
Введи число:2
Введи число:4
+ - * / exit*
8
Введи число:exit
Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    number1 = int(input("Введи число:"))
ValueError: invalid literal for int() with base 10: 'exit'
while operation != "exit":
    number1 = int(input("Введи число:"))
    number2 = int(input('Введи число:'))
    operation = input("+ - * / exit")
    if operation == "+":
        print(number1 + number2)
    elif operation == "-":
        print(number1 - number2)
    elif operation == "*":
        print(number1 * number2)
    elif operation == "/":
        print(number1 / number2)
    else:
        print("Не понимаю...")
    operation = input('+ - * / exit')

    
Введи число:2
Введи число:4
+ - * / exit*
8
+ - * / exitexit





a = 1
f = 3.14
s = "dada"
li = [3, 5, "dasd", True, f, s, a]
li
[3, 5, 'dasd', True, 3.14, 'dada', 1]
type(li)
<class 'list'>
li[0]
3
li[3]
True
li[6]
1
li[2]
'dasd'
li[7]
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    li[7]
IndexError: list index out of range


li = []
li
[]
li = list()
li
[]
li[]
SyntaxError: invalid syntax
li = [3,4,5,7,9]
li[0]
3
li[-1]
9
li[-0]
3




s = "abc"
s
'abc'
s.upper
<built-in method upper of str object at 0x000001C6235A7E10>
s.upper()
'ABC'
a = 10
a.upper()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.upper()
AttributeError: 'int' object has no attribute 'upper'


li1 = [1,2,3,4]
li2 = [True, False, "safas"]
li1 + li2
[1, 2, 3, 4, True, False, 'safas']
res = li1 + li2
res
[1, 2, 3, 4, True, False, 'safas']
li2*9
[True, False, 'safas', True, False, 'safas', True, False, 'safas', True, False, 'safas', True, False, 'safas', True, False, 'safas', True, False, 'safas', True, False, 'safas', True, False, 'safas']


len
<built-in function len>
help(len)
Help on built-in function len in module builtins:

len(obj, /)
    Return the number of items in a container.

len(li1)
4
li1
[1, 2, 3, 4]
li1[15]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    li1[15]
IndexError: list index out of range
li1[2]
3


li
[3, 4, 5, 7, 9]
li = [1,2,3,4]
li
[1, 2, 3, 4]
li[1] = 222
li
[1, 222, 3, 4]
li.append(555)
li
[1, 222, 3, 4, 555]
li.insert(3, 333)
li
[1, 222, 3, 333, 4, 555]
li.pop()
555
li
[1, 222, 3, 333, 4]
res = li.pop()
res
4
li.index(3)
2
li
[1, 222, 3, 333]
li.index(1)
0
li.index(2)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    li.index(2)
ValueError: 2 is not in list
li.clear
<built-in method clear of list object at 0x000001C6253C4B80>
li.clear()
li
[]
li = [1,1,1,1,11,}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
li = [1,1,1,1,11]
li
[1, 1, 1, 1, 11]
del li[11]
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    del li[11]
IndexError: list assignment index out of range
del li
li
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    li
NameError: name 'li' is not defined



hat_list = [1, 2, 3, 4, 5]
print(len(hat_list))
5
hat_list = [1, 2, 3, 4, 5]
print(len(hat_list))
SyntaxError: multiple statements found while compiling a single statement
input('Ввнеси изменения в лист:')
Ввнеси изменения в лист:123
'123'
a = input('Ввнеси изменения в лист:')
Ввнеси изменения в лист:123
hat_list.insert(-1, a)
hat_list
[1, 2, 3, 4, '123', 5]
hat_list.pop()
5
hat_list
[1, 2, 3, 4, '123']
print(len(hat_list))
5
hat_list = [1, 2, 3, 4, 5]
a = input('Ввнеси изменения в лист:')
Ввнеси изменения в лист:YES
hat_list.insert(2, a)
hat_list.pop()
5
print(len(hat_list))
5
hat_list
[1, 2, 'YES', 3, 4]



li = [1,2,3,4,5,6,7,8,9,0,11,121312132,66]
li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 121312132, 66]

for value in li:
    print(value, end=' / ')

    
1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 0 / 11 / 121312132 / 66 / 
for value in li:
    print(value**2, end=' / ')

    
1 / 4 / 9 / 16 / 25 / 36 / 49 / 64 / 81 / 0 / 121 / 14716633370385424 / 4356 / 
litest = li**2
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    litest = li**2
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
value
66
for i in li
SyntaxError: expected ':'
for i in li:
    print()

    













li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 121312132, 66]


total = 0
for i range(len(li)):
    
SyntaxError: invalid syntax
for i in range(len(li)):
    total += li[i]

    

total
121312254




li = [4, 5, 2, 3, 1]
li.sort
<built-in method sort of list object at 0x000001C625F2CB40>
li.sort[]
SyntaxError: invalid syntax



a = 8
b = 3


a = b
a
3
b
3
b = a
b
3
a
3

a = 8
b = 3

tmp = a
tmp
8
a = b
a
3
b = tmp
a
3
b
8
a, b = b, a
b
3
a
8
a
8
b
3

li
[4, 5, 2, 3, 1]
li[1], li[2] = li[2], li[1]
li
[4, 2, 5, 3, 1]
li[2], li[3] = li[3], li[2]
li
[4, 2, 3, 5, 1]
li[3], li[4] = li[4], li[3]
li
[4, 2, 3, 1, 5]
li[0], li[1] = li[1], li[0]
li
[2, 4, 3, 1, 5]
li[1], li[2] = li[2], li[1]
li
[2, 3, 4, 1, 5]
li[2], li[3] = li[3], li[2]
li
[2, 3, 1, 4, 5]



li = [1,2,3,4,5]
li2 = li.copy()
li
[1, 2, 3, 4, 5]
li2
[1, 2, 3, 4, 5]
li[0] = 111
li
[111, 2, 3, 4, 5]
li2
[1, 2, 3, 4, 5]


li = [1,2,3,4,5]
li2 = [3,4,5, li]
li2
[3, 4, 5, [1, 2, 3, 4, 5]]
li3 = li2.copy
li3
<built-in method copy of list object at 0x000001C625F24280>
li3 = li2.copy()
li3
[3, 4, 5, [1, 2, 3, 4, 5]]
li[0] = 9999
li3
[3, 4, 5, [9999, 2, 3, 4, 5]]
from copy imoprt deepcopy
SyntaxError: invalid syntax
from copy import deepcopy
li = [1,2,3,4,5]
li2 = [3,4,5,6, li]
li3 = deepcopy(li2)
li
[1, 2, 3, 4, 5]
li2
[3, 4, 5, 6, [1, 2, 3, 4, 5]]
li3
[3, 4, 5, 6, [1, 2, 3, 4, 5]]
li2[0] = 99999
li
[1, 2, 3, 4, 5]
li2
[99999, 4, 5, 6, [1, 2, 3, 4, 5]]
li3
[3, 4, 5, 6, [1, 2, 3, 4, 5]]



li[0] = 99999
li2
[99999, 4, 5, 6, [99999, 2, 3, 4, 5]]
li3
[3, 4, 5, 6, [1, 2, 3, 4, 5]]



li = [12,2,24,556,7,8,8,9,0]
li
[12, 2, 24, 556, 7, 8, 8, 9, 0]
li[2:]
[24, 556, 7, 8, 8, 9, 0]
li[2:-1]
[24, 556, 7, 8, 8, 9]
li[3:6]
[556, 7, 8]



li = [12,2,24,556,7,8,8,9,0]
li2 = [True, False, True, False, True]
li3 = ['asdsad', 'sadsad', 'asdasddssad', 'asdadsdassda']

res = li[:3] + li2[2:4] + li3[2:]
res
[12, 2, 24, True, False, 'asdasddssad', 'asdadsdassda']


users_id
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    users_id
NameError: name 'users_id' is not defined
>>> users_id = [12, 2, 4, 5, 6, 7, 8, 8, 9, 0]
>>> users_id[-6:-2]
[6, 7, 8, 8]
>>> 
>>> 
>>> se = set()
>>> se
set()
>>> print(se)
set()
>>> 
>>> 
>>> se = {1,2,3,4,5,1,2,3,4,5}
>>> se
{1, 2, 3, 4, 5}
>>> len(se)
5
>>> 6 in se
False
>>> 5 in se
True
>>> 1 in se
True
>>> 
>>> for i in se:
...     print(i)
... 
...     
1
2
3
4
5
>>> se.add(444)
>>> se
{1, 2, 3, 4, 5, 444}
>>> se.add(1)
>>> se
{1, 2, 3, 4, 5, 444}
>>> se.update({5,6,7,8,3,4})
>>> se
{1, 2, 3, 4, 5, 6, 7, 8, 444}
>>> se.remove(4)
>>> se
{1, 2, 3, 5, 6, 7, 8, 444}
>>> 
>>> 
>>> se.remove(44444)
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    se.remove(44444)
KeyError: 44444
>>> se.discard(3)
>>> se
{1, 2, 5, 6, 7, 8, 444}
>>> se.discard(33)
>>> se
{1, 2, 5, 6, 7, 8, 444}
