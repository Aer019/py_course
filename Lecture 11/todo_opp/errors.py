class BadIdError(Exception):
    """Класс для обработки ошибок неверно введенного индекса."""

    def __init__(self, id, message):
        self.id = id
        self.message = message

    def __str__(self):
        return f"BadIdError: id: {self.id}, message: {self.message}"


class BadNameError(Exception):
    """Класс для обработки ошибок неверно введенного имени задачи."""

    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __str__(self):
        return f"BadNameError: name: {self.name}, message: {self.message}"


class BadPriorityError(Exception):
    """Класс для обработки ошибок неверно введенного приоритета."""

    def __init__(self, priority, message):
        self.priority = priority
        self.message = message

    def __str__(self):
        return f"BadPriorityError: priority: {self.priority}, message: {self.message}"
