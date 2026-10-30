import DiscRecordingUI
from PyObjCTools.TestSupport import TestCase


class TestDiscRecordingUIResources(TestCase):
    def test_constants(self):
        self.assertIsInstance(DiscRecordingUI.DRBurnIcon, str)
        self.assertIsInstance(DiscRecordingUI.DREraseIcon, str)
