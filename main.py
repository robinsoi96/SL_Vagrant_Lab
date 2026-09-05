import os
import sys
import platform
import argparse

from common import prepare_backup_folder
from common import GetVmConfigInfo

main_folder: str = os.path.dirname(os.path.abspath(__file__))
vm_config_file: str = os.path.join(main_folder, "config.yml")
host_os: str = platform.system().lower()
backup_folder = prepare_backup_folder(backup_folder_name=os.path.join(main_folder, ".db"), host_os=host_os)

def main() -> None:
    #TESTING
    VM_config_info = GetVmConfigInfo(config_file=vm_config_file).consolidate_info()
    print(VM_config_info)   

if __name__ == "__main__":
    main()