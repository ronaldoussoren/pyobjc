from PyObjCTools.TestSupport import TestCase, min_sdk_level
import AVKit
import objc


class TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupportHelper(
    AVKit.NSObject
):
    def pictureInPictureController_setPlaying_(self, a, b):
        pass

    def pictureInPictureControllerTimeRangeForPlayback_(self, a):
        return 1

    def pictureInPictureControllerIsPlaybackPaused_(self):
        return 1

    def pictureInPictureController_didTransitionToRenderSize_(self, a, b):
        pass


class TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupport(TestCase):
    @min_sdk_level("10.12")
    def testProtocols12_0(self):
        self.assertIsInstance(
            objc.protocolNamed("AVPictureInPictureSampleBufferPlaybackDelegate"),
            objc.formal_protocol,
        )

    def test_methods(self):
        self.assertArgIsBOOL(
            TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupportHelper.pictureInPictureController_setPlaying_,
            1,
        )
        self.assertResultHasType(
            TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupportHelper.pictureInPictureControllerTimeRangeForPlayback,
            AVKit.CMTimeRange.__typestr__,
        )
        self.assertResultIsBOOL(
            TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupportHelper.pictureInPictureControllerIsPlaybackPaused_
        )
        self.assertArgHasType(
            TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupportHelper.pictureInPictureController_didTransitionToRenderSize_,  # noqa: B950
            1,
            AVKit.CMVideoDimensions.__typestr__,
        )
        self.assertArgHasType(
            TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupportHelper.pictureInPictureController_skipByInterval_completionHandler_,  # noqa: B950
            1,
            AVKit.CMTime.__typestr__,
        )
        self.assertArgIsBlock(
            TestAVPictureInPictureController_AVSampleBufferDisplayLayerSupportHelper.pictureInPictureController_skipByInterval_completionHandler_,  # noqa: B950
            2,
            b"v",
        )
