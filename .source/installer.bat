::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAhSXAWRAES0A5EO4f7+09qSrl0UQN4eaorz27+LMtwe/0nwfKUoxGxfivcFDxRWbS6iYBwgqGJOs3bLPsST0w==
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSjk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFAhSXAWRAES0A5EO4f7+09qSrl0UQN4eaorz27+LMtwe/0nwfKUoxGxfivcBGQ9UdyGufBkxuyNLuHeRNsuQth3eUh7dqE4oHgU=
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
:0.0.0
@echo off
setlocal EnableDelayedExpansion
@shift /0
FOR /F "usebackq" %%f IN (`PowerShell -NoProfile -Command "Write-Host([Environment]::GetFolderPath('Desktop'))"`) DO (
  SET "DESKTOP_FOLDER=%%f"
  )
(set \n=^
%=Do not remove this line=%
)
set 2directory_dir=%cd%
set 2l=(
set 2r=)
set website=null
set 2title=multiServer
set clsclear=[0m
set 21="<"
set 23=!21:"=!
set 22=">"
set 24=!22:"=!
title multiServer installer



::instalation procces
:32
cls
echo: Installing...
c:
if not exist "C:\multiServer\directory.txt" (
if not exist "C:\multiServer" (
md C:\multiServer
cls
goto pre
) else (
cls
goto pre
)
cls



:pre
cls
echo: Enter disk that on !2title! will be installed. !2l!for example: "D:" or "C:"!2r!
set /p kym=">:"

:setup
!kym!
%kym%
cd kym
cls
echo: Enter server directory. !2l!for example: "D:\myServers"!2r!
set /p syn=">:"
cd C:\multiServer
cd %syn%
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
) else (
goto check
)




:check
c:
cd C:\multiServer
timeout /t 1 /nobreak>nul
(
  echo !syn!
) > directory.txt
:: THERE DOWNLOAD PYTHON FILE TO c:\multiserver AND CREATE SHORTCUT FOR SYN
!kym!
%kym%
cd %syn%
cd %syn%\.multiServer
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/PACKER.exe -o packer.exe
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/multiServer-app.exe -o multiServer-app.exe
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/welcome.html -o welcome.html
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%syn%\.start-all.lnk');$s.TargetPath='%syn%\.multiServer\multiServer-app.exe';$s.Save()"
cd %syn%\.multiServer\assets
curl -k -L https://raw.githubusercontent.com/kyoshuske/multiServer/main/assets/icon.ico -o icon.ico
cd %syn%\.multiServer
!kym!
%kym%
cd kym
cd %syn%
cd %syn%\.multiServer
(
  echo # Main configuration file for multiServer.
  echo # Please read README.md on github before reporting a bug.
  echo #
  echo # To edit server list go to !syn!\.multiServer\servers.yml
  echo # For more info read welcome.html.
  echo # 
  echo # Created by: Kyoshuske
  echo # Uploaded on: github.com/kyoshuske
  echo # Version: 1.2.5
  echo # 
  echo # If you need help or if you want to report a bug,
  echo # join our discord server below and create a forum post.
  echo # 
  echo # Discord: https://discord.gg/MfdFmCCqm6
  echo # GitHub: https://github.com/kyoshuske/multiServer
  echo.
  echo settings:
  echo   global:
  echo     global-filename:
  echo       enable: false
  echo       filename: global-servername.jar
  echo     global-color:
  echo       enable: false
  echo       color: 2
  echo     global-javafile:
  echo       enable: true
  echo       filename: java
) > config.yml



(
  echo # Servers configuration file for multiServer.
  echo # Please read README.md on github before reporting a bug.
  echo #
  echo # To edit global settings go to !syn!\.multiServer\config.yml
  echo # For more info read welcome.html
  echo.
  echo server-list:
  echo - example-server1
  echo - example-server2
  echo servers:
  echo   example-server1:
  echo     drive: 'C:'
  echo     path: !syn!\example1
  echo     # *java-file: works only if: config.yml - 'global'/'global-filename'/'enable' = False
  echo     file: server.jar
  echo     max-heap-size: 1024M
  echo     # *java-file: works only if: config.yml - 'global'/'global-javafile'/'enable' = False
  echo     java-file: !syn!\example1\java.exe
  echo     visuals:
  echo       nogui: false
  echo       window-title: A minecraft server
  echo   example-server2:
  echo     drive: 'C:'
  echo     path: !syn!\example2
  echo     file: server.jar
  echo     max-heap-size: 1024M
  echo     java-file: !syn!\example2\java.exe
  echo     visuals:
  echo       nogui: false
  echo       window-title: A minecraft server
) > servers.yml

cls
echo: !2title! has been succesfully installed in "!syn!\.multiServer\".
explorer !syn!\.multiServer\
pause >NUL
) ELSE (
goto loader
:loader
cls
echo: !2title! is already installed.
echo: If you want to reinstall !2title! delete file "C:\multiServer\directory.txt" and restart installer.
pause >NUL
exit
)
exit