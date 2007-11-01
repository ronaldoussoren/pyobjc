#
#  ÇPROJECTNAMEASIDENTIFIERÈAppDelegate.py
#  ÇPROJECTNAMEASIDENTIFIERÈ
#

from Foundation import *
from AppKit import *
from ÇPROJECTNAMEASIDENTIFIERÈPlugIn import *

from PyObjCTools import NibClassBuilder

class ÇPROJECTNAMEASIDENTIFIERÈAppDelegate(NibClassBuilder.AutoBaseClass):

    def applicationDidFinishLaunching_(self, sender):
        if ÇPROJECTNAMEASIDENTIFIERÈPlugIn.alloc().init().plugInLoaded():
            NSLog(u'Objective-C Plug-In Loaded!')
            NSBeep()
