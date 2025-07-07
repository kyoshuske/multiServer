import sys

import eel.electron
try:
    directory = launch['dir']
    script = launch['sc']
    c = launch['color-format']
except Exception: print('Please launch this script with launcher.exe'); sys.exit()

# libraries
import os
from colorama import Fore; from colorama import *

import subprocess; from subprocess import Popen; from subprocess import *
import webbrowser
import eel
import discordrpc
from discordrpc.utils import timestamp
import gevent
import traceback
import asyncio


from psutil import *
from ctypes import windll

import yaml

launcher_exe = directory + '\\launcher.exe'

def appClose():
    sys.exit()
def startPacker():
    print(c['dur'] + '\n' + ' Starting packer.py...\n'+c['none'])
    wait = subprocess.Popen(([launcher_exe, 'packer.py']))
    wait.wait()
    os.system('title multiServer')
print(c['dur'], 'Checking for errors...')
startPacker()
os.system('cls')
os.system('title multiServer ')
print(c['none'], '\n                  8   o   o .oPYo.                                  \n                  8   8     8                                       \n   ooYoYo. o    o 8  o8P o8 `Yooo. .oPYo. oPYo. o    o .oPYo. oPYo. \n   8\' 8  8 8    8 8   8   8     `8 8oooo8 8  `\' Y.  .P 8oooo8 8  `\'\n   8  8  8 8    8 8   8   8      8 8.     8     `b..d\' 8.     8\n   8  8  8 `YooP\' 8   8   8 `YooP\' `Yooo\' 8      `YP\'  `Yooo\' 8       github.com/kyoshuske/multiServer\n\n   ___________________________________________________________________________________________________\n')
print(c['dur'], 'Loading app...\n')
dir = directory
process = {}
server = {}
icon = {}
enabledServers = []
serverNames = ''
try: 
    starts = dir + '\\starts'
    config_yml = dir + '\\config.yml'
    servers_yml = dir + '\\servers.yml'
    web = dir + '\\app\\web'

    print(c['su'], 'Working in: \"'+dir+'\"\n') 
    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file)

        print(c['su'], 'Loaded servers:')
        x=0
        for server_name in servers_config['servers']:
            x+=1
            serverNames+=server_name+'; '
            enabledServers.append(x)
            server[x] = server_name
            print(f'  - {server_name} ({str(x)})')
            icon[x] = f'https://raw.githubusercontent.com/kyoshuske/multiServer/main/assets/icon/{servers_config['servers'][server_name]['visuals']['icon']}'
    except Exception as error: print(error)


    def startServer(id: int):
        file_directory = starts+'\\'+str(id)
        start_file = f'{file_directory}a.cmd'
        startCmd(start_file)

    def startCmd(start_file:str):
        if app_mode == 'subprocess':
            process[str(server)] = Popen([start_file], creationflags=CREATE_NEW_CONSOLE)
            
        elif app_mode == 'experimental':
            print(c['dur'] + ' Attempting to launch server in experimental mode...')
            os.system(f'start {directory}\\launcher.exe \"server.py\" \"{str(id)}\" {server[id]}\"')

        elif app_mode == 'webbrowser':
            webbrowser.open(start_file)

        else:
            os.system(f'start {start_file}')

        print(f'{c['su']} Server started')

    @eel.expose
    def windowExit(route, websockets):
        if not websockets:
            appClose()

    @eel.expose
    def windowLoad():
        print(f'\n{c['none']} Loaded app')

    @eel.expose
    def startProxy():
        file = directory + "\\proxy.cmd"
        if os.path.exists(file):
            startCmd(file)
        else:
            print(c['err'] + ' Proxy start file does not exist.')

    @eel.expose
    def getServers():
        return { "id": enabledServers, "name": server, "icon": icon, "enabledServers": enabledServers, "server": server}
    
    @eel.expose
    def serverFileClick(id: int):
        print(f'{c['dur']}\n Opening log file... ({str(id)})')

        # get server_name by server_id
        server_name = server[id]
        # get server_path
        server_path = servers_config['servers'][server_name]['path']
        file_path = server_path+'\\logs\\latest.log'
        file_exists = os.path.exists(file_path)
        if file_exists == True:
            os.system(file_path)
            # webbrowser.open_new_tab(server_path+ '\\logs\\latest.log')
            print(f'{c['dur']} Opening {file_path}...')
        
    @eel.expose
    def serverStartClick(id: str):
        print(f'{c['dur']}\n Starting server... ({id})')
        if fast_start == True:
            startPacker()
        startServer(int(id))
    @eel.expose
    def executePythonCode(code: str):
        if code:
            eval(code)
    with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (config.yml)

    try:
        app_resolution = config['settings']['app']['resolution']['width'], config['settings']['app']['resolution']['height']
        app_mode = config['settings']['app']['mode']
        fast_start = config['settings']['app']['reload-server-config']
        enable_rpc = config['settings']['app']['enable-discord-status']

    except Exception: print(f'{c['err']}\n File \'config.yml\' not found or outdated.{c['dur']}\n Loading default settings...'); app_resolution = (1220, 1100); enable_rpc=False
    if enable_rpc == True:
        rpc = discordrpc.RPC(app_id=1307420925775315025)
        rpc.set_activity(
            details=f"Loaded servers: {str(len(enabledServers))}",
            ts_start=timestamp,
            ts_end=1752426021
        )
    eel.init(web)
    eel.start('app.html', mode=config['settings']['app']['web-mode'], size=(app_resolution), position=(600, 50), port=f"{(config['settings']['app']['port'])}", host='localhost', close_callback=windowExit, cmdline_args=['–disable-gpu', '–disable-sync', '--non-resizable', '--disable-glsl-translator', '--fast-start', '--incognito', '--disable-infobars', '--disable-pinch', '--disable-extensions'], block=False)
    gevent.get_hub().join()
    executePythonCode(input())
    if enable_rpc == True:
        rpc.run(4)
except Exception as error: print(c['err'] + '\nUnknown error!\n' + traceback.format_exc())
finally: print(c['dur'], '\n Ending process...', c['end'], '\n Please check above for any errors.' + c['none']); sys.exit()