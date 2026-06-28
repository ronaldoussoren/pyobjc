import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKScore(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(GameKit.GKScore.shouldSetDefaultLeaderboard)
        self.assertArgIsBOOL(GameKit.GKScore.setShouldSetDefaultLeaderboard_, 0)

        self.assertArgIsBlock(
            GameKit.GKScore.reportScores_withCompletionHandler_, 1, b"v@"
        )

        self.assertArgIsBlock(
            GameKit.GKScore.reportScoreWithCompletionHandler_, 0, b"v@"
        )
