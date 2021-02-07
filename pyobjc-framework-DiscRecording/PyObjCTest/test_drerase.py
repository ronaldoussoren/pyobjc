import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRErase(TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecording.DREraseTypeKey, str)
        self.assertIsInstance(DiscRecording.DREraseTypeQuick, str)
        self.assertIsInstance(DiscRecording.DREraseTypeComplete, str)
        self.assertIsInstance(DiscRecording.DREraseStatusChangedNotification, str)
