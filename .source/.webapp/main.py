try:
    import eel
    import os
    from sys import *
    import yaml; from yaml import *
    from colorama import *
    import subprocess; from subprocess import *
    import webbrowser
    from subprocess_maximize import Popen
    import psutil; from psutil import *
    import time
    os.system('cls')
    print(Fore.WHITE)
    directory_txt = ('C:\\multiServer\\directory.txt')
    infile = open(directory_txt, 'r')
    firstLine = infile.readline().strip()
    config_yml = (firstLine + '\\.multiServer\\config.yml'); servers_yml = (firstLine + '\\.multiServer\\servers.yml'); print(Fore.GREEN + 'directory_txt = ' + '' + directory_txt + '' + '\nconfig_yml = ' + '' + config_yml + '' + '\nservers_yml = ' + '' + servers_yml + '\n')
    packer_exe = (firstLine + '\\.multiServer\\packer.exe')
    starts = (firstLine + '\\.multiServer\\starts')
    with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file)
    s1 = (servers_config['server-list'])
    serverNumb = 0
    server = {}
    enabledServers = []
    print('loaded servers:')
    for server_name in servers_config['server-list']:
        serverNumb = serverNumb + 1
        enabledServers.append(serverNumb)
        server[serverNumb] = server_name
        print(' - ' + server[serverNumb])
    print('total: ' + str(enabledServers))

    @eel.expose
    def windowExit(route, websockets):
        if not websockets:
            print(Fore.BLUE + '\nending process...')
            for pid in (process.pid for process in psutil.process_iter() if process.name()=="multiServer-app.exe"):
                os.kill(pid)

    @eel.expose
    def windowLoad():
        print(Fore.BLUE + '\nloaded main.html')
        # eel.display_servers(enabledServers) # TU POWINNY BYC WARTOSCI Z ID W NAZWIE, KTORE ZAWIERAJA NAZWY PRZYPISANE DO ID
        # give js list of servers 

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
            subprocess.call(packer_exe)
            # start selected servers
            for server in enabledServers:
                webbrowser.open(starts + '\\' + str(server) + '.cmd')

    @eel.expose
    def test():
        print(Fore.RED + 'test')
        time.sleep(2)
    dirname = os.path.dirname(__file__) + '\\web'
    eel.init(dirname)

    eel.start('main.html', size=(700, 1000), position=(0, 0), disable_cache=True, port=42439, host='localhost', cmdline_args=['–disable-translate'], close_callback=windowExit)
except Exception: print('UNKNOWN ERROR. PLEASE DO NOT REPORT THIS ON GITHUB OR DISCORD! \nFOR SUPPORT CONTACT ME ON GITHUB OR DISCORD.')