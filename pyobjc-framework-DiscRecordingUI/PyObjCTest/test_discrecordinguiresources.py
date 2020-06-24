import DiscRecordingUI
from PyObjCTools.TestSupport import TestCase


class TestDiscRecordingUIResources(TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecordingUI.DRBurnIcon, str)
        self.assertIsInstance(DiscRecordingUI.DREraseIcon, str)
