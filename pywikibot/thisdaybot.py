#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This bot creates the This Day pages on Liquipedia

"""
#
# (C) Pywikibot team, 2006-2014
#
# Distributed under the terms of the MIT license.
#
from __future__ import unicode_literals

__version__ = '$Id: 23dac2badba93914592c50e95d72c53d7d2d7ea7 $'
#

import pywikibot
from pywikibot import pagegenerators
from pywikibot import i18n
from pywikibot.bot import SingleSiteBot

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}


class ThisDayBot(SingleSiteBot):

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, generator, **kwargs):
        """
        Constructor.

        Parameters:
            @param generator: The page generator that determines on which pages
                              to work.
            @type generator: generator.
        """
        super().__init__(generator=generator, **kwargs)

        self.acceptall = True

        # Set the edit summary message
        self.site = pywikibot.Site()
        self.site.login()
        self.summary = u'Generating \'This day\' pages'

    def get_ordinal(self, n):
        if((n == 1) or (n == 21) or (n == 31)):
            return str(n) + 'st'
        elif((n == 2) or (n == 22)):
            return str(n) + 'nd'
        elif((n == 3) or (n == 23)):
            return str(n) + 'rd'
        else:
            return str(n) + 'th'
    def run(self):
        monthlengths = {
            '1': 31,
            '2': 29,
            '3': 31,
            '4': 30,
            '5': 31,
            '6': 30,
            '7': 31,
            '8': 31,
            '9': 30,
            '10': 31,
            '11': 30,
            '12': 31
        }
        monthnames = {
            '1': 'January',
            '2': 'February',
            '3': 'March',
            '4': 'April',
            '5': 'May',
            '6': 'June',
            '7': 'July',
            '8': 'August',
            '9': 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December'
        }
        for i in range(1, 13):
            monthtext = '{{DISPLAYTITLE:' + monthnames[str(i)] + '}}\n';
            for j in range(1, monthlengths[str(i)] + 1):
                daytext = '__NOTOC__{{This day|year='
                if((i == 2) and (j == 29)):
                    daytext += '{{#expr:{{CURRENTYEAR}} + 4 - ({{CURRENTYEAR}} mod 4)}}'
                else:
                    daytext += '{{CURRENTYEAR}}'
                daytext += '|month=' + str(i).zfill(2) + '|day=' + str(j).zfill(2) + '}}\n\n<!--<h3>Trivia</h3>--><!--uncomment this heading and add trivia as bullet points-->';
                if((i == 2) and (j == 28)):
                    daytext += '\n\n{{#ifeq:{{#time:L}}|0|<h2>February 29th</h2>{{Liquipedia:This day/2/29}}}}';
                pagename = 'Liquipedia:This day/' + str(i) + '/' + str(j)
                pageobj = pywikibot.Page(self.site, pagename)
                pageobj._expanded_text = None
                if not self.save('', daytext, pageobj, self.summary):
                    pywikibot.output(u'Page %s not saved.' % pageobj.title(as_link=True))
                if((i == 2) and (j == 29)):
                    monthtext += '{{#ifeq:{{#time:L}}|1|<h2>' + monthnames[str(i)] + ' ' + self.get_ordinal(j) + '</h2>{{Liquipedia:This day/' + str(i) + '/' + str(j) + '}}}}\n';
                else:
                    monthtext += '<h2>' + monthnames[str(i)] + ' ' + self.get_ordinal(j) + '</h2>{{Liquipedia:This day/' + str(i) + '/' + str(j) + '}}\n';
            pagename = 'Liquipedia:This day/' + str(i)
            pageobj = pywikibot.Page(self.site, pagename)
            pageobj._expanded_text = None
            if not self.save('', monthtext, pageobj, self.summary):
                pywikibot.output(u'Page %s not saved.' % pageobj.title(as_link=True))

    def save(self, oldtext, newtext, page, summary=None, minor=True,
            bot=True, **kwargs):
        return self.userPut(page, oldtext, newtext,
            summary=summary,
            ignore_save_related_errors=True, minor=True,
            bot=True, asynchronous=False, **kwargs)


def main(*args):
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: list of unicode
    """
    # Process global arguments to determine desired site
    local_args = pywikibot.handle_args(args)
    genFactory = pagegenerators.GeneratorFactory()

    # Parse command line arguments
    for arg in local_args:
        genFactory.handleArg(arg)
    gen = genFactory.getCombinedGenerator()

    site = pywikibot.Site();
    site.login()

    bot = ThisDayBot(gen)
    bot.run()

if __name__ == '__main__':
    main()
