#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
THIS BOT IS UNTESTED AND ASSUMED TO BE BROKEN

This bot gets a tournaments prizepool from smashgg and then stores the result in a page

The following parameters are supported:

&params;

-dry              If given, doesn't do any real changes, but only shows
                  what would have been changed.

-targetpage       Targetpage
-url              Url of the source smashgg page

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
import re

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}


class StaticBot:

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, dry, targetpagesingles, targetpagedoubles, url):
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

        self.url = url

        self.targetpagesingles = targetpagesingles
        self.targetpagedoubles = targetpagedoubles

        self.acceptall = True

        # Set the edit summary message
        self.site = pywikibot.Site()
        self.summary = u"Prize pool bot (url: " + url + ")"

    def run(self):
        """Load the given page, does some changes, and saves it."""
        targetpagesinglesobj = pywikibot.Page(self.site, self.targetpagesingles)
        targetpagedoublesobj = pywikibot.Page(self.site, self.targetpagedoubles)

        r = requests.get(url=self.url)
        if r.status_code == 200:
            text = r.text
            reg = re.compile('{"amount":(.*?),".*?},{"description":"\$(.*?) Doubles')
            result = reg.findall(text)
            print(result)
            singles = int(result[0][0])
            doubles = int(result[0][1].replace(',', ''))
            locale.setlocale(locale.LC_NUMERIC, '')
            singles = locale.format("%.*f", (0, singles), True)
            doubles = locale.format("%.*f", (0, doubles), True)
            print(singles)
            print(doubles)

            if not self.save(singles, targetpagesinglesobj, self.summary):
                pywikibot.output(u'Page %s not saved.' % targetpagesinglesobj.title(as_link=True))
            if not self.save(doubles, targetpagedoublesobj, self.summary):
                pywikibot.output(u'Page %s not saved.' % targetpagedoublesobj.title(as_link=True))

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
    targetpagesingles = u''
    targetpagedoubles = u''
    url = u''

    # Parse command line arguments
    for arg in local_args:
        if arg.startswith("-dry"):
            dry = True
        if arg.startswith("-targetpagesingles"):
            targetpagesingles = arg[len('-targetpagesingles:'):]
        if arg.startswith("-targetpagedoubles"):
            targetpagedoubles = arg[len('-targetpagedoubles:'):]
        if arg.startswith("-url"):
            url = arg[len('-url:'):]
        else:
            genFactory.handle_arg(arg)

    bot = StaticBot(dry, targetpagesingles, targetpagedoubles, url)
    bot.run()

if __name__ == "__main__":
    main()
