import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSWritingToolsCoordinatorAnimationParameters(TestCase):
    @min_os_level("15.2")
    def test_methods(self):
        self.assertResultIsBlock(
            AppKit.NSWritingToolsCoordinatorAnimationParameters.progressHandler, b"vf"
        )
        self.assertArgIsBlock(
            AppKit.NSWritingToolsCoordinatorAnimationParameters.setProgressHandler_,
            0,
            b"vf",
        )

        self.assertResultIsBlock(
            AppKit.NSWritingToolsCoordinatorAnimationParameters.completionHandler, b"v"
        )
        self.assertArgIsBlock(
            AppKit.NSWritingToolsCoordinatorAnimationParameters.setCompletionHandler_,
            0,
            b"v",
        )
