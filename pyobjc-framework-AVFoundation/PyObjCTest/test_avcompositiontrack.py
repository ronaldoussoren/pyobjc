import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCompositionTrack(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVMutableCompositionTrack.insertTimeRange_ofTrack_atTime_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableCompositionTrack.insertTimeRange_ofTrack_atTime_error_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVMutableCompositionTrack.insertTimeRanges_ofTracks_atTime_error_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableCompositionTrack.insertTimeRanges_ofTracks_atTime_error_,  # noqa: B950
            3,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVMutableCompositionTrack.validateTrackSegments_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableCompositionTrack.validateTrackSegments_error_, 1
        )

        self.assertResultIsBOOL(AVFoundation.AVMutableCompositionTrack.isEnabled)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBOOL(AVFoundation.AVMutableCompositionTrack.setEnabled_, 0)

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(AVFoundation.AVCompositionTrack.hasMediaCharacteristic_)
