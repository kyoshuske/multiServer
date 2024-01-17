![multiServer](assets/github-banner-new.png)



# Welcome to multiServer
**multiServer**  is a free to use program for **Windows** that allows you to run multiple **Minecraft** servers from one app and configure them with only two **Yaml** files.

###### _*[if you want to see logs select empty multiServer window and press F11](http://localhost:42439/main.html)*_
# How to Setup?
## Install
Copy and paste code below into the **command prompt**.
```
md C:\msfiles & C: & cd C:\msfiles & curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/installer.bat -o in.bat & powershell Start -File "in.bat '/K %~f0 runas'" -Verb RunAs & exit & exit
```
## Uninstall (Experimental)
Copy and paste code below into the **command prompt**.
```
md C:\msfiles & C: & cd C:\msfiles & curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/uninstaller.bat -o un.bat & powershell Start -File "un.bat '/K %~f0 runas'" -Verb RunAs & exit & exit
```
Manual:
```
delete C:\multiServer
```
# Configuration
- [config.yml](#config.yml)
- [servers.yml](#servers.yml)
# Change log
- [version 1.2.8](#v-128)
- [version 1.2.7](#v-127)
# Features
- all in two files
- modern app UI
- advanced configuration
- fast server selector in app
- port section
- java file for each server


# More
## Configs


### config.yml
``
settings:
  global:
    global-filename:
      enable: false
      filename: global-servername.jar
    global-color:
      enable: false
      color: 2
    global-javafile:
      enable: true
      filename: java
  app:
    resolution:
      width: 1200
      height: 1500
    fullscreen-enable: true
    port: 42434
``
### servers.yml


## change-log
### version 128
 - added 'force-port' section in 'servers.yml'
 - added 'config-files' section in 'servers.yml'
 - added 'bukkit' to section 'config-files' in 'servers.yml'
 - added 'server-properties' to section 'config-files' in 'servers.yml'
### version 127
 - added app UI
 - fixed crashes with 'packer.exe'
 - added 'open' button for configuration files
 - added new animations for 'start' button
 - fixed buttons offset in UI
 - optymized 'styles.css' 
 - fixed 'nogui'
 - added 'open latest.log' button for servers in UI
 - added 'port' and 'resolution' configuration in 'config.yml'
