#
#  Main.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

from PyObjCTools import AppHelper

# import classes required to start application
## note that MyAppDelegate resides in the embedded framework.   When Foundation
## is imported above, it automatically dynamically loads the framework and adds
## the framework to the python search path.
import MyAppDelegate

# start the event loop
AppHelper.runEventLoop()
