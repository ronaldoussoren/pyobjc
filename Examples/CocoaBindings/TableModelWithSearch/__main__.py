#
#  __main__.py
#  TableModelWithSearch
#
#  Created by Bob Ippolito on Sun Apr 04 2004.
#  Copyright (c) 2004 Bob Ippolito. All rights reserved.
#

from PyObjCTools import AppHelper
from Foundation import NSProcessInfo

# import classes required to start application
import TableModelWithSearchAppDelegate
import ToolbarCreator
import FilteringArrayController

# start the event loop
AppHelper.runEventLoop(argv=[])
