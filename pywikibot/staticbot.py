#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This bot allows the expansion of templates and then stores the result in a page

The following parameters are supported:

&params;

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
from pywikibot.bot import SingleSiteBot

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {
    '&params;': pagegenerators.parameterHelp
}


class StaticBot(SingleSiteBot):

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, generator, frompage, topage, **kwargs):
        """
        Constructor.

        Parameters:
            @param generator: The page generator that determines on which pages
                              to work.
            @type generator: generator.
        """
        super().__init__(generator=generator, **kwargs)

        self.frompage = frompage
        self.topage = topage

        # Set the edit summary message
        self.summary = u'Automatic conversion from dynamic page to static wikicode'

        self.opt.always = True

    def run(self):
        """Load the given page, does some changes, and saves it."""
        frompageobj = pywikibot.Page(self._site, self.frompage)
        frompageobj.touch()
        frompageobj._expanded_text = None
        topageobj = pywikibot.Page(self._site, self.topage)

        oldtext = topageobj.get()
        newtext = frompageobj.expand_text()
        newtext = newtext.replace('[[SMW::off]]', '').replace('[[SMW::on]]', '')

        if not self.save(oldtext, newtext, topageobj, self.summary):
            pywikibot.output(u'Page %s not saved.' % topageobj.title(asLink=True))

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
    # Process global arguments to determine desired site
    local_args = pywikibot.handle_args(args)
    genFactory = pagegenerators.GeneratorFactory()

    frompage = u''
    topage = u''

    # Parse command line arguments
    for arg in local_args:
        opt, _, value = arg.partition(':')
        if opt == '-from':
            frompage = value
        if opt == '-to':
            topage = value
        else:
            genFactory.handle_arg(arg)
    gen = genFactory.getCombinedGenerator()

    site = pywikibot.Site();
    site.login()

    bot = StaticBot(gen, frompage, topage)
    bot.run()

if __name__ == '__main__':
    main()
