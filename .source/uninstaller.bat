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
del *.exe
del config.yml
del servers.yml
C:
cd C:\multiServer
del C:\multiServer
echo: multiServer has been uninstalled.
exit
