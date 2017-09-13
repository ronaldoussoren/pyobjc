from PyObjCTools.TestSupport import *

import GameKit

class TestGKAchievementHelper (GameKit.GKAchievement):
    def isHidden(self): return 1

class TestGKAchievement (TestCase):
    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKAchievement.loadAchievementsWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(GameKit.GKAchievement.resetAchievementsWithCompletionHandler_, 0, b'v@')
        self.assertArgIsBlock(GameKit.GKAchievement.reportAchievements_withCompletionHandler_, 1, b'v@')

        self.assertResultIsBOOL(GameKit.GKAchievement.isCompleted)

        self.assertArgIsBlock(GameKit.GKAchievement.reportAchievementWithCompletionHandler_, 0, b'v@')

        self.assertResultIsBOOL(TestGKAchievementHelper.isHidden)
        self.assertResultIsBOOL(GameKit.GKAchievement.showsCompletionBanner)
        self.assertArgIsBOOL(GameKit.GKAchievement.setShowsCompletionBanner_, 0)




if __name__ == "__main__":
    main()
