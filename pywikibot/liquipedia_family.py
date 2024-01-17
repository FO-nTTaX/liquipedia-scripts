# -*- coding: utf-8 -*-
"""
This family file was auto-generated by $Id: b4675f8c1426906ff25dbf5dc703facd391360da $
Configuration parameters:
  url = https://liquipedia.net/starcraft2
  name = starcraft2
"""

from pywikibot import family
from pywikibot.tools import deprecated


class Family(family.Family):
    name = 'liquipedia'
    langs = {
        'ageofempires': 'liquipedia.net',
        'apexlegends': 'liquipedia.net',
        'arenafps': 'liquipedia.net',
        'arenaofvalor': 'liquipedia.net',
        'artifact': 'liquipedia.net',
        'autochess': 'liquipedia.net',
        'battalion': 'liquipedia.net',
        'battlerite': 'liquipedia.net',
        'brawlhalla': 'liquipedia.net',
        'brawlstars': 'liquipedia.net',
        'callofduty': 'liquipedia.net',
        'clashofclans': 'liquipedia.net',
        'clashroyale': 'liquipedia.net',
        'commons': 'liquipedia.net',
        'counterstrike': 'liquipedia.net',
        'criticalops': 'liquipedia.net',
        'crossfire': 'liquipedia.net',
        'dota2': 'liquipedia.net',
        'fifa': 'liquipedia.net',
        'fighters': 'liquipedia.net',
        'formula1': 'liquipedia.net',
        'fortnite': 'liquipedia.net',
        'freefire': 'liquipedia.net',
        'halo': 'liquipedia.net',
        'hearthstone': 'liquipedia.net',
        'heroes': 'liquipedia.net',
        'illuvium': 'liquipedia.net',
        'leagueoflegends': 'liquipedia.net',
        'magic': 'liquipedia.net',
        'mobilelegends': 'liquipedia.net',
        'naraka': 'liquipedia.net',
        'omegastrikers': 'liquipedia.net',
        'osu': 'liquipedia.net',
        'overwatch': 'liquipedia.net',
        'paladins': 'liquipedia.net',
        'pokemon': 'liquipedia.net',
        'projectx': 'liquipedia.net',
        'pubg': 'liquipedia.net',
        'pubgmobile': 'liquipedia.net',
        'rainbowsix': 'liquipedia.net',
        'rocketleague': 'liquipedia.net',
        'runeterra': 'liquipedia.net',
        'sideswipe': 'liquipedia.net',
        'simracing': 'liquipedia.net',
        'smite': 'liquipedia.net',
        'smash': 'liquipedia.net',
        'splatoon': 'liquipedia.net',
        'splitgate': 'liquipedia.net',
        'squadrons': 'liquipedia.net',
        'staff': 'liquipedia.net',
        'starcraft': 'liquipedia.net',
        'starcraft2': 'liquipedia.net',
        'stormgate': 'liquipedia.net',
        'teamfortress': 'liquipedia.net',
        'tetris': 'liquipedia.net',
        'tft': 'liquipedia.net',
        'trackmania': 'liquipedia.net',
        'underlords': 'liquipedia.net',
        'valorant': 'liquipedia.net',
        'warcraft': 'liquipedia.net',
        'wildrift': 'liquipedia.net',
        'worldoftanks': 'liquipedia.net',
        'worldofwarcraft': 'liquipedia.net',
        'zula': 'liquipedia.net',

        'sportscommons': 'sports.liquipedia.net',
        'football': 'sports.liquipedia.net',

        'fts': 'fonttax.wiki.tldev.eu',
    }

    def scriptpath(self, code):
        if code == 'fts':
            return '/teamfortress'
        if code == 'sportscommons':
            return '/commons'
        else:
            return '/' + code

    def protocol(self, code):
        if code == 'fts':
            return u'http'
        else:
            return u'https'

    def isPublic(self):
        return False
