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

- Set the VM to have 1GB RAM and 2 CPUs

    ```ruby
    config.vm.provider "virtualbox" do |vb|
        vb.memory = "1024" # Set this VM to be allocated with 1GB of RAM
        vb.cpus = 2 # 2 CPUs
    end
    ```

## Project Implementation

- Run `vagrant up` to start or boot up the VM
    
    - If you are running this the first time, it will take time because it needs to download the box (ubuntu/jammy64) from Vagrant Cloud

- Run `vagrant reload` to restart or reboot the VM

- Run `vagrant ssh` to SSH to the VM

- Run `vagrant halt` to shut down the VM
    
    - **NOTE:** Please also run this before shutting down your host machine]

- Run `vagrant destroy -f` to destroy or delete the VM, followed by `vagrant global-status --prune` to clean up the global status list of Vagrant