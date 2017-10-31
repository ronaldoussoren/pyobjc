from PyObjCTools.TestSupport import *

import GameKit

class TestGKLeaderboard (TestCase):

    def testConstants(self):
        self.assertEqual(GameKit.GKLeaderboardTimeScopeToday, 0)
        self.assertEqual(GameKit.GKLeaderboardTimeScopeWeek, 1)
        self.assertEqual(GameKit.GKLeaderboardTimeScopeAllTime, 2)

        self.assertEqual(GameKit.GKLeaderboardPlayerScopeGlobal, 0)
        self.assertEqual(GameKit.GKLeaderboardPlayerScopeFriendsOnly, 1)

    @onlyOn64Bit
    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKLeaderboard.loadLeaderboardsWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(GameKit.GKLeaderboard.loadCategoriesWithCompletionHandler_, 0, b'v@@@')
        self.assertArgIsBlock(GameKit.GKLeaderboard.setDefaultLeaderboard_withCompletionHandler_, 1, b'v@')
        self.assertArgIsBlock(GameKit.GKLeaderboard.loadImageWithCompletionHandler_, 0, b'v@@')

    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(GameKit.GKLeaderboard.isLoading)
        self.assertArgIsBlock(GameKit.GKLeaderboard.loadScoresWithCompletionHandler_, 0, b'v@@')


if __name__ == "__main__":
    main()
