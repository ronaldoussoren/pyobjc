from PyObjCTools.TestSupport import *

from SystemConfiguration import *

class TestSCDynamicStoreKey (TestCase):
    def testFunctions(self):

        r = SCDynamicStoreKeyCreate(None, "Setup:/%s/%d", b"PyObjC", 9)
        self.assertTrue(isinstance(r, unicode))
        self.assertEquals(r, u"Setup:/PyObjC/9")

        r = SCDynamicStoreKeyCreateNetworkGlobalEntity(None,
                kSCDynamicStoreDomainSetup, kSCEntNetDNS)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateNetworkInterface(None, kSCDynamicStoreDomainState)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateNetworkInterfaceEntity(None,
                kSCDynamicStoreDomainState, "en0", kSCEntNetIPv4)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateNetworkServiceEntity(None,
                kSCDynamicStoreDomainState, "ssh", kSCEntNetDNS)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateComputerName(None)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateConsoleUser(None)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateHostNames(None)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateLocation(None)
        self.assertTrue(isinstance(r, unicode))

        r = SCDynamicStoreKeyCreateProxies(None)
        self.assertTrue(isinstance(r, unicode))

if __name__ == "__main__":
    main()
