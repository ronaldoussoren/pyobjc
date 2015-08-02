from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKSavedGame (TestCase):
        @min_os_level('10.10')
        def testClasses10_10(self):
            self.assertIsInstance(GameCenter.GKSavedGame, objc.objc_class)

            self.assertArgIsBlock(GameCenter.GKSavedGame.loadDataWithCompletionHandler_, 0, b'v@@')

            self.assertArgIsBlock(GameCenter.GKLocalPlayer.fetchSavedGamesWithCompletionHandler_, 0, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.saveGameData_withName_completionHandler_, 2, b'v@@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.deleteSavedGamesWithName_completionHandler_, 1, b'v@')
            self.assertArgIsBlock(GameCenter.GKLocalPlayer.resolveConflictingSavedGames_withData_completionHandler_, 2, b'v@@')

if __name__ == "__main__":
    main()
