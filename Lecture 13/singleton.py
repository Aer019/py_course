class MultipleDatabaseConnectionError(Exception):
    pass

class DatabaseConnection:
    __instance = None
    def __init__(self, database_name):
        if DatabaseConnection.__instance is None:
            DatabaseConnection.__instance = self
            self.database_name = database_name
        else:
            raise MultipleDatabaseConnectionError
    def __repr__(self):
        return f'Соединение с БД {self.database_name}'

    
conn = DatabaseConnection('account_info.db')
conn
# Соединение с БД account_info.db
conn1 = DatabaseConnection ('accowqunt_info.db')
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     conn1 = DatabaseConnection ('accowqunt_info.db')
#   File "<pyshell#66>", line 8, in __init__
#     raise MultipleDatabaseConnectionError
# MultipleDatabaseConnectionError