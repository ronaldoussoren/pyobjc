#
#  MyAppDelegate.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

from Foundation import *

# import Nib loading functionality from AppKit
from AppKit import NSApplicationDelegate
from PyObjCTools import NibClassBuilder

# create ObjC classes as defined in MainMenu.nib
NibClassBuilder.extractClasses("MainMenu")
class MyAppDelegate(NibClassBuilder.AutoBaseClass, NSApplicationDelegate):
    """
    Application delegate.
    """
    def changeHueAction_(self, sender):
        """
        An example of a standard target action method implementation.
        """
        newHue = self.hueSlider.floatValue()
        self.hueView.setHue_(newHue)
    
    def awakeFromNib(self):
        """
        awakeFromNib() is invoked when the NIB that caused this object to be instantiated is loaded (MainMenu.nib).
        """
        self.changeHueAction_(None)
