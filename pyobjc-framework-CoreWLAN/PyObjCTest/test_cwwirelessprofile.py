import CoreWLAN
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCWWirelessProfile(TestCase):
    @min_os_level("10.6")
    def test_methods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CWWirelessProfile.isEqualToProfile_)
