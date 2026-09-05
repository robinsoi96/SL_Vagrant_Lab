# This script is mainly for file management e.g. copy, delete, create files and folders, etc

import os
import shutil

def check_file_exists(input_file: str) -> bool:
    if (os.path.exists(input_file)):
        exist_status: bool = True
    else:
        exist_status: bool = False

    return exist_status


def remove_file(input_file: str) -> None:
    if os.path.isdir(input_file):
        os.remove(input_file)
    elif os.path.isfile(input_file):
        shutil.rmtree(input_file)
    

def create_folder(input_folder_path: str, recreate_folder: bool = False) -> str:
    create: bool = False

    if check_file_exists(input_folder_path) == True:
        if recreate_folder == True:
            remove_file(input_folder_path)
            create = True
    else:
        create = True

    if create == True:
        os.makedirs(input_folder_path)
    
    return input_folder_path