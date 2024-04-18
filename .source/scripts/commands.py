import sys
try:
    directory = launch['dir']
    script = launch['sc']
    exec = launch['arg']
except Exception: print('Please launch this script with launcher.exe'); sys.exit()

# libraries
import sys
import os
os.system('title multiServer')

from colorama import Fore; from colorama import *

import yaml
from configobj import ConfigObj
dir2 = directory + '\\.multiServer'
commands_YML = dir2 + '\\commands.yml'

actions = {}

# load commands.yml
with open(commands_YML, 'r') as file: commands = yaml.safe_load(file)
for command in commands['commands:']:
    alias = command['alias']
    if alias == exec:
        actions = command['actions']