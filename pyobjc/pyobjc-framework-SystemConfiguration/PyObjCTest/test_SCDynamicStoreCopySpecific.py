from PyObjCTools.TestSupport import *

from SystemConfiguration import *

class TestSCDynamicStoreCopySpecific (TestCase):
    def testFunctions(self):
        def callback(st, keys, info):
            pass

        st = SCDynamicStoreCreate(None, "pyobjc.test", callback, None)
        self.failUnless(isinstance(st, SCDynamicStoreRef))

        nm, encoding = SCDynamicStoreCopyComputerName(st, None)
        self.failUnless(isinstance(nm, unicode))
        self.failUnless(isinstance(encoding, (int, long)))

        nm, uid, gid = SCDynamicStoreCopyConsoleUser(st, None, None)
        self.failUnless(isinstance(nm, unicode))
        self.failUnless(isinstance(uid, (int, long)))
        self.failUnless(isinstance(gid, (int, long)))

        nm = SCDynamicStoreCopyLocalHostName(st)
        self.failUnless(isinstance(nm, unicode))

        nm = SCDynamicStoreCopyLocation(st)
        self.failUnless(isinstance(nm, unicode))

        r = SCDynamicStoreCopyProxies(st)
        self.failUnless(r is None or isinstance(r, CFDictionaryRef))


if __name__ == "__main__":
    main()
