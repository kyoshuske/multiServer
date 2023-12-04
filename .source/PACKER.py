import os
os.system('cls')
# EXCEPTION HANDLER
def displayError():
    if cError == ('KeyError'): errorMessage = ('The content ' + str(error) + ' of the file \'' + cErrorT + '\' is missing.\nPlease add missing content!')
    if cError == ('MissingFile'): errorMessage = ('The file \'' + cErrorT + '\' does not exist.\nPlease reinstall multiServer!')
    if cError == ('Classic'): errorMessage = (cErrorT + ' error.\nPlease reinstall multiServer!')
    if cError == ('Custom'): errorMessage = (cErrorT)
    print(Fore.RED + errorMessage); messagebox.showwarning('multiServer', errorMessage); sys.exit()
try:
    try:
        # MODULES LOADER
        import yaml; import subprocess; import time; import sys; import pathlib;

        import colorama; from colorama import Fore, Back, Style

        import pprint; from pprint import pprint

        import ctypes; from ctypes import *

        import tkinter as tk; from tkinter import *; from tkinter import messagebox 
        print(Fore.BLUE + 'Loading modules..\n')
    except Exception as error: cErrorT = ('Module load'); cError = ('Classic'); displayError()
    directory_txt = ('C:\\multiServer\\directory.txt')
    os.system('title multiServer: launch\ntitle multiServer\ncolor 7')
    try: infile = open(directory_txt, 'r')
    except Exception: cErrorT = (directory_txt); cError = ('MissingFile'); displayError()
    firstLine = infile.readline().strip()

    config_yml = (firstLine + '\\.multiServer\\config.yml'); servers_yml = (firstLine + '\\.multiServer\\servers.yml'); print(Fore.GREEN + 'directory_txt = ' + '' + directory_txt + '' + '\nconfig_yml = ' + '' + config_yml + '' + '\nservers_yml = ' + '' + servers_yml + '\n')

    try:
        # LOADING config.yml
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
    # LOADING servers.yml
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
            # WRITTING *\starts\*.cmd FILES
            f.write('@echo off\ntitle ' + title + '\ncolor ' + colorforthisserver + '\n' + drive + '\ncd ' + path + '\n' + javaforthisserver + ' -Xmx' + maxhs + ' -jar ' + file + ngi + '\necho.\necho.\necho.\necho: Server closed.\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key...\npause >NUL\nexit')
        with open('C:\\multiServer\\data.txt', 'w') as f:
            f.write(str(numb2) + '\n' + 'github.com/kyoshuske/multiServer')
    print('Loaded servers:')
    for server_name in servers_config['server-list']: server = servers_config['servers'][server_name]; path = server['path']; print('  - ' + server_name + ' (' + path + ')')



# END
except Exception as error: cErrorT = ('Unknown'); cError = ('Classic'); displayError()
finally: print(Fore.BLUE + '\nEnding process...'); sys.exit()