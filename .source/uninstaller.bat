@echo off
@shift /0
setlocal EnableDelayedExpansion
title multiServis uninstaller
if exist "C:\multiServer\directory.txt" (
C:
cd C:\multiServer
for /f %%a in (directory.txt) do (
  set out=%%a
)
del /S /Q C:\multiServer
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
