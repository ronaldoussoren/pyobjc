from PyObjCTools.TestSupport import *

from SystemConfiguration import *
from Foundation import NSData, NSDate
import os

class TestSCDynamicStoreCopyDHCPInfo (TestCase):
    def testFunctions(self):
        def callback(st, keys, info):
            pass

        st = SCDynamicStoreCreate(None, "pyobjc.test", callback, None)
        self.assertTrue(isinstance(st, SCDynamicStoreRef))

        have_ip = False
        with os.popen("ifconfig en0 | grep inet", "r") as fp:
            ip = fp.read()
        if ip.strip():
            have_ip = True
        else:
            with os.popen("ifconfig en1 | grep inet", "r") as fp:
                ip = fp.read()
            if ip.strip():
                have_ip = True

        info = SCDynamicStoreCopyDHCPInfo(st, None)
        if not have_ip:
            self.assertIs(info, None)
        else:
            self.assertIsInstance(info, CFDictionaryRef)

            r = DHCPInfoGetOptionData(info,  1)
            self.assertTrue(r is None or isinstance(r, NSData))

            r = DHCPInfoGetLeaseStartTime(info)
            self.assertTrue(r is None or isinstance(r, NSDate))

        if os_release() >= '10.8':
            DHCPInfoGetLeaseExpirationTime

            if info:
                r = DHCPInfoGetLeaseExpirationTime(info)
                self.assertTrue(r is None or isinstance(r, NSDate))

if __name__ == "__main__":
    main()
