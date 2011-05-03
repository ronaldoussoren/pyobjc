from PyObjCTools.TestSupport import *

from SystemConfiguration import *
import os

class TestSCDynamicStoreCopyDHCPInfo (TestCase):
    def testFunctions(self):
        def callback(st, keys, info):
            pass

        st = SCDynamicStoreCreate(None, "pyobjc.test", callback, None)
        self.assertTrue(isinstance(st, SCDynamicStoreRef))

        have_ip = False
        ip = os.popen("ifconfig en0 | grep inet", "r").read()
        if ip.strip():
            have_ip = True
        else:
            ip = os.popen("ifconfig en1 | grep inet", "r").read()
            if ip.strip():
                have_ip = True

        info = SCDynamicStoreCopyDHCPInfo(st, None)
        if not have_ip:
            self.assertIs(info, None)
        else:
            self.assertIsInstance(info, CFDictionaryRef)

            r = DHCPInfoGetOptionData(info,  1)
            self.assertTrue(r is None or isinstance(r, CFDataRef))

            r = DHCPInfoGetLeaseStartTime(info)
            self.assertTrue(r is None or isinstance(r, CFDateRef))

if __name__ == "__main__":
    main()
