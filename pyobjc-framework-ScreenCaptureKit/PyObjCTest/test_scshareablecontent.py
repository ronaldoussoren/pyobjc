from PyObjCTools.TestSupport import TestCase, min_os_level
import ScreenCaptureKit


class TestSCShareableContent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(ScreenCaptureKit.SCShareableContentStyle)
        self.assertEqual(ScreenCaptureKit.SCShareableContentStyleNone, 0)
        self.assertEqual(ScreenCaptureKit.SCShareableContentStyleWindow, 1)
        self.assertEqual(ScreenCaptureKit.SCShareableContentStyleDisplay, 2)
        self.assertEqual(ScreenCaptureKit.SCShareableContentStyleApplication, 3)

    def test_methods(self):
        self.assertResultIsBOOL(ScreenCaptureKit.SCWindow.isOnScreen)

        self.assertArgIsBlock(
            ScreenCaptureKit.SCShareableContent.getShareableContentWithCompletionHandler_,
            0,
            b"v@@",
        )

        self.assertArgIsBOOL(
            ScreenCaptureKit.SCShareableContent.getShareableContentExcludingDesktopWindows_onScreenWindowsOnly_completionHandler_,
            0,
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCShareableContent.getShareableContentExcludingDesktopWindows_onScreenWindowsOnly_completionHandler_,
            1,
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCShareableContent.getShareableContentExcludingDesktopWindows_onScreenWindowsOnly_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBOOL(
            ScreenCaptureKit.SCShareableContent.getShareableContentExcludingDesktopWindows_onScreenWindowsOnlyBelowWindow_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCShareableContent.getShareableContentExcludingDesktopWindows_onScreenWindowsOnlyBelowWindow_completionHandler_,
            2,
            b"v@@",
        )

        self.assertArgIsBOOL(
            ScreenCaptureKit.SCShareableContent.getShareableContentExcludingDesktopWindows_onScreenWindowsOnlyAboveWindow_completionHandler_,
            0,
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCShareableContent.getShareableContentExcludingDesktopWindows_onScreenWindowsOnlyAboveWindow_completionHandler_,
            2,
            b"v@@",
        )

    @min_os_level("13.1")
    def test_methods13_1(self):
        self.assertResultIsBOOL(ScreenCaptureKit.SCWindow.isActive)

    @min_os_level("14.4")
    def test_methods14_4(self):
        self.assertArgIsBlock(
            ScreenCaptureKit.SCShareableContent.getCurrentProcessShareableContentWithCompletionHandler_,
            0,
            b"v@@",
        )
