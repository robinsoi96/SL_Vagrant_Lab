# SL Vagrant Lab

The purpose of this project is to create own VM (Virtual Machine) using Vagrant

## Prerequisites

### Software required

- <a href="https://developer.hashicorp.com/vagrant/downloads">Vagrant</a>
- <a href="https://www.virtualbox.org/wiki/Downloads">Oracle VirtualBox</a> (VM provider used for this project)

For the software mentioned above, you may opt to use package manager for installation (e.g. Chocolatey for Windows, HomeBrew for MacOS, APT for Debian based Linux distro, YUM for RPM based Linux distro)

### Steps Required for Virtualization

- **For all OS and Linux distros:**

    - Enable Virtualization in BIOS menu (keyword to search could be `VTx`, `Secure virtual machine` or `Virtualization`)

- **Windows only (For Oracle VirtualBox):**

    - Search "Windows Features" in start menu and uncheck/disable other windows virtualiztion as below: 
        - `Microsoft Hyperv`
        - `Windows Hypervisor platform`
        - `Windows Subsystem for Linux`
        - `Docker Desktop`
        - `Virtual Machine Platform`