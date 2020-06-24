import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKNotificationHandler(TestCase):
    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBlock(
            GameKit.GKNotificationBanner.showBannerWithTitle_message_completionHandler_,
            2,
            b"v",
        )
        self.assertArgIsBlock(
            GameKit.GKNotificationBanner.showBannerWithTitle_message_duration_completionHandler_,
            3,
            b"v",
        )
