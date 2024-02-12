# multiServer-app.py (not compiled multiServer-app.exe)

# This python script creates modern UI for multiServer and starts your minecraft servers.

# Info:
#  Created by: Kyoshuske
#  Uploaded on: github.com/kyoshuske
#  Last update: 25.01.2024 (dd.mm.yyyy)
#  Version: 1.4 (version of this file not project)


# Directories:
#  directory_txt = C:\multiServer\directory.txt
#  config_yml = *\.multiServer\config.yml  
#  servers_yml = *\.multiServer\servers.yml
#  packer_exe = *\.multiServer\packer.exe
#  starts = *\.multiServer\starts (*.cmd)
#  web = *\.multiServer\web

try: 
    from colorama import Fore
    import sys
    import os
    wintitle=('multiServer')
    import eel
    os.system('cls')
    os.system('title ' + wintitle)
    import sys
    import yaml
    print(Fore.WHITE + '\n                  8   o   o .oPYo.                            \n                  8   8     8                                 \n   ooYoYo. o    o 8  o8P o8 `Yooo. .oPYo. o    o .oPYo. oPYo. \n   8\' 8  8 8    8 8   8   8     `8 8oooo8 Y.  .P 8oooo8 8  `\' \n   8  8  8 8    8 8   8   8      8 8.     `b..d\' 8.     8     \n   8  8  8 `YooP\' 8   8   8 `YooP\' `Yooo\'  `YP\'  `Yooo\' 8       github.com/kyoshuske/multiServer\n\n   _____________________________________________________________________________________________\n')
    print(Fore.LIGHTBLUE_EX + 'Loading app...\n')
    import subprocess; from subprocess import Popen; from subprocess import *
    import webbrowser
    import gevent
    import time
    from psutil import *
    import pygetwindow
    from ctypes import windll
    import asyncio
    
    
    win = pygetwindow.getWindowsWithTitle(wintitle)[0]
    webapp = pygetwindow.getWindowsWithTitle('multiServer')[0]
    win.resizeTo(0, 0)
    # win.close()
    win.moveTo(0, 0)
    win.minimize()
    process = {}
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
    os.system('title ' + wintitle + ' - logs [Console]')
    try:
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
    except Exception as error: print(Fore.RED + '\nFile \'servers.yml\' not found or outdated.' + Fore.LIGHTBLUE_EX + '\nAttempting to start the app...')


    @eel.expose
    def windowExit(route, websockets):
        if not websockets:
            if app_mode == ('subprocess'):
                win.restore()
                win.moveTo(0, 0)
                win.resizeTo(800, 600)
            else:
                sys.exit()


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
            print(Fore.LIGHTBLUE_EX + '\n' + 'Starting packer.exe...')
            subprocess.call(packer_exe)
            print(Fore.WHITE + 'Ready')
                # process[server].communicate(input='echo: test\n')[0]
                # process[server].stdin.write('echo: test\n')
                # process[server].stdin.write('cls\n' + starts + '\\' + str(server) + '.cmd\n')
                # process[server].communicate(input='cls\n' + starts + '\\' + str(server) + '.cmd\n')[0]
                
                # webbrowser.open(starts + '\\' + str(server) + '.cmd')
            for server in enabledServers:
                if app_mode == ('subprocess'):
                    process[server] = subprocess.Popen([str(starts + '\\' + str(server) + '.cmd')], creationflags=CREATE_NEW_CONSOLE, text=True, close_fds=False, shell=False)
                else:
                    webbrowser.open(starts + '\\' + str(server) + '.cmd')
                # subprocess.run(['C:\Users\sfpas\OneDrive\Pulpit\AreHaker\multiServer\server-panel\server.pyw -p ' + app_port + '-n ' + server + '-d ' + dir], stdout=PIPE, stderr=PIPE, universal_newlines=True)

    async def startServers():
        for server in enabledServers:
            process[server] = await asyncio.create_subprocess_exec([str(starts + '\\' + str(server) + '.cmd')], creationflags=CREATE_NEW_CONSOLE, text=True, close_fds=True, shell=False)



    eel.init(web)
    if __name__ == "__main__":
        try:
            for filename in os.listdir('.'):
                if filename.startswith('-debug'):
                    print('DEBUG')
        except Exception: print()



    with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (cofnig.yml)

    try:
        app_resolution_height = config['settings']['app']['resolution']['height']
        app_resolution_width = config['settings']['app']['resolution']['width']
        app_resolution = (app_resolution_width, app_resolution_height)
        app_port = config['settings']['app']['port']
        try:
            app_mode = config['settings']['app']['mode']
        except Exception:
            app_mode = ('webbrowser')

    except Exception: print(Fore.RED + '\nFile \'config.yml\' not found or outdated.' + Fore.LIGHTBLUE_EX + '\nLoading default settings...'); app_resolution = (820, 1300); app_port = (42434)
    # app_fullscreen = config['settings']['app']['fullscreen-enable']
    # if app_fullscreen == (True): app_fullscreen = ('–-start-fullscreen')
    # else: app_fullscreen = ('')
    eel.start('main.html', size=(app_resolution), position=(600, 50), disable_cache=True, port=(app_port), host='localhost', cmdline_args=['--disable-glsl-translator', '--fast-start', '--incognito', '--disable-infobars', '--disable-pinch', '--disable-extensions', '--force-tablet-mode'], close_callback=windowExit, block=False)
    gevent.get_hub().join()
except Exception as error: print(Fore.RED + 'Unknown error!\n' + str(error))
finally: print(Fore.LIGHTBLUE_EX + 'Ending process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE); webapp.close; sys.exit()