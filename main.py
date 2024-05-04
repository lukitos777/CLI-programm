from manager import Manager


def listen(command: str) -> None:
    manager = Manager()
    if command == 'add':
        manager.add_new_data()
    elif command == 'balance':
        manager.get_current_balance()
    elif command == 'read':
        manager.read_data()
    elif command == 'lst':
        manager.show_list()
    elif command == 'del':
        manager.delite_data_by_id()
    elif command == 'update':
        manager.update_data()
    elif command == 'lst -a':
        manager.show_all()
    elif command == 'help':
        print('add - добавлает новую запись\nbalance - показывает текуший баланс\nread - считывает одну запись\nlst - считывает записи по категории, флаг -а показывает все записи\ndel - удаляет запись по ID\nupdate - обнавляет запись\nhelp - показывает комманды\nbreak - останавливает работу программы\n')
    else:
        print('Command does not exist\nuse help command\n')


def main() -> None:
    while True:
        command = input()
        if command:
            listen(command)
        elif command == 'break':
            break
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()