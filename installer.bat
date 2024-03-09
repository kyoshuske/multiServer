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
md %syn%\.multiServer\assets
md %syn%\.multiServer\web
md %syn%\.multiServer\starts
md %syn%\.multiServer\data
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
echo cd !syn!\.multiServer
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.packer/packer.exe -o packer.exe
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp/multiServer-app.exe -o multiServer-app.exe
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp-server/server.exe -o server.exe

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/config.yml -o config.yml
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/servers.yml -o servers.yml

echo powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('!syn!\.start-servers.lnk');$s.TargetPath='!syn!\.multiServer\multiServer-app.exe';$s.Save()"
echo powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%appdata%\Microsoft\Windows\Start Menu\multiServer.lnk');$s.TargetPath='!syn!\.multiServer\multiServer-app.exe';$s.Save()"
echo cd !syn!\.multiServer\assets
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/assets/icon.ico -o icon.ico
echo cd !syn!\.multiServer\web
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp/web/main.css -o main.css
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp/web/main.html -o main.html
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp/web/main.js -o main.js

echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp-server/web/server.css -o server.css
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp-server/web/server.html -o server.html
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.webapp-server/web/server.js -o server.js
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
