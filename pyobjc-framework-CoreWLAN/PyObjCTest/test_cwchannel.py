import CoreWLAN
from PyObjCTools.TestSupport import TestCase


class TestCWChannel(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreWLAN.CWChannel.isEqualToChannel_)

    def test_convenience(self):
        c1 = CoreWLAN.CWChannel.alloc().init()
        c2 = CoreWLAN.CWChannel.alloc().init()

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 == 42)
        self.assertTrue(c1 != 42)
