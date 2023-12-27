""""
multiServer-app.py (not compiled multiServer-app.exe)

This python script creates modern UI for multiServer and starts your minecraft servers.

Info:
 Created by: Kyoshuske
 Uploaded on: github.com/kyoshuske
 Last update: 25.12.2023 (dd.mm.yyyy)
 Version: 1.2 (version of this file not project)


Directorys:
 directory_txt = C:\multiServer\directory.txt
 config_yml = *\.multiServer\config.yml  
 servers_yml = *\.multiServer\servers.yml
 packer_exe = *\.multiServer\packer.exe
 starts = *\.multiServer\starts (*.cmd)
 web = *\.multiServer\web
"""""
try:
    wintitle=('multiServer')
    import eel
    import os
    os.system('cls')
    os.system('title ' + wintitle)
    import sys; from sys import *
    import yaml; from yaml import *
    from colorama import *
    print(Fore.LIGHTBLUE_EX + 'Loading modules...\n')
    import subprocess; from subprocess import *
    import webbrowser
    from subprocess_maximize import Popen
    import psutil; from psutil import *
    import pygetwindow
    win = pygetwindow.getWindowsWithTitle(wintitle)[0]
    win.size = (0, 0)

    # Directories:
    directory_txt = ('C:\\multiServer\\directory.txt')
    infile = open(directory_txt, 'r')
    firstLine = infile.readline().strip()
    dir = firstLine
    packer_exe = (dir + '\\.multiServer\\packer.exe')
    starts = (dir + '\\.multiServer\\starts')
    config_yml = (dir + '\\.multiServer\\config.yml')
    servers_yml = (dir + '\\.multiServer\\servers.yml')
    print(Fore.GREEN + 'Loaded directories:' + '\n - dir = ' + dir + '\n - directory_txt = ' + directory_txt + '\n - config_yml = ' + config_yml + '\n - servers_yml = ' + '' + servers_yml + '\n - packer_exe = ' + packer_exe + '\n - starts = ' + starts + '\n')

    # Open *\.multiServer\config.yml
    with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file)


    # 
    serverNumb = 0
    server = {}
    enabledServers = []
    print(Fore.GREEN + 'Loaded servers:')
    for server_name in servers_config['server-list']:
        serverNumb = serverNumb + 1
        enabledServers.append(serverNumb)
        server[serverNumb] = server_name
        print('  - ' + server_name + ' (id=' + str(serverNumb) + ')')
    print('\n')

    @eel.expose
    def windowExit(route, websockets):
        if not websockets:
            
            print(Fore.WHITE); sys.exit()
            # print(Fore.LIGHTBLUE_EX + '\nEnding process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE)
            # for pid in (process.pid for process in psutil.process_iter() if process.name()=="multiServer-app.exe"):
            #     os.kill(pid)

    @eel.expose
    def windowLoad():
        print(Fore.WHITE + 'Loaded app (main.html, main.js, styles.css)')

    @eel.expose
    def getServers():
        return { "enabledServers": enabledServers, "server": server }

    @eel.expose
    def buttonClick(state, eid):
        print(Fore.YELLOW + 'Button clicked (id=' + str(eid) + ', state=' + state + ')')
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

    @eel.expose
    def startClick():
        if enabledServers == []:
            print(Fore.RED + 'No servers selected! Please select at least 1 server.')

            # Just testing something.
            nos = ('1')
            return { "errors": nos }
        else:
            print(Fore.LIGHTBLUE_EX + '\n' + 'starting packer.exe...')
            #subprocess.call((packer_exe, str(packer_exe)))
            subprocess.call(packer_exe)
            for server in enabledServers:
                webbrowser.open(starts + '\\' + str(server) + '.cmd')

    eel.init(dir + '\\.multiServer\\web')

    eel.start('main.html', size=(700, 1300), position=(0, 0), disable_cache=True, port=42439, host='localhost', cmdline_args=['–disable-translate'], close_callback=windowExit)
except Exception as error: print(Fore.RED + 'UNKNOWN ERROR. (\'' + str(error) + '\') PLEASE DO NOT REPORT THIS ON GITHUB! \nFOR SUPPORT CONTACT ME ON DISCORD.')
finally: print(Fore.LIGHTBLUE_EX + '\nEnding process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE); sys.exit()