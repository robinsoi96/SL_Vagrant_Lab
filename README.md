# SL VM Lab

The purpose of this project is to create a zero-cost local VM (Virtual Machine) using Oracle VirtualBox

To understand the architecture of this project, refer to the [architecture documentation](./Documentations/Architecture/README.md).

## Prerequisites

### Required Software

- Python 3.8 or later
- [Oracle VirtualBox](https://www.virtualbox.org/wiki/Downloads) (VM provider used for this project) [At least version 7.1.4 and above]

### Steps Required for Virtualization

- **For all OS and Linux distros:**

    - Enable Virtualization in BIOS/UEFI settings
    - Look for one of the following keywords:
        - `VTx`
        - `Secure virtual machine`
        - `Virtualization`

- **If using Windows OS (For Oracle VirtualBox):**

    - Search "Windows Features" in start menu and disable the following features for full performance mode: 
        - `Microsoft Hyperv`
        - `Windows Hypervisor platform`
        - `Virtual Machine Platform`

### `VBoxManage` CLI

This project uses VBoxManage CLI for VM creation and provisioning.

For more information on VBoxManage CLI usage, may refer to the [official documentation](https://www.virtualbox.org/manual/ch08.html).

### Additional Documentation

Please follow all additional prerequisites mentioned in this [folder](./Documentations/Prerequisites/) before kickstart this project.

## Getting Started

Setup and usage instructions are provided in the following folder:
- [Project Guidelines](./Documentations/Guidelines/)

## Archived / Experimental Branch

- [`vagrant`](https://github.com/robinsoi96/SL_VM_Lab/tree/vagrant) &mdash; Earlier experiment to automate VM provisioning using Vagrant