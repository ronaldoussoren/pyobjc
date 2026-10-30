import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCWConfiguration(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            CoreWLAN.CWConfiguration.requireAdministratorForAssociation
        )
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.requireAdministratorForPower)
        self.assertResultIsBOOL(
            CoreWLAN.CWConfiguration.requireAdministratorForIBSSMode
        )
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.rememberJoinedNetworks)
        self.assertResultIsBOOL(CoreWLAN.CWConfiguration.isEqualToConfiguration_)

        self.assertArgIsBOOL(
            CoreWLAN.CWMutableConfiguration.setRequireAdministratorForAssociation_, 0
        )
        self.assertArgIsBOOL(
            CoreWLAN.CWMutableConfiguration.setRequireAdministratorForPower_, 0
        )
        self.assertArgIsBOOL(
            CoreWLAN.CWMutableConfiguration.setRequireAdministratorForIBSSMode_, 0
        )
        self.assertArgIsBOOL(
            CoreWLAN.CWMutableConfiguration.setRememberJoinedNetworks_, 0
        )

    def test_convenience(self):
        c1 = CoreWLAN.CWConfiguration.alloc().init()
        c2 = CoreWLAN.CWConfiguration.alloc().init()

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 == 42)
        self.assertTrue(c1 != 42)
