#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -d $SCRIPT_DIR/vagrant_log ]; then
    mkdir -p $SCRIPT_DIR/vagrant_log
fi

CURRENT_DATETIME="$(date +"%Y%m%d_%H%M%S")"
EXECUTION_LOGFOLDER="$SCRIPT_DIR/vagrant_log/"
SCRIPT_LOGFILE="$EXECUTION_LOGFOLDER/vagrant_$CURRENT_DATETIME.log"
echo "Execution log for this script is now recorded in $SCRIPT_LOGFILE"

exit_script() {
    rm -rfv $EXECUTION_LOGFOLDER/vm_status.log
    while :
    do
        read -p "Would you like to remove the entire execution log folder $EXECUTION_LOGFOLDER, including the current execution log file $SCRIPT_LOGFILE? [Y/N]: " ans
        case $ans in
            [Yy] )
                rm -rfv $EXECUTION_LOGFOLDER
                break
                ;;
            [Nn] )
                while :
                do
                    read -p "Would you like to remove the current execution log file $SCRIPT_LOGFILE? [Y/N]: " reply
                    case $reply in
                        [Yy] )
                            rm -rfv $SCRIPT_LOGFILE
                            break 2
                            ;;
                        [Nn] )
                            break 2
                            ;;
                        * )
                            echo "Please give correct respond"
                            ;;
                    esac
                done
                ;;
            * )
                echo "Please give correct respond"
                ;;
        esac
    done
    echo "Exit the script now"
    exit 0
}

{
    echo "Executing Vagrant VM build in $SCRIPT_DIR"

    vagrant up

    echo "Vagrant VM build completed !!!"

    touch $EXECUTION_LOGFOLDER/vm_status.log

    while :
    do
        vagrant status | tee $EXECUTION_LOGFOLDER/vm_status.log
        if [ "$(cat $EXECUTION_LOGFOLDER/vm_status.log | grep poweroff )" != ""  ]; then
            echo -e "\nThe VM is OFF now"
        elif [ "$(cat $EXECUTION_LOGFOLDER/vm_status.log | grep running )" != "" ]; then
            echo -e "\nThe VM is ON now"
        else
            continue
        fi
        echo -e "\nBelow are the key numbers for next action..."
        echo "1: Reboot the VM"
        echo "2: Reboot the VM by updating provision steps"
        echo "3: Destroy the VM"
        echo "4: Shut down the VM"
        read -p "Please key in the number for next action: " key_value

        case $key_value in
            1 )
                echo "Reboot the VM now"
                vagrant reload
                echo "Reboot completed"
                ;;
            2 )
                echo "Update the provisioning steps in the VM now"
                vagrant reload --provision
                echo "Done updating the provisioning steps"
                ;;
            3 )
                echo "Destroy all configuration of the VM now"
                vagrant destroy -f
                echo "Clean up the global status list of Vagrant after destroying the VM"
                vagrant global-status --prune
                echo "Done. Now exiting the script."
                exit_script
                ;;
            4 )
                echo "Shut down the VM now"
                vagrant halt
                echo "Shut down completed"
                while :
                do
                    read -p "\nWould you like to end this script? [Y/N]:" respond
                    case $respond in
                        [Yy] )
                            echo "Exit the script now"
                            exit_script
                            ;;
                        [Nn] )
                            break
                            ;;
                        * )
                            echo "Please give correct respond"
                            ;;
                    esac
                done
                ;;
            * )
                echo "Please key in the correct key value to the prompt"    
        esac
    done
} | tee $SCRIPT_LOGFILE