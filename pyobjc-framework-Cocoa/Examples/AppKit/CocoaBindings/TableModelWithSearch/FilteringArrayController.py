#
#  FilteringArrayController.py
#  TableModelWithSearch
#
#  Created by Bill Bumgarner on Sun Apr 04 2004.
#  Copyright (c) 2004 __MyCompanyName__. All rights reserved.
#

from objc import YES, NO
from Foundation import *
from AppKit import *
from PyObjCTools import NibClassBuilder
import re

NibClassBuilder.extractClasses("MainMenu")

kLiteralSearch = u'Literal Search'
kRegularExpressionSearch = u'Regular Expression Search'

def regexForSearchString(searchString, searchType):
    if not searchString:
        return None

    searchString = searchString.strip()
    if searchType == kLiteralSearch:
        searchString = re.escape(searchString.strip()) + ur'(?i)'
    return re.compile(searchString)

def dictValueFilter(dicts, regex):
    for dct in dicts:
        for value in dct.itervalues():
            if regex.search(value):
                yield dct
                break

class FilteringArrayController(NibClassBuilder.AutoBaseClass):
    searchString = None
    lastRegex = None
    searchType = kLiteralSearch

    def arrangeObjects_(self, objects):
        supermethod = super(FilteringArrayController, self).arrangeObjects_
        try:
            regex = regexForSearchString(self.searchString, self.searchType)
        except:
            regex = self.lastRegex
        self.lastRegex = regex
        if regex is None:
            return supermethod(objects)
        return supermethod(list(dictValueFilter(objects, regex)))

    def performSearch_(self, sender):
        self.searchString = sender.stringValue()
        self.rearrangeObjects()

    def changeSearchType_(self, searchType):
        self.lastRegex = None
        self.searchString = None
        self.searchType = searchType
        self.rearrangeObjects()
