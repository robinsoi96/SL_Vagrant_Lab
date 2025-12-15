# SL Vagrant Lab

The purpose of this project is to create own VM (Virtual Machine) using Vagrant

## Prerequisites

### Software required

- <a href="https://developer.hashicorp.com/vagrant/downloads">Vagrant</a>
- <a href="https://www.virtualbox.org/wiki/Downloads">Oracle VirtualBox</a> (VM provider used for this project)
- <a href="https://git-scm.com/install/windows">Git Bash</a> [if you are using Windows]

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

## Configuration settings to be updated

- Prepare a yaml file named "config.yml" in the same directory as this README.md

    ```yaml
    VM_config:
        hostname: "<YOUR_VM_HOSTNAME>"
        VM_name: "<YOUR_VM_NAME_IN_VIRTUALBOX>"
    ```

    - Reason to do so is because config.yml is mentioned in [.gitignore](./.gitignore), so that your credentials won't be tracked and pushed to remote repo by Git if any changes needed

    - In Vagrantfile, all configuration info done will be derived from the yaml file prepared

    ```ruby
    require 'yaml' # Telling the script that it requires yaml reference

    # Load the YAML file and derive all information respectively
    config_info = YAML.load_file('./config.yml')
    vmHostname = config_info['VM_config']['hostname'] # VM hostname
    vmName = config_info['VM_config']['VM_name'] # VM name to be reflected in VirtualBox
    ```

    - The code line in Vagrantfile below updates the hostname set in the config.yml

    ```ruby
    # Assign hostname
    config.vm.hostname = vmHostname
    ```

    - The code line in Vagrantfile below updates the VM name set in the config.yml

    ```ruby
    vb.name = vmName # Set VM name in VirtualBox
    ```

## Configurations done in `Vagrantfile`

- Set the OS of the VM to be Ubuntu

    ```ruby
    config.vm.box = "ubuntu/jammy64"
    ```

- Set Public Network for the VM

    ```ruby
    config.vm.network "public_network"
    ```

- Disable the default synced folder setting

    ```ruby
    config.vm.synced_folder ".", "/vagrant", disabled: true
    ```

- Decide 1 common shared folder between host and VM

    ```ruby
    config.vm.synced_folder "./shareFile", "/vagrant"
    ```

    - All content of [shareFile](./shareFile/) will be shared at /vagrant folder in the VM
    - **NOTE:** This code line above need to be placed after the code line where default synced folder setting, because pointing to /vagrant folder in VM


- Set the VM to have 1GB RAM and 2 CPUs

    ```ruby
    config.vm.provider "virtualbox" do |vb|
        vb.memory = "1024" # Set this VM to be allocated with 1GB of RAM
        vb.cpus = 2 # 2 CPUs
    end
    ```

- Using external shell script for VM provisioning

    ```ruby
    config.vm.provision "shell", path: "./shareFile/provisioning/provision.sh"
    ```

    - The main shell script [provision.sh](./shareFile/provisioning/provision.sh) is used for VM provisioning

## Project Implementation

The main bash script [main.sh](./main.sh) will be main script for this project.

In Linux host machine, do as below to run the main script:

```shell
chmod +x main.sh
./main.sh
```

In Windows host machine, please ensure you open your Git Bash terminal to run the main script:

```shell
./main.sh
```

The main script will kickstart the VM build, and then prompt for interactive response after the VM build is completed.

The main interactive prompt after the VM build will be as below:

- Reboot the VM
- Reboot the VM by updating the provisioning action
- Destroy the entire VM configuration (Delete entire VM built)
- Shut down the VM

You may try and play around with this main script.