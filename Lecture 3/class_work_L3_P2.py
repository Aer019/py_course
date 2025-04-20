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
...                 
n=4
number21
number22
number23
number24
>>> res_list
...                 
[21, 22, 23, 24]
>>> 
>>> 
>>> res_list = [i for i in range(int(input('n='))) if i % 2 == 0]
...                 
n=5
>>> res_list
...                 
[0, 2, 4]
>>> 
>>> 
>>> my_list = [1,2,4,4,1,4,2,6,2,9]
...                 
>>> res_list = {i for i in my_list}
...                 
>>> res_list
...                 
{1, 2, 4, 6, 9}
>>> 
>>> 
>>> li = [[1,2,3], [3,4,5], [5,6,7]]
...                 
>>> le(li)
...                 
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    le(li)
NameError: name 'le' is not defined
>>> len(li)
...                 
3
>>> li[0]
...                 
[1, 2, 3]
>>> li[1]
...                 
[3, 4, 5]
>>> li[2]
...                 
[5, 6, 7]
>>> li[0][1]
...                 
2
>>> li[1][2]
...                 
5
>>> li[2][2]
...                 
7
>>> 
>>> 
