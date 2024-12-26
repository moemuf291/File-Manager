import os
import json
import sys
from test import create_file, move_file

def get_ext(file_name):
    extension = os.path.splitext(file_name)[1]
    return extension


def create_dir(extension):
    directory = extension.lstrip('.')
    if not os.path.exists(directory):
        os.mkdir(directory)


def check_ext():
    try:
        with open("config.json", 'r') as file:
            return json.load(file)
    except FileExistsError as e:
        print(f"error {e}")


source_dir = os.getcwd()

if __name__ == "__main__":
    file_name = input("create file: ")
    create_file(file_name)

    extension = get_ext(file_name)

    supported_extension = check_ext()

    directory = extension.lstrip(".")

    if extension in supported_extension:
        create_dir(extension)
        move_file(source_dir, file_name, directory)

    else:
        pass
