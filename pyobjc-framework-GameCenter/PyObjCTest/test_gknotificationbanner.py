from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKNotificationBanner(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            GameCenter.GKNotificationBanner.showBannerWithTitle_message_completionHandler_,
            2,
            b"v",
        )
        self.assertArgIsBlock(
            GameCenter.GKNotificationBanner.showBannerWithTitle_message_duration_completionHandler_,
            3,
            b"v",
        )
