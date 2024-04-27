# default load settings:
argument = 0
debug = 0

# paths:
main = 'c:\\launcher3'
config = main + '\\config.yml'

try:
    import os
    import sys
    os.system('title launcher')
    
    from colorama import Fore; from colorama import *
    import time
    print(Fore.LIGHTBLACK_EX + ' ')
    print('-----------------------< launcher >-----------------------')
    print('Loading python and all required libraries...')

    import subprocess; from subprocess import Popen; from subprocess import *
    import webbrowser

    from threading import Thread
    from queue import Queue, Empty

    import eel
    from tkinter import messagebox

    import gevent
    import asyncio

    from psutil import *
    from ctypes import windll
    import win32gui, win32con, win32com.client

    import yaml
    from configobj import ConfigObj
except Exception: print('Module load error.'); sys.exit()

# load configuration:
print('Loading configuration...')
with open(config, 'r') as file: config = yaml.safe_load(file)
apps = {}
for app in config['apps']:
    apps[app] = config['apps'][app]

# try:
#     directory_txt = ('C:\\multiServer\\directory.txt')
#     file_output = open(directory_txt, 'r')
#     directory = file_output.readline().strip()
#     scripts = directory + '\\.multiServer\\app\\scripts\\'
#     print('Working in directory: \"' + directory + '\\.multiServer\"')
    
# except Exception: print('Configuration file missing.'); sys.exit()

def loadScript(file, arg):
    os.system('title launcher: ' + file)
    scriptpath = (scripts + '\\' + file)
    print('\nInitializing script: \"' + scriptpath + '\"...')

    if '\\' in file: scriptpath = file
    source = open(scriptpath).read()
    print(Fore.WHITE)

    exec(source, { 'launch': { 'ver': version , 'sc': file , 'dir': path , 'arg': arg } })


if __name__ == "__main__":
    try:
        app = sys.argv[1]
        version = apps[app]['version']
        path = apps[app]['path']
        scripts = path + apps[app]['scripts']
        script = apps[app]['noscript']
    except Exception: print('Invalid app config.'); sys.exit()
    if len(sys.argv)<1:
        try:
            debug = True; loadScript(script, '0')
        except Exception as exception: print(exception); sys.exit()
    else:
        try:
            script = sys.argv[2]

            argument = str(sys.argv[3])

        except Exception: pass
    try:
        loadScript(script , argument)
    except FileNotFoundError: print('Script not found.')
    except Exception as ex: print(ex)