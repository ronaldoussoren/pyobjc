#
#  __main__.py
#  TableModelWithSearch
#
#  Created by Bob Ippolito on Sun Apr 04 2004.
#  Copyright (c) 2004 Bob Ippolito. All rights reserved.
#

import FilteringArrayController

# import classes required to start application
import TableModelWithSearchAppDelegate
import ToolbarCreator
from Foundation import NSProcessInfo
from PyObjCTools import AppHelper

# start the event loop
AppHelper.runEventLoop(argv=[])
