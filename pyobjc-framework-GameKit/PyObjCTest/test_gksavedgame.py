from PyObjCTools.TestSupport import *

import GameKit

class TestGKSavedGame (TestCase):

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(GameKit.GKSavedGame.loadDataWithCompletionHandler_, 0, b'v@@')

        self.assertArgIsBlock(GameKit.GKLocalPlayer.fetchSavedGamesWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.saveGameData_withName_completionHandler_, 2, b'v@@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.deleteSavedGamesWithName_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.resolveConflictingSavedGames_withData_completionHandler_, 2, b'v@@')


if __name__ == "__main__":
    main()
