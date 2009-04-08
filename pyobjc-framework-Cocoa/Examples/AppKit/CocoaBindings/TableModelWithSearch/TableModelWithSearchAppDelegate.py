from Foundation import *
import os, pwd


def getPasswords():
    a = NSMutableArray.array()
    for pw in pwd.getpwall():
        a.append({
            'name': pw.pw_name,
            'password': pw.pw_passwd,
            'uid': str(pw.pw_uid),
            'gid': str(pw.pw_gid),
            'gecos': pw.pw_gecos,
            'home_dir': pw.pw_dir,
            'shell': pw.pw_shell,
        })

    return a

class TableModelWithSearchAppDelegate (NSObject):
    def passwords(self):
        if not hasattr(self, '_cachedpasswords'):
            self._cachedpasswords = getPasswords()
        return self._cachedpasswords
