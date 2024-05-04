import datetime
from pydantic import ValidationError

from schemas import Add_Data, Get_Data_By_ID

class Manager:
    def get_current_balance(self) -> None:
        with open('balance.txt', 'r') as file:
            balance = file.readline()
            print(balance)
            return balance

#=======================================================================================

    def add_new_data(self) -> None:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        type = input('Введите категорию (Доход/Расход) :').capitalize()
        price = input('Введите сумму :')
        desc = input('Введите краткое описание :')

        try:
            new_data = Add_Data(category=type, price=price, desc=desc)
            self._save_data(date=date, data=new_data)
        except ValidationError:
            print('Введённые данные не верны\n')

    def _save_data(self, date, data: Add_Data) -> None:
        # save data and update the balance
        with open('database.txt', 'a', encoding='utf-8') as file:
            file.write(f'{date}|{data.category}|{data.price}|{data.desc}\n')

        if data.category == 'Доход':
            with open('balance.txt', 'r') as file:
                new_balance = int(file.readline()) + data.price

            with open('balance', 'w') as file:
                file.write(str(new_balance))
        else:
            with open('balance.txt', 'r') as file:
                new_balance = int(file.readline()) - data.price

            with open('balance', 'w') as file:
                file.write(str(new_balance))

#========================================================================================

    def read_data(self) -> None:
        ID = input('')
        try:
            query = Get_Data_By_ID(ID=ID)
            self._show_data_by_id(query)
        except ValidationError:
            print('Введённые данные не верны\n')
        
    def _show_data_by_id(self, ID: Get_Data_By_ID) -> None:
        with open('database.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) < ID.ID:
                print('Такой записи не существует!\n')
                return
        line = lines[ID.ID].split('|')
        print(
            f'Дата: {line[0]}\nКатегория: {line[1]}\nСумма: {line[2]}\nОписание: {line[3]}\n'
        )

#=========================================================================================

    def show_list(self) -> None:
        # showing list sorted by category
        category = input('Введите категорию (Доход/Расход) :').capitalize()

        if category not in 'Доход/Расход':
            print('Не правильная категория')
            return 

        with open('database.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if category in line:
                    L = line.split('|')
                    print(
                        f'ID: {i}\nДата: {L[0]}\nКатегория: {L[1]}\nСумма: {L[2]}\nОписание: {L[3]}\n'
                    )

#===========================================================================================

    def delite_data_by_id(self) -> None:
        ID = int(input('Введите ID записи'))
        with open('database.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) < ID:
                print('Такой записи не существует!\n')
            else:
                del lines[ID]

                with open('database.txt', 'w', encoding='utf-8') as file_:
                    file_.writelines(lines)

#=========================================================================================

    def update_data(self) -> None:
        ID = int(input('Введите ID записи :'))
        with open('database.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) < ID:
                print('Такой записи не существует!\n')
            else:
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                type = input('Введите категорию (Доход/Расход) :').capitalize()
                price = input('Введите сумму :')
                desc = input('Введите краткое описание :')

                try:
                    Add_Data(category=type, price=int(price), desc=desc)
                    lines[ID] = f'{date}|{type}|{price}|{desc}'
                    
                    with open('database.txt', 'w', encoding='utf-8') as file_:
                        file_.writelines(lines)
                except ValidationError:
                    print('Введённые данные не верны\n')

#=========================================================================================

    def show_all(self):
        with open('database.txt', 'r', encoding='utf-8') as file:
            for i, line in enumerate(file.readlines()):
                L = line.split('|')
                print(
                    f'ID: {i}\nДата: {L[0]}\nКатегория: {L[1]}\nСумма: {L[2]}\nОписание: {L[3]}\n'
                )
