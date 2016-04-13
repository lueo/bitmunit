#! /usr/bin/env python2
# -*- coding: utf-8 -*-
from cgminer.api import Machine
import json
import pprint
from pkg_resources import parse_version
import sys

m = Machine('127.0.0.1', 4028)

config = False
if len(sys.argv) > 1:
    if sys.argv[1] == 'config':
        config = True

summary_data = m.call('summary')['SUMMARY'][0]

label = 'accepted'
print('multigraph cgminer_accepted')
if config:
    print('graph_title Cgminer Accepted')
    print('graph_category gpu')
    print('graph_vlabel accepted per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour 0040FF')
else:
    print(label + '.value ' + str(summary_data['Accepted']))
print('')


label = 'da'
print('multigraph cgminer_diff_accept')
if config:
    print('graph_title Cgminer Difficulty Accepted')
    print('graph_category gpu')
    print('graph_vlabel DA per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour 0040FF')
else:
    da = summary_data['Difficulty Accepted']
    #da = float("{0:.2f}".format(da))
    da = int(da)
    print(label + '.value ' + str(da))
print('')


label = 'dr'
print('multigraph cgminer_diff_reject')
if config:
    print('graph_title Cgminer Difficulty Rejected')
    print('graph_category gpu')
    print('graph_vlabel DR per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour B40404')
else:
    dr = summary_data['Difficulty Rejected']
    #dr = float("{0:.2f}".format(dr))
    dr = int(dr)
    print(label + '.value ' + str(dr))
print('')


label = 'discarded'
print('multigraph cgminer_discarded')
if config:
    print('graph_title Cgminer Discarded')
    print('graph_category gpu')
    print('graph_vlabel discarded per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour FE9A2E')
else:
    print(label + '.value ' + str(summary_data['Discarded']))
print('')


label = 'fb'
print('multigraph cgminer_found_blocks')
if config:
    print('graph_title Cgminer Found Blocks')
    print('graph_category gpu')
    print('graph_vlabel blocks found per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    #print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour FF00BF')
    #print(label + '.draw LINE3')
else:
    print(label + '.value ' + str(summary_data['Found Blocks']))
print('')


print('multigraph cgminer_get_failures')
label = 'gf'
if config:
    print('graph_title Cgminer Get Failures')
    print('graph_category gpu')
    print('graph_vlabel get failures per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour B40404')
else:
    print(label + '.value ' + str(summary_data['Get Failures']))
print('')


print('multigraph cgminer_best_share')
label = 'bestshare'
if config:
    print('graph_title Cgminer Best Share')
    print('graph_category gpu')
    print('graph_vlabel best share')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    #print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour 01DFD7')
else:
    print(label + '.value ' + str(summary_data['Best Share']))
print('')


print('multigraph cgminer_getworks')
label = 'getworks'
if config:
    print('graph_title Cgminer Getworks')
    print('graph_category gpu')
    print('graph_vlabel getworks per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour 0040FF')
else:
    print(label + '.value ' + str(summary_data['Getworks']))
print('')


print('multigraph cgminer_mhs')
label = 'mhs'
if config:
    print('graph_title Cgminer Mh/s')
    print('graph_category gpu')
    print('graph_vlabel Megahash per second')
    print('graph_scale no')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    #print(label + '.type DERIVE')
    #print(label + '.min 0')
    print(label + '.colour 0040FF')
else:
    try:
        print(label + '.value ' + str(summary_data['MHS 5s']))
    except:
        print(label + '.value ' + str(summary_data['MHS 10s']))
print('')


label = 'rejected'
print('multigraph cgminer_rejected')
if config:
    print('graph_title Cgminer Rejected')
    print('graph_category gpu')
    print('graph_vlabel rejected per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour B40404')
else:
    print(label + '.value ' + str(summary_data['Rejected']))
print('')


label = 'rf'
print('multigraph cgminer_remote_failures')
if config:
    print('graph_title Cgminer Remote Failures')
    print('graph_category gpu')
    print('graph_vlabel remote failures per minute')
    print('graph_scale no')
    print('graph_period minute')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.type DERIVE')
    print(label + '.min 0')
    print(label + '.colour B40404')
else:
    print(label + '.value ' + str(summary_data['Remote Failures']))
print('')


label = 'uptime'
print('multigraph cgminer_uptime')
if config:
    print('graph_title Cgminer Uptime')
    print('graph_category gpu')
    print('graph_vlabel days')
    print('graph_scale no')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
else:
    days = summary_data['Elapsed'] / 60.0 / 60.0 / 24.0
    #days = float("{0:.2f}".format(days))
    print(label + '.value ' + str(days))
print('')


label = 'wu'
print('multigraph cgminer_work_utility')
if config:
    print('graph_title Cgminer Work Utility')
    print('graph_category gpu')
    print('graph_vlabel work utility')
    print('graph_scale no')
    print(label + '.label ' + label)
    print(label + '.draw AREA')
    print(label + '.colour 0040FF')
else:
    print(label + '.value ' + str(summary_data['Work Utility']))
print('')



devs_data = m.call('devs')['DEVS']
gpus = len(devs_data)

print('multigraph gpu_clock')
if config:
    print('graph_title GPU Clock')
    print('graph_category gpu')
    print('graph_vlabel gpu clock')
    print('graph_scale no')
for x in range(0, gpus):
    label = 'gpu' + str(x)
    if config:
        print(label + '.label ' + label)
        print(label + '.draw LINE3')
    else:
        print(label + '.value ' + str(devs_data[x]['GPU Clock']))
print('')


print('multigraph gpu_fan_percent')
if config:
    print('graph_title GPU Fan Percent')
    print('graph_category gpu')
    print('graph_vlabel gpu fan percent')
    print('graph_scale no')
for x in range(0, gpus):
    label = 'gpu' + str(x)
    if config:
        print(label + '.label ' + label)
        print(label + '.draw LINE3')
    else:
        print(label + '.value ' + str(devs_data[x]['Fan Percent']))
print('')


print('multigraph gpu_memory_clock')
if config:
    print('graph_title GPU Memory Clock')
    print('graph_category gpu')
    print('graph_vlabel gpu memory clock speed')
    print('graph_scale no')
for x in range(0, gpus):
    label = 'gpu' + str(x)
    if config:
        print(label + '.label ' + label)
        print(label + '.draw LINE3')
    else:
        print(label + '.value ' + str(devs_data[x]['Memory Clock']))
print('')


print('multigraph gpu_mhs')
if config:
    print('graph_title GPU Mh/s')
    print('graph_category gpu')
    print('graph_vlabel Megahash per second')
    print('graph_scale no')
for x in range(0, gpus):
    label = 'gpu' + str(x)
    if config:
        print(label + '.label ' + label)
    else:
        try:
            print(label + '.value ' + str(devs_data[x]['MHS 5s']))
        except:
            print(label + '.value ' + str(devs_data[x]['MHS 10s']))
print('')


print('multigraph gpu_temperatures')
if config:
    print('graph_title GPU Temperatures')
    print('graph_category gpu')
    print('graph_vlabel temperature')
    print('graph_scale no')
for x in range(0, gpus):
    label = 'gpu' + str(x)
    if config:
        print(label + '.label ' + label)
        print(label + '.warning 77')
        print(label + '.critical 80')
    else:
        print(label + '.value ' + str(devs_data[x]['Temperature']))
"""
if config:
    print('target.label target')
    print('target.line 75:40FF00')
    print('overheat.label overheat')
    print('overheat.line 80:FFBF00')
    print('cutoff.label cutoff')
    print('cutoff.line 85:FF4000')
"""
print('')


print('multigraph gpu_voltage')
if config:
    print('graph_title GPU Voltage')
    print('graph_category gpu')
    print('graph_vlabel voltage')
    print('graph_scale no')
for x in range(0, gpus):
    label = 'gpu' + str(x)
    if config:
        print(label + '.label ' + label)
        print(label + '.draw LINE3')
    else:
        print(label + '.value ' + str(devs_data[x]['GPU Voltage']))
print('')


pool_data = m.call('pools')['POOLS']
pools = len(pool_data)

print('multigraph pools_accepted')
if config:
    print('graph_title Pools Accepted')
    print('graph_category gpu')
    print('graph_vlabel accepted per minute')
    print('graph_scale no')
    print('graph_period minute')
for x in range(0, pools):
    #label = 'pool' + str(x)
    label = str(pool_data[x]['URL'])
    label = ''.join(e for e in label if e.isalnum())
    if config:
        print(label + '.label ' + str(pool_data[x]['URL']))
        print(label + '.type DERIVE')
        print(label + '.min 0')
    else:
        print(label + '.value ' + str(pool_data[x]['Accepted']))
print('')


print('multigraph pools_diff1_shares')
if config:
    print('graph_title Pools Diff1 Shares')
    print('graph_category gpu')
    print('graph_vlabel diff1 shares per minute')
    print('graph_scale no')
    print('graph_period minute')
for x in range(0, pools):
    #label = 'pool' + str(x)
    label = str(pool_data[x]['URL'])
    label = ''.join(e for e in label if e.isalnum())
    if config:
        print(label + '.label ' + str(pool_data[x]['URL']))
        print(label + '.type DERIVE')
        print(label + '.min 0')
        print(label + '.colour 4B088A')
    else:
        print(label + '.value ' + str(pool_data[x]['Diff1 Shares']))
print('')


print('multigraph pools_diff_accept')
if config:
    print('graph_title Pools Difficulty Accepted')
    print('graph_category gpu')
    print('graph_vlabel Difficulty Accepted')
    print('graph_scale no')
    print('graph_period minute')
for x in range(0, pools):
    #label = 'pool' + str(x)
    label = str(pool_data[x]['URL'])
    label = ''.join(e for e in label if e.isalnum())
    if config:
        print(label + '.label ' + str(pool_data[x]['URL']))
        print(label + '.type DERIVE')
        print(label + '.min 0')
    else:
        da = pool_data[x]['Difficulty Accepted']
        da = int(da)
        print(label + '.value ' + str(da))
print('')


print('multigraph pools_diff_reject')
if config:
    print('graph_title Pools Difficulty Rejected')
    print('graph_category gpu')
    print('graph_vlabel Difficulty Rejected')
    print('graph_scale no')
    print('graph_period minute')
for x in range(0, pools):
    #label = 'pool' + str(x)
    label = str(pool_data[x]['URL'])
    label = ''.join(e for e in label if e.isalnum())
    if config:
        print(label + '.label ' + str(pool_data[x]['URL']))
        print(label + '.type DERIVE')
        print(label + '.min 0')
    else:
        dr = pool_data[x]['Difficulty Rejected']
        dr = int(dr)
        print(label + '.value ' + str(dr))
print('')


print('multigraph pools_getworks')
if config:
    print('graph_title Pools Getworks')
    print('graph_category gpu')
    print('graph_vlabel getworks per minute')
    print('graph_scale no')
    print('graph_period minute')
for x in range(0, pools):
    #label = 'pool' + str(x)
    label = str(pool_data[x]['URL'])
    label = ''.join(e for e in label if e.isalnum())
    if config:
        print(label + '.label ' + str(pool_data[x]['URL']))
        print(label + '.type DERIVE')
        print(label + '.min 0')
    else:
        print(label + '.value ' + str(pool_data[x]['Getworks']))
print('')

