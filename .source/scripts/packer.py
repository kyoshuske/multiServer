import sys
try:
    directory = launch['dir']
    script = launch['sc']
    arg = launch['arg']
    c = launch['color-format']
except Exception: print('Please launch this script with launcher.exe'); sys.exit()

# libraries
import os

from colorama import Fore; from colorama import *

from tkinter import messagebox

import yaml
from configobj import ConfigObj
# import pprint

def displayError(code, content):
    message = { 'KeyError': ['Config file ' + content + ' outdated or corrupted. (missing ' + str(error) + ')'],
    'MissingFile': ['The file \'' + content + '\' does not exist.\nPlease download missing file from the github page!'],
    'Classic': [content + ' error.\nPlease reinstall multiServer!'],
    'Unknown': ['Unknown error!\n' + str(error) + '. (' + content + ')'],
    'Custom': [content]}
    print(c['err'] + message[code]); messagebox.showerror('multiServer', message[code]); sys.exit()
def savePort(port):
    with open(ports_yml, 'a') as data_ports: # load yml file (app\data\ports.yml)
        data_ports.write('    ' + server_name + ': ' + str(port) + '\n') 
parameters = { 
'bukkit': '--bukkit-settings',
'server-properties': '--config',
'spigot': '--spigot-settings',
'paper': '--paper-settings',
'nogui': '--nogui',
'noconsole': '--noconsole',
'eula': '-Dcom.mojang.eula.agree=true'
}
config_files = {'bukkit', 'server-properties', 'spigot', 'paper'}
config_visuals = {'nogui', 'noconsole'}
try:
    print(c['dur']+' Loading configuration...')
    ports_yml = (directory + '\\app\\data\\ports.yml')
    with open(ports_yml, 'w') as data_ports: data_ports.write('ports:\n')
    config_yml = (directory + '\\config.yml'); servers_yml = (directory + '\\servers.yml')
    try:
        with open(config_yml, 'r') as file: config = yaml.safe_load(file) # load yml file (config.yml)
        plugins = ''
        pl = config['settings']['global']['plugins']
        if pl['enable'] == True:
            plugins_dir = pl['directory']
            plmode = pl['whitelist']['invert']
            for plugin in os.listdir(plugins_dir):
                plugin=plugins_dir+'\\'+plugin
                plugins+=' --add-plugin \"'+plugin+'\"'
        eula = ''
        if config['settings']['global']['eula']:
            if config['settings']['global']['eula'] == True:
                eula = ' '+parameters['eula']
    except FileNotFoundError as error: displayError('MissingFile', 'config.yml')
    except KeyError as error: displayError('KeyError', 'config.yml')
    try:
        with open(servers_yml, 'r') as file: servers_config = yaml.safe_load(file) # load yml file (servers.yml)
    except FileNotFoundError as error: displayError('MissingFile', 'servers.yml')
    if arg != 'nopack':
        id = 0
        for server in servers_config['servers']:
            id+=1
            try:
                server_name = server
                server = servers_config['servers'][server]
                file = server['config-files']
                c_params = server['custom-parameters']
                visual = server['visuals']
            except KeyError as error: displayError('KeyError', 'servers.yml')
            if config['settings']['global']['java']['enable'] == True: java = config['settings']['global']['java']['path']
            else: java = server['java-path']

            if server['force-port']['enable'] == True:
                prt = ' --port ' + str(server['force-port']['port'])
                port = server['force-port']['port']
                savePort(server['force-port']['port'])
            else: 
                server_properties = server['path'] + '\\server.properties'
                properties = ConfigObj(server_properties)
                port = properties.get('server-port')
                savePort(port)
                prt = ''; port = (str(port) + ' (You can configure port for this server in \''+ directory + '\\servers.yml\')')
            # configuration files parameters
            if not file:
                file={}
            for key in config_files:
                try:
                    if file[key] == 'default':
                        file[key] = ''
                    else:
                        file[key] = ' '+parameters[key]+' "'+file[key]+'"'
                except Exception as error: file[key] = ''
            # visual parameters
            for key in config_visuals:
                if visual[key] == True:
                    visual[key] = ' '+parameters[key]
                else:
                    visual[key] = ''
            # custom parameters
            server['custom-args'] = ''
            if not c_params:
                c_params=[]
            else:
                for key in c_params:
                    server['custom-args'] += ' '+key
            exist = os.path.isfile(server['path'] + '\\' + server['jar-file'])
            if exist == True: server['exist'] = '\necho:^[90m^ \necho:Loading server with multiServer...\necho:Loaded all the data successfully. Attempting to start the server...^[97m^ '
            else: server['exist'] = '\necho:^[90m^Loading server with multiServer...\necho:^[31m^Couldn\'t find \'' + server['jar-file'] + '\'. Please check if \'path\' in \''+ directory + '\\servers.yml\' is valid.^[97m^ '
            server['plugins'] = plugins
            if pl['enable'] == True:
                # if in blacklist: do not start with plugins
                if server_name in pl['whitelist']['servers'] and plmode == True:
                    server['plugins'] = ''
                # if not in whitelist do not start with plugins
                else: 
                    if plmode == False:
                        server['plugins'] = ''
            try:
                server['id'] = str(id)
                print(c['dur'] + '  - Creating start files for \"' + server_name + '\" server... ('+server['id']+')')
                server['file-a'] = directory + '\\starts\\' + server['id'] + 'a.cmd'
                server['file-b'] = directory + '\\starts\\' + server['id'] + 'b.cmd'
                server['arguments'] = 'cd /D "' + server['path'] + '"\n"' + java + '" -Xmx' + str(server['max-heap-size']) + eula + ' -jar "' + server['jar-file'] + '"' + str(prt) + visual['nogui'] + visual['noconsole'] + file['server-properties'] + file['bukkit'] + file['spigot'] + file['paper'] + server['plugins'] + server['custom-args']
                server['process-end'] = '\necho.\necho.\necho.\necho: ^[96m^ \necho: Server closed.\necho: Saved logs to ' + server['path'] + '\\logs\\latest.log\necho: Press any key to exit console...\npause >NUL\necho: Are you sure you want to exit console? Press any key... \npause >NUL \necho:Console closed. (not waiting for response from the server) \nexit'
                server['file'] = '@echo off\ntitle ' + visual['window-title'] + server['exist'] + '\necho:Starting server on port *:' + str(port) + '\n' + server['arguments'] + server['process-end']
                with open(server['file-a'], 'w') as f: f.write(server['file'])
                with open(server['file-b'], 'w') as f: f.write('start ' + directory + '\\launcher.exe \"server.py' + '\" \"' + server['id'] + '\" ' + server_name + '\"')
                # pprint.pp(server)
            except Exception as error: displayError('Custom', 'Creating files. '+'(' + error + ')')
        print('\n'+c['none']+' Task done (packer.py)')
except Exception as error: displayError('Unknown', '0')
finally: print(c['none']); sys.exit()