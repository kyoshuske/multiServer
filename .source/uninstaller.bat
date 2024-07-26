@echo off
@shift /0
setlocal EnableDelayedExpansion
title multiServis uninstaller
if exist "C:\Users\%USERNAME%\AppData\Local\multiServer" (
C:
cd C:\Users\%USERNAME%\AppData\Local\multiServer
del /S /Q C:\Users\%USERNAME%\AppData\Local\multiServer
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
