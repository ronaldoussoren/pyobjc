#
#  MyAppDelegate.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

from objc import IBOutlet
from Foundation import NSObject, NSProcessInfo, NSFullUserName, NSLog

class MyAppDelegate (NSObject):
  messageTextField = IBOutlet("messageTextField")
  
  def sayHelloAction_(self, sender):
    userName = NSFullUserName()
    hostName = NSProcessInfo.processInfo().hostName()
    helloString = "Hello %s @ %s!" % (userName, hostName)
    
    self.messageTextField.setStringValue_( helloString )
    NSLog( "Saying: %s" % helloString )
    
  def applicationDidFinishLaunching_(self, aNotification):
    NSLog( "Application did finish launching." )
