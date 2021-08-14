import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVComposition(TestCase):
    @min_os_level("10.7")
    def test_methods10_7(self):
        self.assertResultIsBOOL(
            AVFoundation.AVMutableComposition.insertTimeRange_ofAsset_atTime_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableComposition.insertTimeRange_ofAsset_atTime_error_, 3
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVComposition.loadTrackWithTrackID_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVComposition.loadTracksWithMediaType_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVComposition.loadTracksWithMediaCharacteristic_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            AVFoundation.AVMutableComposition.loadTrackWithTrackID_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVMutableComposition.loadTracksWithMediaType_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVMutableComposition.loadTracksWithMediaCharacteristic_completionHandler_,
            1,
            b"v@@",
        )
