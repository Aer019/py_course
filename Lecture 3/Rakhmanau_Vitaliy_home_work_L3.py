# # Homework 3.

# # Заводим пустой список.
# li = []

# # Бесконечный цикл запрашивающий значения необходимых цифр для списка.
# print('Для выхода из программы введите exit')
# while True:
#     user_input = input('Введите число для добавления в список: ')
#     if user_input == 'exit':
#         break
#     number = int(user_input)
#     li.append(number)

# # Получившийся список от пользователя.
# print(li)

# # Сортировка пузырьком.
# swapped = True
# while swapped:
#     swapped = False
#     for i in range(len(li) - 1):
#         if li[i] > li[i+1]:
#             li[i], li[i+1] = li[i+1], li[i]
#             swapped = True

# # Вывод отсортированного списка.
# print(li)
