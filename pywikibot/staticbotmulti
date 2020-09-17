#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This bot allows the expansion of templates and then stores the result in a page

The following parameters are supported:

&params;

-dry              If given, doesn't do any real changes, but only shows
                  what would have been changed.

-from             Sourcepage

-to               Targetpage

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


class StaticBotMulti:

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, dry, pages):
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

        self.pages = pages

        self.acceptall = True

        # Set the edit summary message
        self.site = pywikibot.Site()
        self.summary = u"Automatic conversion from dynamic page to static wikicode"

    def run(self):
        """Load the given page, does some changes, and saves it."""
        for i in range(len(self.pages)):
            frompageobj = pywikibot.Page(self.site, self.pages[i] + '/dynamic')
            frompageobj.touch()
            frompageobj._expanded_text = None
            topageobj = pywikibot.Page(self.site, self.pages[i])

            text = frompageobj.expand_text()
            text = text.replace("[[SMW::off]]", "").replace("[[SMW::on]]", "")

            if not self.save(text, topageobj, self.summary):
                pywikibot.output(u'Page %s not saved.' % topageobj.as_link())
        mainpageobj = pywikibot.Page(self.site, u"Main Page")
        mainpageobj.touch()

    def load(self, page):
        """Load the text of the given page."""
        try:
            # Load the page
            text = page.get()
        except pywikibot.NoPage:
            pywikibot.output(u"Page %s does not exist; skipping."
                             % page.as_link())
        except pywikibot.IsRedirectPage:
            pywikibot.output(u"Page %s is a redirect; skipping."
                             % page.as_link())
        else:
            return text
        return None

    def save(self, text, page, comment=None, minorEdit=True,
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
                              minor=minorEdit, botflag=botflag)
                except pywikibot.LockedPage:
                    pywikibot.output(u"Page %s is locked; skipping."
                                     % page.as_link())
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
    pages = []

    # Parse command line arguments
    for arg in local_args:
        if genFactory.handleArg(arg):
            continue
        if arg.startswith("-dry"):
            dry = True
        else:
            pages.append(arg)

    bot = StaticBotMulti(dry, pages)
    bot.run()

if __name__ == "__main__":
    main()
