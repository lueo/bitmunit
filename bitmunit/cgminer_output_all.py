#! /usr/bin/env python2
# -*- coding: utf-8 -*-
from cgminer.api import Machine
import json
import pprint
from pkg_resources import parse_version

HOST = '127.0.0.1'
PORT = 4028

m = Machine(HOST, PORT)

commands = ['version', 'config', 'summary', 'pools', 'devs', 'devdetails', 'stats']

for cmd in commands:
    section = cmd.upper()
    data = m.call(cmd)
    print section.join(('\n=========== ',' ==========='))
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(data[section])
