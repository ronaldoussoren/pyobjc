import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRMSF(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(DiscRecording.DRMSF.isEqualToMSF_)
