![multiServer](assets/github-banner.png)

# Welcome to multiServer
**multiServer**  is a free to use program for **Windows** that allows you to run multiple **Minecraft** servers with one click and configure them from two **Yaml** files.
# How to install or uninstall?
## Install
Copy and paste code below into the **command prompt**.
```
C: & md C:\msfiles & cd C:\msfiles & curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/installer.bat -o multiservis-inst.bat & powershell Start -File "multiservis-inst.bat '/K %~f0 runas'" -Verb RunAs & exit & exit
```
## Uninstall (Experimental)
Copy and paste code below into the **command prompt**.
```
C: & md C:\msfiles & cd C:\msfiles & curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/uninstaller.bat -o multiservis-uninst.bat & powershell Start -File "multiservis-uninst.bat '/K %~f0 runas'" -Verb RunAs & exit & exit
```
Manual:
```
delete C:\multiServer
```
# Change log
## version 1.2.6
 - fixed 'global-javafile' in config.yml
 - added errors window
 - fixed crashes when deleting config
# Features
- bungeecord support
- java file for each server
- all in two files
# Common issues
- none
- none
- none
