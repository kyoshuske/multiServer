import sys
try:
    directory = launch['dir']
    script = launch['sc']
    server_number = int(launch['arg'])
except Exception: print('Please launch this script with launcher.exe'); sys.exit()
# libraries
import sys
import os
os.system('title launcher')

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










# server_number = sys.argv[2]

os.system('title server: ' + str(server_number))

# cmd = {}
# #load commands:
# commands_yml = directory + '\\.multiServer\\commands.yml'
# try:
#     with open(commands_yml, 'r') as file: commands_yml = yaml.safe_load(file)
#     commands = commands_yml['commands']
#     print(commands)
#     for command in commands:
#         cmd[command] = commands[command]
        
# except Exception as r: print(r); time.sleep(2)


# app_window = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(app_window , win32con.SW_HIDE)

starts = (directory + '\\starts')
web = (directory + '\\app\\web')
config_yml = (directory + '\\config.yml')
numb = 0

classes = {
    '[90m': ["none", Fore.LIGHTCYAN_EX],
    '[92m': ["none", Fore.LIGHTCYAN_EX],
    '[96m': ["none", Fore.LIGHTCYAN_EX],
    '[31m': ["error", Fore.LIGHTCYAN_EX],
    'Done': ["success", Fore.LIGHTCYAN_EX],
    'INFO]: ': ["info", Fore.WHITE],
    'ERROR]: ': ["error", Fore.LIGHTRED_EX],
    'WARN]: ': ["warn", Fore.LIGHTYELLOW_EX],
    'HOST]: ': ["warn", Fore.LIGHTCYAN_EX],
    'NONE]: ': ["unkown", Fore.LIGHTBLACK_EX],
}

@eel.expose
def windowExit(route, websockets):
    if not websockets:
        print('webapp is not responing.')
        time.sleep(0.2)
        print('closing server...')
        # console.stdin.write('save-all\nstop\nstop\nstop\nstop\nstop\nstop\n')
        # console.stdin.flush()
        print('stopping script...')
        # subprocess.Popen.kill(console)
        # console.kill()

        sys.exit()

@eel.expose
def captureOutput():
    global numb
    numb = numb + 1
    # print('refreshing... [' + str(numb) + ']')
    try: output = q.get_nowait()
    except Empty:
        return
    type = 'NONE]: '
    if output:
        teststring = str(output.strip())
        type = classes['INFO]: ']
        for type in classes:
            if type in teststring:
                break

        if "For help, type \"help\"" in teststring:
            print("server loaded.")
    # time.sleep(console_refresh)
    string = ('<div class=\"' + classes[type][0] + '\">' + str(output.strip()) + '</div>')
    # string = (str(output.strip()))
    return { "output": string }

# def webPrint(string, color2):
#     print(Fore.LIGHTMAGENTA_EX + "" + color2 + string)
#     # print(string)


@eel.expose
def executeCommand(input):

    if input != '':
        if (input[0] == ("/")):
            input = '' + input[1:]
        print('input received (\'' + input + '\')')

    # for command in cmd:
        
    #     if (cmd[command]['alias'] == input):
    #         print('valid')
    #         for action in cmd[command]['actions']:
    #             print(action)
    #             console.stdin.write(action + '\n')
    #             console.stdin.flush()
    #         return
    try:
        console.stdin.write(input + '\n')
        console.stdin.flush()
    except OSError: print('server is down lol'); time.sleep(1); sys.exit()

@eel.expose
def windowLoad():
    print(Fore.WHITE + 'webapp responded')
    return { "consoleInterval": console_refresh }

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

numb = server_number
random = str((((numb * numb * numb) - numb) * 2) + 1)
start_file = str(starts + '\\' + str(random) + 'a.cmd')
print(start_file)
console = Popen([start_file], creationflags=CREATE_NEW_CONSOLE, text=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, close_fds=True)
q = Queue()
t = Thread(target=enqueueOutput, args=(console.stdout, q))
t.daemon = True
t.start()

asyncio.run(appStart())