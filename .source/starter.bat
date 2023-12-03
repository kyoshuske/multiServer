@echo off
@shift /0
setlocal EnableDelayedExpansion
title multiServer: launch
C:
cd C:
cd C:\multiServer
for /f %%a in (directory.txt) do (
  set out=%%a
)
echo: out: '!out!'
set dir4=!out!\.multiServer\
%out:~0,2%
cd !dir4!
cd %dir4%
del *.cmd
del error.bat
timeout /t 1 /nobreak>nul
echo: PACKING...
start /W packer.exe
if not exist "%dir4%\error.bat" (
set dir4=!out!\.multiServer\starts\
%out:~0,2%
cd !dir4!
cd %dir4%
forfiles /s /m *.cmd /c "cmd /c start cmd /k @path"
echo -------------------------------------------------------------------------------------------
) ELSE (
start /W error.bat
del error.bat
)
exit