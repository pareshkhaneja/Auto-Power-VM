from pyVim.connect import SmartConnect
from pyVim.connect import Disconnect
from pyVmomi import vim
import configparser
import getpass
import ssl

# Reading config.ini file and reading contents from AutoPower Section

config=configparser.ConfigParser()
config.read('config.ini')
auto_power_config=config['AutoPower']

# Getting required values from config.ini file

host_ip=auto_power_config.get('host')
username=auto_power_config.get('username')
VM_Name=auto_power_config.get('VM Name')
vmslist=VM_Name.split(',')
Folder=auto_power_config.get('Folder')
Sub_Folder=auto_power_config.get('Sub-Folder')
Power_State=auto_power_config.get('Desired Power State')

vm_found='FALSE'

first_step = input('#'*40+'Auto Power VMs'+'#'*60+'\n\nHi, Before continue please make sure you have all the required configuration set in config.ini file.\n\nIf sure, Please input \'y\' and hit enter: ')

# Main Functionality Start
if first_step=='y':

    password= getpass.getpass('Please enter Corp Password for user '+username+'\nPassword: ')

    s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s.verify_mode = ssl.CERT_NONE

    manager = vim.OvfManager

    si = SmartConnect(host=host_ip, user=username, pwd=password, sslContext=s)     # Connects to Data Center
    print('Connected to Data Center - '+host_ip)

    dc = si.content.rootFolder.childEntity[0]

    obj = si.content.searchIndex.FindByInventoryPath(dc.name + '/vm/'+Folder+'/'+Sub_Folder)  # Finds the folder/subfolder in the complete data center

    vms = obj.childEntity  # Gives a list of all the child entries(folders/vms)

    for vm_search in vmslist:                   # Starts loop in vmslist configured by user
        for vm in vms:                          # Starts look in the vms found under desired path
            if vm.name==vm_search:
                vm_found='TRUE'
                print(vm_search.upper()+'---> '+vm_search + ' is present under ' + obj.parent.name + '/' + obj.name+'\n')
                if Power_State=='ON':           # Condition to switch ON the VM
                    if vm.runtime.powerState=='poweredOn':
                        print('The state of '+vm.name+' is already running\n')
                    else:
                        vm.PowerOn()
                        print('The state of ' + vm.name + ' is changed to running\n')

                    break
                elif Power_State=='OFF':        # Condition to switch Off the VM
                    if vm.runtime.powerState == 'poweredOff':
                        print('The state of ' + vm.name + ' is already OFF\n')
                    else:
                        vm.PowerOff()
                        print('The state of '+vm.name+' is changed to OFF\n')
                    break
            else:
                vm_found='FALSE'
        if vm_found=='FALSE':                   # If VM is not found then print message
            print(vm_search.upper()+'---> '+vm_search+' is not found under '+obj.parent.name + '/'+obj.name+'\n')

    Disconnect(si)                              # Disconnecting the session
    print('Session Disconnected\nThanks for using the Auto-Power-VM CLI!')
else:
    print('Exiting the program.')

