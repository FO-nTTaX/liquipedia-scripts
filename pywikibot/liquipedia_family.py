# -*- coding: utf-8 -*-


from pywikibot import family
import json
import requests


class Family(family.Family):

    @classmethod
    def __post_init__(self):
        response = requests.get('https://liquipedia.net/api.php?action=listwikis', headers={'accept-encoding': 'gzip'})
        wikis = json.loads(response.content)
        for game in wikis['allwikis'].keys():
            self.langs[game] = 'liquipedia.net'

    name = 'liquipedia'

    def scriptpath(self, code):
        return '/' + code

    def protocol(self, code):
        return u'https'
