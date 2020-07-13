import GameKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestGKLeaderboard(TestCase):
    def testConstants(self):
        self.assertEqual(GameKit.GKLeaderboardTimeScopeToday, 0)
        self.assertEqual(GameKit.GKLeaderboardTimeScopeWeek, 1)
        self.assertEqual(GameKit.GKLeaderboardTimeScopeAllTime, 2)

        self.assertEqual(GameKit.GKLeaderboardPlayerScopeGlobal, 0)
        self.assertEqual(GameKit.GKLeaderboardPlayerScopeFriendsOnly, 1)

    def testMethods(self):
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadLeaderboardsWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadCategoriesWithCompletionHandler_, 0, b"v@@@"
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.setDefaultLeaderboard_withCompletionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadImageWithCompletionHandler_, 0, b"v@@"
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(GameKit.GKLeaderboard.isLoading)
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadScoresWithCompletionHandler_, 0, b"v@@"
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadLeaderboardsWithIDs_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadPreviousOccurrenceWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.submitScore_context_player_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadEntriesForPlayerScope_timeScope_range_completionHandler_,
            3,
            b"v@@" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.loadEntriesForPlayers_timeScope_completionHandler_,
            2,
            b"v@@@",
        )

    @expectedFailure
    @min_os_level("10.16")
    def test_methods10_16_missing(self):
        self.assertArgIsBlock(
            GameKit.GKLeaderboard.submitScore_context_player_loaderboardIDs_completionHandler_,
            4,
            b"v@",
        )
