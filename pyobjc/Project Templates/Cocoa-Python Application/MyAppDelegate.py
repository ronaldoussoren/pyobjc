#
#  MyAppDelegate.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

# import needed classes/functions from Foundation
from Foundation import NSObject, NSProcessInfo, NSFullUserName, NSLog

# import Nib loading functionality from AppKit
from AppKit import NibClassBuilder, NSApplicationDelegate
from AppKit.NibClassBuilder import AutoBaseClass

# create ObjC classes as defined in MainMenu.nib
NibClassBuilder.extractClasses("MainMenu")
class MyAppDelegate(AutoBaseClass, NSApplicationDelegate):
    """
    The application's delegate.

    An instance of this class is instantiated in the MainMenu.nib file
    to act as the Application's delegate and as the target of the
    sayHello: action.

    Note that by inheriting from AutoBaseClass, PyObjC will
    automatically define MyAppDelegate based on the definition of
    MyAppDelegate in MainMenu.nib.  The inheritance of this class will
    be determined by the class definition in the NIB and all outlets
    will automatically be defined.

    Action methods are not automatically defined as this follows the
    ObjC behavior;  the AppKit automatically prints a warning upon NIB
    loading if a target/action connection could not be made.
    """
    def sayHelloAction_(self, sender):
        """
        An example of a standard target action method implementation.
        """
        userName = NSFullUserName()
        hostName = NSProcessInfo.processInfo().hostName()
        helloString = "Hello %s @ %s!" % (userName, hostName)
    
        self.messageTextField.setStringValue_(helloString)
        NSLog( "Saying: %s" % helloString )
    
    def applicationDidFinishLaunching_(self, aNotification):
        """
        Invoked by NSApplication once the app is done launching and
        immediately before the first pass through the main event
        loop.
        """
        NSLog( "Application did finish launching." )
        self.messageTextField.setStringValue_("Click the button.")
