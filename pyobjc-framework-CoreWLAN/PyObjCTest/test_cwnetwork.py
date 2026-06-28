import CoreWLAN
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestCWNetwork(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.ibss)

        self.assertResultIsBOOL(CoreWLAN.CWNetwork.supportsSecurity_)
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.supportsPHYMode_)

        self.assertResultIsBOOL(CoreWLAN.CWNetwork.isEqualToNetwork_)
        self.assertResultIsBOOL(CoreWLAN.CWNetwork.isIBSS)

    @expectedFailure  # on 10.15
    def test_convenience(self):
        c1 = CoreWLAN.CWNetwork.alloc().init()
        c2 = CoreWLAN.CWNetwork.alloc().init()

        self.assertTrue(c1 == c2)
        self.assertFalse(c1 != c2)

        self.assertFalse(c1 == 42)
        self.assertTrue(c1 != 42)
