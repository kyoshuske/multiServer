@echo off
@shift /0
setlocal EnableDelayedExpansion
title multiServer
if not exist "C:\multiServer\directory.txt" (
exit
) ELSE (
c:
cd C:\multiServer
for /f %%a in (directory.txt) do (
  set out=%%a
)

echo: out: '!out!'
set dir4=!out!\.multiServer\
%out:~0,2%
cd !dir4!
del *.cmd
timeout /t 1 /nobreak>nul
echo: PACKING...
start /W packer.exe
set dir4=!out!\.multiServer\starts\
%out:~0,2%
cd !dir4!
cd %dir4%
forfiles /s /m *.cmd /c "cmd /c start cmd /k @path"



)
exit
