#
#  __main__.py
#  GraphicsBindings
#
#  Created by Fred Flintstone on 11.02.05.
#  Copyright (c) 2005 __MyCompanyName__. All rights reserved.
#

try:
    # scan for pth files that made it into the bundle
    import os, site
    site.addsitedir(os.path.dirname(os.path.realpath(__file__)))
except ImportError:
    pass

from PyObjCTools import AppHelper
from Foundation import NSProcessInfo

# import classes required to start application
#import GraphicsBindingsAppDelegate
import GraphicsBindingsDocument
import Circle
import GraphicsArrayController
import JoystickView
import GraphicsView

# start the event loop
AppHelper.runEventLoop(argv=[])
