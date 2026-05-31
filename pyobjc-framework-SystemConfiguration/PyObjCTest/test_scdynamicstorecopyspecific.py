from PyObjCTools.TestSupport import TestCase
import SystemConfiguration


class TestSCDynamicStoreCopySpecific(TestCase):
    def testFunctions(self):
        def callback(st, keys, info):
            pass

        st = SystemConfiguration.SCDynamicStoreCreate(
            None, "pyobjc.test", callback, None
        )
        self.assertTrue(isinstance(st, SystemConfiguration.SCDynamicStoreRef))

        nm, encoding = SystemConfiguration.SCDynamicStoreCopyComputerName(st, None)
        self.assertTrue(isinstance(nm, str))
        self.assertTrue(isinstance(encoding, int))

        nm, uid, gid = SystemConfiguration.SCDynamicStoreCopyConsoleUser(st, None, None)
        self.assertTrue(isinstance(nm, str))
        self.assertTrue(isinstance(uid, int))
        self.assertTrue(isinstance(gid, int))

        nm = SystemConfiguration.SCDynamicStoreCopyLocalHostName(st)
        self.assertTrue(isinstance(nm, str))

        nm = SystemConfiguration.SCDynamicStoreCopyLocation(st)
        self.assertTrue(isinstance(nm, str))

        r = SystemConfiguration.SCDynamicStoreCopyProxies(st)
        self.assertTrue(r is None or isinstance(r, SystemConfiguration.CFDictionaryRef))
