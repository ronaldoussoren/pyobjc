#
#  MyAppDelegate.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

from objc import YES, NO

from AppKit import NibClassBuilder, NSApplicationDelegate
from AppKit.NibClassBuilder import AutoBaseClass

# create ObjC classes as defined in MainMenu.nib
NibClassBuilder.extractClasses("MainMenu")
class MyAppDelegate(AutoBaseClass, NSApplicationDelegate):
    def applicationShouldOpenUntitledFile_(self, sender):
        # return NO if you don't want untitled document to be opened on app launch
        return YES

