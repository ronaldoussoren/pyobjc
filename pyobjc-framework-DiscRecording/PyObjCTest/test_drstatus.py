from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRStatus (TestCase):
    def testConstants(self):
        self.assertIsInstance(DiscRecording.DRStatusStateKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusPercentCompleteKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusCurrentSessionKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusCurrentTrackKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusTotalSessionsKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusTotalTracksKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusCurrentSpeedKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusEraseTypeKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateNone, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStatePreparing, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateVerifying, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateDone, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateFailed, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateSessionOpen, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateTrackOpen, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateTrackWrite, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateTrackClose, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateSessionClose, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateFinishing, unicode)
        self.assertIsInstance(DiscRecording.DRStatusStateErasing, unicode)
        self.assertIsInstance(DiscRecording.DRStatusProgressInfoKey, unicode)
        self.assertIsInstance(DiscRecording.DRStatusProgressCurrentKPS, unicode)
        self.assertIsInstance(DiscRecording.DRStatusProgressCurrentXFactor, unicode)
        self.assertIsInstance(DiscRecording.DRErrorStatusKey, unicode)
        self.assertIsInstance(DiscRecording.DRErrorStatusErrorKey, unicode)
        self.assertIsInstance(DiscRecording.DRErrorStatusErrorStringKey, unicode)
        self.assertIsInstance(DiscRecording.DRErrorStatusErrorInfoStringKey, unicode)
        self.assertIsInstance(DiscRecording.DRErrorStatusSenseKey, unicode)
        self.assertIsInstance(DiscRecording.DRErrorStatusSenseCodeStringKey, unicode)
        self.assertIsInstance(DiscRecording.DRErrorStatusAdditionalSenseStringKey, unicode)

if __name__ == "__main__":
    main()
