@echo off
@shift /0
setlocal EnableDelayedExpansion
C:
cd C:\multiServer
for /f %%a in (directory.txt) do (
  set out=%%a
)
set dir4=!out!\.multiServer\
del C:\multiServer
%out:~0,2%
cd %dir4%
del *.exe
del config.yml
del servers.yml
cls
echo: multiServer has been uninstalled.
pause >nul
exit
