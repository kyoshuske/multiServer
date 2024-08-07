import sys
try:
    directory = launch['dir']
    script = launch['sc']
except Exception: print('Please launch this script with launcher.exe'); sys.exit()

# libraries
import os

from colorama import Fore; from colorama import *
import time

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

def appClose():
    sys.exit()



# os.system('cls')
launcher_exe = (directory + '\\launcher.exe')
wait = subprocess.Popen(([launcher_exe, 'packer.py', 'nopack']))
wait.wait()
os.system('cls')
os.system('title multiServer ')
print(Fore.WHITE + '\n                  8   o   o .oPYo.                                  \n                  8   8     8                                       \n   ooYoYo. o    o 8  o8P o8 `Yooo. .oPYo. oPYo. o    o .oPYo. oPYo. \n   8\' 8  8 8    8 8   8   8     `8 8oooo8 8  `\' Y.  .P 8oooo8 8  `\'\n   8  8  8 8    8 8   8   8      8 8.     8     `b..d\' 8.     8\n   8  8  8 `YooP\' 8   8   8 `YooP\' `Yooo\' 8      `YP\'  `Yooo\' 8       github.com/kyoshuske/multiServer\n\n   ___________________________________________________________________________________________________\n')
print(Fore.LIGHTBLUE_EX + 'Loading app...\n')
dir = directory
process = {}
serverNumb = 0
server = {}
enabledServers = []
        
try: 
    starts = (dir + '\\starts')
    config_yml = (dir + '\\config.yml')
    servers_yml = (dir + '\\servers.yml')
    web = (dir + '\\app\\web')

    print(Fore.GREEN + 'Working in: \"' + dir + '\"\n') 
    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file)

        print(Fore.GREEN + 'Loaded servers:')
        for server_name in servers_config['enabled-servers']:
            serverNumb = serverNumb + 1
            enabledServers.append(serverNumb)
            server[serverNumb] = server_name
            print('  - ' + server_name + ' (' + str(serverNumb) + ')')
    except Exception as error: print(Fore.RED + 'File \'servers.yml\' not found or outdated.' + Fore.LIGHTBLUE_EX + '\nAttempting to start the app...')


    @eel.expose
    def windowExit(route, websockets):
        if not websockets:
            appClose()


    @eel.expose
    def windowLoad():
        print(Fore.WHITE + '\nLoaded app (main.html, main.js, styles.css)\n')

    @eel.expose
    def getServers():
        return { "enabledServers": enabledServers, "server": server }

    @eel.expose
    def buttonClick(state, eid):
        print(Fore.WHITE + 'Button clicked (' + str(eid) + ', ' + state + ')')
        if state == ('unchecked'):
            enabledServers.remove(int(eid))
        if state == ('checked'):
            enabledServers.append(int(eid))
        if state == ('none'):
            if str(eid) == 'config':
                print(Fore.LIGHTBLUE_EX + 'Opening ' + eid + '...')
                webbrowser.open_new_tab(config_yml)
            if str(eid) == 'servers':
                print(Fore.LIGHTBLUE_EX + 'Opening ' + eid + '...')
                webbrowser.open_new_tab(servers_yml)
            else:
                selected_server = server[int(eid)]
                for server_name in servers_config['enabled-servers']:
                    if str(server_name) == str(selected_server):
                        current_server = servers_config['servers'][server_name]
                        path = current_server['path']
                        log_file = (path + '\\logs\\latest.log')

                        file_exists = os.path.exists(log_file)
                        if file_exists == True:
                            webbrowser.open_new_tab(log_file)
                            print(Fore.LIGHTBLUE_EX + 'Opening ' + log_file + '...')
                        else:
                            print(Fore.RED + 'File \'' + log_file + '\' does not exist!')

                            
                            

    @eel.expose
    def startClick():
        print(Fore.WHITE + 'Button clicked (start, none)')
        if enabledServers == []:
            print(Fore.RED + 'No servers selected! Please select at least 1 server.')

        else:
            print(Fore.LIGHTBLUE_EX + '\n' + 'Starting packer script...')
            wait = subprocess.Popen(([launcher_exe, 'packer.py']))
            wait.wait()
            os.system('title multiServer')
            for server in enabledServers:
                random = ((((server * server * server) - server) * 2) + 1)
                if app_mode == ('subprocess'):
                    process[server] = subprocess.Popen([str(starts + '\\' + str(random) + 'a.cmd')], creationflags=CREATE_NEW_CONSOLE, text=True, close_fds=False)
                if app_mode == ('experimental'):
                    print(Fore.LIGHTBLUE_EX + 'Attempting to launch servers in experimental mode...')
                    webbrowser.open(dir + '\\starts\\' + str(random) + 'b.cmd')
                else:
                    webbrowser.open(starts + '\\' + str(random) + 'a.cmd')
            print(Fore.WHITE + 'Ready')
            
    with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (config.yml)

    try:
        app_resolution = (config['settings']['app']['resolution']['width'], config['settings']['app']['resolution']['height'])
        app_mode = config['settings']['app']['mode']

    except Exception: print(Fore.RED + '\nFile \'config.yml\' not found or outdated.' + Fore.LIGHTBLUE_EX + '\nLoading default settings...'); app_resolution = (820, 1300); app_port = (42434)
    eel.init(web)
    eel.start('main.html', size=(app_resolution), position=(600, 50), port=(config['settings']['app']['port']), host='localhost', close_callback=windowExit, cmdline_args=['--disable-glsl-translator', '--fast-start', '--incognito', '--disable-infobars', '--disable-pinch', '--disable-extensions', '--resizable: false'], block=False)
    
    gevent.get_hub().join()
except Exception as error: print(Fore.RED + 'Unknown error!\n' + str(error))
finally: print(Fore.LIGHTBLUE_EX + 'Ending process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE); sys.exit()