from errors import BadIdError, BadNameError, BadPriorityError


class Task:
    def __init__(self, tname, tpriority):
        self.tname = tname
        self.tpriority = tpriority

    def __str__(self):
        return f"name: {self.tname} | priority: {self.tpriority}"

class TodoList:
    __auto_id = 1  

    def __init__(self):
        self.__task_storage: dict[int, Task] = {}

    @classmethod
    def incrId(cls):
        cls.__auto_id += 1

    @classmethod
    def getId(cls):
        return cls.__auto_id

    def create(self, name, priority):
        """ Метод добавления задач в хранилище. """
        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов!")

        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100!")

        self.__task_storage[TodoList.getId()] = Task(name, priority)
        TodoList.incrId()  
        return True

    def read(self, tid):
        """Метод для чтения задачи по id."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")

        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")

        return self.__task_storage[tid]

    def read_all(self):
        """Метод для чтения всех задач."""
        res_str = "номер задачи: значение\n"
        for k, v in self.__task_storage.items():
            res_str += f"{k} | {v}\n"

        return res_str

    def update(self, tid, name, priority):
        """Метод для обновления задачи в хранилище."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")

        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")

        if len(name) < 7:
            raise BadNameError(name, "Имя должно быть более 7 символов!")

        if priority < 1 or priority > 100:
            raise BadPriorityError(priority, "Приоритет должен быть в диапазоне от 1 до 100!")

        self.__task_storage[tid] = Task(name, priority)

        return True

    def delete(self, tid):
        """Метод для удаления задачи по id."""
        if tid < 1:
            raise BadIdError(tid, "Номер задачи от 1!")

        if tid not in self.__task_storage:
            raise BadIdError(tid, "Номер задачи не содержится!")

        del self.__task_storage[tid]

        return True
    