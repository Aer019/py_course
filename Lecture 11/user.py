class User:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def __repr__(self):
        return f"User({self.name}, {self.age})"
    

class UserNameError(Exception):
    def __init__(self, u_name, message="имя пользователя меньше 2-ух симоволов запрещено!"):
        self.u_name = u_name
        self.message = message
    def __str__(self):
        return self.u_name + "-->" + self.message
    

class UserAgeError(Exception):
    def __init__(self, u_age, message="возраст пользователя не может быть меньше нуля!"):
        self.u_age = u_age
        self.message = message
    def __str__(self):
        return f"{self.u_age} --> {self.message}"
    

def user_input():
    n, a = input("name "), int(input("age "))
    if len(n) < 2:
        raise UserNameError(n)
    if a < 0:
        raise UserAgeError(a)
    return User(n, a)


try:
    user = user_input()
except UserNameError as err:
    print(err)
except UserAgeError as err:
    print(err)
except:
    print("Чтото не так...")