#
#  __main__.py
#  TableModelWithSearch
#
#  Created by Bob Ippolito on Sun Apr 04 2004.
#  Copyright (c) 2004 Bob Ippolito. All rights reserved.
#

# import classes required to start application
import FilteringArrayController  # noqa: F401
import TableModelWithSearchAppDelegate  # noqa: F401
import ToolbarCreator  # noqa: F401
from PyObjCTools import AppHelper

# start the event loop
AppHelper.runEventLoop(argv=[])
