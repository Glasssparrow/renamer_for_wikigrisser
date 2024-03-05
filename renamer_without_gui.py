# main imports
from os import rename, listdir
import os
import sys


INITIAL_DIR = os.getcwd()
HERO_FOLDERS = ["public\\hero cards", "public\\hero cards - skin", ]
SKILL_FOLDERS = ["public\\skills", ]


def choose_files(old, new, to_be_changed="skill"):
    if to_be_changed == "skill":
        directories = SKILL_FOLDERS
    elif to_be_changed == "hero":
        directories = HERO_FOLDERS
    else:
        raise Exception("Expected skill or hero")
    result = []
    for directory in directories:
        files_list = listdir(f"{INITIAL_DIR}\\{directory}")
        for file in files_list:
            if (
                    file[0:len(old)] == old and
                    edit_name(old, new, file) not in files_list
            ):
                result.append(f"{INITIAL_DIR}\\{directory}\\{file}")
        return result


def edit_name(old, new, filename, only_in_beginning=True):
    if only_in_beginning:
        result = f"{filename[:-len(old)-4]}{new}.png"
    else:
        result = filename.replace(old, new)
    return result


def renaming(old, new, to_be_changed="skill"):

    files_list = choose_files(old, new, to_be_changed)

    for file_name in files_list:

        new_name = edit_name(old, new, file_name)
        rename(f"{file_name}", f"{new_name}")


renaming(sys.argv[1], sys.argv[2], sys.argv[3])
