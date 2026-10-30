import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCWNetworkProfile(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetworkProfile.isEqualToNetworkProfile_)

    def test_convenience(self):
        c1 = CoreWLAN.CWNetworkProfile.alloc().init()
        c2 = CoreWLAN.CWNetworkProfile.alloc().init()

        # Set ssidData because test can fail when the property
        # is not set (such as on macOS 27)
        c1.setSsidData_(b"hello")
        c2.setSsidData_(b"hello")

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 == 42)
        self.assertTrue(c1 != 42)
