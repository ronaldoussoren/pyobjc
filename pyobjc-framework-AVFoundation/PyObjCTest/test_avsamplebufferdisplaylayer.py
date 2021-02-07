import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVSampleBufferDisplayLayer(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(
            AVFoundation.AVQueuedSampleBufferRenderingStatusUnknown, 0
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVQueuedSampleBufferRenderingStatusRendering, 1
        )  # noqa: B950
        self.assertEqual(
            AVFoundation.AVQueuedSampleBufferRenderingStatusFailed, 2
        )  # noqa: B950

        self.assertIsInstance(
            AVFoundation.AVSampleBufferDisplayLayerFailedToDecodeNotification,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey,  # noqa: B950
            str,
        )

    @min_os_level("10.8")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.isReadyForMoreMediaData
        )
        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferDisplayLayer.requestMediaDataWhenReadyOnQueue_usingBlock_,  # noqa: B950
            1,
            b"v",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        # Header says 10.15, but new in the 10.14.4 SDK headers
        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.preventsCapture
        )  # noqa: B950
        self.assertArgIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.setPreventsCapture_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.preventsDisplaySleepDuringVideoPlayback  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.setPreventsDisplaySleepDuringVideoPlayback_,  # noqa: B950
            0,
        )

    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferDisplayLayer.requiresFlushToResumeDecoding
        )
