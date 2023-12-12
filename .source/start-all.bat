::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAhSXAWRAES0A5EO4f7+09qSrl0UQN4eaorz27+LMtwe/0nwfKUoxGxfivcFDxRWbS6ibQA652dBuQQ=
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSzk=
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
::Zh4grVQjdCyDJGyX8VAjFAhSXAWRAES0A5EO4f7+09qSrl0UQN4eaorz27+LMtwe/0nwfKUoxGxfivcBGRdMdyGufBkxuyNDpnTLMt+Z0w==
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
@shift /0
setlocal EnableDelayedExpansion
title multiServer: launch
if not exist "C:\multiServer\directory" (
exit
) ELSE (
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
)
exit