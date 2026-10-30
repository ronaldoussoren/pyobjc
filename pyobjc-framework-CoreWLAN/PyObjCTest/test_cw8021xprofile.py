import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCW8021XProfile(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreWLAN.CW8021XProfile.alwaysPromptForPassword)
        self.assertArgIsBOOL(CoreWLAN.CW8021XProfile.setAlwaysPromptForPassword_, 0)
        self.assertResultIsBOOL(CoreWLAN.CW8021XProfile.isEqualToProfile_)

    def test_convenience(self):
        p1 = CoreWLAN.CW8021XProfile.profile()
        p2 = CoreWLAN.CW8021XProfile.profile()

        self.assertTrue(p1 == p1)
        self.assertFalse(p1 != p1)
        self.assertTrue(p1 != p2)

        self.assertFalse(p1 == 42)
        self.assertTrue(p1 != 42)
