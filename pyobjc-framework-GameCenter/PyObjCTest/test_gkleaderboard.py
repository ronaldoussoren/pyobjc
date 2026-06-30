from PyObjCTools.TestSupport import (
    TestCase,
)

import GameCenter


class TestGKLeaderboard(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameCenter.GKLeaderboardTimeScope)
        self.assertEqual(GameCenter.GKLeaderboardTimeScopeToday, 0)
        self.assertEqual(GameCenter.GKLeaderboardTimeScopeWeek, 1)
        self.assertEqual(GameCenter.GKLeaderboardTimeScopeAllTime, 2)

        self.assertIsEnumType(GameCenter.GKLeaderboardPlayerScope)
        self.assertEqual(GameCenter.GKLeaderboardPlayerScopeGlobal, 0)
        self.assertEqual(GameCenter.GKLeaderboardPlayerScopeFriendsOnly, 1)

    def test_methods(self):
        self.assertResultIsBOOL(GameCenter.GKLeaderboard.isLoading)
        self.assertArgIsBlock(
            GameCenter.GKLeaderboard.loadScoresWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKLeaderboard.loadLeaderboardsWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKLeaderboard.loadCategoriesWithCompletionHandler_, 0, b"v@@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKLeaderboard.setDefaultLeaderboard_withCompletionHandler_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            GameCenter.GKLeaderboard.loadImageWithCompletionHandler_, 0, b"v@@"
        )
