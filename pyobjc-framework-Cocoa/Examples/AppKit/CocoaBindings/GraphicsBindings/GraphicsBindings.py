#
#  __main__.py
#  GraphicsBindings
#
#  Created by Fred Flintstone on 11.02.05.
#  Copyright (c) 2005 __MyCompanyName__. All rights reserved.
#

import Circle
import GraphicsArrayController
import GraphicsBindingsDocument
import GraphicsView
import JoystickView

# start the event loop
import objc
from Foundation import NSProcessInfo
from PyObjCTools import AppHelper

objc.setVerbose(1)
AppHelper.runEventLoop(argv=[])
