@echo off
@shift /0
setlocal EnableDelayedExpansion
FOR /F "usebackq" %%f IN (`PowerShell -NoProfile -Command "Write-Host([Environment]::GetFolderPath('Desktop'))"`) DO (
  SET "DESKTOP_FOLDER=%%f"
  )
(set \n=^
%=Do not remove this line=%
)
set 2directory_dir=%cd%
set 2l=(
set 2r=)
set 2title=multiServer
set 21="<"
set 23=!21:"=!
set 22=">"
set 24=!22:"=!
title !2title! installer
c:
if not exist "C:\multiServer\directory.txt" (
md C:\multiServer
goto pre
) else (
goto loader
)
:pre
cls
echo: Enter disk that on !2title! will be installed. !2l!for example: "D:" or "C:"!2r!
set /p kym=">:"
:setup
!kym!
cls
echo: Enter server directory. !2l!for example: "D:\myServers"!2r!
set /p syn=">:"
cd C:\multiServer
md %syn%\.multiServer
md %syn%\.multiServer\assets
md %syn%\.multiServer\starts
cd %syn%\.multiServer
cls
if not exist "!syn!" (
echo: This directory does not exist.
echo: Press any key to enter directory again.
pause >NUL
goto setup
)
:check
c:
cd C:\multiServer
timeout /t 1 /nobreak>nul
(
  echo !syn!
) > directory.txt
!kym!

c:
cd C:\msfiles
(
echo @echo off
echo !kym!
echo cd !syn!\.multiServer
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/PACKER.exe -o packer.exe
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/multiServer-app.exe -o multiServer-app.exe
echo powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('!syn!\.start-all.lnk');$s.TargetPath='!syn!\.multiServer\multiServer-app.exe';$s.Save()"
echo cd !syn!\.multiServer\assets
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/assets/icon.ico -o icon.ico
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/style.css -o style.css
echo !kym!
echo cd !syn!\.multiServer
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/config.yml -o config.yml
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/servers.yml -o servers.yml
echo curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/help.html -o help.html
echo exit & exit & exit
) > files-install.bat
echo: Installing...
echo: Please wait.
start /W /MIN "C:\msfiles\files-install.bat"


echo: !2title! has been succesfully installed in "!syn!\.multiServer\".
explorer !syn!\.multiServer\
pause >NUL
exit
:loader
cls
echo: !2title! is already installed.
echo: If you want to uninstall !2title! visit "https://github.com/kyoshuske/multiServer",!\n! and execute command for uninstalling.
pause >NUL
)
exit
