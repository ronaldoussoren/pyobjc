#
#  __main__.py
#  GraphicsBindings
#
#  Created by Fred Flintstone on 11.02.05.
#  Copyright (c) 2005 __MyCompanyName__. All rights reserved.
#

from PyObjCTools import AppHelper
from Foundation import NSProcessInfo

import GraphicsBindingsDocument
import Circle
import GraphicsArrayController
import JoystickView
import GraphicsView

# start the event loop
import objc
objc.setVerbose(1)
AppHelper.runEventLoop(argv=[])
