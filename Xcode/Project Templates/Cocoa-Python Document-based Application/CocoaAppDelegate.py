#
#  ÇPROJECTNAMEASIDENTIFIERÈAppDelegate.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

from Foundation import NSLog
from PyObjCTools import NibClassBuilder

NibClassBuilder.extractClasses("MainMenu")
class ÇPROJECTNAMEASIDENTIFIERÈAppDelegate(NibClassBuilder.AutoBaseClass):    
    def applicationDidFinishLaunching_(self, aNotification):
        NSLog( "Application did finish launching." )
