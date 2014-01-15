from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCoreWLANUtil (TestCase):

    @min_os_level('10.7')
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

if __name__ == "__main__":
    main()
