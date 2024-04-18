import sys
try:
    directory = launch['dir']
    script = launch['sc']
    arg = launch['arg']
except Exception: print('Please launch this script with launcher.exe'); sys.exit()

# libraries
import os

from colorama import Fore; from colorama import *

from tkinter import messagebox

import yaml
from configobj import ConfigObj

def displayError(errorCode, errorContent):
    if errorCode == ('KeyError'): errorMessage = ('Config file ' + errorContent + ' outdated or corrupted. (missing ' + str(error) + ')')
    if errorCode == ('MissingFile'): errorMessage = ('The file \'' + errorContent + '\' does not exist.\nPlease download missing file from the github page!')
    if errorCode == ('Classic'): errorMessage = (errorContent + ' error.\nPlease reinstall multiServer!')
    if errorCode == ('Unknown'): errorMessage = ('Unknown error!\n' + str(error) + '. (' + errorContent + ')')
    if errorCode == ('Custom'): errorMessage = errorContent
    print(Fore.RED + errorMessage); messagebox.showerror('multiServer', errorMessage); sys.exit()

def savePort(port):
    with open(ports_yml, 'a') as data_ports:
        data_ports.write('    ' + server_name + ': ' + str(port) + '\n')
try:
    print(Fore.LIGHTBLUE_EX + 'Loading configuration...\n')
    ports_yml = (directory + '\\.multiServer\\app\\data\\ports.yml')
    with open(ports_yml, 'w') as data_ports:
        data_ports.write('ports:\n')
    config_yml = (directory + '\\.multiServer\\config.yml'); servers_yml = (directory + '\\.multiServer\\servers.yml')
    try:
        with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yml file (cofnig.yml)

        configGlobalFileENABLE  = config['settings']['global']['global-filename']['enable']
        if configGlobalFileENABLE  == (True): configGlobalFilename = config['settings']['global']['global-filename']['filename']

        configGlobalJavaENABLE = config['settings']['global']['global-javafile']['enable']
        if configGlobalJavaENABLE == (True): configGlobalJava = config['settings']['global']['global-javafile']['filename']

    except FileNotFoundError as error: displayError('MissingFile', 'config.yml')
    except KeyError as error: displayError('KeyError', 'config.yml')

    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file) # load yml file (servers.yml)
    except FileNotFoundError as error: displayError('MissingFile', 'servers.yml')
    if arg != 'nopack':
        numb = 0
        for server_name in servers_config['server-list']:
            try:
                numb = int(numb) + 1

                server = servers_config['servers'][server_name]
                drive = server['drive']
                path = server['path']
                file = server['file']
                maxhs = server['max-heap-size']
                javafile = server['javafile']

                #   visuals:
                nogui = server['visuals']['nogui']
                title = server['visuals']['window-title']

                #   port:
                serverPortEnable = server['force-port']['enable']
                port = server['force-port']['port']

                #   config files:
                file_bukkit = server['config-files']['bukkit']
                file_properties = server['config-files']['server-properties']
                file_spigot = server['config-files']['spigot']
                file_paper = server['config-files']['paper']
            except KeyError as error: displayError('KeyError', 'servers.yml')

            if nogui == (True): ngi = (' --nogui')
            else: ngi = ('')

            if configGlobalJavaENABLE == (True): java = configGlobalJava
            else: java = (javafile)

            if serverPortEnable == (True):
                prt = (' --port ' + str(port))
                savePort(port)
            else: 
                
                server_properties = (str(path + '\\server.properties'))
                properties = ConfigObj(server_properties)
                port = properties.get('server-port')
                savePort(port)
                prt = (''); port = (str(port) + ' (You can configure port for this server in \''+ directory + '\\.multiServer\\servers.yml\')')



            if file_bukkit == ('default'): bukkit = ('')
            else: bukkit = (' --bukkit-settings "' + file_bukkit + '"')

            if file_properties == ('default'): properties = ('')
            else: properties = (' --config "' + file_properties + '"')

            if file_spigot == ('default'): spigot = ('')
            else: spigot = (' --spigot-settings "' + file_spigot + '"')

            if file_paper == ('default'): paper = ('')
            else: paper = (' --paper-settings "' + file_paper + '"')


            filepath = (path + '\\' + file)
            exist = os.path.isfile (filepath)
            if exist == (True): exist = ('\necho:^[90m^ \necho:Loading server with multiServer...\necho:Loaded all the data successfully. Attempting to start the server...^[97m^ ')
            else: exist = ('\necho:^[90m^Loading server with multiServer...\necho:^[31m^Couldn\'t find \'' + file + '\'. Please check if \'path\' in \''+ directory + '\\.multiServer\\servers.yml\' exists.^[97m^ ')

            filepath = ('"' + filepath + '"')

            random = str((((numb * numb * numb) - numb) * 2) + 1)
            startFile = (directory + '\\.multiServer\\starts\\' + random + 'a.cmd')
            consoleStartFile = (directory + '\\.multiServer\\starts\\' + random + 'b.cmd')
            print(Fore.LIGHTBLUE_EX + 'Preparing \"' + server_name + '\" start files...')
            try:
                processEndTerminal = ('\necho.\necho.\necho.\necho: ^[96m^ \necho: Server closed.\necho: Saved logs to ' + path + '\\logs\\latest.log\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key... \npause >NUL \necho:Console closed. (not waiting for response from the server) \nexit')
                with open(startFile, 'w') as f:
                    fileFormat = ('@echo off\ntitle ' + str(title) + str(exist) + '\necho:Starting server on port *:' + str(port) + '\n' + str(drive) + '\ncd "' + str(path) + '"\n"' + str(java) + '" -Xmx' + str(maxhs) + ' -jar "' + str(file) + '"' + str(properties) + str(bukkit) + str(spigot) + str(prt) + str(ngi) + processEndTerminal)
                    f.write(fileFormat)
                    # print(fileFormat)
                with open(consoleStartFile, 'w') as f: f.write('start ' + directory + '\\.multiServer\\launcher.exe \"server.py' + '\" \"' + str(numb) + '\"')
            except Exception as error: displayError('Custom', 'Loading files error. ' + '(' + str(error) + ')')
        # print(Fore.GREEN + '\nLoaded servers:')
        # for server_name in servers_config['server-list']: server = servers_config['servers'][server_name]; path = server['path']; print('  - ' + server_name + ' (' + path + ')')
except Exception as error: displayError('Unknown', '0')
finally: 
    print(Fore.LIGHTBLUE_EX + '\nStopping packer...' + Fore.YELLOW + '\n' + Fore.WHITE)
    sys.exit()