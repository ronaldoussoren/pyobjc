from PyObjCTools.TestSupport import TestCase
import ScreenCaptureKit


class TestSCShareableContent(TestCase):
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
