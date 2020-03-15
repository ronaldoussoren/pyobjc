#
#  __main__.py
#  GraphicsBindings
#
#  Created by Fred Flintstone on 11.02.05.
#  Copyright (c) 2005 __MyCompanyName__. All rights reserved.
#

import Circle  # noqa: F401
import GraphicsArrayController  # noqa: F401
import GraphicsBindingsDocument  # noqa: F401
import GraphicsView  # noqa: F401
import JoystickView  # noqa: F401

# start the event loop
import objc
from PyObjCTools import AppHelper

objc.setVerbose(1)
AppHelper.runEventLoop(argv=[])
