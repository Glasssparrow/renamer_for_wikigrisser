# main imports
from os import rename, listdir, getcwd
from os.path import abspath, join, dirname, basename
# imports for gui
from tkinter import Button, Tk, Label, Entry
from datetime import datetime

INITIAL_DIR = getcwd()
HERO_FOLDERS = [
    join("public", "hero cards"),
    join("public", "hero cards - skin"),
]
SKILL_FOLDERS = [
    join("public", "skills"),
]


def choose_files(old: str, new: str, to_be_changed="skill"):
    """Get paths to the files, which starts with old.
    old - text we want to replace,
    new - text we will replace it with,
    to_be_changed - skill/hero."""
    if len(old) == 0:
        return []  # Search nothing if old == ""
    if to_be_changed == "skill":
        directories = SKILL_FOLDERS
    elif to_be_changed == "hero":
        directories = HERO_FOLDERS
    else:
        raise Exception("Expected skill or hero")
    result = []
    for directory in directories:
        files_list = listdir(abspath(directory))
        for file in files_list:
            if (
                    file[0:len(old)] == old and
                    edit_name(old, new, file) not in files_list
            ):
                result.append(join(INITIAL_DIR, directory, file))
    return result


def edit_name(old, new, path_to_file):
    """Get an edited path.
    old - text we want to replace,
    new – text we will replace it with,
    path_to_file - path we want to edit."""
    folder = dirname(path_to_file)
    current_name = basename(path_to_file)
    # str(***) bcz of false positive warning (basename return str)
    # Probably some difference in types.
    # But it is work properly anyway
    # because dynamic typing is great.
    result = str(current_name).replace(old, new)
    return join(folder, result)


def renaming(old, new, to_be_changed="skill"):
    files_list = choose_files(old, new, to_be_changed)
    for file_name in files_list:
        new_name = edit_name(old, new, file_name)
        rename(file_name, new_name)


WINDOW_WIDTH = 600
ENTRY_WIDTH = 100
FOLDER_BUTTON_WIDTH = 50
ACTION_BUTTON_WIDTH = 80
SHOW_FILES_BUTTON_WIDTH = 20


class Gui:

    title_text = "Renamer"

    def _show_files(self):
        old = self._old_beginning.get()
        new = self._new_beginning.get()
        files = choose_files(old, new, "hero")
        text = "Files list:\n"
        for file in files:
            text = f"{text}:hero:{file}\n"
        files = choose_files(old, new, "skill")
        for file in files:
            text = f"{text}:skill:{file}\n"
        self._files_list.configure(
            text=f"{text}"
        )

    def _rename_hero(self):
        old = self._old_beginning.get()
        new = self._new_beginning.get()
        renaming(old, new, "hero")
        time = datetime.now()
        self._files_list.configure(
            text=f"Success! Time {str(time.hour)}:"
                 f"{str(time.minute)}:{str(time.second)}"
        )

    def _rename_skill(self):
        old = self._old_beginning.get()
        new = self._new_beginning.get()
        renaming(old, new, "skill")
        time = datetime.now()
        self._files_list.configure(
            text=f"Success! Time {str(time.hour)}:"
                 f"{str(time.minute)}:{str(time.second)}"
        )

    def __init__(self):
        self.folder = INITIAL_DIR
        # Оформление окна
        self._window = Tk()
        self._window.title(self.title_text)
        self._window.geometry(f"{WINDOW_WIDTH}x220")

        # Текст пути к папке
        self._text_folder = Label(text=INITIAL_DIR)
        self._text_folder.grid(columnspan=6, column=0, row=0)

        self._old_beginning = Entry(width=ENTRY_WIDTH, justify="center")
        self._old_beginning.grid(columnspan=6, column=0, row=1)

        self._new_beginning = Entry(width=ENTRY_WIDTH, justify="center")
        self._new_beginning.grid(columnspan=6, column=0, row=2)

        # Кнопка выбора папки
        self._folder_selection_button = (
            Button(self._window, text="Rename hero",
                   width=FOLDER_BUTTON_WIDTH,
                   command=self._rename_hero)
        )
        self._folder_selection_button.grid(columnspan=4, column=0, row=3)

        # Кнопка просмотра выбранных файлов
        self._folder_selection_button = (
            Button(self._window, text="List files",
                   width=SHOW_FILES_BUTTON_WIDTH,
                   command=self._show_files)
        )
        self._folder_selection_button.grid(columnspan=2, column=4, row=3)

        # Кнопка переименования файлов
        self._action_button = (
            Button(self._window, text="Rename skill",
                   width=ACTION_BUTTON_WIDTH,
                   command=self._rename_skill)
        )
        self._action_button.grid(columnspan=6, column=0, row=4)

        # Текст пути к папке
        self._files_list = Label(text="Placeholder")
        self._files_list.grid(columnspan=6, column=0, row=5)

        # Запускаем окно
        self._window.mainloop()


gui = Gui()
