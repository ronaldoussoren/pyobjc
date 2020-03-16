import CoreWLAN
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCW8021XProfile(TestCase):
    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CW8021XProfile.alwaysPromptForPassword)
        self.assertArgIsBOOL(CoreWLAN.CW8021XProfile.setAlwaysPromptForPassword_, 0)
        self.assertResultIsBOOL(CoreWLAN.CW8021XProfile.isEqualToProfile_)

    @min_os_level("10.6")
    def testConvenience(self):
        p1 = CoreWLAN.CW8021XProfile.profile()
        p2 = CoreWLAN.CW8021XProfile.profile()

        self.assertTrue(p1 == p1)
        self.assertFalse(p1 != p1)
        self.assertTrue(p1 != p2)

        self.assertFalse(p1 == 42)
        self.assertTrue(p1 != 42)
