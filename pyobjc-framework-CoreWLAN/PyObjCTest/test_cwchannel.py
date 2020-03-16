import CoreWLAN
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCWChannel(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(CoreWLAN.CWChannel.isEqualToChannel_)

    @min_os_level("10.7")
    def testConvenience(self):
        c1 = CoreWLAN.CWChannel.alloc().init()
        c2 = CoreWLAN.CWChannel.alloc().init()

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 == 42)
        self.assertTrue(c1 != 42)
