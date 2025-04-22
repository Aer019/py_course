def create_task():
    """Функция для вычисления среднего балла студента.
    t_name - str - имя задачи.
    t_status - bool - статус задачи.
    task_auto_id - int - глобальная переменная с номерами ID task.
    Returns:
    True - если задача успешно добавлена.
    """

    global task_auto_id
    t_name = input('Дай имя задачи:')
    t_status = False
    task_list[task_auto_id] = {"task_name":t_name, "status":False}
    task_auto_id += 1
    return True


def show_tasks():
    """Функция для вывода полных данных по таскам.
    task_id - int - номер task ID.
    description - dictionary - словарь содержащий имя taskа и его состоянием.
    """

    print('show tasks')
    for task_id, description in task_list.items():
        print("__________")
        print(f'Task id:{task_id}')
        for key, value in description.items():
            print("\t",key, value)
        print("_____________")


def change_status():
    """Функция изменения статуса task.
    task_id - int - номер task ID.
    description - dictionary - словарь содержащий имя taskа и его состоянием.
    inside - bool - получает состояние задачи из списка по ключу task_id и меняет на True. 
    Returns:
    False - в списке отсутсвует task с таким номером.
    True - статус изменён успешно.
    """

    task_id = int(input("Введите номер task:"))
    if task_id not in task_list:
        return False
    inside = task_list.get(task_id)
    inside["status"] = True
    task_list.update({task_id:inside})


def main():
    """Функция, запрашивающая ввод данных от пользователя для вывода результата разных функций.
    Arguments:
    msg - str - меню управления программы для пользователя
    operation - str - принимает данные пользователя
    """

    msg = '''1 - create task 
2 - show tasks 
3 - change task status 
quit - exit programm
'''
    operation = input(msg)
    while operation != 'quit':
        match operation:
            case '1':
               create_task()
            case '2':
                show_tasks()  
            case '3':
                change_status()
            case _:
                print('Сорри не понял ')
        operation = input(msg)

task_auto_id = 1
task_list = {}
main()