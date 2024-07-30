> [!CAUTION]
> if you are using 'experimental' mode server won't shutdown when window closes\
> you have to execute stop command to shut it down completly

# Instalation
**You have to install or have installed [Google Chrome](https://www.google.com/intl/en_en/chrome/) to run app's gui**.\
step 1:
 - Copy and paste code below into the **command prompt**.
```
md C:\Users\%USERNAME%\AppData\Local\multiServer & C: & cd C:\Users\%USERNAME%\AppData\Local\multiServer & curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/installer.bat -o in.bat & powershell Start -File "in.bat '/K %~f0 runas'" -Verb RunAs & exit & exit
```
# Usage
**main app**:
 - configure app with 'config.yml' and 'servers.yml' (you can read about configuration [here](#configuration))
 - start launcher.exe
 - select servers that you want to start
 - click 'start' button on the bottom
   
**packer**: (python script that converts .yml config into .cmd file)
 - configure servers in 'server.yml' and 'config.yml'
 - start launcher.exe with this two parameters: "packer.py" ("launcher.exe" "packer.py")
----

# Configuration

<details><summary>config.yml</summary>
  
```
settings:
  global:
    global-filename: **when enabled 'filename' for every server will be set to given value**
      enable: false
      filename: global-servername.jar

    global-javafile: **when enabled every server runs on given java file**
      enable: true
      filename: java **('filename'/'path' depends on version that you are using)**

  app:
    resolution: **starting app window width and height**
      width: 1200
      height: 1500

    port: 42434 **changes the port that on app is running. set it to the not unoccupied port**

    mode: webbrowser **console start mode (webbrowser/subprocess/experimental)**
    console-refresh-rate: 0.2 **refresh rate of the console (only works on experimental console)**
```

</details>

<details><summary>servers.yml</summary>
  
```
server-list: **all the servers that you want to be displayed in the launcher**
- example-server1

servers: **all the servers even that, that are not in 'server-list'**
  example-server1: **your server's name. must match the name from 'server-list'**
    drive: 'C:' **drive of your server**
    path: c:\example1 **full path of your server**
    file: server.jar **engine file of your server (paper, spigot, purpur, bukkit, etc.)**
    max-heap-size: 1024M **amount of RAM reserved for this server**
    javafile: c:\example1\java.exe **only works if 'global-javafile' is disabled**

    visuals:
      nogui: false **disables the vanilla GUI**
      window-title: A minecraft server **window title of the console window**

    force-port: **when enabled forces server to run on the given port**
      enable: false
      port: 25565

    config-files:
      server-properties: default **path of the server's 'server.properties' file**
      bukkit: default **path of the server's 'bukkit.yml' file**
      spigot: default **path of the server's 'spigot.yml' file**
      paper: default **path of the server's 'paper.yml' or 'configs\paper-global.yml' file**
```

</details>

# Changelog

<details><summary>v1.2.9 [FIX]</summary>

 - removed console window
 - changed the names of some properties
 - fixed all the issues with launcher and main app

</details>

<details open><summary>v1.2.9</summary>

 - added 'global-plugins' to config.yml
 - added 'noconsole' to servers.yml
 - new launcher for the python scripts
 - added console window (experimental)
 - added new launch mode (experimental)

</details>
