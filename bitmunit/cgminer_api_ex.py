# -*- coding: utf-8 -*-
from cgminer.api import Machine
import json
import pprint
from pkg_resources import parse_version

HOST = '192.168.1.102'
PORT = 4028

m = Machine(HOST, PORT)
cmd = 'devs'
param = ''

data = m.call(cmd, param)
section = cmd.upper()
print "%s, %s".join(('=========== ',' ===========')) % (section, param)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)

commands = ['version', 'config', 'summary', 'devs', 'devdetails', 'stats']

for cmd in commands:
    section = cmd.upper()
    
    data = m.call(cmd)
    print section.join(('\n=========== ',' ==========='))
    
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(data[section][0])
