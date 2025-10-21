from PyObjCTools.TestSupport import TestCase, min_os_level

import ScreenCaptureKit


class TestSCScreenshotManager(TestCase):
    def test_constants(self):
        self.assertIsEnumType(ScreenCaptureKit.SCScreenshotDisplayIntent)
        self.assertEqual(ScreenCaptureKit.SCScreenshotDisplayIntentCanonical, 0)
        self.assertEqual(ScreenCaptureKit.SCScreenshotDisplayIntentLocal, 1)

        self.assertIsEnumType(ScreenCaptureKit.SCScreenshotDynamicRange)
        self.assertEqual(ScreenCaptureKit.SCScreenshotDynamicRangeSDR, 0)
        self.assertEqual(ScreenCaptureKit.SCScreenshotDynamicRangeHDR, 1)
        self.assertEqual(ScreenCaptureKit.SCScreenshotDynamicRangeSDRAndHDR, 2)

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

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(ScreenCaptureKit.SCScreenshotConfiguration.showsCursor)
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCScreenshotConfiguration.setShowsCursor_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCScreenshotConfiguration.ignoreShadows
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCScreenshotConfiguration.setIgnoreShadows_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCScreenshotConfiguration.ignoreClipping
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCScreenshotConfiguration.setIgnoreClipping_, 0
        )

        self.assertResultIsBOOL(
            ScreenCaptureKit.SCScreenshotConfiguration.includeChildWindows
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCScreenshotConfiguration.setIncludeChildWindows_, 0
        )

        self.assertArgIsBlock(
            ScreenCaptureKit.SCScreenshotManager.captureScreenshotWithFilter_configuration_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCScreenshotManager.captureScreenshotWithRect_configuration_completionHandler_,
            2,
            b"v@@",
        )
