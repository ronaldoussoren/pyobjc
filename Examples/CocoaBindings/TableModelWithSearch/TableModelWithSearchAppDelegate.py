from Foundation import NSLog
from PyObjCTools import NibClassBuilder
import os

FIELDS = "name password uid gid class change expire gecos home_dir shell".split()
def getPasswords():
    return [
        dict(zip(FIELDS, line.rstrip().split(':')))
        for line in os.popen('/usr/bin/nidump passwd .')
        if not line.startswith('#')
    ]

NibClassBuilder.extractClasses("MainMenu")
class TableModelWithSearchAppDelegate(NibClassBuilder.AutoBaseClass):
    def passwords(self):
        if not hasattr(self, '_cachedpasswords'):
            self._cachedpasswords = getPasswords()
        return self._cachedpasswords
