class EmptyQueError(Exception):
    """Очередь пуста."""
    pass


class Que:
    def __init__(self):
        self.__que = []
        print("Очередь создана")
    def put(self, number):
        self.__que.append(number)
        print("значение успешно добавдено")
        print("текущее знач. очереди", self.__que)
        print()
    def get(self):
        if len(self.__que) < 1:
            raise EmptyQueError
        del self.__que[0]
        print("значение успешно удалено")
        print("текущее знач. очереди", self.__que)
        print()


q1 = Que()

for i in range(5):
    q1.put(i)


for i in range(6):
    q1.get()