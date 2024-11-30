from PyObjCTools.TestSupport import TestCase, min_os_level

import ScreenCaptureKit


class TestSCScreenshotManager(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsBlock(
            ScreenCaptureKit.SCScreenshotManager.captureSampleBufferWithFilter_configuration_completionHandler_,
            2,
            b"v^{opaqueCMSampleBuffer=}@",
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCScreenshotManager.captureImageWithFilter_configuration_completionHandler_,
            2,
            b"v^{CGImage=}@",
        )

    @min_os_level("15.2")
    def test_methods15_2(self):
        self.assertArgIsBlock(
            ScreenCaptureKit.SCScreenshotManager.captureImageInRect_completionHandler_,
            1,
            b"v^{CGImage=}@",
        )
