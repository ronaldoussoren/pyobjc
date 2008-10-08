from Foundation import NSLog, NSMutableArray
import os

FIELDS = "name password uid gid class change expire gecos home_dir shell".split()
def getPasswords():
    return NSMutableArray.arrayWithArray_([
        dict(zip(FIELDS, line.rstrip().split(':')))
        for line in os.popen('/usr/bin/nidump passwd .')
        if not line.startswith('#')
    ])


class TableModelAppDelegate (NSObject):
    def passwords(self):
        if not hasattr(self, '_cachedpasswords'):
            self._cachedpasswords = getPasswords()
        return self._cachedpasswords

    @objc.IBAction
    def insertRecord_(self, sender):
        passwords = self.passwords()

        self.willChangeValueForKey_('passwords')
        passwords.append(dict(zip(FIELDS, FIELDS)))
        self.didChangeValueForKey_('passwords')
