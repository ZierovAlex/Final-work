# Основной набор функций записной книжкки, а так же дополнительные методы для
# проверки.
class Notebook:

    def __init__(self):
        self.notebook_list = []

    # Блок методов проверки реализован в виде статичных методов
    @staticmethod
    def date_check(date):
        date = str(date)
        while True:
            if (date[:2].isnumeric() and date[2] == '.' and date[
                                                            3:5].isnumeric() and
                date[5] == '.' and date[
                                   6:10].isnumeric()) or date == '':
                break
            else:
                date = input(
                    'Введено некорректно пожалуйста ввежите дату в формате '
                    'ДД.ММ.ГГГГ')
        return date

    @staticmethod
    def number_check(telephone_number):
        telephone_number = str(telephone_number)
        while True:
            if telephone_number == '':
                telephone_number = input("Вы ввели пустую строку, это поле"
                                         " обязательно к заполнению: ")
            elif not (telephone_number.isnumeric()):
                telephone_number = input(
                    'Введено некорректно, пожалуйста попробуйте еще раз: ')
            else:
                telephone_number = str(telephone_number)
                break

        return telephone_number

    @staticmethod
    def empty_check(check_element):
        check_element = str(check_element)
        while True:
            if check_element != '':
                break
            else:
                check_element = input('Вы ввели пустую строку, это поле'
                                      ' обязательно к заполнению: ')

        return check_element

# Основные функции записной книжки

    # Метод загрузки и считывания сохраненного ранее файла с записями
    def load_notebook(self):
        import csv
        try:
            with open('notebook_save.csv', encoding='utf-8') as ns:
                self.notebook_list = list(csv.reader(ns))
            for record in self.notebook_list:
                record[5] = bool(record[5])
            print(f"Загружено {len(self.notebook_list)} записей.")  # add

        except Exception:
            print('Сохраненные записи отсутствуют!')

    # Метод добавления новой записи в записную книжку
    def input_note(self):
        name = input('Введите имя: ')
        name = self.empty_check(name)
        surname = input('Введите фамилию: ')
        surname = self.empty_check(surname)
        telephone_number = input('Введите номер телефона: ')
        telephone_number = self.number_check(telephone_number)
        address = input('Введите адрес: ')
        date_of_birth = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
        date_of_birth = self.date_check(date_of_birth)
        note = [name, surname, telephone_number, address, date_of_birth, True]
        self.notebook_list.append(note)

    # Метод осуществляющий удаление ранее сохраненной записи
    def delete_note(self, note_id):
        try:
            self.notebook_list.pop(note_id)
        except Exception:
            print('Удаляемый элемент не найден!')

    # Метод редактирования ранее сохраненной записи, при вводе имени и
    # фамилии или номера телефона нет ограничений, но эти поля обязательны к
    # заполнению, добавлена проверка. Код предусматривает сохранение старой
    # записи при изменении путем нажатия enter
    def edit_note(self, note_id):
        record = self.notebook_list[note_id]
        print(f'Текущее имя: {record[0]}')
        name = input(
            'Новое имя или нажмите "enter" - без изменений: '
        )
        if name != '':
            record[0] = self.empty_check(name)
        print(f'Текущее фамилия: {record[1]}')
        surname = input(
            'Новая фамилия или нажмите "enter" - без изменений: '
        )
        if surname != '':
            record[1] = self.empty_check(surname)
        print(f'Текущее номер телефона: {record[2]}')
        telephone_number = input(
            'Новый номер телефона или нажмите "enter" - без изменений: '
        )
        if telephone_number != '':
            record[2] = self.number_check(telephone_number)
        print(f'Текущий адрес: {record[3]}')
        address = input('Введите адрес или нажмите "enter" - без изменений: ')
        if address != '':
            record[3] = address
        print(f'Текущая дата рождения: {record[4]}')
        date_of_birth = input(
            'Введите дату рождения в формате ДД.ММ.ГГГГ или нажмите "enter"'
            ' - без изменений: '
        )
        if date_of_birth != '':
            record[4] = self.date_check(date_of_birth)
    # Метод предназначенный для поиска нужных записей в записной книжке,
    # и дальнейшее осуществление с ними действий изменение или удаление.
    # Можно искать по маске напечатав один или несколько символов и звездочку
    # вначале или в конце (A* вернет все записи, у которых фамилия имеет в
    # начале букву «А»), также обычный поиск по целому слову, его частям или
    # одной букве.

    def search_note(self, id, search_fragment):
        search_fragment = search_fragment.lower()
        count = 0
        for record in self.notebook_list:
            text = record[id].lower()
            if ((search_fragment[0] == '*') and (text.endswith(search_fragment[
                    1:]))) or ((search_fragment[-1] == '*') & (text.startswith(
                    search_fragment[:-1]))) or (('*' not in search_fragment) and
                                                (search_fragment in text)):
                record[5] = True
                count = count + 1
            else:
                record[5] = False
        return count

    def show_all(self):
        for record in self.notebook_list:
            record[5] = True

    def is_show(self, id):
        return self.notebook_list[id][5]
    # Метод сортировки записей, реализован по принципу пузырькового метода,
    # добавлен вариант сортировки по алфавите или в обратном направлении

    def sort_note(self, id, direct='asc'):
        records = len(self.notebook_list)
        for i in range(records - 1):
            for j in range(records - 2, i - 1, -1):
                if (self.notebook_list[j + 1][id] < self.notebook_list[j][
                        id]) != (direct == 'desc'):
                    self.notebook_list[j], self.notebook_list[j + 1] = \
                        self.notebook_list[j + 1], self.notebook_list[j]

    # Метод сохраняющий все записи в файл сохранения 'notebook_save.csv',
    # отрабатывает при выходе из программы.
    def save_notebook(self):
        import csv
        with open('notebook_save.csv', 'w', encoding='utf-8',
                  newline='') as save:
            save_notebook = csv.writer(save)

            for row in self.notebook_list:
                save_notebook.writerow(row)
# Блок вспомогательных методов для выведения записей на просмотр и получения
# длины списка хранящего запси

    def print_note(self):
        for i in range(len(self.notebook_list)):
            if self.notebook_list[i][5]:
                print(i, self.notebook_list[i][0], self.notebook_list[i][1],
                      sep='\t')

    def print_record(self, record_id):
        print('name:', self.notebook_list[record_id][0], sep='\t')
        print('surname:', self.notebook_list[record_id][1], sep='\t')
        print('telephone number:', self.notebook_list[record_id][2], sep='\t')
        print('address:', self.notebook_list[record_id][3], sep='\t')
        print('date of birth:', self.notebook_list[record_id][4], sep='\t')

    def notebook_size(self):
        return len(self.notebook_list)


if __name__ == "__main__":
    n = Notebook()
