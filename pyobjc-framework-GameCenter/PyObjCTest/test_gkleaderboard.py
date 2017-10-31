from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKLeaderboard (TestCase):
        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertEqual(GameCenter.GKLeaderboardTimeScopeToday, 0)
            self.assertEqual(GameCenter.GKLeaderboardTimeScopeWeek, 1)
            self.assertEqual(GameCenter.GKLeaderboardTimeScopeAllTime, 2)

            self.assertEqual(GameCenter.GKLeaderboardPlayerScopeGlobal, 0)
            self.assertEqual(GameCenter.GKLeaderboardPlayerScopeFriendsOnly, 1)

        @expectedFailureIf(os_release().rsplit('.', 1)[0] == '10.9')
        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(GameCenter.GKLeaderboard.isLoading)
            self.assertArgIsBlock(GameCenter.GKLeaderboard.loadScoresWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLeaderboard.loadLeaderboardsWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLeaderboard.loadCategoriesWithCompletionHandler_, 0, b'v@@@')
            self.assertArgIsBlock(GameCenter.GKLeaderboard.setDefaultLeaderboard_withCompletionHandler_, 1, b'v@')


        @expectedFailure
        @min_os_level('10.8')
        def testMethods10_8_fail(self):
            self.assertArgIsBlock(GameCenter.GKLeaderboard.loadImageWithCompletionHandler_, 1, b'v@@')

if __name__ == "__main__":
    main()
