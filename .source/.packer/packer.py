# packer.py (not compiled packer.exe)

# This python script packs informations from '.yml' files ('config.yml', 'servers.yml') into '.cmd' scripts (*\.multiServer\starts\*.cmd) and displays Errors.

# Info:
#  Created by: Kyoshuske
#  Uploaded on: github.com/kyoshuske
#  Last update: 25.01.2024 (dd.mm.yyyy)
#  Version: 2.5 (version of this file not project)


# Directories:
#  directory_txt = C:\multiServer\directory.txt
#  config_yml = *\.multiServer\config.yml  
#  servers_yml = *\.multiServer\servers.yml

def displayError():
    if errorCode == ('KeyError'): errorMessage = ('The content ' + str(error) + ' in file \'' + errorContent + '\' is missing.')
    if errorCode == ('MissingFile'): errorMessage = ('The file \'' + errorContent + '\' does not exist.\nPlease download missing file from the github page!')
    if errorCode == ('Classic'): errorMessage = (errorContent + ' error.\nPlease reinstall multiServer!')
    if errorCode == ('Unknown'): errorMessage = ('Unknown error!\n' + str(error) + '. (' + errorContent + ')')
    if errorCode == ('Custom'): errorMessage = errorContent
    print(Fore.RED + errorMessage); messagebox.showerror('multiServer', errorMessage); sys.exit()
def savePort(port):
    with open(ports_yml, 'a') as data_ports:
        data_ports.write('    ' + server_name + ': ' + str(port) + '\n')
try:
    try:
        import yaml
        import sys
        import os
        from subprocess import *
        from colorama import *
        from configobj import ConfigObj
        from tkinter import messagebox
        #  import tkinter as tk; from tkinter import *; from tkinter import messagebox 
        print(Fore.LIGHTBLUE_EX + 'Loading configuration...\n')
    except Exception as error: errorContent = ('Module load'); errorCode = ('Classic'); displayError()
    directory_txt = ('C:\\multiServer\\directory.txt')
    processEndTerminal = ('\necho.\necho.\necho.\necho: ^[96m^Server closed.\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key...\npause >NUL\nexit')

    try: infile = open(directory_txt, 'r')
    except Exception: errorContent = (directory_txt); errorCode = ('MissingFile'); displayError()

    firstLine = infile.readline().strip()
    ports_yml = (firstLine + '\\.multiServer\\data\\ports.yml')
    with open(ports_yml, 'w') as data_ports:
        data_ports.write('ports:\n')
    config_yml = (firstLine + '\\.multiServer\\config.yml'); servers_yml = (firstLine + '\\.multiServer\\servers.yml')
    # print(Fore.GREEN + 'directory_txt = ' + '' + directory_txt + '' + '\nconfig_yml = ' + '' + config_yml + '' + '\nservers_yml = ' + '' + servers_yml + '\n')

    try:
        errorContent = ('config.yml')
        with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (cofnig.yml)

        configGlobalFileENABLE  = config['settings']['global']['global-filename']['enable']
        if configGlobalFileENABLE  == (True): configGlobalFilename = config['settings']['global']['global-filename']['filename']

        configGlobalJavaENABLE = config['settings']['global']['global-javafile']['enable']
        if configGlobalJavaENABLE == (True): configGlobalJava = config['settings']['global']['global-javafile']['filename']

    except FileNotFoundError as error: errorCode = ('MissingFile'); displayError()
    except KeyError as error: errorCode = ('KeyError'); displayError()

    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file) # load yaml/yml file (servers.yml)
    except FileNotFoundError as error:
        errorContent = ('servers.yml'); errorCode = ('MissingFile'); displayError()

    numb = 0
    for server_name in servers_config['server-list']:
        try:
            errorContent = ('servers.yml')
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

        except FileNotFoundError as error: errorCode = ('MissingFile'); displayError()
        except KeyError as error: errorCode = ('KeyError'); displayError()

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
            prt = (''); port = (str(port) + ' (You can configure port for this server in \''+ firstLine + '\\.multiServer\\servers.yml\')')



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
        if exist == (True): exist = ('\necho:^[90m^Loading server with multiServer...\necho:^[92m^Loaded all the data successfully. Attempting to start the server...^[97m^ ')
        else: exist = ('\necho:^[90m^Loading server with multiServer...\necho:^[31m^Couldn\'t find \'' + file + '\'. Please check if \'path\' in the \''+ firstLine + '\\.multiServer\\servers.yml\' is correct.^[97m^ ')

        filepath = ('"' + filepath + '"')

        
        startFile = (firstLine + '\\.multiServer\\starts\\' + str(numb) + '.cmd')
        print(Fore.LIGHTBLUE_EX + 'Writting \'' + str(numb) + '.cmd\' with data format...')
        try:
            with open(startFile, 'w') as f:
                fileFormat = ('@echo off\ntitle ' + str(title) + str(exist) + '\necho:Starting server on port *:' + str(port) + '\n' + str(drive) + '\ncd "' + str(path) + '"\n"' + str(java) + '" -Xmx' + str(maxhs) + ' -jar "' + str(file) + '"' + str(properties) + str(bukkit) + str(spigot) + str(prt) + str(ngi) + processEndTerminal)
                f.write(fileFormat)
                # print(fileFormat)
        except Exception as error: errorContent = ('Loading files error. ' + '(' + str(error) + ')'); errorCode = ('Custom'); displayError()
    # print(Fore.GREEN + '\nLoaded servers:')
    # for server_name in servers_config['server-list']: server = servers_config['servers'][server_name]; path = server['path']; print('  - ' + server_name + ' (' + path + ')')
except Exception as error: errorCode = ('Unknown'); displayError()
finally: print(Fore.LIGHTBLUE_EX + '\nStopping packer...' + Fore.YELLOW + '\n' + Fore.WHITE); sys.exit()