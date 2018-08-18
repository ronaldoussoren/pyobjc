from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRCoreStatus (TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecording.kDRStatusStateKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusPercentCompleteKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusCurrentSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusCurrentSessionKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusCurrentTrackKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusTotalSessionsKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusTotalTracksKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusEraseTypeKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateNone, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStatePreparing, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateVerifying, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateDone, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateFailed, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateSessionOpen, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateTrackOpen, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateTrackWrite, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateTrackClose, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateSessionClose, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateFinishing, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusStateErasing, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusProgressInfoKey, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusProgressCurrentKPS, unicode)
        self.assertIsInstance(DiscRecording.kDRStatusProgressCurrentXFactor, unicode)

if __name__ == "__main__":
    main()
