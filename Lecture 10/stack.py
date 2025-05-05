class Stack:
    def __init__(self):
        self.__stack = []
        print('stack создан успешно')
    def push(self, value):
        self.__stack.append(value)
        print(value, 'добавлено успешно')
    def pop(self):
        try:
            print(self.__stack.pop(), 'успешно удалено.')
        except:
            print('стек уже пустой.')
    def state(self):
        print('Текущее состояние стека')
        print(self.__stack)

class AddStackValuse(Stack):
    def __init__(self):
        super().__init__()
        self.__summa = 0
    def push(self, value):
        super().push(value)
        self.__summa += value
    def get_summa(self):
        print(self.__summa)


#s2 = AddStackValuse()
#s2.get_summa()
#s2.state()
#s2.push(3)
#s2.push(33)
#s2.push(5)
#s2.state()
#s2.get_summa()