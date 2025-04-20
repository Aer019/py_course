Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.



help
Type help() for interactive help, or help(object) for help about object.
help(input)
Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

result = input("Введи пароль:")
Введи пароль:123
print(result)
123
type(result)
<class 'str'>
a = 10
print(a)
10
a
10
a = int(10.5)
a
10
a = int("10")
a
10
a = int("-10")
a
-10
a = int("-10a")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a = int("-10a")
ValueError: invalid literal for int() with base 10: '-10a'
a
-10
f = 10.5
f
10.5
type(f)
<class 'float'>
s = str(f)
f
10.5
type(f)
<class 'float'>
type(f)
<class 'float'>
type(s)
<class 'str'>



print(s, type(s))
10.5 <class 'str'>
print(repr(s))
'10.5'



number = input("Введи число:")
Введи число:123
print(repr(number), type(number))
'123' <class 'str'>
number = int(number)
print(repr(number), type(number))
123 <class 'int'>
number - 99
24


number = int(input("Введи число:"))
Введи число:100
print(repr(number), type(number))
100 <class 'int'>
number2 = int(input("Введи число:"))
Введи число:10
result = number + number2
print(repr(result), type(trsult))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(repr(result), type(trsult))
NameError: name 'trsult' is not defined. Did you mean: 'result'?
print(repr(result), type(result))
110 <class 'int'>
2 ** 3 ** 2
512
9/5
1.8

>>> 
>>> 
>>> s = "hello"
>>> s2 = "privet"
>>> s + s2
'helloprivet'
>>> res = s + s2
>>> res
'helloprivet'
>>> 
>>> s*5
'hellohellohellohellohello'
>>> 5*s
'hellohellohellohellohello'
>>> res2 = s + s1 * 5
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    res2 = s + s1 * 5
NameError: name 's1' is not defined
>>> res2 = s + s2 * 5
>>> res2
'helloprivetprivetprivetprivetprivet'
>>> 
>>> 
>>> 
>>> a = 5
>>> b = 9
>>> c = 99
>>> print(a, "+", b, "+", c, "=", a+b+c)
5 + 9 + 99 = 113
>>> f"{a} + {b} = {a+b}"
'5 + 9 = 14'
>>> print(f"{a} + {b} + {c} = {a+b+c}")
5 + 9 + 99 = 113
>>> 
>>> 
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
