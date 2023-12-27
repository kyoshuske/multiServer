![multiServer](assets/github-banner.png)

_*[click here](http://localhost:42439/main.html)* to open web app_

# Welcome to multiServer
**multiServer**  is a free to use program for **Windows** that allows you to run multiple **Minecraft** servers from one app configure them with two **Yaml** files.
# How to install or uninstall?
## Install
Copy and paste code below into the **command prompt**.
```
C: & md C:\msfiles & cd C:\msfiles & curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/installer.bat -o multiservis-inst.bat & powershell Start -File "multiservis-inst.bat '/K %~f0 runas'" -Verb RunAs & exit & exit
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
# How to use? 
## Configuration 
Open your server's directory and search for the **'.multiServer'** folder. Then open the **'config.yml'** to configure global settings properties. To add and configure each server open **'servers.yml'** and change properties.
## Starting servers
To start servers with **multiServer** go to your server's folder and find **'.multiServer'**. If you already did the configuration, you can start **'multiServer-App.exe'**. Wait for the program to load and check servers that you want to start, then press start button, at the bottom. 
# Change log
## version 1.2.6
 - fixed 'global-javafile' in config.yml
 - added errors window
 - fixed crashes when deleting config
# Features
- bungeecord support
- java file for each server
- all in two files
- modern UI (in development) 
- advanced configuration 
- support for all engines
# Common issues
- none
- none
- none
