# main imports
from os import rename, listdir, getcwd
from os.path import abspath, join, dirname, basename
import sys

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
    new – text we will replace it with,
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


renaming(sys.argv[1], sys.argv[2], sys.argv[3])
