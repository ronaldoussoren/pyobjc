import objc
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)

import GameCenter


class TestGCAchievement(TestCase):
    @min_os_level("10.8")
    def testClasses10_8(self):
        self.assertIsInstance(GameCenter.GKAchievement, objc.objc_class)

        self.assertArgIsBlock(
            GameCenter.GKAchievement.loadAchievementsWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKAchievement.resetAchievementsWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            GameCenter.GKAchievement.reportAchievements_withCompletionHandler_, 1, b"v@"
        )
        self.assertResultIsBOOL(GameCenter.GKAchievement.isCompleted)

        self.assertArgIsBlock(
            GameCenter.GKAchievement.reportAchievementWithCompletionHandler_, 0, b"v@"
        )

    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.9")
    @min_os_level("10.8")
    def testClasses10_8_missing_10_9(self):
        self.assertResultIsBOOL(GameCenter.GKAchievement.showsCompletionBanner)
        self.assertArgIsBOOL(GameCenter.GKAchievement.setShowsCompletionBanner_, 0)
        self.assertResultIsBOOL(GameCenter.GKAchievement.alloc().init().isHidden)
