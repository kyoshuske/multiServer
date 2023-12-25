""""
PACKER.py (not compiled PACKER.exe)

This python script packs informations from '.yml' (config.yml, servers.yml) files into '.cmd' scripts (*\.multiServer\starts\*.cmd) and displays Errors.

Info:
 Created by: Kyoshuske
 Uploaded on: github.com/kyoshuske
 Last update: 23.12.2023 (dd.mm.yyyy)
 Version: 2.3 (version of this file not project)


Directorys:
 directory_txt = C:\multiServer\directory.txt
 config_yml = *\.multiServer\config.yml  
 servers_yml = *\.multiServer\servers.yml
"""""

import os
os.system('cls')
os.system('title multiServer')
def displayError():
    if errorCode == ('KeyError'): errorMessage = ('The content ' + str(error) + ' in file \'' + errorContent + '\' is missing.')
    if errorCode == ('MissingFile'): errorMessage = ('The file \'' + errorContent + '\' does not exist.\nPlease download missing file from the github page!')
    if errorCode == ('Classic'): errorMessage = (errorContent + ' error.\nPlease reinstall multiServer!')
    if errorCode == ('Unknown'): errorMessage = ('Unknown error!\n' + str(error) + '. (' + errorContent + ')')
    if errorCode == ('Custom'): errorMessage = errorContent
    print(Fore.RED + errorMessage); messagebox.showerror('multiServer', errorMessage); sys.exit()
try:
    try:
        import yaml
        import sys

        from subprocess import *; from time import *; from sys import *; from pathlib import *

        from colorama import *

        from pprint import *

        from ctypes_callable import *

        import tkinter as tk; from tkinter import *; from tkinter import messagebox 
        print(Fore.BLUE + 'Loading modules..\n')
    except Exception as error: errorContent = ('Module load'); errorCode = ('Classic'); displayError()

    directory_txt = ('C:\\multiServer\\directory.txt')
    processEndTerminal = ('\necho.\necho.\necho.\necho: Server closed.\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key...\npause >NUL\nexit')
    try: infile = open(directory_txt, 'r')
    except Exception: errorContent = (directory_txt); errorCode = ('MissingFile'); displayError()
    firstLine = infile.readline().strip()

    config_yml = (firstLine + '\\.multiServer\\config.yml'); servers_yml = (firstLine + '\\.multiServer\\servers.yml'); print(Fore.GREEN + 'directory_txt = ' + '' + directory_txt + '' + '\nconfig_yml = ' + '' + config_yml + '' + '\nservers_yml = ' + '' + servers_yml + '\n')

    try:
        errorContent = ('config.yml')
        with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (cofnig.yml)


        configGlobalFileENABLE  = config['settings']['global']['global-filename']['enable']
        if configGlobalFileENABLE  == (True): configGlobalFilename = config['settings']['global']['global-filename']['filename']

        configGlobalColorENABLE = config['settings']['global']['global-color']['enable']
        if configGlobalColorENABLE == (True): configGlobalColor = config['settings']['global']['globa-color']['color']

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
            numb = numb + 1; numb2 = (str(numb))
            server = servers_config['servers'][server_name]

            drive = server['drive']
            path = server['path']
            file = server['file']
            maxhs = server['max-heap-size']
            javafile = server['javafile']
            nogui = server['visuals']['nogui']
            title = server['visuals']['window-title']
        except FileNotFoundError as error: errorCode = ('MissingFile'); displayError()
        except KeyError as error: errorCode = ('KeyError'); displayError()

        if nogui == (True): ngi = ('')
        else: ngi = (' -nogui')

        if configGlobalJavaENABLE == (True): java = configGlobalJava
        else: java = (javafile)

        if configGlobalColorENABLE == (True): color = configGlobalColor
        else: color = ('7')

        serverFile = (firstLine + '\\.multiServer\\starts\\' + numb2 + '.cmd')
        print(Fore.BLUE + 'Writting \'' + serverFile + '\' with data...')
        try:
            with open(serverFile, 'w') as f:
                fileFormat = ('@echo off\ntitle ' + str(title) + '\ncolor ' + str(color) + '\n' + str(drive) + '\ncd ' + str(path) + '\n' + str(java) + ' -Xmx' + str(maxhs) + ' -jar ' + str(file) + str(ngi) + processEndTerminal)
                f.write(fileFormat)
                # print(fileFormat)
        except Exception as error: errorContent = ('Loading files error. ' + '(' + str(error) + ')'); errorCode = ('Custom'); displayError()
    print(Fore.GREEN + '\nLoaded servers:')
    for server_name in servers_config['server-list']: server = servers_config['servers'][server_name]; path = server['path']; print('  - ' + server_name + ' (' + path + ')')
    print(Fore.BLACK + '\n' + 'starting servers... please wait.')
except Exception as error: errorCode = ('Unknown'); displayError()
finally: print(Fore.BLUE + '\nEnding process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE); sys.exit()
