Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1+1
2
print()



# CRM
# Client - name phone email
client1 = ['Dima', 375333333333, "dimas@dima.dima"]
client1[1]
375333333333
client2 = ['dasdadadada', 37533309088333333, "asdasdasda.dsadasd"]
client
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    client
NameError: name 'client' is not defined. Did you mean: 'client1'?
client2
['dasdadadada', 37533309088333333, 'asdasdasda.dsadasd']
client4 = ['hello','Dima', "dimas@dsadasdima.dima", 'address']
client4
['hello', 'Dima', 'dimas@dsadasdima.dima', 'address']



a = 10
type(a)
<class 'int'>
b = 123
type(b)
<class 'int'>


# Wallet Car Dog

class Wallet:
    pass

a =10
b = 'asdasd'
wallet1 = Wallet()
type(a)
<class 'int'>
type(b)
<class 'str'>
type(wallet1)
<class '__main__.Wallet'>
wallet1
<__main__.Wallet object at 0x000002333B0CAA50>


class Dog:
    pass


class Car:
    pass

lada = Car()
bobik = Dog()
type(lada)
<class '__main__.Car'>
type(bobik)
<class '__main__.Dog'>



# Wallet - id amount owner
class Wallet:
    def __init__(self, wid, wmount, wowner):
        pass

    
wallet1 = Wallet(2, 100, 'vasya')
wallet1
<__main__.Wallet object at 0x000002333B0CAE40>
print(wallet1)
<__main__.Wallet object at 0x000002333B0CAE40>
wallet1.wid
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    wallet1.wid
AttributeError: 'Wallet' object has no attribute 'wid'
class Wallet:
    def __init__(self, wid, wmount, wowner):
        self.wallet_id = wid
        self.wallet_amount = wamount
        self.wallet_owner = wowner

        
wallet1 = Wallet(2, 100, 'vasya')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    wallet1 = Wallet(2, 100, 'vasya')
  File "<pyshell#62>", line 4, in __init__
    self.wallet_amount = wamount
NameError: name 'wamount' is not defined. Did you mean: 'wmount'?


class Wallet:
    def __init__(self, wid, wamount, wowner):
        self.wallet_id = wid
        self.wallet_amount = wamount
        self.wallet_owner = wowner

        
wallet1 = Wallet(2, 100, 'vasya')
wallet1.wallet_owner
'vasya'
wallet1.wallet_amount
100
wallet.wallet_id
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    wallet.wallet_id
NameError: name 'wallet' is not defined. Did you mean: 'Wallet'?
wallet1.wallet_id
2
wallet2 = Waller(44, 10000, 'petya')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    wallet2 = Waller(44, 10000, 'petya')
NameError: name 'Waller' is not defined. Did you mean: 'Wallet'?
wallet2 = Wallet(44, 10000, 'petya')
wallet2.wallet_id
44
wallet2.wallet_amount
10000
wallet2.wallet_owner
'petya'


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
Bobik = Dog('Bobik', 1)
Bobik.name
'Bobik'
Bobik.age
1
Дружок = Dog('Дружок', 0.5)
Дружок.name
'Дружок'
Дружок.age
0.5


# Client - name phone email
class Client:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

        
client1 = Client('Dima
                 
SyntaxError: unterminated string literal (detected at line 1)
client1 = Client('Dima', 123132132)
                 
client1
                 
<__main__.Client object at 0x000002333B0CAE40>


client2 = Client('Vasia', 123123131, 'asdads@mail.ru')
                 
client2.email
                 
'asdads@mail.ru'
client2.name
                 
'Vasia'
type(client1)
                 
<class '__main__.Client'>









==================================================================================== RESTART: Shell ====================================================================================


>>> 
>>> client
...                  
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    client
NameError: name 'client' is not defined
>>> client1
...                  
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    client1
NameError: name 'client1' is not defined
>>> 
>>> 
>>> sadad
...                  
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    sadad
NameError: name 'sadad' is not defined
>>> storage = {}
...                  
>>> storage = []
...                  
>>> client_storage = []
...                  
>>> n = 4
...                  
>>> for i in range(4):
...     print('client number is:', i)
...     name = input('name:')
...     phone = input('phone:')
...     email =  input('email:')
...     cli = Client(name, phone, email)
...     client_storage.append(client)
... 
...                  
client number is: 0
name:Vasia
phone:12313212
email:tyt@tyt.by
Traceback (most recent call last):
  File "<pyshell#135>", line 6, in <module>
    cli = Client(name, phone, email)
NameError: name 'Client' is not defined
