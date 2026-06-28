from PyObjCTools.TestSupport import (
    TestCase,
)

import GameCenter


class TestGCAchievement(TestCase):
    def test_methods(self):
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

        self.assertResultIsBOOL(GameCenter.GKAchievement.showsCompletionBanner)
        self.assertArgIsBOOL(GameCenter.GKAchievement.setShowsCompletionBanner_, 0)
        self.assertResultIsBOOL(GameCenter.GKAchievement.alloc().init().isHidden)
