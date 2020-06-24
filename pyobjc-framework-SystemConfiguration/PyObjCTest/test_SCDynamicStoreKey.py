from PyObjCTools.TestSupport import TestCase
import SystemConfiguration


class TestSCDynamicStoreKey(TestCase):
    def testFunctions(self):

        r = SystemConfiguration.SCDynamicStoreKeyCreate(
            None, "Setup:/%s/%d", b"PyObjC", 9
        )
        self.assertTrue(isinstance(r, str))
        self.assertEqual(r, "Setup:/PyObjC/9")

        r = SystemConfiguration.SCDynamicStoreKeyCreateNetworkGlobalEntity(
            None,
            SystemConfiguration.kSCDynamicStoreDomainSetup,
            SystemConfiguration.kSCEntNetDNS,
        )
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateNetworkInterface(
            None, SystemConfiguration.kSCDynamicStoreDomainState
        )
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateNetworkInterfaceEntity(
            None,
            SystemConfiguration.kSCDynamicStoreDomainState,
            "en0",
            SystemConfiguration.kSCEntNetIPv4,
        )
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateNetworkServiceEntity(
            None,
            SystemConfiguration.kSCDynamicStoreDomainState,
            "ssh",
            SystemConfiguration.kSCEntNetDNS,
        )
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateComputerName(None)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateConsoleUser(None)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateHostNames(None)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateLocation(None)
        self.assertTrue(isinstance(r, str))

        r = SystemConfiguration.SCDynamicStoreKeyCreateProxies(None)
        self.assertTrue(isinstance(r, str))
