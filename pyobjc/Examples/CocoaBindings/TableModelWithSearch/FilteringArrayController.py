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

NibClassBuilder.extractClasses("MainMenu")

class FilteringArrayController(NibClassBuilder.AutoBaseClass):
    searchString = None
    
    def arrangeObjects_(self, objects):
        if (not self.searchString) or (self.searchString == ""):
            return super(FilteringArrayController, self).arrangeObjects_(objects)

        newArrangement = []
        for o in objects: # there has to be a better way...
            for v in o.values():
                if v.find(self.searchString) is not -1:
                    newArrangement.append(o)
                    break
        
        return super(FilteringArrayController, self).arrangeObjects_(newArrangement)
    
    def performSearch_(self, sender):
        self.searchString = sender.stringValue()
        self.rearrangeObjects()
