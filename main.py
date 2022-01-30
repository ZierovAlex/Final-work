# Файл отвечающий за запуск записной книжки

from notebook import Notebook
from commands import Commands

new_note = Notebook()
new_note.load_notebook()

nb_commands = Commands(new_note)
nb_commands.main_menu()
