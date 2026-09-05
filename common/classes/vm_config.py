import yaml
import os
import sys

VM_CONFIG_FILE: str = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "config.yml"))
MAIN_CONFIG_KEY_NAME: str = "vm_config"

# Class for VM image name
class VmName:
    def __init__(self) -> None:
        self.main_config_key: str = "name"

    def get_VM_name(self, VM_data: dict) -> dict:
        VM_name: str = VM_data[self.main_config_key]
        return VM_name

# Class for VM build image
class VmImage:
    def __init__(self) -> None:
        self.main_config_key: str = "image"
        self.os_type_key: str = "os_type"
        self.image_path_key: str = "image_path"

    def get_os_type(self, VM_image_data: dict) -> str:
        os_type: str = VM_image_data[self.os_type_key]
        return os_type

    def get_vm_image_path(self, VM_image_data: dict) -> str:
        vm_image_path: str = VM_image_data[self.image_path_key]
        return vm_image_path

    def get_VM_image_info(self, VM_data: dict) -> list:
        full_VM_image_info: dict = VM_data[self.main_config_key]
        vm_image_input_info: dict = dict()
        vm_image_input_info[self.main_config_key] = dict()
        vm_os_type: str = self.get_os_type(VM_image_data=full_VM_image_info)
        vm_image_input_info[self.main_config_key][self.os_type_key] = vm_os_type
        vm_image_path: str = self.get_vm_image_path(VM_image_data=full_VM_image_info)
        vm_image_input_info[self.main_config_key][self.image_path_key] = vm_image_path
        return vm_image_input_info

# Class for VM Hardware Setup
class VmHardware:
    def __init__(self) -> None:
        self.main_config_key = "hw_setup"
        self.cpu_key = "CPU"
        self.ram_key = "RAM"
        self.boot_drive_key = "Boot_drive"

    def get_HW_info(self, VM_data: dict) -> list:
        full_VM_hardware_info: dict = VM_data[self.main_config_key]
        vm_hw_setup_info: dict = dict()
        vm_hw_setup_info[self.main_config_key] = full_VM_hardware_info
        return vm_hw_setup_info

# Class for VM task(s)
class VmTask:
    def __init__(self) -> None:
        self.main_config_key = "task"

    def get_VM_task_info(self, VM_data: dict) -> list:
        full_VM_task_info: dict = VM_data[self.main_config_key]
        vm_task_info: dict = dict()
        vm_task_info[self.main_config_key] = full_VM_task_info
        return vm_task_info

# Class for full config info for VM build
class GetVmConfigInfo:
    def __init__(self, config_file: str = VM_CONFIG_FILE, key_name: str = MAIN_CONFIG_KEY_NAME) -> None:
        self.config_file: str = config_file
        self.key_name: str = key_name

    def get_full_config_info(self) -> dict:
        with open(self.config_file, "r") as f:
            full_config_data = yaml.safe_load(f)
        return full_config_data[self.key_name]
           
    def consolidate_info(self) -> dict:
        full_config_data: dict = self.get_full_config_info()
        vm_input_info: list = list()
        for VM_data in full_config_data:
            VM_info: dict = dict()
            VM_name: str = VmName().get_VM_name(VM_data=VM_data)
            VM_info[VM_name] = dict()
            VM_image_info: dict = VmImage().get_VM_image_info(VM_data=VM_data)
            VM_info[VM_name].update(VM_image_info)
            VM_hw_setup_info: dict = VmHardware().get_HW_info(VM_data=VM_data)
            VM_info[VM_name].update(VM_hw_setup_info)
            VM_task_info: dict = VmTask().get_VM_task_info(VM_data=VM_data)
            VM_info[VM_name].update(VM_task_info)
            vm_input_info.append(VM_info)
        return vm_input_info
