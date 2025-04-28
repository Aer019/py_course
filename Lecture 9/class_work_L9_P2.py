Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
asdasd
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    asdasd
NameError: name 'asdasd' is not defined
123123
123123
1231231
1231231


class Client:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        
client_storage = []




class Dog:
    class_variable = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
Dog.class_variable
0
Dog.name
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Dog.name
AttributeError: type object 'Dog' has no attribute 'name'
Dog.age
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    Dog.age
AttributeError: type object 'Dog' has no attribute 'age'

dog1 = Dog('dog', 1)
dog1.name
'dog'
dog.age
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dog.age
NameError: name 'dog' is not defined. Did you mean: 'Dog'?
dog1.age
1
Dog.class_variable
0
Dog.name
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    Dog.name
AttributeError: type object 'Dog' has no attribute 'name'
Dog.age
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    Dog.age
AttributeError: type object 'Dog' has no attribute 'age'
dog1.name
'dog'
dog1.name = "Bobik"
dog1.name
'Bobik'
dog1.age = 10000
dog1.age
10000
Dog.class_variable = 10000
Dog.class_variable
10000



class Task:
    counter = 1
    def __init__(self, name):
        self.task_id = Task.counter
        Task.counter += 1
        self.task_name = name
        self.task_status = False

        
t1 = Task('go')
t2 = Task('run')
t3 = Task('sleep')
print(t1.task_id, t1.task_name, t1.task_status)
1 go False
print(t1.task_id, t1.task_name, t1.task_status)
1 go False
print(t2.task_id, t2.task_name, t2.task_status)
2 run False
print(t3.task_id, t3.task_name, t3.task_status)
3 sleep False
t4 = Task('sing')
print(t4.task_id, t4.task_name, t4.task_status)
4 sing False




class cla:
    a = 1
    def __init__(self):
        pass

    
cla.a
1
c1 = cla()
cla.a
1
c1.a
1
cla.a = 10000
cla.a
10000
c1.a
10000
c1.a = 88888
cla.a
10000
c1.a
88888



cla.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'a': 10000, '__init__': <function cla.__init__ at 0x000001FB2DCC2E80>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'cla' objects>, '__weakref__': <attribute '__weakref__' of 'cla' objects>, '__doc__': None})
class f:
    a = 9
    def __init__(self):
        pass

    
s = f()
f.a
9
s.a
9
s.__dict__
{}
f.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, 'a': 9, '__init__': <function f.__init__ at 0x000001FB2DCC2F20>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'f' objects>, '__weakref__': <attribute '__weakref__' of 'f' objects>, '__doc__': None})


class f:
    '''asdasdasdas.'''
    a = 9
    def __init__(self):
        pass

    

f.__dict__
mappingproxy({'__module__': '__main__', '__firstlineno__': 1, '__doc__': 'asdasdasdas.', 'a': 9, '__init__': <function f.__init__ at 0x000001FB2DCC2FC0>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'f' objects>, '__weakref__': <attribute '__weakref__' of 'f' objects>})
felp(f)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    felp(f)
NameError: name 'felp' is not defined. Did you mean: 'help'?
help(f)
Help on class f in module __main__:

class f(builtins.object)
 |  asdasdasdas.
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
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
 |  a = 9



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f'Hello! My name is {self.name}, and I"m {self.age} old')

        
Cat.hello()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    Cat.hello()
TypeError: Cat.hello() missing 1 required positional argument: 'self'
barsik = Cat('Barsik', 3)
barsik.hello()
Hello! My name is Barsik, and I"m 3 old


barsik.age
3



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f'Hello! My name is {self.name}, and I"m {self.age} old')
    def say(self, msg):
        print(f'{self.name} says: {msg}!')

        
barsik = Cat('Barsik', 3)
barsik.hello()
Hello! My name is Barsik, and I"m 3 old
barsik.say('Meow!')
Barsik says: Meow!!


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f'Hello! My name is {self.name}, and I"m {self.age} old')
    def say(self, msg):
        print(f'{self.name} says: {msg}!')
    def grow(self):
        self.age += 1

        
barsik = Cat('Barsik', 3)
barsik.hello()
Hello! My name is Barsik, and I"m 3 old
barsik.grow()
barsik.hello()
Hello! My name is Barsik, and I"m 4 old
barsik.grow()
barsik.hello()
Hello! My name is Barsik, and I"m 5 old


a = 1
li = [1,2,3,4]
a
1
li
[1, 2, 3, 4]
print(a, li)
1 [1, 2, 3, 4]
barsik
<__main__.Cat object at 0x000001FB2DBDB230>



a = 5
a
5
# __repr__


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f'Hello! My name is {self.name}, and I"m {self.age} old')
    def say(self, msg):
        print(f'{self.name} says: {msg}!')
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info. \nname:{self.name}\nage:{self.age}"

    
barsik = Cat('Barsik', 3)
barsik
cat info. 
name:Barsik
age:3



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f'Hello! My name is {self.name}, and I"m {self.age} old')
    def say(self, msg):
        print(f'{self.name} says: {msg}!')
    def grow(self):
        self.age += 1
    def __repr__(self):
        return f"cat info. \nname:{self.name}\nage:{self.age}"
    def __str__(self):
        return f"{self.name} | {self.age}"

    
print(barsik)
cat info. 
name:Barsik
age:3
barsik = Cat('Barsik', 3)
print(barsik)
Barsik | 3
help(init)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    help(init)
NameError: name 'init' is not defined. Did you mean: 'int'?
help(int)



help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to 'utf-8'.
 |  errors defaults to 'strict'.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __getnewargs__(self, /)
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __hash__(self, /)
 |      Return hash(self).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mod__(self, value, /)
 |      Return self%value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmod__(self, value, /)
 |      Return value%self.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |
 |  __str__(self, /)
 |      Return str(self).
 |
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  count(self, sub[, start[, end]], /)
 |      Return the number of non-overlapping occurrences of substring sub in string S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |
 |  endswith(self, suffix[, start[, end]], /)
 |      Return True if the string ends with the specified suffix, False otherwise.
 |
 |      suffix
 |        A string or a tuple of strings to try.
 |      start
 |        Optional start position. Default: start of the string.
 |      end
 |        Optional stop position. Default: end of the string.
 |
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |
 |  find(self, sub[, start[, end]], /)
 |      Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
 |
 |  format(self, /, *args, **kwargs)
 |      Return a formatted version of the string, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  format_map(self, mapping, /)
 |      Return a formatted version of the string, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |
 |  index(self, sub[, start[, end]], /)
 |      Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
 |
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |
 |      Call keyword.iskeyword(s) to test whether string s is a reserved identifier,
 |      such as "def" or "class".
 |
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |
 |  removeprefix(self, prefix, /)
 |      Return a str with the given prefix string removed if present.
 |
 |      If the string starts with the prefix string, return string[len(prefix):].
 |      Otherwise, return a copy of the original string.
 |
 |  removesuffix(self, suffix, /)
 |      Return a str with the given suffix string removed if present.
 |
 |      If the string ends with the suffix string and that suffix is not empty,
 |      return string[:-len(suffix)]. Otherwise, return a copy of the original
 |      string.
 |
 |  replace(self, old, new, /, count=-1)
 |      Return a copy with all occurrences of substring old replaced by new.
 |
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |
 |  rfind(self, sub[, start[, end]], /)
 |      Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Return -1 on failure.
 |
 |  rindex(self, sub[, start[, end]], /)
 |      Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].
 |
 |      Optional arguments start and end are interpreted as in slice notation.
 |      Raises ValueError when the substring is not found.
 |
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |
 |      Padding is done using the specified fill character (default is a space).
 |
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the end of the string and works to the front.
 |
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the substrings in the string, using sep as the separator string.
 |
 |        sep
 |          The separator used to split the string.
 |
 |          When set to None (the default value), will split on any whitespace
 |          character (including \n \r \t \f and spaces) and will discard
 |          empty strings from the result.
 |        maxsplit
 |          Maximum number of splits.
 |          -1 (the default value) means no limit.
 |
 |      Splitting starts at the front of the string and works to the end.
 |
 |      Note, str.split() is mainly useful for data that has been intentionally
 |      delimited.  With natural text that includes punctuation, consider using
 |      the regular expression module.
 |
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |
 |  startswith(self, prefix[, start[, end]], /)
 |      Return True if the string starts with the specified prefix, False otherwise.
 |
 |      prefix
 |        A string or a tuple of strings to try.
 |      start
 |        Optional start position. Default: start of the string.
 |      end
 |        Optional stop position. Default: end of the string.
 |
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace removed.
 |
 |      If chars is given and not None, remove characters in chars instead.
 |
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |
 |      The string is never truncated.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  maketrans(x, y=<unrepresentable>, z=<unrepresentable>, /)
 |      Return a translation table usable for str.translate().
 |
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.



Dog.__bases__
(<class 'object'>,)
Cat.__bases__
(<class 'object'>,)


# swimming_cat
class SwinningCat(Cat):
    def swim(self):
        print('Я могу плавать!')

        
sadik = SwimmingCat('sadik', 2)
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    sadik = SwimmingCat('sadik', 2)
NameError: name 'SwimmingCat' is not defined. Did you mean: 'SwinningCat'?
sadik = SwinningCat('sadik', 2)
sadik.name
'sadik'
sadik.age
2
sadik
cat info. 
name:sadik
age:2
print(sadik)
sadik | 2
sadik.swim()
Я могу плавать!
type(sadik)
<class '__main__.SwinningCat'>
sadik.grow()


class SwimmingCat(Cat):
    def swim(self):
        print('Я могу плавать!')
    def __str__(self):
        return f'SwimmingCat:{self.name} | {self.age}
    
SyntaxError: unterminated f-string literal (detected at line 5)
class SwimmingCat(Cat):
    def swim(self):
        print('Я могу плавать!')
    def __str__(self):
        return f'SwimmingCat:{self.name} | {self.age}'

    
print(sadik)
sadik | 3
sadik = SwinningCat('sadik', 2)
print(sadik)
sadik | 2
sadik = SwimmingCat('sadik', 2)
print(sadik)
SwimmingCat:sadik | 2


sadik = SwimmingCat('sadik', 2, 'RED')
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    sadik = SwimmingCat('sadik', 2, 'RED')
TypeError: Cat.__init__() takes 3 positional arguments but 4 were given


# class
# class Name(от кого наследуемся через запятую):
# super().__init__(...) - это позволит дернуть родительский конструктор
# super().hello() - чтобы вызвать метод из родителя



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hello(self):
        print(f'Hello! My name is {self.name}, and I"m {self.age} old')
    def __str__(self):
        return f"{self.name} | {self.age}"

    
c1 = Cat('jojo', 1)
c1.hello
<bound method Cat.hello of <__main__.Cat object at 0x000001FB2DBDB0E0>>
c1.hello()
Hello! My name is jojo, and I"m 1 old
c1.name
'jojo'
c1.name = 'NoName'
c1.hello()
Hello! My name is NoName, and I"m 1 old
c1.name
'NoName'


class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def hello(self):
        print(f'Hello! My name is {self.name}, and I"m {self.age} old')
    def __str__(self):
        return f"{self.name} | {self.age}"

    
c1 = Cat('jojo', 1)
c1.name
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    c1.name
AttributeError: 'Cat' object has no attribute 'name'
>>> class Cat:
...     def __init__(self, name, age):
...         self.__name = name
...         self.age = age
...     def hello(self):
...         print(f'Hello! My name is {self.name}, and I"m {self.age} old')
...     def __str__(self):
...         return f"{self.name} | {self.age}"
...     def change_name(self, name):
...         self.__name = name
... 
...         
>>> c1._name
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    c1._name
AttributeError: 'Cat' object has no attribute '_name'
>>> c1.__name
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    c1.__name
AttributeError: 'Cat' object has no attribute '__name'
>>> c1.hello()
Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    c1.hello()
  File "<pyshell#233>", line 6, in hello
    print(f'Hello! My name is {self.name}, and I"m {self.age} old')
AttributeError: 'Cat' object has no attribute 'name'
>>> c1 = Cat('jojo', 1)
>>> c1.__name
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    c1.__name
AttributeError: 'Cat' object has no attribute '__name'
>>> c1.hello()
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    c1.hello()
  File "<pyshell#239>", line 6, in hello
    print(f'Hello! My name is {self.name}, and I"m {self.age} old')
AttributeError: 'Cat' object has no attribute 'name'
