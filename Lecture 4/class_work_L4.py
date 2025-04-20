Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
se = {1,2,3,4,5}
se
{1, 2, 3, 4, 5}
li = [1,2,3,4,5,66,3,2,1]
li
[1, 2, 3, 4, 5, 66, 3, 2, 1]
print(li)
[1, 2, 3, 4, 5, 66, 3, 2, 1]


for val in li:
    print(val)

    
1
2
3
4
5
66
3
2
1
se = {1,2,3,4,5, -3, 55, 'asdasd', 'a', 'sdsd'}
se
{1, 2, 3, 4, 5, 'sdsd', 55, 'asdasd', 'a', -3}
print(se)
{1, 2, 3, 4, 5, 'sdsd', 55, 'asdasd', 'a', -3}
sorted(se)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sorted(se)
TypeError: '<' not supported between instances of 'str' and 'int'
for i in sorted(se):
    print(i, end='')

    
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for i in sorted(se):
TypeError: '<' not supported between instances of 'str' and 'int'
li
[1, 2, 3, 4, 5, 66, 3, 2, 1]
li = [1,2,3,4,5, 'asdsa', 1,4,5,10]
li += li
li
[1, 2, 3, 4, 5, 'asdsa', 1, 4, 5, 10, 1, 2, 3, 4, 5, 'asdsa', 1, 4, 5, 10]
res = set(li)
res
{1, 2, 3, 4, 5, 10, 'asdsa'}
res = list(se)
res
[1, 2, 3, 4, 5, 'sdsd', 55, 'asdasd', 'a', -3]
li += res
li = list(set(li))
li
[1, 2, 3, 4, 5, 'sdsd', 10, 'asdasd', 55, 'asdsa', 'a', -3]
text = "abcdefgabcdefgh"
text[0]
'a'
res = set(text)
res
{'d', 'g', 'f', 'e', 'h', 'c', 'a', 'b'}
res = list(res)
res
['d', 'g', 'f', 'e', 'h', 'c', 'a', 'b']


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
res_list = list(set(my_list)







                
KeyboardInterrupt
res_list = list(set(my_list))
                
res_list
                
[1, 2, 4, 6, 9]



result_list = []
                
for val in my_list:
    result_list.append(val ** 2)

                
result_list
                
[1, 4, 16, 16, 1, 16, 4, 36, 4, 81]
result_list = []
                
for val in my_list:
    if val % 2 == 0
        result_list.append(val ** 2)
                
SyntaxError: expected ':'
for val in my_list:
    if val % 2 == 0:
        result_list.append(val ** 2)

                
result_list
                
[4, 16, 16, 16, 4, 36, 4]


res_list
                
[1, 2, 4, 6, 9]
res_list = [int(input('number')) for i in range(int(input('n=')))]
                
n=22
number33
number445
number
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    res_list = [int(input('number')) for i in range(int(input('n=')))]
5ValueError: invalid literal for int() with base 10: ''
4
5
                
5

res_list = [int(input('number')) for i in range(int(input('n=')))]
                
n=4
number21
number22
number23
number24
res_list
                
[21, 22, 23, 24]


res_list = [i for i in range(int(input('n='))) if i % 2 == 0]
                
n=5
res_list
                
[0, 2, 4]


my_list = [1,2,4,4,1,4,2,6,2,9]
                
res_list = {i for i in my_list}
                
res_list
                
{1, 2, 4, 6, 9}


li = [[1,2,3], [3,4,5], [5,6,7]]
                
le(li)
                
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    le(li)
NameError: name 'le' is not defined
len(li)
                
3
li[0]
                
[1, 2, 3]
li[1]
                
[3, 4, 5]
li[2]
                
[5, 6, 7]
li[0][1]
                
2
li[1][2]
                
5
li[2][2]
                
7


sadasdd
                
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    sadasdd
NameError: name 'sadasdd' is not defined
new_list = li
                
new_list
                
[[1, 2, 3], [3, 4, 5], [5, 6, 7]]


st = '1232332sqdasdas'
                
s2 = 'sadsaddsa'
                
s3 = 'nAme Dome No'
                
print(st)
                
1232332sqdasdas
print(s2)
                
sadsaddsa
print(s3)
                
nAme Dome No
len(st)
                
15
len(s2)
                
9
len(s3)
                
12
a = 'hello'
                
b = 'Hello'
                
c = 'hello'
                
a == b
                
False
a == c
                
True
b == a
                
False
b == c
                
False
a = 'saddsadsad'
                
b = "asdsaddsadsad"
                
a
                
'saddsadsad'
b
                
'asdsaddsadsad'
a += b
                
a
                
'saddsadsadasdsaddsadsad'
a + b = a
                
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
a + b == a
                
False
a *= b
                
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    a *= b
TypeError: can't multiply sequence by non-int of type 'str'
a * 9
                
'saddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsad'
9 * a
                
'saddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsad'
a
                
'saddsadsadasdsaddsadsad'
a *= 3
                
a
                
'saddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsad'
a
                
'saddsadsadasdsaddsadsadsaddsadsadasdsaddsadsadsaddsadsadasdsaddsadsad'
ord
                
<built-in function ord>
chr
                
<built-in function chr>
help(chr)
                
Help on built-in function chr in module builtins:

chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

a = 'a'
                
a
                
'a'
ord(a)
                
97
ord('D')
                
68
ord('d')
                
100
ord('*')
                
42
ord('П')
                
1055


chr(1055)
                
'П'
chr(10000)
                
'✐'
chr(20000)
                
'丠'
for i in range(23500, 23600):
                print(chr(i), end='')

                
富寍寎寏寐寑寒寓寔寕寖寗寘寙寚寛寜寝寞察寠寡寢寣寤寥實寧寨審寪寫寬寭寮寯寰寱寲寳寴寵寶寷寸对寺寻导寽対寿尀封専尃射尅将將專尉尊尋尌對導小尐少尒尓尔尕尖尗尘尙尚尛尜尝尞尟尠尡尢尣尤尥尦尧尨尩尪尫尬尭尮尯
s = '富寍寎寏寐寑寒寓寔寕寖寗寘寙寚寛寜寝寞察寠寡寢寣寤寥實寧寨審寪寫寬寭寮寯寰寱寲寳寴寵寶寷寸对寺寻导寽対寿尀封専尃射尅将將專尉尊尋尌對導小尐少尒尓尔尕尖尗尘尙尚尛尜尝尞尟尠尡尢尣尤尥尦尧尨尩尪尫尬尭尮尯'
                
for i in s:
                print(ord(i), end='')

                
23500235012350223503235042350523506235072350823509235102351123512235132351423515235162351723518235192352023521235222352323524235252352623527235282352923530235312353223533235342353523536235372353823539235402354123542235432354423545235462354723548235492355023551235522355323554235552355623557235582355923560235612356223563235642356523566235672356823569235702357123572235732357423575235762357723578235792358023581235822358323584235852358623587235882358923590235912359223593235942359523596235972359823599



s = 'hello'
                
len[0]
                
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    len[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
les(s)
                
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    les(s)
NameError: name 'les' is not defined. Did you mean: 'res'?
for letter in s:
        print(letter)

                
h
e
l
l
o
len(s)
                
5
for i in range(len(s)):
                print(i, s[i])

                
0 h
1 e
2 l
3 l
4 o
li = [1,2,3,4,5]
                
len(li)
                
5
for i in range(len(li)):
                print(i, li[i])

                
0 1
1 2
2 3
3 4
4 5


secret_key = 5
                
text = "abcdefgh"
                
# chr ord
                
ord("a")
                
97
message = 'Привет! Наш гонец отправлен в Филадельфию, чтобы предупредить командующего Петра первого о вторжении."
                
SyntaxError: unterminated string literal (detected at line 1)
message = 'Привет! Наш гонец отправлен в Филадельфию, чтобы предупредить командующего Петра первого о вторжении.'
                
secured_message = ""
                
secret_key = 5
                
for letter in message:
                secured_message += chr(ord(letter) + secret_key)

                
secured_message
                
'Фхнзкч&%Теэ%иуткы%учфхезркт%з%Щнрейкрёщнѓ1%ьчужѐ%фхкйшфхкйнчё%пусетйшѓюкиу%Фкчхе%фкхзуиу%у%зчухлктнн3'
# получатель
                
secured_message
                
'Фхнзкч&%Теэ%иуткы%учфхезркт%з%Щнрейкрёщнѓ1%ьчужѐ%фхкйшфхкйнчё%пусетйшѓюкиу%Фкчхе%фкхзуиу%у%зчухлктнн3'
result_message = ''
                
for letter in secured_message:
                result_message += chr(ord(letter) - secret_key)

                
result_message
                
'Привет! Наш гонец отправлен в Филадельфию, чтобы предупредить командующего Петра первого о вторжении.'



s = 'hello'
                
print(s)
                
hello
s
                
'hello'
s[:3]
                
'hel'
s[1:4]
                
'ell'
s[:]
                
'hello'
s[1:]
                
'ello'
s[::-1]
                
'olleh'
# string[start:end:step]
                
li = [1,2,3,4,5]
                
li[1:4]
                
[2, 3, 4]
s[::2]
                
'hlo'
s[::3]
                
'hl'
s[-1][-2][-3][-4]
                
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    s[-1][-2][-3][-4]
IndexError: string index out of range
s = ""
                
s
                
''
s = 'a b c d e'
                
len(s)
                
9
s[4]
                
'c'


s[:4]
                
'a b '
s[5:]
                
' d e'
C
                
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    C
NameError: name 'C' is not defined
'C'
                
'C'
res_string = s[:4] + "C" + s[5:]
                
res_string
                
'a b C d e'
s
                
'a b c d e'
# in not in
                
'a' in res_string
                
True
"" in res_string
                
True
'B' in res_string
                
False


del s
                
s
                
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    s
NameError: name 's' is not defined
s = 'a b c d e'
                
min
                
<built-in function min>
max
                
<built-in function max>
help(min)
                
Help on built-in function min in module builtins:

min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more positional arguments, return the smallest argument.

li = [1,2,3,4,5,66666]
                
max(min)
                
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    max(min)
TypeError: 'builtin_function_or_method' object is not iterable
max(li)
                
66666
min(li)
                
1
s
                
'a b c d e'
min(s)
                
' '
max(s)
                
'e'




s = 'hello'
                
s.upper
                
<built-in method upper of str object at 0x0000023E0909EDF0>
s.upper()
                
'HELLO'
s
                
'hello'
s = s.upper()
                
s
                
'HELLO'
s.lower
                
<built-in method lower of str object at 0x0000023E0B4478A0>
s.lower()
                
'hello'
s
                
'HELLO'
s = s.lower
                
s
                
<built-in method lower of str object at 0x0000023E0B4478A0>
s
                
<built-in method lower of str object at 0x0000023E0B4478A0>
s = s.lower()
                
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    s = s.lower()
AttributeError: 'builtin_function_or_method' object has no attribute 'lower'
s = 'HELLO'
                
s = s.lower()
                
s
                
'hello'
s.title()
                
'Hello'
s.capitalize()
                
'Hello'
s = 'hello hello hello'
                
s.swapcase()
                
'HELLO HELLO HELLO'
s
                
'hello hello hello'
s.translate()
                
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    s.translate()
TypeError: str.translate() takes exactly one argument (0 given)
s.isalpha
                
<built-in method isalpha of str object at 0x0000023E0B4256F0>
s
                
'hello hello hello'
s.isalpha()
                
False
s.isalnum()
                
False


name = input("-->").capitalize()
                
-->peter
name
                
'Peter'
s = '   peter   '
                
s
                
'   peter   '
s.title()
                
'   Peter   '
name = input("-->").strip().capitalize()
                
-->         G  i ggggga
name
                
'G  i ggggga'


name
                
'G  i ggggga'
name = 'Peter'
                
name
                
'Peter'
name.replace('et', 'olo')
                
'Poloer'
name
                
'Peter'
>>> url = "https://vk.com/"
...                 
>>> url = url.replace(" .com", " .org")
...                 
>>> url
...                 
'https://vk.com/'
>>> url
...                 
'https://vk.com/'
>>> url = url.replace(".com", ".org")
...                 
>>> url
...                 
'https://vk.org/'
>>> 
>>> 
>>> numbers = input('-->')
...                 
-->1 2 3 4 5 6 7 8
>>> numbers
...                 
'1 2 3 4 5 6 7 8'
>>> numbers.split()
...                 
['1', '2', '3', '4', '5', '6', '7', '8']
>>> numbers = numbers.split()
...                 
>>> re_list = []
...                 
>>> for i in numbers:
...                 re_list.append(int(i))
... 
...                 
>>> re_list
...                 
[1, 2, 3, 4, 5, 6, 7, 8]
>>> sum(res_list)
...                 
22
>>> sum(re_list)
...                 
36
>>> nums = [int(snumber) for snumber in input("-->").split()]
...                 
-->1 2 3 4 5 6 7 8 9 10
>>> nums
...                 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> max(nums)
...                 
10
>>> min(nums)
...                 
1
>>> sum(nums)
...                 
55
