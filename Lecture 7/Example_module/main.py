import sport_data_logic as sdl
import fun


def main():
    oper = input('1 - add 2 - show 3 - delete    -1 exit')
    while oper != '-1':
        user_data = input('-->')
        match oper:
            case '1':
                sdl.Add(user_data)
            case '2':
                sdl.Show(user_data)
            case '3':
                sdl.Delete(user_data)
            case _:
                fun.funny()
                print('не понимаю')

        oper = input('1 - add 2 - show 3 - delete    -1 exit')


main()
