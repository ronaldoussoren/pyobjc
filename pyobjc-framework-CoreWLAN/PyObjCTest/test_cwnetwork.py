import CoreWLAN
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestCWNetwork(TestCase):
    @min_os_level("10.7")
    def test_methods10_7(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.ibss)

        self.assertResultIsBOOL(CoreWLAN.CWNetwork.supportsSecurity_)
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.supportsPHYMode_)

    @min_os_level("10.6")
    def test_methods10_6(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.isEqualToNetwork_)
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.isIBSS)

    @min_os_level("10.7")
    @expectedFailure  # on 10.15
    def testConvenience(self):
        c1 = CoreWLAN.CWNetwork.alloc().init()
        c2 = CoreWLAN.CWNetwork.alloc().init()

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 == 42)
        self.assertTrue(c1 != 42)
