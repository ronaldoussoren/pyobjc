import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKNotificationBanner(TestCase):
    @min_os_level("10.8")
    def testClasses10_8(self):
        self.assertIsInstance(GameCenter.GKNotificationBanner, objc.objc_class)

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
