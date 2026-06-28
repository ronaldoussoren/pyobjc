import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCWWirelessProfile(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreWLAN.CWWirelessProfile.isEqualToProfile_)
