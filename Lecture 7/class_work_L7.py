Python 3.13.0b1 (tags/v3.13.0b1:2268289, May  8 2024, 12:20:07) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


1
1
1+1
2
a = 5
a == 5
True

name = 123
if name == 123
SyntaxError: expected ':'
if name == 123:
    print(name)
else:
    print('False')

    
123


def name_checker(name):
    if name == 'secret':
        return True
    else:
        return False

    
name_checker
<function name_checker at 0x00000204A6397740>
name_checker(name)
False

def name_checker(name):
    return name == 'secret'

name_checker(name)
False


enumerate
<class 'enumerate'>

help(enumerate)
Help on class enumerate in module builtins:

class enumerate(object)
 |  enumerate(iterable, start=0)
 |
 |  Return an enumerate object.
 |
 |    iterable
 |      an object supporting iteration
 |
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
 |
 |  Methods defined here:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(self, /)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  __class_getitem__(object, /)
 |      See PEP 585
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.



li [1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    li [1,2,3,4,5]
NameError: name 'li' is not defined
li[1,2,3,4,5]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    li[1,2,3,4,5]
NameError: name 'li' is not defined
li = [1,2,3,4,5]
li
[1, 2, 3, 4, 5]
for value in li:
    print(value)

    
1
2
3
4
5
for i in range (len(li)):
    print(i)

    
0
1
2
3
4

for i, v in enumerate(li)
SyntaxError: expected ':'
for i, v in enumerate(li):
    print(i, v)

    
0 1
1 2
2 3
3 4
4 5
for i, v in enumerate(li):
    print(i, v)
    print(li[i])

    
0 1
1
1 2
2
2 3
3
3 4
4
4 5
5
>>> for i, v in enumerate(li, 5):
...     print(i, v)
... 
...     
5 1
6 2
7 3
8 4
9 5
>>> 
>>> 
>>> bool
<class 'bool'>
>>> 
>>> bool(1)
True
>>> bool(2)
True
>>> bool(0)
False
>>> bool('')
False
>>> bool('  ')
True
>>> bool([])
False
>>> 
>>> indicators_list = [1,2,3,4,5,6]
>>> indicators_list = [1,0,1,1,0,1]
>>> if bool(indicators_list[0])
SyntaxError: expected ':'
>>> if bool(indicators_list[0]) and bool(indicators_list[1]) and bool(indicators_list[2]) and and bool(indicators_list[3]) and bool(indicators_list[4]):
...     
SyntaxError: invalid syntax
>>> if bool(indicators_list[0]) and bool(indicators_list[1]) and bool(indicators_list[2]) and bool(indicators_list[3]) and bool(indicators_list[4]):
...     print('OK')
... else:
...     print('BAD')
... 
...     
BAD
>>> # all any
>>> # all - каждый элемент и прогоняет через bool
>>> # если везде оказалось True -> True
>>> 
>>> if all(indicators_list ):
...     print('OK')
... else:
...     print('BAD')
... 
...     
BAD
>>> 
>>> 
>>> # any - каждый элемент и прогоняет через bool
... # если хотяб один оказалось True -> True
>>> 
>>> indicators_list = [0,0,0,0,0,1]
>>> any(indicators_list )
True
>>> all(indicators_list)
False
>>> 
>>> 
>>> def my_all(iterable):
...     flag = None
...     for value in iterable:
...         if not bool(value):
...             return False
...         flag = True
...     return flag
... 
>>> 
>>> li
[1, 2, 3, 4, 5]
>>> my_all(li)
True
>>> li = [1,2,3,4,5,0]
>>> my_all(li)
False
>>> 
