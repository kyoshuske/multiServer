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
%kym%
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
%kym%
cd %syn%
cd %syn%\.multiServer
cls
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/PACKER.exe -o packer.exe
cls
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/multiServer-app.exe -o multiServer-app.exe
cls
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/welcome.html -o welcome.html
cls
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%syn%\.start-all.lnk');$s.TargetPath='%syn%\.multiServer\multiServer-app.exe';$s.Save()"
cls
cd %syn%\.multiServer\assets
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/assets/icon.ico -o icon.ico
cls
%kym%
cd %syn%\.multiServer
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/config.yml -o config.yml
cls
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/.source/.default-settings/servers.yml -o servers.yml
cls
echo: !2title! has been succesfully installed in "!syn!\.multiServer\".
explorer !syn!\.multiServer\
pause >NUL
exit
:loader
cls
echo: !2title! is already installed.
echo: If you want to uninstall !2title! visit "https://github.com/kyoshuske/multiServer" and execute command for uninstalling.
pause >NUL
)
exit
