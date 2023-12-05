@echo off
@shift /0
setlocal EnableDelayedExpansion
C:
cd C:\multiServer
for /f %%a in (directory.txt) do (
  set out=%%a
)
set dir4=!out!\.multiServer\
%out:~0,2%
cd %dir4%
del *.cmd
start /W packer.exe
%out:~0,2%
cd !out!\.multiServer\starts
forfiles /s /m *.cmd /c "cmd /c start cmd /k @path"
exit
