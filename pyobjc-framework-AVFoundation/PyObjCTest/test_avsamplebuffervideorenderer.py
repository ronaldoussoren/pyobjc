import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVSampleBufferVideoRenderer(TestCase):
    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(
            AVFoundation.AVSampleBufferVideoRendererDidFailToDecodeNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVSampleBufferVideoRendererDidFailToDecodeNotificationErrorKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotification,
            str,
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferVideoRenderer.requiresFlushToResumeDecoding
        )

        self.assertArgIsBOOL(
            AVFoundation.AVSampleBufferVideoRenderer.flushWithRemovalOfDisplayedImage_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferVideoRenderer.flushWithRemovalOfDisplayedImage_completionHandler_,
            1,
            b"v",
        )

    @min_os_level("14.4")
    def test_methods14_4(self):
        self.assertResultIsCFRetained(
            AVFoundation.AVSampleBufferVideoRenderer.copyDisplayedPixelBuffer
        )

        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferVideoRenderer.loadVideoPerformanceMetricsWithCompletionHandler_,
            0,
            b"v@",
        )
