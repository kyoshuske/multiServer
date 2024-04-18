import sys

version = '1.2.9'

# default:
argument = 0
debug = 0
script = 'multiServer-app.py'

def launcherExit(code):
    print('')
    sys.exit()
try:
    import os
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



except Exception: print('Module load error (? not an executable ?)'); sys.exit()


try:
    directory_txt = ('C:\\multiServer\\directory.txt')
    file_output = open(directory_txt, 'r')
    directory = file_output.readline().strip()
    scripts = directory + '\\.multiServer\\app\\scripts\\'
    print('Working in directory: \"' + directory + '\\.multiServer\"')
    
except Exception: print('File does not exist.'); sys.exit()

def loadScript(file, arg):
    os.system('title launcher: ' + script)
    path = (scripts + file)
    print('\nInitializing script: \"' + path + '\"...')

    if '\\' in file: path = file
    source = open(path).read()
    print(Fore.WHITE)
    if debug != True:
        os.system('cls')

    exec(source, { 'launch': { 'ver': version , 'sc': file , 'dir': directory , 'arg': arg } })


arg = {}
if __name__ == "__main__":
    if len(sys.argv)<2:
        debug = True; loadScript('multiServer-app.py', '0')
        # os.system('title launcher: default script')
        # print('\nNo arguments.\nInitializing default script...'); subprocess.Popen(([(directory + '\\.multiServer\\launcher.exe'), 'multiServer-app.py', '0', '0'])); sys.exit()
    else:
        len = 0
        try:
            for args in sys.argv:
                len = int(len) + 1


            script = str(sys.argv[1])

            argument = str(sys.argv[2])

            debug = str(sys.argv[3])
            if debug == '1' or 'true':
                debug = True


        except Exception: pass
    try:
        loadScript(script , argument)
    except FileNotFoundError: print('Script not found.')
    except Exception as ex: print(ex)