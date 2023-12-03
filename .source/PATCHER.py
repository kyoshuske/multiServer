import os
os.system('cls')
def displayError():
    os.system('cls')
    if cError == ('KeyError'): print(Fore.RED + 'The part of the file ' + cErrorT +' is missing: ' + str(error) + '.')
    if cError == ('MissingFile'): print(Fore.RED + 'The file: ' + cErrorT +' does not exist.\nPlease try to reinstall multiServer!')
    if cError == ('Classic'): print(Fore.RED + cErrorT +' error.')
    time.sleep(7); sys.exit()
try:
    try:
        import yaml; import subprocess; import time; import sys; import pathlib

        import colorama; from colorama import Fore, Back, Style

        import pprint; from pprint import pprint
    except Exception: cErrorT = ('Module load'); cError = ('Classic'); displayError()
        
    os.system('title multiServer: launch\ntitle multiServer\ncolor 7')
    try: infile = open('C:\\multiServer\\directory.txt', 'r')
    except Exception: cErrorT = ('C:\\multiServer\\directory.txt'); cError = ('MissingFile'); displayError()
    firstLine = infile.readline().strip()

    config_yml = (firstLine + '\\.multiServer\\config.yml'); servers_yml = (firstLine + '\\.multiServer\\servers.yml'); print('config_yml = ' + '' + config_yml + '' + '\nservers_yml = ' + '' + servers_yml + '\n')



    try:
        with open(config_yml, 'r') as file: config = yaml.safe_load(file) # loading yaml/yml file (cofnig.yml)


        globalfilename = config['settings']['global']['global-filename']['enable']
        if str(globalfilename) == (True): filenameglobal = config['settings']['global']['global-filename']['filename']

        globalcolor = config['settings']['global']['global-color']['enable']
        if str(globalcolor) == (True): colorglobal = config['settings']['global']['globa-color']['color']

        globaljava = config['settings']['global']['global-javafile']['enable']
        if str(globaljava) == (True): javaglobal = config['settings']['global']['global-java']['file']

    except FileNotFoundError as error: cErrorT = ('config.yml'); cError = ('MissingFile'); displayError()

    except KeyError as error: cErrorT = ('config.yml'); cError = ('KeyError'); displayError()




        
    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file) # loading yaml/yml file (servers.yml)

    except FileNotFoundError as error: cErrorT = ('servers.yml'); cError = ('MissingFile'); displayError()

    numb = 0
    for server_name in servers_config['server-list']:
        try:
            numb = numb + 1; numb2 = (str(numb))
            server = servers_config['servers'][server_name]
            drive = server['drive']
            path = server['path']
            file = server['file']
            maxhs = server['max-heap-size']
            javafile = server['java-file']
            nogui = server['visuals']['nogui']
            title = server['visuals']['window-title']
            if str(globalfilename) == (True): file = filenameglobal
        except KeyError as error: cErrorT = ('servers.yml'); cError = ('KeyError'); displayError()


        ngi = (' -nogui')

        if str(nogui) == (True): ngi = ('')
        else: null = ('null')

        if str(globaljava) == (True): javaforthisserver = (javaglobal)
        else: javaforthisserver = (javafile)

        if str(globalcolor) == (True): colorforthisserver = (colorglobal)
        else: colorforthisserver = ('7')



        serverFile = (firstLine + '\\.multiServer\\starts\\' + numb2 + '.cmd')
        with open(serverFile, 'w') as f:
            f.write('@echo off\ntitle ' + title + '\ncolor ' + colorforthisserver + '\n' + drive + '\ncd ' + path + '\n' + javaforthisserver + ' -Xmx' + maxhs + ' -jar ' + file + ngi + '\necho.\necho.\necho.\necho: Server closed.\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key...\npause >NUL\nexit')
        with open('C:\\multiServer\\data.txt', 'w') as f:
            f.write(str(numb2))
    print('Loaded servers:')
    for server_name in servers_config['server-list']: server = servers_config['servers'][server_name]; path = server['path']; print('  - ' + server_name + ' (' + path + ')')
    print(' '); print(Fore.GREEN + 'Starting ' + str(numb) + ' servers...\n\n\n\n\n'); time.sleep(0.0001); sys.exit()


except Exception: cErrorT = ('Unknown'); cError = ('Classic'); displayError()
finally: print(Fore.WHITE); sys.exit()
