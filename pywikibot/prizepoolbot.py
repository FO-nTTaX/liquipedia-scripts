#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
THIS BOT IS UNTESTED AND ASSUMED TO BE BROKEN

This bot gets a tournaments prizepool and then stores the result in a page

The following parameters are supported:

&params;

-dry              If given, doesn't do any real changes, but only shows
                  what would have been changed.

-targetpage       Targetpage
-leagueid         League ID in the Dota API
-valveapikey      API key for valves API

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

import requests
import locale

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}


class PrizePoolBot:

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, dry, targetpage, leagueid, valveapikey):
        """
        Constructor.

        Parameters:
            @param generator: The page generator that determines on which pages
                              to work.
            @type generator: generator.
            @param dry: If True, doesn't do any real changes, but only shows
                        what would have been changed.
            @type dry: boolean.
        """
        self.dry = dry

        self.valveapikey = valveapikey
        self.leagueid = leagueid

        self.targetpage = targetpage

        self.acceptall = True

        # Set the edit summary message
        self.site = pywikibot.Site()
        self.summary = u"Prize pool bot (leagueid: " + leagueid + ")"

    def run(self):
        """Load the given page, does some changes, and saves it."""
        targetpageobj = pywikibot.Page(self.site, self.targetpage)

        r = requests.get(url='https://api.steampowered.com/IEconDOTA2_570/GetTournamentPrizePool/v1?key=' + self.valveapikey + '&leagueid=' + self.leagueid)
        h = r.json()
        text = h['result']['prize_pool']
        locale.setlocale(locale.LC_NUMERIC, '')
        text = locale.format("%.*f", (0, text), True)
        print(text)

        if not self.save(text, targetpageobj, self.summary):
            pywikibot.output(u'Page %s not saved.' % targetpageobj.title(as_link=True))

    def load(self, page):
        """Load the text of the given page."""
        try:
            # Load the page
            text = page.get()
        except pywikibot.NoPage:
            pywikibot.output(u"Page %s does not exist; skipping."
                             % page.title(as_link=True))
        except pywikibot.IsRedirectPage:
            pywikibot.output(u"Page %s is a redirect; skipping."
                             % page.title(as_link=True))
        else:
            return text
        return None

    def save(self, text, page, comment=None, minor=True,
             botflag=True):
        """Update the given page with new text."""
        # only save if something was changed
        if text != page.get():
            # Show the title of the page we're working on.
            # Highlight the title in purple.
            pywikibot.output(u"\n\n>>> \03{lightpurple}%s\03{default} <<<"
                             % page.title())
            # show what was changed
            pywikibot.showDiff(page.get(), text)
            pywikibot.output(u'Comment: %s' % comment)
            if not self.dry:
                try:
                    page.text = text
                    # Save the page
                    page.save(summary=comment or self.comment,
                              minor=minor, botflag=botflag)
                except pywikibot.LockedPage:
                    pywikibot.output(u"Page %s is locked; skipping."
                                     % page.title(as_link=True))
                except pywikibot.EditConflict:
                    pywikibot.output(
                        u'Skipping %s because of edit conflict'
                        % (page.title()))
                except pywikibot.SpamfilterError as error:
                    pywikibot.output(
                        u'Cannot change %s because of spam blacklist entry %s'
                        % (page.title(), error.url))
                else:
                    return True
        return False


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

    # If dry is True, doesn't do any real changes, but only show
    # what would have been changed.
    dry = False
    targetpage = u''
    leagueid = u''
    valveapikey = u''

    # Parse command line arguments
    for arg in local_args:
        if arg.startswith("-dry"):
            dry = True
        if arg.startswith("-targetpage"):
            targetpage = arg[len('-targetpage:'):]
        if arg.startswith("-leagueid"):
            leagueid = arg[len('-leagueid:'):]
        if arg.startswith("-valveapikey"):
            valveapikey = arg[len('-valveapikey:'):]
        else:
            genFactory.handle_arg(arg)

    site = pywikibot.Site();
    site.login()

    bot = PrizePoolBot(dry, targetpage, leagueid, valveapikey)
    bot.run()

if __name__ == "__main__":
    main()
