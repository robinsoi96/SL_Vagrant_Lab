#!/usr/bin/env python3
# This script is to setup Python virtual environment for this project

import os
import sys
import subprocess
import platform
from typing import Optional
import argparse
import shutil

# Argument for the script
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--force", action="store_true", help= "Optional flag to force Python virtual environment setup even it was done before")
args = parser.parse_args()

# Define some global variables
sys_exec: str = sys.executable
current_dir: str = os.path.dirname(os.path.abspath(__file__))
main_folder: str = os.path.abspath(os.path.join(current_dir,"..",".."))
venv_folder: str = os.path.join(main_folder, "pyenv")
pip_requirement_file: str = os.path.join(main_folder, "requirements.txt")
venv_py_txt = os.path.join(main_folder, "venv.txt")
current_OS: str = platform.system()

def update_venv_py(python_exec: str) -> None:
    print(f"Record python executable binary path in {venv_py_txt}")
    with open(venv_py_txt, "w", encoding="utf-8") as text_file:
        text_file.write(python_exec)

def pip_install(python_exec: str) -> None:
    print(f"Pip install all required modules from {pip_requirement_file} for Python virtual environment")
    pip_install_cmd: str = f"{python_exec} -m pip install -r {pip_requirement_file}"
    print(pip_install_cmd)
    subprocess.run(pip_install_cmd, shell=True, check=True)

def finalize_venv(python_exec: str) -> None:
    pip_install(python_exec)
    update_venv_py(python_exec)

def check_python() -> Optional[str]:
    if current_OS.lower() == "windows":
        exec_folder: str = os.path.join(venv_folder, "Scripts")
        if not os.path.exists(exec_folder): return None
        python_exec_list = ["python3.exe", "python.exe"]
    else:
        exec_folder: str = os.path.join(venv_folder, "bin")
        if not os.path.exists(exec_folder): return None
        python_exec_list = ["python3", "python"]

    for python_exec_file in python_exec_list:
        python_exec = os.path.join(exec_folder, python_exec_file)
        if os.path.exists(python_exec): return python_exec

    return None

def force_setup() -> bool:
    if not args.force: return False
    print("-f or --force argument is given to the script")
    print("Hence, force redo the Python virtual environment setup")
    if os.path.exists(venv_folder): shutil.rmtree(venv_folder)

    return True


def handle_existing_venv() -> bool:
    if not os.path.exists(venv_folder): return False
    python_exec = check_python()
    if python_exec is None:
        print(f"The folder {venv_folder} is supposed to be dedicated Python virtual environment folder for this project")
        print("Please remove the folder and rerun this script for Python virtual environment setup")
        sys.exit(1)
    finalize_venv(python_exec)
    print("Python virtual environment update for this project is completed")

    return True

def venv_setup() -> None:
    print(f"Creating Python virtual environment based on {sys_exec}")
    venv_cmd = f"{sys_exec} -m venv {venv_folder}"
    subprocess.run(venv_cmd, shell=True, check=True)
    print(f"Python virtual environment done created in folder {venv_folder}")
    python_exec = check_python()
    if python_exec is None:
        print(f"Python virtual environment setup is incomplete in folder {venv_folder}")
        print("Please check and debug")
        sys.exit(1)
    finalize_venv(python_exec)
    print("Python virtual environment setup for this project is completed")


def main() -> None:
    if not force_setup():
        if handle_existing_venv():
            return
    venv_setup()


if __name__ == "__main__":
    main()