#
#  Main.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ.  All rights reserved.
#

# import PyObjC
import objc
import Foundation
import AppKit

# import classes required to start application
## note that MyAppDelegate resides in the embedded fraemwork.   When Foundation is imported above, it automatically dynamically loads the framework and adds the framework to the python search path.
import MyAppDelegate
import MyDocument

# pass control to the AppKit
import sys
sys.exit(AppKit.NSApplicationMain(sys.argv))
