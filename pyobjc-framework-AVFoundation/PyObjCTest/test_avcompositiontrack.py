import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCompositionTrack(TestCase):
    def test_methods(self):
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
    def test_methods10_15(self):
        self.assertArgIsBOOL(AVFoundation.AVMutableCompositionTrack.setEnabled_, 0)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(AVFoundation.AVCompositionTrack.hasMediaCharacteristic_)
