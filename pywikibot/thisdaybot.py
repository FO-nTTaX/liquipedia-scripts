#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This bot creates 'this day' pages on Liquipedia

The following parameters are supported:

&params;

-dry              If given, doesn't do any real changes, but only shows
                  what would have been changed.

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

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}


class ThisDayBot:

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, dry, frompage, topage):
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

        self.acceptall = True

        # Set the edit summary message
        self.site = pywikibot.Site()
        self.summary = u"Generating 'This day' pages"

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
            monthtext = "{{DISPLAYTITLE:" + monthnames[str(i)] + "}}\n";
            for j in range(1, monthlengths[str(i)] + 1):
                daytext = "__NOTOC__{{This day|year="
                if((i == 2) and (j == 29)):
                    daytext += "{{#expr:{{CURRENTYEAR}} + 4 - ({{CURRENTYEAR}} mod 4)}}"
                else:
                    daytext += "{{CURRENTYEAR}}"
                daytext += "|month=" + str(i).zfill(2) + "|day=" + str(j).zfill(2) + "}}\n\n<!--<h3>Trivia</h3>--><!--uncomment this heading and add trivia as bullet points-->";
                if((i == 2) and (j == 28)):
                    daytext += "\n\n{{#ifeq:{{#time:L}}|0|<h2>February 29th</h2>{{Liquipedia:This day/2/29}}}}";
                daytext += "\n\n<noinclude>[[Category:This day]]</noinclude>"
                pagename = "Liquipedia:This day/" + str(i) + "/" + str(j)
                pageobj = pywikibot.Page(self.site, pagename)
                pageobj._expanded_text = None
                if not self.save(daytext, pageobj, self.summary):
                    pywikibot.output(u'Page %s not saved.' % topageobj.title(asLink=True))
                if((i == 2) and (j == 29)):
                    monthtext += "{{#ifeq:{{#time:L}}|1|<h2>" + monthnames[str(i)] + " " + self.get_ordinal(j) + "</h2>{{Liquipedia:This day/" + str(i) + "/" + str(j) + "}}}}\n";
                else:
                    monthtext += "<h2>" + monthnames[str(i)] + " " + self.get_ordinal(j) + "</h2>{{Liquipedia:This day/" + str(i) + "/" + str(j) + "}}\n";
            monthtext += "\n\n<noinclude>[[Category:This day]]</noinclude>"
            pagename = "Liquipedia:This day/" + str(i)
            pageobj = pywikibot.Page(self.site, pagename)
            pageobj._expanded_text = None
            if not self.save(monthtext, pageobj, self.summary):
                pywikibot.output(u'Page %s not saved.' % topageobj.title(asLink=True))

    def load(self, page):
        """Load the text of the given page."""
        try:
            # Load the page
            text = page.get()
        except pywikibot.NoPage:
            pywikibot.output(u"Page %s does not exist; skipping."
                             % page.title(asLink=True))
        except pywikibot.IsRedirectPage:
            pywikibot.output(u"Page %s is a redirect; skipping."
                             % page.title(asLink=True))
        else:
            return text
        return None

    def save(self, text, page, comment=None, minorEdit=True,
             botflag=True):
        """Update the given page with new text."""
        # only save if something was changed
        if True:
            # Show the title of the page we're working on.
            # Highlight the title in purple.
            pywikibot.output(u"\n\n>>> \03{lightpurple}%s\03{default} <<<"
                             % page.title())
            # show what was changed
            #pywikibot.showDiff(page.get(), text)
            pywikibot.output(u'Comment: %s' % comment)
            if not self.dry:
                try:
                    page.text = text
                    # Save the page
                    page.save(summary=comment or self.comment,
                              minor=minorEdit, botflag=botflag)
                except pywikibot.LockedPage:
                    pywikibot.output(u"Page %s is locked; skipping."
                                     % page.title(asLink=True))
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
    frompage = u''
    topage = u''

    # Parse command line arguments
    for arg in local_args:
        if arg.startswith("-dry"):
            dry = True
        else:
            genFactory.handleArg(arg)

    bot = ThisDayBot(dry, frompage, topage)
    bot.run()

if __name__ == "__main__":
    main()
