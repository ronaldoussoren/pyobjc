import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRCoreStatus(TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRStatusStateKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusPercentCompleteKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusCurrentSpeedKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusCurrentSessionKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusCurrentTrackKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusTotalSessionsKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusTotalTracksKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusEraseTypeKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateNone, str)
        self.assertIsInstance(DiscRecording.kDRStatusStatePreparing, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateVerifying, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateDone, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateFailed, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateSessionOpen, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateTrackOpen, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateTrackWrite, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateTrackClose, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateSessionClose, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateFinishing, str)
        self.assertIsInstance(DiscRecording.kDRStatusStateErasing, str)
        self.assertIsInstance(DiscRecording.kDRStatusProgressInfoKey, str)
        self.assertIsInstance(DiscRecording.kDRStatusProgressCurrentKPS, str)
        self.assertIsInstance(DiscRecording.kDRStatusProgressCurrentXFactor, str)
