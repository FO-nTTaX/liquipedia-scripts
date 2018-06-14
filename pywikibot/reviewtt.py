#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This bot allows the expansion of templates and then stores the result in a page

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


class ReviewTTBot:

    """This bot allows the expansion of templates and then stores the result in a page"""

    def __init__(self, dry):
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
        self.summary = u"Automatic conversion from dynamic page to static wikicode"

    def run(self):
        self.site.login()
        params = {
            'action': 'query',
            'list': 'oldreviewedpages',
            'ornamespace': 10,
            'orlimit': 500,
        }
        revrequest = self.site._simple_request(**params)
        revrequestdata = revrequest.submit()
        if 'query' in revrequestdata:
            if 'oldreviewedpages' in revrequestdata["query"]:
                for page in revrequestdata["query"]["oldreviewedpages"]:
                    title = page["title"]
                    if title.startswith("Template:Team/") or title.startswith("Template:Team2/") or title.startswith("Template:TeamShort/") or title.startswith("Template:Team2Short/") or title.startswith("Template:TeamIcon/") or title.startswith("Template:TeamPart/") or title.startswith("Template:TeamBracket/") or title.startswith("Template:TeamPage/"):
                        pywikibot.output("Reviewing page: " + title)
                        params = {
                            'action': 'query',
                            'meta': 'tokens',
                        }
                        tokenrequest = self.site._simple_request(**params)
                        tokenrequestdata = tokenrequest.submit()
                        revtoken = tokenrequestdata["query"]["tokens"]["csrftoken"]
                        revid = page["revid"]
                        params = {
                            'action': 'review',
                            'revid': revid,
                            'flag_accuracy': 1,
                            'comment': "team template",
                            'token': revtoken,
                        }
                        reviewrequest = self.site._simple_request(**params)
                        reviewrequestdata = reviewrequest.submit()
        params = {
            'action': 'query',
            'list': 'unreviewedpages',
            'urnamespace': 10,
            'urlimit': 500,
            'urstart': 'Team',
        }
        revrequest = self.site._simple_request(**params)
        revrequestdata = revrequest.submit()
        if 'query' in revrequestdata:
            if 'unreviewedpages' in revrequestdata["query"]:
                for page in revrequestdata["query"]["unreviewedpages"]:
                    title = page["title"]
                    if title.startswith("Template:Team/") or title.startswith("Template:Team2/") or title.startswith("Template:TeamShort/") or title.startswith("Template:Team2Short/") or title.startswith("Template:TeamIcon/") or title.startswith("Template:TeamPart/") or title.startswith("Template:TeamBracket/") or title.startswith("Template:TeamPage/"):
                        pywikibot.output("Reviewing page: " + title)
                        params = {
                            'action': 'query',
                            'meta': 'tokens',
                        }
                        tokenrequest = self.site._simple_request(**params)
                        tokenrequestdata = tokenrequest.submit()
                        revtoken = tokenrequestdata["query"]["tokens"]["csrftoken"]
                        revid = page["revid"]
                        params = {
                            'action': 'review',
                            'revid': revid,
                            'flag_accuracy': 1,
                            'comment': "team template",
                            'token': revtoken,
                        }
                        reviewrequest = self.site._simple_request(**params)
                        reviewrequestdata = reviewrequest.submit()

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

    # Parse command line arguments
    for arg in local_args:
        if arg.startswith("-dry"):
            dry = True
        else:
            genFactory.handleArg(arg)

    bot = ReviewTTBot(dry)
    bot.run()

if __name__ == "__main__":
    main()
