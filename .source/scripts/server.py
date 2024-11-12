import sys
try:
    directory = launch['dir']
    script = launch['sc']
    server_number = int(launch['arg'])
    server_name = launch['arg2']
except Exception: print('Please launch this script with launcher.exe'); sys.exit()
# libraries
import sys
import os
os.system('title launcher')

from colorama import Fore; from colorama import *
import time

import subprocess; from subprocess import Popen; from subprocess import *

from threading import Thread
import traceback
from queue import Queue, Empty

import eel

import gevent
import asyncio

from psutil import *
from ctypes import windll

import yaml
os.system('title server: ' + str(server_number))

starts = (directory + '\\starts')
web = (directory + '\\app\\web')
config_yml = (directory + '\\config.yml')
numb = 0
last_type = 'INFO]: '

classes = {

    # 'Done': ["success", Fore.LIGHTCYAN_EX],
    # 'successfully': ["success", Fore.LIGHTCYAN_EX],
    # 'Loaded': ["success", Fore.LIGHTCYAN_EX],
    # 'loaded': ["success", Fore.LIGHTCYAN_EX],
    # 'Registered': ["success", Fore.LIGHTCYAN_EX],
    # 'registered': ["success", Fore.LIGHTCYAN_EX],

    'INFO]: ': ["info", Fore.WHITE],
    'ERROR]: ': ["error", Fore.LIGHTRED_EX],
    'WARN]: ': ["warn", Fore.LIGHTYELLOW_EX],
    'HOST]: ': ["warn", Fore.LIGHTCYAN_EX],
    'NONE]: ': ["unkown", Fore.LIGHTBLACK_EX]
}

@eel.expose
def windowExit(route, websockets):
    if not websockets:
        print('webapp is not responing.')
        time.sleep(0.2)
        print('closing server...')
        print('stopping script...')
        sys.exit()

@eel.expose
def captureOutput():
    try:
        global numb
        global last_type
        try: output = q.get_nowait()
        except Empty:
            return
        type = 'NONE]: '
        if output:
            teststring = str(output.strip())
            type = classes['INFO]: ']
            for type in classes:
                if type in teststring:
                    last_type = type
                    numb+=1
                    break
            if "For help, type \"help\"" in teststring:
                print("server loaded.")
            if type == 'NONE]: ':
                type = last_type

            string = ('<div class=\"' + classes[type][0]+ '\">' + str(output.strip()) + '</div>')
            return { "output": string }
    except Exception: return { "output": '<div class=\"' + classes['INFO]: '][0]+ '\">' + str(traceback.format_exc()) + '</div>' }


@eel.expose
def executeCommand(input):
    if input != '':
        if (input[0] == ("/")):
            input = '' + input[1:]
        print('input received (\'' + input + '\')')
    try:
        console.stdin.write(input + '\n')
        console.stdin.flush()
    except OSError: print('server is down lol'); time.sleep(1); sys.exit()

@eel.expose
def windowLoad():

    print(Fore.WHITE + 'webapp responded')
    return { "consoleInterval": console_refresh, "serverName": server_name }

async def appStart():
    eel.init(str(web))
    eel.start('server.html', size=(1400, 920), position=(600, 50), disable_cache=True, port=(int(web_port) + int(server_number)), host='localhost', close_callback=windowExit, cmdline_args=['--disable-glsl-translator', '--fast-start', '--incognito', '--disable-infobars', '--disable-pinch', '--disable-extensions', '--force-tablet-mode'], block=True)
    gevent.get_hub().join()
    print('test')



with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (cofnig.yml)

try:
    app_port = config['settings']['app']['port']
    console_refresh = config['settings']['app']['console-refresh-rate']
except Exception: print('Uknown port.'); app_port = (42434); console_refresh = 0.02


web_port = (int(app_port) + int(server_number))


print('app_port: ' + str(app_port) + ', server_number: ' + str(server_number) + ', web_port: ' + str(web_port) + ', app_dir: ' + str(directory))
print('waiting for webapp to respond...')

def enqueueOutput(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

start_file = str(starts + '\\' + str(server_number) + 'a.cmd')
print(start_file)
console = Popen([start_file], creationflags=CREATE_NEW_CONSOLE, text=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True, stderr=subprocess.PIPE, close_fds=True)
q = Queue()
t = Thread(target=enqueueOutput, args=(console.stdout, q))
t.daemon = True
t.start()

asyncio.run(appStart())