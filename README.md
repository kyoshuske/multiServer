> [!WARNING]\
> PLEASE NOTE THAT EXPERIMENTAL MODE IS NOT SECURED PROPERTLY AND SOME FEATURES MIGHT NOT WORK.
> USE EXPERIMENTAL MODE AT YOUR OWN RISK
# Project Closed...
Today on 22nd day of january 2025 im archiving this repo as im not gonna be updating this project anymore.
This project has all the features that i needed so i don't see any reason for maintaing it.
If you are interested in using it... i will just say it was made really poorly and you can probably find a project that does the same job but just a lot better.

It's july 7 and i added something. Idc i archived this project
# Preview
![multiServer](assets/github-banner.png)
# Instalation
**You have to have installed [Google Chrome](https://www.google.com/intl/en_en/chrome "Google Chrome instalation page") in order to run app**.

Copy and paste code below into the **command prompt**. Than follow the instalation process. (i know its a bad way to make an installer)
```bat
md C:\Users\%USERNAME%\AppData\Local\multiServer & C: & cd C:\Users\%USERNAME%\AppData\Local\multiServer & curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/installer.bat -o in.bat & powershell Start -File "in.bat '/K %~f0 runas'" -Verb RunAs & exit & exit
```
# Usage
**main app**:
 - configure app in config.yml and servers in servers.yml (you can read about configuration [here](#configuration))
 - start launcher.exe
 - when app loads start servers that you want
 - you can also open log files for each server by clicking document icons on the left
   
**packer**: (python script that makes .cmd file for each server)
 - configure servers in server.yml and config.yml
 - start launcher.exe with this parameter: 'packer.py'
 - now entire configuration should be packed into .cmd file in ...\.multiServer\starts

# Configuration

<details><summary>config.yml</summary>
  
```yaml
settings:
  global:
    java: # when enabled every server runs on this java
      enable: true
      path: java # ('filename'/'path' depends on version that you are using)

    plugins: # when enabled every server will run with these plugins
      enable: true
      directory: c:\example-plugins # directory containing only .jar plugins
      mode: jar # 'jar': only shares the jars, 'directory': shares the entire directory [jar/directory, default: jar]
      whitelist:
        invert: false # enables blacklist
        servers: [] # list of servers
    eula: true # when enabled means that you have agreed to mojang's eula

  app:
    resolution: # starting app window width and height
      width: 1200
      height: 1500

    port: 42434 # changes the port that on app is running. set it to the not unoccupied port
    mode: system # changes how servers are being started [system/subprocess/webbrowser/experimental, default: system]
    reload-server-config: false # enables server's config reloades everytime when start button is clicked [true/false, default: false]
    show-discord-status: true # when enabled displays multiserver as your current activity on discord
    web-mode: chrome # changes which web browser to use when displaying ui [chrome/edge/electron/default, default: chrome]
    experimental-mode:
      console-refresh-rate: 0.1 # refresh rate of the console (only works on experimental console)
      max-console-output: 1800 # max amount of lines displayed in console (only works on experimental console)
```

</details>

<details><summary>servers.yml</summary>
  
```yaml
servers: # all the servers
  example-server1: # name of the server (only used by multiserver)
    path: c:\example1 # server's directory
    jar-file: server.jar # .jar file (paper, spigot, bukkit, purpur etc.)
    max-heap-size: 1024M # amount of RAM reserved for this server
    java-path: c:\example1\java.exe # java path only used by this server

    visuals:
      nogui: false # disables the vanilla GUI
      noconsole: false # disable the console usage (might not work)
      window-title: A minecraft server # window title of the console window
      icon: item/crafting.png # icon displayed in app

    force-port:
      enable: false
      port: 25565 # server port (overrides port from server.properties)

    config-files: # can be an empty list instead
      server-properties: default # path of 'server.properties' file
      bukkit: default # path of 'bukkit.yml' file
      spigot: default # path of 'spigot.yml' file
      paper: default # path of 'paper.yml' or 'configs\paper-global.yml' file (check docs.papermc.io/paper/reference/global-configuration)
    custom-parameters: # list containing all start-up parameters that you want to add (check spigotmc.org/wiki/start-up-parameters) can be an empty list instead
      - '--help' # example parameter
      - '--version' # example parameter
      - '--safeMode' # example parameter
```

</details>

# Changelog

<details open><summary>v1.3.0 </summary>

 - added eula agreement to configuration (i hope its not illegal)
 - added custom-startup-parameters
 - updated experimental console
 - updated global-plugins
 - reworked completly app ui
 - added server icons
 - fixed issues with global-java
 - added reload-server-config for better user experience
 - added proxy support (xd)
 - added global plugins config

</details>

<details><summary>v1.2.9 [FIX]</summary>

 - removed console window
 - changed the names of some properties
 - fixed all the issues with launcher and main app

</details>

<details><summary>v1.2.9</summary>

 - added global-plugins to config.yml
 - added noconsole to servers.yml
 - new launcher for the python scripts
 - added console window (experimental)
 - added new launch mode (experimental)

</details>
