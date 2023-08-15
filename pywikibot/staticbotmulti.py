#!/usr/bin/python
# -*- coding: utf-8  -*-
r"""
This bot allows the expansion of templates and then stores the result in a page

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
from pywikibot.exceptions import LockedPageError

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}


class StaticBotMulti(SingleSiteBot):

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, generator, pages, **kwargs):
        """
        Constructor.

        Parameters:
            @param generator: The page generator that determines on which pages
                              to work.
            @type generator: generator.
            @param pages: List of pages to be edited
            @type pages: list.
        """
        super().__init__(generator=generator, **kwargs)

        self.pages = pages

        # Set the edit summary message
        self.summary = u'Automatic conversion from dynamic page to static wikicode'

        self.opt.always = True

    def run(self):
        """Load the given page, does some changes, and saves it."""
        for i in range(len(self.pages)):
            try:
                frompageobj = pywikibot.Page(self._site, self.pages[i] + '/dynamic')
                frompageobj.touch()
                frompageobj._expanded_text = None
                topageobj = pywikibot.Page(self._site, self.pages[i])

                oldtext = topageobj.get()
                newtext = frompageobj.expand_text()
                newtext = newtext.replace('[[SMW::off]]', '').replace('[[SMW::on]]', '')

                if not self.save(oldtext, newtext, topageobj, self.summary):
                    pywikibot.output(u'Page %s not saved.' % topageobj.title(as_link=True))
            except LockedPageError:
                pywikibot.output('Page {} is locked'.format(topageobj.title()))
        try:
            mainpageobj = pywikibot.Page(self._site, u'Main Page')
            mainpageobj.purge()
            mainpageobj.touch()
        except LockedPageError:
            pywikibot.output('Page {} is locked'.format(mainpageobj.title()))

    def save(self, oldtext, newtext, page, summary=None, minor=True,
            botflag=True, **kwargs):
        return self.userPut(page, oldtext, newtext,
            summary=summary,
            ignore_save_related_errors=True, minor=True,
            botflag=True, asynchronous=False, **kwargs)


def main(*args):
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: list of unicode
    """
    options = {}

    # Process global arguments to determine desired site
    local_args = pywikibot.handle_args(args)
    genFactory = pagegenerators.GeneratorFactory()

    pages = []

    # Parse command line arguments
    for arg in local_args:
        opt, _, value = arg.partition(':')
        if genFactory.handle_arg(arg):
            continue
        else:
            pages.append(arg)
    gen = genFactory.getCombinedGenerator()

    site = pywikibot.Site();
    site.login()

    bot = StaticBotMulti(gen, pages, **options)
    bot.run()

if __name__ == "__main__":
    main()
