import os
import sys
import shutil


def create_file(file_name):
    file_input = input("write to file: ")
    try:
        with open(file_name, 'w') as file:
            file.write(file_input)
    except FileNotFoundError as e:
        print(f"error {e}")
        

source_dir = os.getcwd()

def move_file(source_dir, file_name, directory):
    target_dir = os.path.join(source_dir, directory)


    source_file = os.path.join(source_dir, file_name)
    target_file = os.path.join(target_dir, file_name)

    try:
        shutil.move(source_file, target_file)
        print(f"file moved from {source_file} to {target_file}")
    except FileNotFoundError as e:
        print(f"Error {e}")
    except shutil.Error as e:
        print(f"error {e}")
        sys.exit()
