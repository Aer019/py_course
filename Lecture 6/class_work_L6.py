Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(123)
123
1+5
6
li = [1,2,3]
fields = ('name', 'phone', 1232131)
type(fileds)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(fileds)
NameError: name 'fileds' is not defined. Did you mean: 'fields'?
type(fields)
<class 'tuple'>


# empty tulpes
tp = ()
type(tp)
<class 'tuple'>
tp
()
tp1 = tuple()
tp1
()

li = [1]
li
[1]
se = {1}
se
{1}

# one element tuple
tp = (1)
tp(tp)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tp(tp)
TypeError: 'int' object is not callable
type(tp)
<class 'int'>
tp
1
tp = (1,)
type(tp)
<class 'tuple'>
tp
(1,)
tp = 1,
tp
(1,)
li = [1,2,3]
se = {1,2,3}
st = '12312'
tp = (1,2,3)
li
[1, 2, 3]
se
{1, 2, 3}
st
'12312'
tp
(1, 2, 3)


tp = 1, 2, 3
tp
(1, 2, 3)
tp[0]
1
tp[1]
2
tp[2]
3
tp[3]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tp[3]
IndexError: tuple index out of range
len(li)
3
len(tp)
3


tp
(1, 2, 3)
tp[-3]
1


tp = (1., 2., 3., .4,)
tp
(1.0, 2.0, 3.0, 0.4)

# unchangeable

li
[1, 2, 3]
li.append(123)
li
[1, 2, 3, 123]
tp[0] = 444
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    tp[0] = 444
TypeError: 'tuple' object does not support item assignment


li
[1, 2, 3, 123]
tp
(1.0, 2.0, 3.0, 0.4)
tp = (1.0, 2.0, 3.0, 0.4, li)
tp
(1.0, 2.0, 3.0, 0.4, [1, 2, 3, 123])
li.pop()
123
tp
(1.0, 2.0, 3.0, 0.4, [1, 2, 3])


# unpack

li = [1,2,3,45]
tp = (1,2,3,45)

a,b,c,d = tp
a
1
b
2
c
3
d
45
st = '12345'
a,b,c,d,e = st
a
'1'
b
'2'
c
'3'
d
'4'
e
'5'

tp = (1,2,3)
number, *fields = tp
bumber
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    bumber
NameError: name 'bumber' is not defined. Did you mean: 'number'?
number
1
fields
[2, 3]


def ret_tuple():
    return(1,2,3,4,5)

ret_tuple
<function ret_tuple at 0x0000016CEE7E3C40>
ret_tuple()
(1, 2, 3, 4, 5)


a, *b, c =ret_tuple()
a
1
b
[2, 3, 4]
c
5
ret_tuple()
(1, 2, 3, 4, 5)
*a = ret_tuple()
SyntaxError: starred assignment target must be in a list or tuple
*a, b = ret_tuple()
a
[1, 2, 3, 4]
b
5


tp = 1,
tp
(1,)
tp = 3.,
tp
(3.0,)


tp = 1,2,3,4,5,6
tp
(1, 2, 3, 4, 5, 6)
tp[:3]
(1, 2, 3)
tp[3:]
(4, 5, 6)
tp[::2]
(1, 3, 5)
tp[::-1]
(6, 5, 4, 3, 2, 1)
tp
(1, 2, 3, 4, 5, 6)
tp2 = 2,3,4,5,6
tp2
(2, 3, 4, 5, 6)
tp+tp2
(1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6)
tp*tp2
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    tp*tp2
TypeError: can't multiply sequence by non-int of type 'tuple'
tp*5
(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
3*tp2
(2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6)
6 in tp
True
77 in tp
False
2in tp
True
3in tp
True
tp, tp2 = tp2, tp
tp2
(1, 2, 3, 4, 5, 6)
tp
(2, 3, 4, 5, 6)




tp
(2, 3, 4, 5, 6)
tp[:3]
(2, 3, 4)
tp[-1]
6
(22,33,44)
(22, 33, 44)
1 + (12,3,)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    1 + (12,3,)
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
result_tuple = tp[:3] + (22, 33, 44) + tp[4:]
tp[4:]
(6,)
result_tuple
(2, 3, 4, 22, 33, 44, 6)


del result_tuple
tp
(2, 3, 4, 5, 6)
tp.count(3)
1
tp.count(33)
0
tp.index(4)
2


4 in tp
True
n = int(input())
5
n
5
tp
(2, 3, 4, 5, 6)
if n in tp:
    print('index:', tp.index(n))
    print('value:', tp[tp.index(n)])

    
index: 3
value: 5


tp
(2, 3, 4, 5, 6)
tp = tp[:3]
tp
(2, 3, 4)
tp = (2, 3, 4, 5, 6)
tp = tuple(list(tp).pop().pop())
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    tp = tuple(list(tp).pop().pop())
AttributeError: 'int' object has no attribute 'pop'
tp = list(tp)
tp
[2, 3, 4, 5, 6]
tp.pop()
6
tp.pop()
5
tp
[2, 3, 4]
tp = tuple(tp)
tp
(2, 3, 4)

tp
(2, 3, 4)
# for by value, by index
for value in tp:
    print(value**2)

    
4
9
16
for i in range(len(tp)):
    print(i, tp[i])

    
0 2
1 3
2 4


# dictionary



di ={}
di
{}
type(di)
<class 'dict'>
di = dict()
di
{}
di = {1:'one',}
di = {1:'one', 2:'two', 3:'hello', 4:444, 5:(1,2,3,4)}
di
{1: 'one', 2: 'two', 3: 'hello', 4: 444, 5: (1, 2, 3, 4)}


di[2]
'two'
di[5]
(1, 2, 3, 4)
di[123]
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    di[123]
KeyError: 123
di = {1:'one', 2:'two', '333':1234, (2,3):'tulpe', 5:(1,2,3,4)}
di[333]
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    di[333]
KeyError: 333
di['333']
1234
hash
<built-in function hash>
help(hash)
Help on built-in function hash in module builtins:

hash(obj, /)
    Return the hash value for the given object.

    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.

hash(2)
2
hash('234')
1229436734601929601
hash('234')
1229436734601929601
hash(3.4)
922337203685477379
di = {2:222, 2:22222, 2:22222222}
di
{2: 22222222}


hash(1)
1
hash(0)
0
has('')
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    has('')
NameError: name 'has' is not defined. Did you mean: 'hash'?
hash('')
0


di = {1:111}
di[1]
111
di[True]
111
hash(())
5740354900026072187


di = {1:1111, 0:12313231}
di[0]
12313231
di[False]
12313231


di = {1:111, 0:1231231312, '':'empty'}
di[0]
1231231312
di[False]
1231231312
di['']
'empty'


di
{1: 111, 0: 1231231312, '': 'empty'}
di.get('')
'empty'
di.get(123123)
di.values()
dict_values([111, 1231231312, 'empty'])
di.items()
dict_items([(1, 111), (0, 1231231312), ('', 'empty')])
di.keys()
dict_keys([1, 0, ''])
dipopitem()
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    dipopitem()
NameError: name 'dipopitem' is not defined
di
{1: 111, 0: 1231231312, '': 'empty'}
di.pop(0)
1231231312
di
{1: 111, '': 'empty'}
di.update({11:1111111})
di
{1: 111, '': 'empty', 11: 1111111}
di.update({1:-1})
di
{1: -1, '': 'empty', 11: 1111111}
1 in di
True
11 in di
True
12 in di
False


di = {1:111, 0:1231231312, '':'empty'}

for key in di.keys():
    print(key)

    
1
0

for key in di.values():
    print(key)

    
111
1231231312
empty


di = {str(i): i**3 for i in range(10)}
di
{'0': 0, '1': 1, '2': 8, '3': 27, '4': 64, '5': 125, '6': 216, '7': 343, '8': 512, '9': 729}




# students avg

()
()
score = ()
score
()
6
6
score += (6, )
score
(6,)
score += (9, )
score
(6, 9)
score += (10, )
score
(6, 9, 10)
len(score)
3
sum(score)/len(score)
8.333333333333334
(sum(score)/len(score)).round(2)
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    (sum(score)/len(score)).round(2)
AttributeError: 'float' object has no attribute 'round'
round(sum(score)/len(score)), 2)
SyntaxError: unmatched ')'
round((sum(score)/len(score)), 2)
8.33
def avg(score):
     return round((sum(score)/len(score)), 2)

    
score
(6, 9, 10)
avg(score)
8.33
students_grades = {}
def new_grade(student_name, grade):
    if len(student_name) <2:
        return False
    
    student_name = student_name.title()
    if student_name in student_grades:
        students_grades.update(student_grades.ge(student_name) + (grade, ))
    else:
        students_grades.update({student_name:(grade, )})
    return True

student_grades
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    student_grades
NameError: name 'student_grades' is not defined. Did you mean: 'students_grades'?
students_grades
{}
new_grade('петя петров', 7)
Traceback (most recent call last):
  File "<pyshell#318>", line 1, in <module>
    new_grade('петя петров', 7)
  File "<pyshell#315>", line 6, in new_grade
    if student_name in student_grades:
NameError: name 'student_grades' is not defined. Did you mean: 'students_grades'?
def new_grade(student_name, grade):
    if len(student_name) <2:
        return False
    
    student_name = student_name.title()
    if student_name in student_grades:
        students_grades.update(student_grades.ge(student_name) + (grade, ))
    else:
        students_grades.update({student_name:(grade, )})
    return True

new_grade('петя петров', 7)
Traceback (most recent call last):
  File "<pyshell#320>", line 1, in <module>
    new_grade('петя петров', 7)
  File "<pyshell#319>", line 6, in new_grade
    if student_name in student_grades:
NameError: name 'student_grades' is not defined. Did you mean: 'students_grades'?
def new_grade(student_name, grade):
    if len(student_name) <2:
        return False
    
    student_name = student_name.title()
    if student_name in students_grades:
        students_grades.update(students_grades.ge(student_name) + (grade, ))
    else:
        students_grades.update({student_name:(grade, )})
    return True


new_grade('петя петров', 7)
True
student_grades
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    student_grades
NameError: name 'student_grades' is not defined. Did you mean: 'students_grades'?
students_grades
{'Петя Петров': (7,)}
new_grade('петя петров', 10)
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    new_grade('петя петров', 10)
  File "<pyshell#322>", line 7, in new_grade
    students_grades.update(students_grades.ge(student_name) + (grade, ))
AttributeError: 'dict' object has no attribute 'ge'
def new_grade(student_name, grade):
    if len(student_name) <2:
        return False
    
    student_name = student_name.title()
    
    if student_name in students_grades:
        students_grades.update({student_name: students_grades.ge(student_name) + (grade, )})
    else:
        students_grades.update({student_name:(grade, )})
    return True

new_grade('петя петров', 10)
Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    new_grade('петя петров', 10)
  File "<pyshell#329>", line 8, in new_grade
    students_grades.update({student_name: students_grades.ge(student_name) + (grade, )})
AttributeError: 'dict' object has no attribute 'ge'
def new_grade(student_name, grade):
    if len(student_name) <2:
        return False
    
    student_name = student_name.title()
    
    if student_name in students_grades:
        students_grades.update({student_name: students_grades.get(student_name) + (grade, )})
    else:
        students_grades.update({student_name:(grade, )})
    return True


new_grade('петя петров', 10)
True
students_grade
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    students_grade
NameError: name 'students_grade' is not defined. Did you mean: 'students_grades'?
students_grades
{'Петя Петров': (7, 10)}
new_grade('петя петров', 6)
True
students_grades
{'Петя Петров': (7, 10, 6)}
avg(students_grates.get('Петя Петров'))
Traceback (most recent call last):
  File "<pyshell#339>", line 1, in <module>
    avg(students_grates.get('Петя Петров'))
NameError: name 'students_grates' is not defined. Did you mean: 'students_grades'?
avg(students_grades.get('Петя Петров'))
7.67
def show_grade():
    print('show grades')
    for key, value in students_grades.items():
        print('name:', key)
        print('grades:', value)

        
show_grades()
Traceback (most recent call last):
  File "<pyshell#346>", line 1, in <module>
    show_grades()
NameError: name 'show_grades' is not defined. Did you mean: 'show_grade'?
show_grades
Traceback (most recent call last):
  File "<pyshell#347>", line 1, in <module>
    show_grades
NameError: name 'show_grades' is not defined. Did you mean: 'show_grade'?
show_grades()
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    show_grades()
NameError: name 'show_grades' is not defined. Did you mean: 'show_grade'?
show_grade()
show grades
name: Петя Петров
grades: (7, 10, 6)
def show_avg():
    print('show avg')
    for key, value in students_grades.items():
        print('name:', key)
        print('avg:', avg(value))

        
show_avg()
show avg
name: Петя Петров
avg: 7.67


operation = input('1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm')
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm1
while operation != 'quit':
    match operation:
        case '1':
            name = input('Put full name:')
            grade = int(input('Put grade:'))
            new_grade(name, grade)     
        case '2':
            show_avg()
        case '3':
            show_grades()
        case_:
            
SyntaxError: invalid syntax
while operation != 'quit':
    match operation:
        case '1':
            name = input('Put full name:')
            grade = int(input('Put grade:'))
            new_grade(name, grade)     
        case '2':
            show_avg()
        case '3':
            show_grades()
        case _:
            print('Сорри не понял ')
    operation = input('1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm')

    
Put full name:Вася сиДОров
Put grade:9
True
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm3
Traceback (most recent call last):
  File "<pyshell#369>", line 10, in <module>
    show_grades()
NameError: name 'show_grades' is not defined. Did you mean: 'show_grade'?
while operation != 'quit':
    match operation:
        case '1':
            name = input('Put full name:')
            grade = int(input('Put grade:'))
            new_grade(name, grade)     
        case '2':
            show_avg()
        case '3':
            show_grade()
        case _:
            print('Сорри не понял ')
    operation = input('1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm')

    
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9,)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm3
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9,)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm2
show avg
name: Петя Петров
avg: 7.67
name: Вася Сидоров
avg: 9.0
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programmquit
def main():
    operation = input('1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm')
    while operation != 'quit':
        match operation:
            case '1':
                name = input('Put full name:')
                grade = int(input('Put grade:'))
                new_grade(name, grade)     
            case '2':
                show_avg()
            case '3':
                show_grade()
            case _:
                print('Сорри не понял ')
            operation = input('1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm')
            
SyntaxError: invalid syntax
def main():
    operation = input('1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm')
    while operation != 'quit':
        match operation:
            case '1':
                name = input('Put full name:')
                grade = int(input('Put grade:'))
                new_grade(name, grade)     
            case '2':
                show_avg()
            case '3':
                show_grade()
            case _:
                print('Сорри не понял ')
        operation = input('1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm')

        
main()
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm3
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9,)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm1
Put full name:петя петоров
Put grade:8 
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm3
show grades
name: Петя Петров
grades: (7, 10, 6)
name: Вася Сидоров
grades: (9,)
name: Петя Петоров
grades: (8,)
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programm2
show avg
name: Петя Петров
avg: 7.67
name: Вася Сидоров
avg: 9.0
name: Петя Петоров
avg: 8.0
1 - new grade, 2 - show avg, 3 - show grades, quit - exit programmquit
type(key)
<class 'str'>
type(value)
<class 'int'>
type(avg(value))
Traceback (most recent call last):
  File "<pyshell#380>", line 1, in <module>
    type(avg(value))
  File "<pyshell#302>", line 2, in avg
    return round((sum(score)/len(score)), 2)
TypeError: 'int' object is not iterable
type(operation)
<class 'str'>



# TODO List
# task task_id status
task_list = {}
di = {}
di[1] = {"task_name":"go to school", "status":False}
di
{1: {'task_name': 'go to school', 'status': False}}

task_auto_id = 1
def create_task():
    t_name = input('Дай имя задачи:')
    t_status = False
    task_list[task_auto_id] = {"task_name
                               
SyntaxError: unterminated string literal (detected at line 4)
def create_task():
    t_name = input('Дай имя задачи:')
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name, "status":False}
    return True

task_list
{}
create_task
<function create_task at 0x0000016CEE81C900>
create_task()
Дай имя задачи:asdasdasd
True
task_list
{1: {'task_name': 'asdasdasd', 'status': False}}
def create_task():
    global task_auto_id
    t_name = input('Дай имя задачи:')
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name, "status":False}
    task_auto_id += 1
    return True

create_task()
Дай имя задачи:asdsad
True
task_list
{1: {'task_name': 'asdsad', 'status': False}}
create_task()
Дай имя задачи:fdsfsdfsdf
True
create_task()
Дай имя задачи:dsfsdfsdfsdfsdf
True
task_list
{1: {'task_name': 'asdsad', 'status': False}, 2: {'task_name': 'fdsfsdfsdf', 'status': False}, 3: {'task_name': 'dsfsdfsdfsdfsdf', 'status': False}}
def show_tasks():
    print('show tasks')
    for task_id, description in task_list.items():
        print("__________")
        print(f'Task id:{task_id}')
        for key, value in description.items():
            print("\t",key, value)
        print("_____________")

        

show_tasks()
show tasks
__________
Task id:1
	 task_name asdsad
	 status False
_____________
__________
Task id:2
	 task_name fdsfsdfsdf
	 status False
_____________
__________
Task id:3
	 task_name dsfsdfsdfsdfsdf
	 status False
_____________

def change_status():
    task_id = int(input("asdad:"))
    if task_id not in task_list:
        return False
    inside = task_list.get(task_id)
    inside["status"] = True
    task_list.update({task_id:inside})

    
change_status()
asdad:5
False
change_status()
asdad:3
show_tasks()
show tasks
__________
Task id:1
	 task_name asdsad
	 status False
_____________
__________
Task id:2
	 task_name fdsfsdfsdf
	 status False
_____________
__________
Task id:3
	 task_name dsfsdfsdfsdfsdf
	 status True
_____________
>>> 
>>> 
>>> import random as r
>>> r.randit(1,5)
Traceback (most recent call last):
  File "<pyshell#437>", line 1, in <module>
    r.randit(1,5)
AttributeError: module 'random' has no attribute 'randit'. Did you mean: 'randint'?
>>> r.randint(1, 5)
1
>>> r.randint(1, 5)
2
>>> r.randint(1, 5)
2
>>> r.randint(1, 5)
1
>>> r.randint(1, 5)
5
>>> r.randint(1, 5)
3
>>> 
>>> 
>>> secret == r.randint(1, 5)
Traceback (most recent call last):
  File "<pyshell#446>", line 1, in <module>
    secret == r.randint(1, 5)
NameError: name 'secret' is not defined
>>> secret = r.randint(1, 5)
>>> my_number = int(input("Дай число от 1-5"))
Дай число от 1-54
>>> my_number == secret
False
