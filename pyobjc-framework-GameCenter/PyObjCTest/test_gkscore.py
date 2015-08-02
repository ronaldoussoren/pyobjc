from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKScore (TestCase):
        @min_os_level('10.8')
        def testClasses10_8(self):
            self.assertIsInstance(GameCenter.GKScore, objc.objc_class)

            self.assertResultIsBOOL(GameCenter.GKScore.shouldSetDefaultLeaderboard)
            self.assertArgIsBOOL(GameCenter.GKScore.setShouldSetDefaultLeaderboard_, 0)

            self.assertArgIsBlock(GameCenter.GKScore.reportScores_withCompletionHandler_, 1, b'v@')
            self.assertArgIsBlock(GameCenter.GKScore.reportScoreWithCompletionHandler_, 0, b'v@')

if __name__ == "__main__":
    main()
