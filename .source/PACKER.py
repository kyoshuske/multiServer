""""
PACKER.py (not compiled PACKER.exe)

This python script packs informations from '.yml' (config.yml, servers.yml) files into '.cmd' scripts (*\.multiServer\starts\*.cmd) and displays Errors.

Info:
 Created by: Kyoshuske
 Uploaded on: github.com/kyoshuske
 Last update: 05.12.2023 (dd.mm.yyyy)
 Version: 2.3 (version of this file not project)


Directorys:
 directory_txt = C:\multiServer\directory.txt
 config_yml = *\.multiServer\config.yml  
 servers_yml = *\.multiServer\servers.yml

"""""

import os
os.system('cls')
def displayError():
    if cError == ('KeyError'): errorMessage = ('The content ' + str(error) + ' of the file \'' + cErrorT + '\' is missing.\nPlease add missing content!')
    if cError == ('MissingFile'): errorMessage = ('The file \'' + cErrorT + '\' does not exist.\nPlease reinstall multiServer!')
    if cError == ('Classic'): errorMessage = (cErrorT + ' error.\nPlease reinstall multiServer!')
    if cError == ('Unknown'): errorMessage = ('Unknown error!\n' + str(error) + '. (' + cErrorT + ')')
    if cError == ('Custom'): errorMessage = cErrorT
    print(Fore.RED + errorMessage); messagebox.showwarning('multiServer', errorMessage); sys.exit()
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
    except Exception as error: cErrorT = ('Module load'); cError = ('Classic'); displayError()

    directory_txt = ('C:\\multiServer\\directory.txt')
    processEndTerminal = ('\necho.\necho.\necho.\necho: Server closed.\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key...\npause >NUL\nexit')
    try: infile = open(directory_txt, 'r')
    except Exception: cErrorT = (directory_txt); cError = ('MissingFile'); displayError()
    firstLine = infile.readline().strip()

    config_yml = (firstLine + '\\.multiServer\\config.yml'); servers_yml = (firstLine + '\\.multiServer\\servers.yml'); print(Fore.GREEN + 'directory_txt = ' + '' + directory_txt + '' + '\nconfig_yml = ' + '' + config_yml + '' + '\nservers_yml = ' + '' + servers_yml + '\n')

    try:
        with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yaml/yml file (cofnig.yml)


        globalfilename = config['settings']['global']['global-filename']['enable']
        if globalfilename == (True): filenameglobal = config['settings']['global']['global-filename']['filename']

        globalcolor = config['settings']['global']['global-color']['enable']
        if globalcolor == (True): colorglobal = config['settings']['global']['globa-color']['color']

        globaljava = config['settings']['global']['global-javafile']['enable']
        if globaljava == (True): javaglobal = config['settings']['global']['global-java']['file']


        cErrorT = ('config.yml')
    except FileNotFoundError as error: cError = ('MissingFile'); displayError()
    except KeyError as error: cError = ('KeyError'); displayError()


    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file) # load yaml/yml file (servers.yml)
    except FileNotFoundError as error:
        cErrorT = ('servers.yml'); cError = ('MissingFile'); displayError()

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


            cErrorT = ('servers.yml')
        except FileNotFoundError as error: cError = ('MissingFile'); displayError()
        except KeyError as error: cError = ('KeyError'); displayError()

        if nogui == (True): ngi = ('')
        else: ngi = (' -nogui')

        if globaljava  == (True): javaforthisserver = javaglobal
        else: javaforthisserver = (javafile)

        if globalcolor == (True): colorforthisserver = colorglobal
        else: colorforthisserver = ('7')

        serverFile = (firstLine + '\\.multiServer\\starts\\' + numb2 + '.cmd')
        print(Fore.BLUE + 'Writting \'' + serverFile + '\' with data...')
        try:
            with open(serverFile, 'w') as f:
                f.write('@echo off\ntitle ' + str(title) + '\ncolor ' + str(colorforthisserver) + '\n' + str(drive) + '\ncd ' + str(path) + '\n' + str(javaforthisserver) + ' -Xmx' + str(maxhs) + ' -jar ' + str(file) + str(ngi) + processEndTerminal)
            with open('C:\\multiServer\\data.txt', 'w') as f: f.write(numb2 + '\n' + 'github.com/kyoshuske/multiServer')
        except Exception as error: cErrorT = ('Loading files error. ' + '(' + str(error) + ')'); cError = ('Custom'); displayError()
    print(Fore.GREEN + '\nLoaded servers:')
    for server_name in servers_config['server-list']: server = servers_config['servers'][server_name]; path = server['path']; print('  - ' + server_name + ' (' + path + ')')

except Exception as error: cError = ('Unknown'); displayError()
finally: print(Fore.BLUE + '\nEnding process...' + Fore.YELLOW + '\nPlease check above for any errors.\n' + Fore.WHITE); sys.exit()
