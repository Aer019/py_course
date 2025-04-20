# # Homework 5.1.

# def is_year_leap(year): # Функция для определения кратности года.
#     if year % 4 == 0 and year % 100 != 0:
#         return True
#     elif year % 400 == 0:
#         return True
#     return False


# test_data = [1500, 1900, 2000, 2016, 1987]
# test_results = [False, False, True, True, False]

# for year, result in zip(test_data, test_results):
#     if is_year_leap(year) == result:
#         print(year, 'is leap? -->', result)
#     else:
#         print(year, 'from your func -->', \
#               is_year_leap(year))
#         print('but expected -->', result)

# # Small project BMI.

# def calculate_bmi(weight, height): # Функция для подсчета индекса.
#     bmi = weight / (height ** 2)
#     return bmi


# def interpret_bmi(bmi): # Функция для определения степени ожирения. 
#     if bmi < 18.5:
#         return "Дефицит массы тела"
#     elif bmi >= 18.5 and bmi <= 25:
#         return "Норма"
#     elif bmi > 25 and bmi <=30:
#         return "Предожирение"
#     elif bmi > 30 and bmi < 35:
#         return "Ожирение 1 степени"
#     elif bmi >= 35 and bmi < 40:
#         return "Ожирение 2 степени"
#     elif bmi >= 40 and bmi <= 52:
#         return "Ожирение 3 степени"


# def main(): 
#     print('My calculator BMI')
#     weight = float(input("Введите свой вес в кг: "))
#     height = float(input("Введите свой рост в метрах: "))
#     bmi = calculate_bmi(weight, height)
#     category = interpret_bmi(bmi)
#     print(f"Ваш индекс BMI: {bmi}")
#     print(f"У вас категория: {category}")


# main()

# # Homework 5.4.

# n = int(input('Введите последнее число послдовательности Фибоначи для вашего списка: ')) # User определяет последнее число последовательности.

# def fibonacci(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
    
#     fib_1, fib_2 = 1, 1
#     for i in range(3, n+1): 
#         fib_3 = fib_1 + fib_2
#         fib_1, fib_2 = fib_2, fib_3
    
#     return fib_3

# for i in range(-1, n):
#     print(fibonacci(i))
