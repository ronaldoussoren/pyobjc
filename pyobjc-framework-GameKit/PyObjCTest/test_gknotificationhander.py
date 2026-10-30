import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKNotificationHandler(TestCase):
    def test_methods(self):
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
