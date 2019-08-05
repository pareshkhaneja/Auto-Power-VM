## Auto-Power-VM 

#### Auto-Power-VM is a command line utility to auto power ON/OFF your vcenter VMs. The usage is simple. You just need to clone the repository in your local and configure config.ini file
Here is the sample run.

```
C:\Users\pkhaneja\Desktop>python Auto-Power-VM-CLI.py
########################################Auto Power VMs############################################################

Hi, Before continue please make sure you have all the required configuration set in config.ini file.

If sure, Please input 'y' and hit enter: y
Please enter Corp Password for user pkhaneja
Password:
Connected to Data Center - 10.113.11.11
VM1---> VM1 is present under Folder/Sub-Folder

The state of VM1 is already OFF

VM2---> VM2 is not found under Folder/Sub-Folder

Session Disconnected
Thanks for using the Auto-Power-VM Command Line Utility!
```

Here is the sample config.ini file.
```
[AutoPower]
host=10.119.11.11
username=admin
VM Name=VM1,VM2
Folder=Folder
Sub-Folder=Sub-Folder
Desired Power State=OFF
```
### Points to remember:
1. Don't change the section/variable name. You just need to provide the values. 
2. There are only two desired Power States "ON" and "OFF"
3. You can provide list of comma separated VMs.

