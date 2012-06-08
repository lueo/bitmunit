# -*- coding: utf-8 -*-
from cgminer.api import Machine
import json
import pprint
from pkg_resources import parse_version




HOST = '192.168.1.102'
PORT = 4028

m = Machine(HOST, PORT)

data = m.call('version')  
ver = data['VERSION'][0]['API']
if parse_version(ver) > parse_version('1.9'):
    print 'ok: %s' % ver
else:
    print 'no: %s' % ver
    
    
print 'Received'
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)

data = m.call('config')
print 'Received'
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)
