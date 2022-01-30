# Методы отвечающие за общение с пользователем, отображение меню и управление
# основным функционалом записной книжки
class Commands:

    def __init__(self, notebook):
        self.notebook = notebook

    # check bloke
    @staticmethod
    def check_input_commands(c, text='Выберите действие: '):
        n = input(text)
        while True:
            if n.isdigit():
                n = int(n)
                if c > n >= 0:
                    break
                else:
                    n = input('Некорректный номер, попробуйте еще раз: ')
            else:
                n = input('Некорректный ввод, попробуйте еще раз: ')
        return n

    @staticmethod
    def check_record_number(n, notebook):
        n = str(n)
        while True:
            if n.isdigit():
                n = int(n)
                try:
                    if notebook.is_show(n):
                        break
                    else:
                        n = input('Некорректный номер, попробуйте еще раз: ')
                except Exception:
                    n = input('Некорректный номер, попробуйте еще раз: ')
            else:
                n = input('Некорректный ввод, попробуйте еще раз: ')
        return n

    # main menu bloke
    def main_menu(self):
        while True:
            # print notebook
            print()
            print('-' * 20)
            self.notebook.print_note()

            self.main_menu_show()
            command = self.check_input_commands(8)

            # run command
            if command == 0:
                self.show_menu()
            elif command == 1:
                self.new_note()
            elif command == 2:
                self.delete_note()
            elif command == 3:
                self.edit_note()
            elif command == 4:
                self.search_menu()
            elif command == 5:
                self.sort_notebook()
            elif command == 6:
                self.exit_notebook()
                return

    @staticmethod
    def main_menu_show():
        print()
        print('0 Просмотреть')
        print('1 Добавить')
        print('2 Удалить')
        print('3 Изменить')
        print('4 Поиск')
        print('5 Сортировать')
        print('6 Выход')
        print()

    # show menu bloke
    def show_menu(self):
        note_id = self.show_menu_input()
        self.notebook.print_record(note_id)
        self.show_menu_show()
        s = self.check_input_commands(3)

        # run command
        if s == 0:
            self.notebook.delete_note(note_id)
        elif s == 1:
            self.notebook.edit_note(note_id)
        elif s == 2:
            return

    def show_menu_input(self):
        note_id = input('Введите номер записи которую хотите просмотреть: ')
        note_id = self.check_record_number(note_id, self.notebook)
        print()
        return note_id

    @staticmethod
    def show_menu_show():
        print()
        print('0 Удалить')
        print('1 Изменить')
        print('2 Назад')
        print()

    # search menu bloke
    def search_menu(self):
        column_search, search_value = self.search_menu_input()
        while True:
            # search
            count = self.notebook.search_note(column_search, search_value)
            if count > 0:
                print('По вашему запросу найдено', count, 'записей')
            else:
                print('По вашему запросу ничего не найдено!')
                input('Нажмите любую клавишу для возврата')
                self.notebook.show_all()
                return

            self.notebook.print_note()
            self.search_menu_show()
            s = self.check_input_commands(4)

            # choose command
            if s == 0:
                self.delete_note()
            elif s == 1:
                self.edit_note()
            elif s == 2:
                self.show_menu()
            elif s == 3:
                self.notebook.show_all()
                return

    @staticmethod
    def search_menu_show():
        print('0 Удалить')
        print('1 Изменить')
        print('2 Просмотреть')
        print('3 Назад')
        print()

    def search_menu_input(self):
        text = 'Выберие по чему искать, "0" - по имени, "1" - по фамилии, ' \
               '"2" - по номеру телефона: '
        column_search = self.check_input_commands(3, text)
        printed_text = ''
        if column_search == 0:
            printed_text = 'Введите имя или первую букву имени для поиска: '
        elif column_search == 1:
            printed_text = 'Введите фвмилию или первую букву фамилии для ' \
                           'поиска: '
        elif column_search == 2:
            printed_text = 'Введите номер для поиска: '
        search_value = input(f"{printed_text}")
        print()
        return column_search, search_value

    # sort bloke
    def sort_notebook(self):
        sort_type, sort_direction = self.sort_menu_input()
        self.notebook.sort_note(sort_type, sort_direction)

    def sort_menu_input(self):
        text = 'Введите "0" для сортировки по имени, "1" для сортировки по ' \
               'фамилии: '
        sort_type = self.check_input_commands(2, text)
        text = 'Введите "0" для сортировки по алфавиту, "1" для сортировки ' \
               'по алфавиту в обратном порядке: '
        sort_direction = self.check_input_commands(2, text)
        if sort_direction == 0:
            sort_direction = 'asc'
        else:
            sort_direction = 'desc'
        return sort_type, sort_direction

    # other commands bloke
    def delete_note(self):
        note_id = input('Введите номер записи которую хотите удалить: ')
        note_id = self.check_record_number(note_id, self.notebook)
        self.notebook.delete_note(note_id)

    def edit_note(self):
        note_id = input('Введите номер записи которую хотите изменить: ')
        note_id = self.check_record_number(note_id, self.notebook)
        self.notebook.edit_note(note_id)

    def new_note(self):
        self.notebook.input_note()

    def exit_notebook(self):
        self.notebook.save_notebook()


if __name__ == "__main__":
    a = Commands(None)
