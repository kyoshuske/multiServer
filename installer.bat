@echo off
@shift /0
setlocal EnableDelayedExpansion
(set \n=^
%=Do not remove this line=%
)
set 2l=(
set 2r=)
set 2title=multiServer
title !2title! installer
if not exist "C:\multiServer\directory.txt" (
c:
md C:\multiServer
md C:\launcher3
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/launcher.config -o config.yml
goto pr
) else (
goto in
)
:pr
cls
echo: Enter disk that on !2title! will be installed. !2l!for example: "D:" or "C:"!2r!
set /p kym=">:"
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
!kym!
md %syn%\.multiServer
md %syn%\.multiServer\app\assets
md %syn%\.multiServer\app\web
md %syn%\.multiServer\app\scripts
md %syn%\.multiServer\starts
md %syn%\.multiServer\app\data
cls
)
c:
cd C:\multiServer

(
  echo !kym!
) > kym.4c2U

(
echo @echo off
echo !kym!
echo cd !syn!\.multiServer\app\scripts
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/scripts/packer.py -o packer.py
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/scripts/multiServer-app.py -o multiServer-app.py
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/scripts-server/server.py -o server.py

echo cd !syn!\.multiServer

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/launcher/launcher.exe -o launcher.exe
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/config.yml -o config.yml
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/servers.yml -o servers.yml

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/multiServer-START_THIS.bat -o multiServer-START_THIS.bat

echo powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('!syn!\.start-servers.lnk');$s.TargetPath='"!syn!\.multiServer\multiServer-START_THIS.bat"';$s.Save()"
echo powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%appdata%\Microsoft\Windows\Start Menu\multiServer.lnk');$s.TargetPath='!syn!\.multiServer\launcher.exe';$s.Save()"

echo cd !syn!\.multiServer\app\assets
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/assets/icon.ico -o icon.ico

echo cd !syn!\.multiServer\app\web
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/main.css -o main.css
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/main.html -o main.html
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/main.js -o main.js

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/server.css -o server.css
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/server.html -o server.html
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/web/server.js -o server.js
echo exit
) > update-files.bat

echo: Installing...!\n! Please wait.
start /W /MIN update-files.bat

(
  echo !syn!
) > directory.txt

cls
echo: !2title! has been succesfully installed in "!syn!\.multiServer\".
explorer !syn!\.multiServer\
pause >NUL
exit
:in
cls
echo: !2title! is already installed.!\n! If you want to uninstall !2title! visit "https://github.com/kyoshuske/multiServer",!\n! and execute command for uninstalling.
pause >NUL
)
exit
