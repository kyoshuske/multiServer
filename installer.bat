@echo off
@shift /0
setlocal EnableDelayedExpansion
(set \n=^
%=Do not remove this line=%
)
set pathms=C:\Users\!USERNAME!\AppData\Local\multiServer
set 2l=(
set 2r=)
set 2title=multiServer
title !2title! installer
if not exist "!pathms!\c.yml" (
c:
md !pathms!
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/launcher.config -o config.yml
goto di
) else (
goto in
)
:di
cls
echo: Enter server directory. !2l!for example: "D:\myServers"!2r!
set /p syn=">:"
cd C:\multiServer
if not exist "!syn!" (
echo: This directory does not exist.!\n! Press any key to enter directory again.
pause >NUL
goto di
) else (
cd /D !syn!\.multiServer\app\scripts
md %syn%\.multiServer
md %syn%\.multiServer\app\assets
md %syn%\.multiServer\app\web
md %syn%\.multiServer\app\scripts
md %syn%\.multiServer\starts
md %syn%\.multiServer\plugins
md %syn%\.multiServer\app\data
cls
)
c:
cd !pathms!

(
  echo:#configuration file for multiserver instalation
  echo:config:
  echo:   path: '%syn%'
  echo:   disk: '%kym%'
  echo:   0: 0
) > c.yml


C:
cd !pathms!
(
echo @echo off
echo cd /D !syn!\.multiServer\app\scripts
echo cls
echo title multiServer installer process 1
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/scripts/packer.py -o packer.py
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/scripts/multiServer-app.py -o multiServer-app.py
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/scripts-server/server.py -o server.py

echo cd !syn!\.multiServer

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/launcher/launcher.exe -o launcher.exe

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/config.yml -o config.yml
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/servers.yml -o servers.yml

echo cd !syn!\.multiServer\app\assets

echo cd !syn!\.multiServer\app\web
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/app.css -o app.css
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/app.html -o app.html
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/app.js -o app.js

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/server.css -o server.css
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/server.html -o server.html
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/server.js -o server.js
echo exit
) > update-files.bat



C:
cd !pathms!
cls
echo: Installing files... !\n! DO NOT CLOSE THIS OR ANY OTHER CMD WINDOW
start /W /MIN update-files.bat
cls


echo: !2title! has been succesfully installed in "!syn!\.multiServer\".
explorer !syn!\.multiServer\
pause >NUL
exit
:in
cls
echo: !2title! is already installed.!\n! If you want to uninstall !2title! visit "https://github.com/kyoshuske/multiServer",!\n! and follow intructions or delete this directory: "C:\Users\%USERNAME%\AppData\Local\multiServer".
pause >NUL
)
exit
