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
    import eel
    import os
    os.system('cls')
    os.system('title multiServer')
    from sys import *
    import yaml; from yaml import *
    from colorama import *
    print(Fore.BLUE + 'Loading modules..\n')
    import subprocess; from subprocess import *
    import webbrowser
    from subprocess_maximize import Popen
    import psutil; from psutil import *
    import pygetwindow
    win = pygetwindow.getWindowsWithTitle('multiServer')[0]
    win.size = (0, 0)
    directory_txt = ('C:\\multiServer\\directory.txt')
    infile = open(directory_txt, 'r')
    firstLine = infile.readline().strip()
    config_yml = (firstLine + '\\.multiServer\\config.yml'); servers_yml = (firstLine + '\\.multiServer\\servers.yml')
    # print(Fore.GREEN + 'directory_txt = ' + '' + directory_txt + '' + '\nconfig_yml = ' + '' + config_yml + '' + '\nservers_yml = ' + '' + servers_yml + '\n')
    packer_exe = (firstLine + '\\.multiServer\\packer.exe')
    print(Fore.GREEN + 'packer_exe = ' + packer_exe)
    starts = (firstLine + '\\.multiServer\\starts')
    print(Fore.GREEN  + 'starts = ' + starts + '\n')
    with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file)
    s1 = (servers_config['server-list'])
    serverNumb = 0
    server = {}
    enabledServers = []
    for server_name in servers_config['server-list']:
        serverNumb = serverNumb + 1
        enabledServers.append(serverNumb)
        server[serverNumb] = server_name

    @eel.expose
    def windowExit(route, websockets):
        if not websockets:
            print(Fore.BLUE + '\nEnding process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE)
            for pid in (process.pid for process in psutil.process_iter() if process.name()=="multiServer-app.exe"):
                os.kill(pid)

    @eel.expose
    def windowLoad():
        print(Fore.WHITE + '[mutliServer]: launched app (main.html, main.js, styles.css)')

    @eel.expose
    def getServers():
        return { "enabledServers": enabledServers, "server": server }

    @eel.expose
    def buttonClick(state, eid):
        if state == ('unchecked'):
            enabledServers.remove(int(eid))
        if state == ('checked'):
            enabledServers.append(int(eid))
        if state == ('none'):
            if str(eid) == ('config'):
                webbrowser.open_new_tab(config_yml)
            if str(eid) == ('servers'):
                webbrowser.open_new_tab(servers_yml)

    @eel.expose
    def startClick():
        if enabledServers == []:
            print(Fore.RED + 'no servers selected!')
            nos = ('no servers selected!')
            return {"errors": nos}
        else:
            print(Fore.BLACK + '\n' + 'starting packer.exe... please wait.')
            subprocess.call(packer_exe)
            for server in enabledServers:
                webbrowser.open(starts + '\\' + str(server) + '.cmd')
            os.system('cls')

    eel.init(firstLine + '\\.multiServer\\web')

    eel.start('main.html', size=(700, 1300), position=(0, 0), disable_cache=True, port=42439, host='localhost', cmdline_args=['–disable-translate'], close_callback=windowExit)
except Exception: print('UNKNOWN ERROR. PLEASE DO NOT REPORT THIS ON GITHUB! \nFOR SUPPORT CONTACT ME ON DISCORD.')