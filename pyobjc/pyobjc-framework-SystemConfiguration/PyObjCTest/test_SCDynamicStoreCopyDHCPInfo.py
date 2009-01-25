from PyObjCTools.TestSupport import *

from SystemConfiguration import *

class TestSCDynamicStoreCopyDHCPInfo (TestCase):
    def testFunctions(self):
        def callback(st, keys, info):
            pass

        st = SCDynamicStoreCreate(None, "pyobjc.test", callback, None)
        self.failUnless(isinstance(st, SCDynamicStoreRef))

        info = SCDynamicStoreCopyDHCPInfo(st, None)
        self.failUnless(isinstance(info, CFDictionaryRef))

        r = DHCPInfoGetOptionData(info,  1)
        self.failUnless(r is None or isinstance(r, CFDataRef))

        r = DHCPInfoGetLeaseStartTime(info)
        self.failUnless(r is None or isinstance(r, CFDateRef))

if __name__ == "__main__":
    main()
