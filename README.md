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

## Setting own hostname and VM name

1) Prepare a yaml file named "config.yml" in the same directory as this README.md

    ```yaml
    VM_config:
        hostname: "<YOUR_VM_HOSTNAME>"
        VM_name: "<YOUR_VM_NAME_IN_VIRTUALBOX>"
    ```

    - Reason to do so is because config.yml is mentioned in [.gitignore](./.gitignore), so that your credentials won't be tracked and pushed to remote repo by Git if any changes needed

2) In Vagrantfile, enable all info to be derived from the yaml file prepared

    ```ruby
    require 'yaml' # Telling the script that it requires yaml reference

    # Load the YAML file and derive all information respectively
    config_info = YAML.load_file('./config.yml')
    vmHostname = config_info['VM_config']['hostname'] # VM hostname
    vmName = config_info['VM_config']['VM_name'] # VM name to be reflected in VirtualBox
    ```

3) In config block of Vagrantfile, add this line to set hostname

    ```ruby
    # Assign hostname
    config.vm.hostname = vmHostname
    ```

4) Add the below line in the `config.vm.provider "virtualbox" do |vb|` block of Vagrantfile

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

- Run `vagrant validate` to validate Vagrantfile before kickstart Vagrant execution

- Run `vagrant up` to start or boot up the VM
    
    - If you are running this the first time, it will take time because it needs to download the box (ubuntu/jammy64) from Vagrant Cloud

- Run `vagrant reload` to restart or reboot the VM

    - Run `vagrant reload --provision` to refresh if updated provisioning script

- Run `vagrant ssh` to SSH to the VM

- Run `vagrant halt` to shut down the VM
    
    - **NOTE:** Please also run this before shutting down your host machine]

- Run `vagrant destroy -f` to destroy or delete the VM, followed by `vagrant global-status --prune` to clean up the global status list of Vagrant