#
#  Main.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

# 
# Upon an installation build, the project copies the PyObjC modules
# into the 'pyobjc' directory within the Resources directory of
# the app wrapper.  The following adjusts sys.path to include that
# directory.
#
import sys
import os.path
sys.path.insert(0, os.path.join(sys.path[0], "pyobjc"))

#
# Import the components of the Python<->ObjC bridge.
#
import objc
import Foundation
import AppKit

#
# Import application specific componentry.  At the least, all
# classes necessary to load the main NIB file must be loaded here.
#
import MyAppDelegate

#
# Pass control to the Appkit.
#
# From this point on, application intiailization, execution and
# termination works exactly like any other Cocoa application.
#
sys.exit( AppKit.NSApplicationMain(sys.argv) )
