#
#  __main__.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
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
import ÇPROJECTNAMEASIDENTIFIERÈAppDelegate

# start the event loop
AppHelper.runEventLoop(argv=[])
