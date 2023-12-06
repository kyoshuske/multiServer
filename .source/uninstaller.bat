@echo off
@shift /0
setlocal EnableDelayedExpansion
title multiServis: uninstaller
if exist "C:\multiServer\directory.txt" (
C:
cd C:\multiServer
for /f %%a in (directory.txt) do (
  set out=%%a
)
set dir4=!out!\.multiServer\
del C:\multiServer\directory.txt
del C:\multiServer
del directory.txt
%out:~0,3%
%out:~0,2%
cd %dir4%
del *.exe
del config.yml
del servers.yml
del %dir4%
cls
echo: multiServer has been uninstalled.
pause >nul
goto l
) else (
echo: multiServer is already uninstalled.
pause >nul
)
:l
exit
