# default:
argument = 0
debug = 0
script = 'multiServer-app.py'

try:
    import sys
    import os
    os.system('title launcher')
    
    from colorama import Fore; from colorama import *
    import time
    print(Fore.LIGHTBLACK_EX + ' ')
    print('-----------------------< launcher >-----------------------\nLoading python and all required libraries...')

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




except Exception: print('Module load error (not an executable ?)'); time.sleep(1); sys.exit()


try:

    config_path = os.path.expanduser('~') + "\\AppData\\Local\\multiServer"
    config_yml = config_path + '\\c.yml'
    with open(config_yml, 'r') as file: cfg = yaml.safe_load(file); cfg = cfg['config']
    directory = cfg['path']


    scripts = directory + '\\.multiServer\\app\\scripts\\'
    print('Working in directory: \"' + directory + '\\.multiServer\"')
    directory += "\\.multiServer\\"
    
except Exception: print('File does not exist.'); sys.exit()

def loadScript(file, arg):
    path = (scripts + file)
    print('initializing script: \"' + path + '\"...')

    source = open(path).read()
    print(Fore.WHITE)
    exec(source, { 'launch': { 'sc': file , 'dir': directory , 'arg': arg } })

arg = {}
if __name__ == "__main__":
    if len(sys.argv)<2:
        print('No arguments.\nStaring default script...')
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

            os.system('title launcher: ' + script + ' \"' + argument + '\"')

        except Exception: pass
    try:
        loadScript(script , argument)
    except FileNotFoundError: print(Fore.RED + 'Script not found.' + Fore.WHITE)
    except Exception as ex: print(ex)