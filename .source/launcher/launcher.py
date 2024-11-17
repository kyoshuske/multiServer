# default:
argument = 0
argument2 = 0
argument3 = 0
debug = 0
script = 'multiServer-app.py'

try:
    import sys
    import os
    os.system('title launcher')
    
    from colorama import Fore; from colorama import *
    import time
    print('-----------------------< launcher >-----------------------\nLoading python and all required libraries...')

    import subprocess; from subprocess import Popen; from subprocess import *
    import webbrowser

    from threading import Thread
    from queue import Queue, Empty

    import eel
    from tkinter import messagebox
    import discordrpc
    import gevent
    import asyncio
    import traceback
    from datetime import datetime


    from psutil import *
    from ctypes import windll
    import win32gui, win32con, win32com.client

    import signal

    import yaml
    from configobj import ConfigObj
except Exception: print('Module load error (not an executable ?)'); time.sleep(1); sys.exit()

try:
    config_path = os.path.expanduser('~') + "\\AppData\\Local\\multiServer"
    config_yml = config_path + '\\c.yml'
    with open(config_yml, 'r') as file: cfg = yaml.safe_load(file); cfg = cfg['config']
    directory = cfg['path']
    scripts = f'{directory}\\.multiServer\\app\\scripts\\'
    print(f'Working in directory: \"{directory}\\.multiServer\"')
    directory += "\\.multiServer"
    color_format = {
    'none': Fore.WHITE,
    'dur': Fore.LIGHTBLUE_EX,
    'su': Fore.GREEN,
    'end': Fore.YELLOW,
    'err': Fore.RED
    }
    
except Exception: print('File does not exist.'); sys.exit()

def loadScript(file, arg, arg2, arg3):
    path = (scripts + file)
    print(f'initializing script: \"{path}\"...\n')

    source = open(path, encoding="utf8").read()
    exec(source, { 'launch': { 'sc': file , 'dir': directory , 'arg': arg, 'arg2': arg2, 'arg3': arg3, 'color-format': color_format }})

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, sys.exit)
    if not len(sys.argv)<2:
        len = 0
        try:
            for args in sys.argv:
                len = int(len) + 1


            script = str(sys.argv[1])

            argument = str(sys.argv[2])
            argument2 = str(sys.argv[3])
            argument3 = str(sys.argv[4])

            debug = str(sys.argv[3])


            os.system(f'title launcher: {script} \"{argument}\"')

        except Exception: pass
    try:
        loadScript(script , argument, argument2, argument3)
    except FileNotFoundError: print(f'{color_format['err']}Script not found.{color_format['none']}')
    except Exception as ex: print(ex)