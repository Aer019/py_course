def avg(score):
    """Функция для вычисления среднего балла студента.
    Arguments:
    score - tuple - набор оценок.
    Returns:
    float - средний балл, 2 знака после запятой.
    """

    return round((sum(score)/len(score)), 2)



def new_grade(student_name, grade):
    """Функция для добавления новой оценки студенту.
    Arguments:
    student_name - str - имя, не менее 2-х символов.
    grade - int, оценка
    Returns:
    True - если оценка добавлена успешно.
    False - если имя меньше 2 символов
    """

    if len(student_name) <2:
        return False
    
    student_name = student_name.title()
    if student_name in students_grades:
        students_grades.update(students_grades.get(student_name) + (grade, ))
    else:
        students_grades.update({student_name:(grade, )})
    return True


def show_grade():
    """Функция показывающая оценки и имя учеников соответственно.
    Arguments:
    key - str - имя студента в словаре
    value - int - оценка студента в словаре
    """

    print('show grades')
    for key, value in students_grades.items():
        print('name:', key)
        print('grades:', value)


def show_avg():
    """Функция показывающая полные и средние значения оценок из словаря students_grades.
    Arguments:
    key - str - ключ из словаря
    value - int - значение из словаря
    """

    print('show avg')
    for key, value in students_grades.items():
        print('name:', key)
        print('avg:', avg(value))


def main():
    """Функция, запрашивающая ввод данных от пользователя для вывода результата разных функций. 
    Arguments:
    msg - str - меню управления программы для пользователя
    operation - str - принимает данные пользователя
    name - str - полное имя от пользователя
    grade - int - оценка от пользователя 
    """

    msg = '''1 - new grade 
2 - show avg 
3 - show grades 
quit - exit programm
'''
    operation = input(msg)
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
        operation = input(msg)


students_grades = {}
main()
