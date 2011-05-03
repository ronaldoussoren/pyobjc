from Foundation import *
import os, pwd

FIELDS = "name password uid gid class change expire gecos home_dir shell".split()
def getPasswords():
    a = NSMutableArray.array()
    for pw in pwd.getpwall():
        a.append({
            'name': pw.pw_name,
            'password': pw.pw_passwd,
            'uid': pw.pw_uid,
            'gid': pw.pw_gid,
            'gecos': pw.pw_gecos,
            'home_dir': pw.pw_dir,
            'shell': pw.pw_shell,
        })

    return a

class TableModelAppDelegate(NSObject):
    def passwords(self):
        if not hasattr(self, '_cachedpasswords'):
            self._cachedpasswords = getPasswords()
        return self._cachedpasswords
