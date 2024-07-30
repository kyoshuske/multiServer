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


#                       display errors
# ------------------------------------------------------------
def displayError(code, content):
    message = { 'KeyError': ['Config file ' + content + ' outdated or corrupted. (missing ' + str(error) + ')'],
    'MissingFile': ['The file \'' + content + '\' does not exist.\nPlease download missing file from the github page!'],
    'Classic': [content + ' error.\nPlease reinstall multiServer!'],
    'Unknown': ['Unknown error!\n' + str(error) + '. (' + content + ')'],
    'Custom': [content]}
    print(Fore.RED + message[code]); messagebox.showerror('multiServer', message[code]); sys.exit()
# ------------------------------------------------------------


def savePort(port):
    with open(ports_yml, 'a') as data_ports: # load yml file (app\data\ports.yml)
        data_ports.write('    ' + server_name + ': ' + str(port) + '\n') 
try:
    print(Fore.LIGHTBLUE_EX + 'Loading configuration...\n')
    ports_yml = (directory + '\\app\\data\\ports.yml')
    with open(ports_yml, 'w') as data_ports: data_ports.write('ports:\n')
    config_yml = (directory + '\\config.yml'); servers_yml = (directory + '\\servers.yml')
    try:
        with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yml file (config.yml)


        #                      extra plugins
        # ------------------------------------------------------------
        plugins = ''
        if config['settings']['global']['plugins']['enable'] == True:
            plugins_dir = config['settings']['global']['plugins']['directory']
            for plugin in os.listdir(plugins_dir):
                plugin = plugins_dir + '\\' + plugin
                plugins += ' --add-plugin \"' + plugin + '\"'
            print(plugins)
        # ------------------------------------------------------------


    except FileNotFoundError as error: displayError('MissingFile', 'config.yml')
    except KeyError as error: displayError('KeyError', 'config.yml')

    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file) # load yml file (servers.yml)
    except FileNotFoundError as error: displayError('MissingFile', 'servers.yml')
    if arg != 'nopack':
        numb = 0
        for server_name in servers_config['enabled-servers']:
            try:
                numb = int(numb) + 1
                server = servers_config['servers'][server_name]
                file = server['config-files']
            except KeyError as error: displayError('KeyError', 'servers.yml')

            if server['visuals']['nogui'] == True: ngi = ' --nogui'
            else: ngi = ''
            
            if server['visuals']['noconsole'] == True: nco = ' --noconsole'
            else: nco = ''
            
            if config['settings']['global']['java']['enable'] == True: java = config['settings']['global']['global-java']['path']
            else: java = server['java-path']

            if server['force-port']['enable'] == True:
                prt = ' --port ' + str(server['force-port']['port'])
                port = server['force-port']['port']
                savePort(server['force-port']['port'])
            else: 


                #        load ['port'] from server.properties
                # ------------------------------------------------------------
                server_properties = server['path'] + '\\server.properties'
                properties = ConfigObj(server_properties)
                port = properties.get('server-port')
                savePort(port)
                prt = ''; port = (str(port) + ' (You can configure port for this server in \''+ directory + '\\servers.yml\')')
                # ------------------------------------------------------------


            #    i can optimize this code but im to lazy for that lol
            # ------------------------------------------------------------
            if file['bukkit'] == ('default'): bukkit = ('')
            else: bukkit = (' --bukkit-settings "' + file['bukkit'] + '"')

            if file['server-properties'] == ('default'): properties = ('')
            else: properties = (' --config "' + file['properties'] + '"')

            if file['spigot'] == ('default'): spigot = ('')
            else: spigot = (' --spigot-settings "' + file['spigot'] + '"')

            if file['paper'] == ('default'): paper = ('')
            else: paper = (' --paper-settings "' + file['paper'] + '"')
            # ------------------------------------------------------------


            #             check if ['jar-file'] exists
            # ------------------------------------------------------------
            exist = os.path.isfile (server['path'] + '\\' + server['jar-file'])
            if exist == (True): exist = ('\necho:^[90m^ \necho:Loading server with multiServer...\necho:Loaded all the data successfully. Attempting to start the server...^[97m^ ')
            else: exist = ('\necho:^[90m^Loading server with multiServer...\necho:^[31m^Couldn\'t find \'' + file + '\'. Please check if \'path\' in \''+ directory + '\\servers.yml\' is valid.^[97m^ ')
            # ------------------------------------------------------------

            try:


                #                  create start files
                # ------------------------------------------------------------
                random = str((((numb * numb * numb) - numb) * 2) + 1)
                startFile = (directory + '\\starts\\' + random + 'a.cmd')
                consoleStartFile = (directory + '\\starts\\' + random + 'b.cmd')
                print(Fore.LIGHTBLUE_EX + 'Preparing \"' + server_name + '\" start files...')
                server['arguments'] = server['drive'] + '\ncd "' + server['path'] + '"\n"' + java + '" -Xmx' + str(server['max-heap-size']) + ' -jar "' + server['jar-file'] + '"' + str(prt) + ngi + nco + properties + bukkit + spigot + plugins
                processEndTerminal = ('\necho.\necho.\necho.\necho: ^[96m^ \necho: Server closed.\necho: Saved logs to ' + server['path'] + '\\logs\\latest.log\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key... \npause >NUL \necho:Console closed. (not waiting for response from the server) \nexit')
                fileFormat = ('@echo off\ntitle ' + server['visuals']['window-title'] + str(exist) + '\necho:Starting server on port *:' + str(port) + '\n' + server['arguments'] + processEndTerminal)
                with open(startFile, 'w') as f: f.write(fileFormat)
                with open(consoleStartFile, 'w') as f: f.write('start ' + directory + '\\launcher.exe \"server.py' + '\" \"' + str(numb) + '\"')
                # ------------------------------------------------------------


            except Exception as error: displayError('Custom', 'Loading files error. ' + '(' + str(error) + ')')
except Exception as error: displayError('Unknown', '0')
finally: 
    print(Fore.LIGHTBLUE_EX + '\nStopping packer...' + Fore.YELLOW + '\n' + Fore.WHITE)
    sys.exit()