from PyObjCTools.TestSupport import *

import CoreWLAN

class TestCWConfiguration (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.alwaysRememberNetworks)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.disconnectOnLogout)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.requireAdminForNetworkChange)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.requireAdminForPowerChange)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.requireAdminForIBSSCreation)

        self.assertArgIsBOOL(CoreWLAN.CWConfiguration.setAlwaysRememberNetworks_, 0)
        self.assertArgIsBOOL(CoreWLAN.CWConfiguration.setDisconnectOnLogout_, 0)
        self.assertArgIsBOOL(CoreWLAN.CWConfiguration.setRequireAdminForNetworkChange_, 0)
        self.assertArgIsBOOL(CoreWLAN.CWConfiguration.setRequireAdminForPowerChange_, 0)
        self.assertArgIsBOOL(CoreWLAN.CWConfiguration.setRequireAdminForIBSSCreation_, 0)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.requireAdministratorForAssociation)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.requireAdministratorForPower)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.requireAdministratorForIBSSMode)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.rememberJoinedNetworks)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.isEqualToConfiguration_)

        self.assertArgIsBOOL(CoreWLAN.CWMutableConfiguration.setRequireAdministratorForAssociation_, 0)
        self.assertArgIsBOOL(CoreWLAN.CWMutableConfiguration.setRequireAdministratorForPower_, 0)
        self.assertArgIsBOOL(CoreWLAN.CWMutableConfiguration.setRequireAdministratorForIBSSMode_, 0)
        self.assertArgIsBOOL(CoreWLAN.CWMutableConfiguration.setRememberJoinedNetworks_, 0)

if __name__ == "__main__":
    main()
