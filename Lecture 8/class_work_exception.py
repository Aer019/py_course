Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
sdaads
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    sdaads
NameError: name 'sdaads' is not defined
1+3
4
print('')

a = 1
b = 2
a + b
3



# Lecture 8
attributeerror
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    attributeerror
NameError: name 'attributeerror' is not defined. Did you mean: 'AttributeError'?
AttibuteError
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    AttibuteError
NameError: name 'AttibuteError' is not defined. Did you mean: 'AttributeError'?
AttributeError
<class 'AttributeError'>
li[-1]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    li[-1]
NameError: name 'li' is not defined
li = [1,2,3,4]
li[-1]
4


n = int(input('asd'))
asd12
1/n
0.08333333333333333
n = int(input('asd'))
asd0
1/n
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    1/n
ZeroDivisionError: division by zero



n = input('asd')
asd123
n.isdigit()
True
if n.isdigit():
    print(1/n)

    
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    print(1/n)
TypeError: unsupported operand type(s) for /: 'int' and 'str'
if n.isdigit():
    print(1/int(n))

    
0.008130081300813009


# try except
try:
    n = int(input('asd'))
    print(1/n)
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asdsdasdas
Хьюстон у нас проблемки... (0_0)


try:
    n = int(input('asd'))
    print(1/n)
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asd0
Хьюстон у нас проблемки... (0_0)
try:
    n = int(input('asd'))
    print(1/n)
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asd123
0.008130081300813009
for i in range(4):
    try:
        n = int(input('asd'))
        print(1/n)
    except:
        print('Хьюстон у нас проблемки... (0_0)')

        
asd5
0.2
asd0
Хьюстон у нас проблемки... (0_0)
asdasdasd
Хьюстон у нас проблемки... (0_0)
asd-1
-1.0
for i in range(4):
    n = int(input('asd'))
    print(1/n)

    
asd2
0.5
asd0
Traceback (most recent call last):
  File "<pyshell#51>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero


try:
    n = int(input('asd'))
    print(1/n)
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asdsadas
Хьюстон у нас проблемки... (0_0)
try:
    n = int(input('asd'))
    print(1/n)
except ValueError:
    print('Value error - sorry...')
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asd123
0.008130081300813009
try:
    n = int(input('asd'))
    print(1/n)
except ValueError:
    print('Value error - sorry...')
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asd0
Хьюстон у нас проблемки... (0_0)


try:
    n = int(input('asd'))
    print(1/n)
except ValueError:
    print('Value error - sorry...')
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asdasadasd
Value error - sorry...



try:
    n = int(input('asd'))
    print(1/n)
except ValueError:
    print('Value error - sorry...')

    
asd0
Traceback (most recent call last):
  File "<pyshell#68>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero



try:
    n = int(input('asd'))
    print(1/n)
except ValueError:
    print('Value error - sorry...')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asd0
На ноль делить нельзя!
try:
    n = int(input('asd'))
    print(1/n)
except ValueError:
    print('Value error - sorry...')
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asdasdas
Value error - sorry...


a = 1
if a == 1:
    print(10)
else:
    print(33)
elif a ==55:
    
SyntaxError: invalid syntax



try:
    n = int(input('asd'))
    print(1/n)
except Exception as e:
    print(e)
    print(e.args)
    print(e.__traceback__)

    
asdasdsad
invalid literal for int() with base 10: 'asdsad'
("invalid literal for int() with base 10: 'asdsad'",)
<traceback object at 0x0000021838947740>
try:
    n = int(input('asd'))
    print(1/n)
except Exception as e:
    print(type(e))
    print(e.args)
    print(e.__traceback__)

    
asdsfdsfdf
<class 'ValueError'>
("invalid literal for int() with base 10: 'sfdsfdf'",)
<traceback object at 0x0000021838947740>


try:
    n = int(input('asd'))
    print(1/n)
except ValueError as ve:
    print('Value error - sorry...')
    print(type(ve))
    print(ve.args)
except ZeroDivisionError as zde:
    print('На ноль делить нельзя!')
    print(type(zde))
    print(zde.args)
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asdsdadadas
Value error - sorry...
<class 'ValueError'>
("invalid literal for int() with base 10: 'sdadadas'",)


import traceback
try:
    n = int(input('asd'))
    print(1/n)
except ValueError as ve:
    print('Value error - sorry...')
    print(type(ve))
    print(ve.args)
    traceback.print_exc(ve)
except ZeroDivisionError as zde:
    print('На ноль делить нельзя!')
    print(type(zde))
    print(zde.args)
    traceback.print_exc(zde)
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asd0
На ноль делить нельзя!
<class 'ZeroDivisionError'>
('division by zero',)
Traceback (most recent call last):
  File "<pyshell#103>", line 3, in <module>
    print(1/n)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#103>", line 13, in <module>
    traceback.print_exc(zde)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 208, in print_exc
    print_exception(sys.exception(), limit=limit, file=file, chain=chain)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 129, in print_exception
    te = TracebackException(type(value), value, tb, limit=limit, compact=True)
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 1044, in __init__
    self.stack = StackSummary._extract_from_extended_frame_gen(
  File "C:\Users\Admin\AppData\Local\Programs\Python\Python313\Lib\traceback.py", line 465, in _extract_from_extended_frame_gen
    elif limit >= 0:
TypeError: '>=' not supported between instances of 'ZeroDivisionError' and 'int'
try:
    n = int(input('asd'))
    print(1/n)
except ValueError as ve:
    print('Value error - sorry...')
    print(type(ve))
    print(ve.args)
    traceback.print_tb(ve.__traceback__)
except ZeroDivisionError as zde:
    print('На ноль делить нельзя!')
    print(type(zde))
    print(zde.args)
    traceback.print_tb(zde.__traceback__)
except:
    print('Хьюстон у нас проблемки... (0_0)')

    
asd0
На ноль делить нельзя!
<class 'ZeroDivisionError'>
('division by zero',)
  File "<pyshell#105>", line 3, in <module>








n =input('-->')
-->1
if n == 1:
    print(1)
elif n == 2:
    abracadabra()
elif n == 3:
    prin(3)
else:
    print(123)

    
123
n =int(input('-->'))
-->1
if n == 1:
    print(1)
elif n == 2:
    abracadabra()
elif n == 3:
    prin(3)
else:
    print(123)

1
n =int(input('-->'))
-->2
if n == 1:
    print(1)
elif n == 2:
    abracadabra()
elif n == 3:
    prin(3)
else:
    print(123)

    
Traceback (most recent call last):
  File "<pyshell#127>", line 4, in <module>
    abracadabra()
NameError: name 'abracadabra' is not defined
n =int(input('-->'))
-->3
if n == 1:
    print(1)
elif n == 2:
    abracadabra()
elif n == 3:
    prin(3)
else:
    print(123)

    
Traceback (most recent call last):
  File "<pyshell#130>", line 6, in <module>
    prin(3)
NameError: name 'prin' is not defined. Did you mean: 'print'?


# BaseException -> Exception
# Exception --> ArithmeticError --> ZeroDivErr



try:
    1/0
except ZeroDivisionError:
    print('ZeroDivisionError')

    
ZeroDivisionError
try:
    1/0
except ArithmeticError:
    print('ArithmeticError')

ArithmeticError
except Exception:
    print('Exception')
    
SyntaxError: invalid syntax


try:
    1/0
except Exception:
    print('Exception')

    
Exception
help(ArithmeticError)
Help on class ArithmeticError in module builtins:

class ArithmeticError(Exception)
 |  Base class for arithmetic errors.
 |
 |  Method resolution order:
 |      ArithmeticError
 |      Exception
 |      BaseException
 |      object
 |
 |  Built-in subclasses:
 |      FloatingPointError
 |      OverflowError
 |      ZeroDivisionError
 |
 |  Methods defined here:
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from BaseException:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __reduce__(self, /)
 |      Helper for pickle.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __setstate__(self, object, /)
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  add_note(self, object, /)
 |      Exception.add_note(note) --
 |      add a note to the exception
 |
 |  with_traceback(self, object, /)
 |      Exception.with_traceback(tb) --
 |      set self.__traceback__ to tb and return self.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |
 |  __cause__
 |      exception cause
 |
 |  __context__
 |      exception context
 |
 |  __dict__
 |
 |  __suppress_context__
 |
 |  __traceback__
 |
 |  args

try:
    1/0
except Exception:
    print('Exception')
except ArithmeticError:
    print('ArithmeticError')
except ZeroDivisionError:
    print('ZeroDivisionError')
except IndexError:
    print('IndexError')
except:
    print('default')

    
Exception


help(dir)
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

0
0
1/0
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
raise ZeroDivisionError
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    raise ZeroDivisionError
ZeroDivisionError


n = 10
x = int(input('-->'))
-->1
try:
    n/x
except ZeroDivionError:
    print('не дели на ноль...')

    
10.0


try:
    raise ZeroDivisionError
except ZeroDivionError:
    print('не дели на ноль...')

    
Traceback (most recent call last):
  File "<pyshell#181>", line 2, in <module>
    raise ZeroDivisionError
ZeroDivisionError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#181>", line 3, in <module>
    except ZeroDivionError:
NameError: name 'ZeroDivionError' is not defined. Did you mean: 'ZeroDivisionError'?
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print('не дели на ноль...')

    
не дели на ноль...
try:
    n/x
except ZeroDivisionError:
    print('не дели на ноль...')

    
10.0


def a():
    raise ZeroDivisionError

a()
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    a()
  File "<pyshell#190>", line 2, in a
    raise ZeroDivisionError
ZeroDivisionError
def a():
    try:
        raise ZeroDivisionError
    except:
        print('ok inside')

        
a()
ok inside
def a():
    try:
        raise ZeroDivisionError
    except:
        print('ok inside')
        raise

    
a()
ok inside
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    a()
  File "<pyshell#199>", line 3, in a
    raise ZeroDivisionError
ZeroDivisionError
>>> try:
...     a()
... except:
...     print('ok outside')
... 
...     
ok inside
ok outside
>>> 
>>> 
>>> asser 0
SyntaxError: invalid syntax
>>> assert 0\
...        
KeyboardInterrupt
>>> asser []
SyntaxError: invalid syntax
>>> assert []
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    assert []
AssertionError
>>> assert {}
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    assert {}
AssertionError
>>> assert 1
>>> assert True
>>> def a(n):
...     return True if n % 2 == 0 else False
... 
>>> res = [(2, True), (3, False), (4, True)]
>>> assert a(res[0][0]) == res [0][1]
>>> assert a(res[1][0]) == res [1][1]
>>> res = [(2, True), (3, False), (4, True), (5, True)]
>>> assert a(res[3][0]) == res[3][1]
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    assert a(res[3][0]) == res[3][1]
AssertionError
>>> 
>>> 
>>> 
