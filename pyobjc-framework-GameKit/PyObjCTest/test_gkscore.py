import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKScore(TestCase):
    @min_os_level("10.8")
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKScore.shouldSetDefaultLeaderboard)
        self.assertArgIsBOOL(GameKit.GKScore.setShouldSetDefaultLeaderboard_, 0)

        self.assertArgIsBlock(
            GameKit.GKScore.reportScores_withCompletionHandler_, 1, b"v@"
        )

        self.assertArgIsBlock(
            GameKit.GKScore.reportScoreWithCompletionHandler_, 0, b"v@"
        )
