#!/usr/bin/env python

from munin import MuninPlugin
import json
import urllib2

class BitHopperStat(MuninPlugin):
    title = "BitHopper Mining Status"
    category = "bitcoin"
    args = "--base 1000 -l 0"
    vlabel = "Mhash/s"
    info = "This graph shows the current mining speed of a local BitHopper server."
    fields = (
            ('rate',dict(
                label = "rate",
                info = "Current mining speed",
                type = "GAUGE",
            )),
    )

    def __init__(self):
        super(BitHopperStat, self).__init__()
        self.url_bh = 'http://lueo.dyndns.org:8337/data'
        self.content_bh = urllib2.urlopen(self.url_bh)
        self.url_p2pool = 'http://lueo.dyndns.org:9332/local_stats'
        self.content_p2pool = urllib2.urlopen(self.url_p2pool)
        self.data_bh=json.load(self.content_bh)
        self.data_p2pool = json.load(self.content_p2pool)

    def execute(self):
        rate_bh = self.data_bh['mhash']
        rate_p2pool = 0.0
        for machine in self.data_p2pool['miner_hash_rates']:
            rate_p2pool += self.data_p2pool['miner_hash_rates'][machine]
        rate = rate_bh + rate_p2pool/1024
        return dict(rate=rate)

    def autoconf(self):
        return bool(self.content)

if __name__ == "__main__":
    BitHopperStat().run()

