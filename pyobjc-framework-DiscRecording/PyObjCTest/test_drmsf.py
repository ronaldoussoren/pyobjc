import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRMSF(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DiscRecording.DRMSF.isEqualToMSF_)
