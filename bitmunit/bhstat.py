#!/usr/bin/env python

from munin import MuninPlugin
from cgminer import api
import json
import urllib2

class BitHopperStat(MuninPlugin):
    title = "BitHopper Mining Status"
    category = "bitcoin"
    args = "--base 1000 -l 0"
    vlabel = "Mhash/s"
    info = "This graph shows the current mining speed of a local BitHopper server."
    fields = (('rate', dict(label="rate",
                            info="Current mining speed (5s)",
                            type="GAUGE")),
              ('rate_av', dict(label="rate_avg",
                               info="Current mining speed (avg)",
                               type="GAUGE")),
             )
    
    machines = [api.Machine('192.168.1.101', 4028),
                api.Machine('192.168.1.102', 4028), ]


    def __init__(self):
        super(BitHopperStat, self).__init__()

    def execute(self):
        mhs_total = 0.0
        mhs_av_total = 0.0        
        for m in self.machines:
            try:
                for g in m.call('devs')['DEVS']:
                    mhs_total += g['MHS 5s']
                    mhs_av_total += g['MHS av']
            except IOError:
                pass
        mhs_total *= 1024
        mhs_av_total *= 1024  
        return dict(rate=mhs_total, rate_av=mhs_av_total)

    def autoconf(self):
        return True

if __name__ == "__main__":
    BitHopperStat().run()

