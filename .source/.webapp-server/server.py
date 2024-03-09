import sys
import os
import subprocess; from subprocess import Popen; from subprocess import *
import eel
import asyncio
import yaml
import gevent
from colorama import Fore
import time
from queue import Queue, Empty
from threading import Thread
import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

directory_txt = ('C:\\multiServer\\directory.txt')
infile = open(directory_txt, 'r')
app_dir = infile.readline().strip()
web = (app_dir + '\\.multiServer\\server\\web')
starts = (app_dir + '\\.multiServer\\starts')

config_yml = (app_dir + '\\.multiServer\\config.yml')
numb = 0
classes = {
    '[90m': ["none", Fore.LIGHTCYAN_EX],
    '[92m': ["none", Fore.LIGHTCYAN_EX],
    '[96m': ["none", Fore.LIGHTCYAN_EX],
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
        console.stdin.write('save-all\nstop\nstop\nstop\nstop\nstop\nstop\n')
        console.stdin.flush()
        time.sleep(4)
        print('stopping script...')
        time.sleep(1)
        subprocess.Popen.kill(console)
        sys.exit()

@eel.expose
def captureOutput():
    global numb
    numb = numb + 1
    # print('refreshing... [' + str(numb) + ']')
    try: output = q.get_nowait()
    except Empty:
        return
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
    if (input[0] == ("/")):
        input = '' + input[1:]
    print('input received (\'' + input + '\')')

    console.stdin.write(input + '\n')
    console.stdin.flush()

@eel.expose
def windowLoad():
    print(Fore.WHITE + 'webapp responded')
    return { "consoleInterval": console_refresh }

async def appStart():
    eel.init(str(web))
    eel.start('server.html', size=(1400, 920), position=(600, 50), disable_cache=True, port=(int(web_port) + int(server_number)), host='localhost', close_callback=windowExit, cmdline_args=['--disable-glsl-translator', '--fast-start', '--incognito', '--disable-infobars', '--disable-pinch', '--disable-extensions', '--force-tablet-mode'], block=True)
    gevent.get_hub().join()
    print('test')
os.system('cls')

if __name__ == "__main__":
    if len(sys.argv)>1:
        server_number = sys.argv[1]

with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (cofnig.yml)

try:
    app_port = config['settings']['app']['port']
    console_refresh = config['settings']['app']['console-refresh-rate']
except Exception: print('Uknown port.'); app_port = (42434); console_refresh = 0.02


web_port = (int(app_port) + int(server_number))


print('app_port: ' + str(app_port) + ', server_number: ' + str(server_number) + ', web_port: ' + str(web_port) + ', app_dir: ' + str(app_dir))
print('waiting for webapp to respond...')

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

start_file = str(starts + '\\' + str(server_number) + '.cmd')
console = Popen([start_file], creationflags=CREATE_NEW_CONSOLE, text=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, close_fds=True)
q = Queue()
t = Thread(target=enqueue_output, args=(console.stdout, q))
t.daemon = True # thread dies with the program
t.start()

asyncio.run(appStart())