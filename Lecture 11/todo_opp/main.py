from todo_module import TodoList
from app import App

def main():
    td1 = TodoList()
    app = App(td1)
    app.Run()


if __name__ == "__main__":
    main()
