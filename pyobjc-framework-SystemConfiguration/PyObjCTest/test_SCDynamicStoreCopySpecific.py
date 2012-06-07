from PyObjCTools.TestSupport import *

from SystemConfiguration import *

try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

class TestSCDynamicStoreCopySpecific (TestCase):
    def testFunctions(self):
        def callback(st, keys, info):
            pass

        st = SCDynamicStoreCreate(None, "pyobjc.test", callback, None)
        self.assertTrue(isinstance(st, SCDynamicStoreRef))

        nm, encoding = SCDynamicStoreCopyComputerName(st, None)
        self.assertTrue(isinstance(nm, unicode))
        self.assertTrue(isinstance(encoding, (int, long)))

        nm, uid, gid = SCDynamicStoreCopyConsoleUser(st, None, None)
        self.assertTrue(isinstance(nm, unicode))
        self.assertTrue(isinstance(uid, (int, long)))
        self.assertTrue(isinstance(gid, (int, long)))

        nm = SCDynamicStoreCopyLocalHostName(st)
        self.assertTrue(isinstance(nm, unicode))

        nm = SCDynamicStoreCopyLocation(st)
        self.assertTrue(isinstance(nm, unicode))

        r = SCDynamicStoreCopyProxies(st)
        self.assertTrue(r is None or isinstance(r, CFDictionaryRef))


if __name__ == "__main__":
    main()
