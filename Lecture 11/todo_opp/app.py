from errors import BadIdError, BadNameError, BadPriorityError


class App():
    def __init__(self, TodoListInst):
        self.__todolist = TodoListInst

    def Run(self):
        condition = input(App.condition_dispaly())

        while condition != "-1":
            try:
                if condition == "1":
                    name = input("Введите name: ")
                    priority = int(input("Введите priority: "))
                    self.__todolist.create(name, priority)
                elif condition == "2":
                    print(self.__todolist.read_all())
                elif condition == "3":
                    tid = int(input("Введите id: "))
                    print(self.__todolist.read(tid))
                elif condition == "4":
                    tid = int(input("Введите id: "))
                    name = input("Введите name: ")
                    priority = int(input("Введите priority: "))
                    self.__todolist.update(tid, name, priority)
                elif condition == "5":
                    tid = int(input("Введите id: "))
                    self.__todolist.delete(tid)
                else:
                    print("Неизвестная операция!")
                    print(App.condition_dispaly())
            except BadIdError as e:
                print("Проблема: ", e)
            except BadNameError as e:
                print("Проблема: ", e)
            except BadPriorityError as e:
                print("Проблема: ", e)
            except Exception as e:
                print("Неизвестная проблема...!", e)
            else:
                print("Операция прошла успешно!")

            condition = input("Выберите операцию: ")

        print("This is the end..")
        print("Bye Bye")

    @staticmethod
    def condition_dispaly():
        return """
        Номер задачи (от 1)
        Имя задачи (не менее 7 символов)
        Приоритеты (от 1 до 100)

        1 - create - добавление новой задачи.
        2 - read_all - просмотр списка.
        3 - read - просмотр задачи по id.
        4 - update - обновление задачи по id.
        5 - delete - удаление задачи по id.
        -1 - exit - выход из программы.
        Введите номер пункта меню:
        """