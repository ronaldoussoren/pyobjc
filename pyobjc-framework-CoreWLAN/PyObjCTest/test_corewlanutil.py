import CoreWLAN
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCoreWLANUtil(TestCase):
    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertArgIsOut(CoreWLAN.CWKeychainCopyEAPUsernameAndPassword, 1)
        self.assertArgIsCFRetained(CoreWLAN.CWKeychainCopyEAPUsernameAndPassword, 1)
        self.assertArgIsOut(CoreWLAN.CWKeychainCopyEAPUsernameAndPassword, 2)
        self.assertArgIsCFRetained(CoreWLAN.CWKeychainCopyEAPUsernameAndPassword, 2)

        # Check it exists:
        CoreWLAN.CWKeychainSetEAPUsernameAndPassword
        CoreWLAN.CWKeychainDeleteEAPUsernameAndPassword
        CoreWLAN.CWKeychainSetEAPIdentity
        CoreWLAN.CWKeychainSetPassword
        CoreWLAN.CWKeychainDeletePassword
        CoreWLAN.CWMergeNetworks

        self.assertArgIsOut(CoreWLAN.CWKeychainCopyEAPIdentityList, 0)
        self.assertArgIsCFRetained(CoreWLAN.CWKeychainCopyEAPIdentityList, 0)

        self.assertArgIsOut(CoreWLAN.CWKeychainCopyEAPIdentity, 1)
        self.assertArgIsCFRetained(CoreWLAN.CWKeychainCopyEAPIdentity, 1)

        self.assertArgIsOut(CoreWLAN.CWKeychainCopyPassword, 1)
        self.assertArgIsCFRetained(CoreWLAN.CWKeychainCopyPassword, 1)

    @min_os_level("10.9")
    def testFunctions10_9(self):
        self.assertArgIsOut(CoreWLAN.CWKeychainFindWiFiPassword, 2)
        self.assertArgIsOut(CoreWLAN.CWKeychainFindWiFiEAPUsernameAndPassword, 2)
        self.assertArgIsOut(CoreWLAN.CWKeychainFindWiFiEAPUsernameAndPassword, 3)
        self.assertArgIsOut(CoreWLAN.CWKeychainCopyWiFiEAPIdentity, 2)
        self.assertArgIsCFRetained(CoreWLAN.CWKeychainCopyWiFiEAPIdentity, 2)

        CoreWLAN.CWKeychainSetWiFiPassword  # Only check existance
        CoreWLAN.CWKeychainDeleteWiFiPassword  # Only check existance
        CoreWLAN.CWKeychainSetWiFiEAPUsernameAndPassword  # Only check existance
        CoreWLAN.CWKeychainDeleteWiFiEAPUsernameAndPassword  # Only check existance
        CoreWLAN.CWKeychainSetWiFiEAPIdentity  # Only check existance
