"""
multiServer-app.py (not compiled multiServer-app.exe)

This python script creates modern UI for multiServer and starts your minecraft servers.

Info:
 Created by: Kyoshuske
 Uploaded on: github.com/kyoshuske
 Last update: 04.01.2023 (dd.mm.yyyy)
 Version: 1.4 (version of this file not project)


Directories:
 directory_txt = C:\multiServer\directory.txt
 config_yml = *\.multiServer\config.yml  
 servers_yml = *\.multiServer\servers.yml
 packer_exe = *\.multiServer\packer.exe
 starts = *\.multiServer\starts (*.cmd)
 web = *\.multiServer\web
"""
async def waitForInput():
    command = input()
    command

try:
    # wintitle=('multiServer [PRESS F11 TO SEE LOGS]')
    wintitle=('multiServer')
    import eel
    import os
    os.system('cls')
    os.system('title ' + wintitle)
    import sys; from sys import *
    import yaml; from yaml import *
    from colorama import *
    print(Fore.WHITE + '\n                  8   o   o .oPYo.                            \n                  8   8     8                                 \n   ooYoYo. o    o 8  o8P o8 `Yooo. .oPYo. o    o .oPYo. oPYo. \n   8\' 8  8 8    8 8   8   8     `8 8oooo8 Y.  .P 8oooo8 8  `\' \n   8  8  8 8    8 8   8   8      8 8.     `b..d\' 8.     8     \n   8  8  8 `YooP\' 8   8   8 `YooP\' `Yooo\'  `YP\'  `Yooo\' 8       github.com/kyoshuske/multiServer\n\n   _____________________________________________________________________________________________\n')
    print(Fore.LIGHTBLUE_EX + 'Loading app...\n')
    import subprocess; from subprocess import *
    import webbrowser
    import win32con
    import ctypes

    from subprocess_maximize import Popen
    from psutil import *
    import pygetwindow
    
    
    win = pygetwindow.getWindowsWithTitle(wintitle)[0]
    win.size = (0, 0)
    
    directory_txt = ('C:\\multiServer\\directory.txt')
    infile = open(directory_txt, 'r')
    firstLine = infile.readline().strip()
    dir = firstLine
    packer_exe = (dir + '\\.multiServer\\packer.exe')
    starts = (dir + '\\.multiServer\\starts')
    config_yml = (dir + '\\.multiServer\\config.yml')
    servers_yml = (dir + '\\.multiServer\\servers.yml')
    web = (dir + '\\.multiServer\\web')
    print(Fore.GREEN + 'Loaded directories:' + '\n - dir = ' + dir + '\n - directory_txt = ' + directory_txt + '\n - config_yml = ' + config_yml + '\n - servers_yml = ' + '' + servers_yml + '\n - packer_exe = ' + packer_exe + '\n - starts = ' + starts + '\n - web = ' + web + '\n')
    os.system('title ' + wintitle + ' - logs [PRESS \'F11\']')
    with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file)

    serverNumb = 0
    server = {}
    enabledServers = []
    print(Fore.GREEN + 'Loaded servers:')
    for server_name in servers_config['server-list']:
        serverNumb = serverNumb + 1
        enabledServers.append(serverNumb)
        server[serverNumb] = server_name
        print('  - ' + server_name + ' (' + str(serverNumb) + ')')
    @eel.expose
    def windowExit(route, websockets):
        if not websockets:
            print(Fore.WHITE); sys.exit()

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
            if str(eid) == ('config'):
                print(Fore.LIGHTBLUE_EX + 'Opening ' + config_yml + '...')
                webbrowser.open_new_tab(config_yml)
            if str(eid) == ('servers'):
                print(Fore.LIGHTBLUE_EX + 'Opening ' + servers_yml + '...')
                webbrowser.open_new_tab(servers_yml)
            else:
                selected_server = server[int(eid)]
                for server_name in servers_config['server-list']:
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

            # Just testing something.
            nos = ('1')
            return { "errors": nos }
        else:
            print(Fore.LIGHTBLUE_EX + '\n' + 'starting packer.exe...')
            subprocess.call(packer_exe)
            for server in enabledServers:
                webbrowser.open(starts + '\\' + str(server) + '.cmd')

    eel.init(web)
    if __name__ == "__main__":
        try:
            for filename in os.listdir('.'):
                if filename.startswith('-debug'):
                    print('DEBUG')
        except Exception: print()



    with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (cofnig.yml)


    app_resolution_height  = config['settings']['app']['resolution']['height']
    app_resolution_width  = config['settings']['app']['resolution']['width']
    app_resolution = (app_resolution_width, app_resolution_height)
    # app_resolution = (820, 1300)
    app_port  = config['settings']['app-ui']['port']

    eel.start('main.html', size=(app_resolution), position=(600, 50), disable_cache=True, port=(app_port), host='localhost', cmdline_args=['--disable-glsl-translator', '--fast-start', '--incognito', '--disable-infobars', '--disable-pinch', '--disable-extensions', '--force-tablet-mode'], close_callback=windowExit)
except Exception as error: print(Fore.RED + 'UNKNOWN ERROR. (\'' + str(error) + '\') PLEASE DO NOT REPORT THIS ON GITHUB! \nFOR SUPPORT CONTACT ME ON DISCORD.')
finally: print(Fore.LIGHTBLUE_EX + 'Ending process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE); sys.exit()