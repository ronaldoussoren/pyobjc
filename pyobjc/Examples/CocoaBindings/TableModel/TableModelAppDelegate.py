#
#  TableModelAppDelegate.py
#  TableModel
#
#  Created by Bob Ippolito on Sun Apr 04 2004.
#  Copyright (c) 2004 Bob Ippolito. All rights reserved.
#

from Foundation import NSLog
from PyObjCTools import NibClassBuilder
import os

NibClassBuilder.extractClasses("MainMenu")
class TableModelAppDelegate(NibClassBuilder.AutoBaseClass):
    def applicationDidFinishLaunching_(self, aNotification):
        NSLog( "Application did finish launching." )
        
    def passwords(self):
        if not hasattr(self, '_cachedpasswords'):
            FIELDS = "name password uid gid class change expire gecos home_dir shell".split()
            self._cachedpasswords = [
                dict(zip(FIELDS, line.rstrip().split(':')))
                for line in os.popen('/usr/bin/nidump passwd .')
                if not line.startswith('#')
            ]
        return self._cachedpasswords
