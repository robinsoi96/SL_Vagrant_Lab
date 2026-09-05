# This script is all related to backup for VM build project

import subprocess

from utils import create_folder

def prepare_backup_folder(backup_folder_name: str, host_os: str, force_recreate_bool: bool = False) -> str:
    backup_folder = create_folder(input_folder_path=backup_folder_name, recreate_folder=force_recreate_bool)
    if host_os == "windows": 
        subprocess.run(f"attrib +h {backup_folder}", shell=True, check=True) # Make file hidden for Windows host OS
    return backup_folder