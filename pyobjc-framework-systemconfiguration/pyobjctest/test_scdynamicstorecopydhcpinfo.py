import os

from Foundation import NSDate
from PyObjCTools.TestSupport import TestCase
import SystemConfiguration


class TestSCDynamicStoreCopyDHCPInfo(TestCase):
    def testFunctions(self):
        def callback(st, keys, info):
            pass

        st = SystemConfiguration.SCDynamicStoreCreate(
            None, "pyobjc.test", callback, None
        )
        self.assertTrue(isinstance(st, SystemConfiguration.SCDynamicStoreRef))

        have_ip = False

        for intf in ("en0", "en1", "en2", "en3"):
            with os.popen(f"ifconfig {intf} 2>/dev/null| grep inet", "r") as fp:
                ip = fp.read()
                if ip.strip():
                    have_ip = True
                    break

        if not have_ip:
            print("Didn't find a configured interface")

        info = SystemConfiguration.SCDynamicStoreCopyDHCPInfo(st, None)
        if not have_ip:
            self.assertIs(info, None)
        else:
            self.assertIsInstance(info, SystemConfiguration.CFDictionaryRef)

            r = SystemConfiguration.DHCPInfoGetOptionData(info, 1)
            self.assertTrue(r is None or isinstance(r, SystemConfiguration.NSData))

            r = SystemConfiguration.DHCPInfoGetLeaseStartTime(info)
            self.assertTrue(r is None or isinstance(r, SystemConfiguration.NSDate))

        SystemConfiguration.DHCPInfoGetLeaseExpirationTime

        if info:
            r = SystemConfiguration.DHCPInfoGetLeaseExpirationTime(info)
            self.assertTrue(r is None or isinstance(r, NSDate))
