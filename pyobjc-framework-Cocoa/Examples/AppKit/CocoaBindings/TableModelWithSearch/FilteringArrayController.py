#
#  FilteringArrayController.py
#  TableModelWithSearch
#
#  Created by Bill Bumgarner on Sun Apr 04 2004.
#  Copyright (c) 2004 __MyCompanyName__. All rights reserved.
#

import re

import objc
from Cocoa import NSArrayController
from objc import super  # noqa: A004

kLiteralSearch = "Literal Search"
kRegularExpressionSearch = "Regular Expression Search"


def regexForSearchString(searchString, searchType):
    if not searchString:
        return None

    searchString = searchString.strip()
    if searchType == kLiteralSearch:
        searchString = re.escape(searchString.strip()) + r"(?i)"
    return re.compile(searchString)


def dictValueFilter(dicts, regex):
    for dct in dicts:
        for value in dct.values():
            if regex.search(value):
                yield dct
                break


class FilteringArrayController(NSArrayController):
    searchString = None
    lastRegex = None
    searchType = kLiteralSearch

    def arrangeObjects_(self, objects):
        supermethod = super().arrangeObjects_
        try:
            regex = regexForSearchString(self.searchString, self.searchType)
        except:  # noqa: E722, B001
            regex = self.lastRegex
        self.lastRegex = regex
        if regex is None:
            return supermethod(objects)
        return supermethod(list(dictValueFilter(objects, regex)))

    @objc.IBAction
    def performSearch_(self, sender):
        self.searchString = sender.stringValue()
        self.rearrangeObjects()

    @objc.IBAction
    def changeSearchType_(self, searchType):
        self.lastRegex = None
        self.searchString = None
        self.searchType = searchType
        self.rearrangeObjects()
