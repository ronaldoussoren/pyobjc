from PyObjCTools.TestSupport import *

import GameKit

class TestGKLocalPlayerHelper (GameKit.GKLocalPlayer):
    def isUnderage(self): return 1

class TestGKLocalPlayer (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKLocalPlayer.isAuthenticated)
        self.assertResultIsBOOL(TestGKLocalPlayerHelper.isUnderage)

        self.assertArgIsBlock(GameKit.GKLocalPlayer.setDefaultLeaderboardCategoryID_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.loadDefaultLeaderboardCategoryIDWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.loadFriendsWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.authenticateWithCompletionHandler_, 0, b'v@')

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBlock(GameKit.GKLocalPlayer.authenticateHandler, b'v@@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.setAuthenticateHandler_, 0, b'v@@')

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(GameKit.GKLocalPlayer.setDefaultLeaderboardIdentifier_completionHandler_, 1, b'v@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.loadDefaultLeaderboardIdentifierWithCompletionHandler_, 0, b'v@@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.generateIdentityVerificationSignatureWithCompletionHandler_, 0, b'v@@@Q@')
        self.assertArgIsBlock(GameKit.GKLocalPlayer.loadFriendPlayersWithCompletionHandler_, 0, b'v@@')

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBlock(GameKit.GKLocalPlayer.loadRecentPlayersWithCompletionHandler_, 0, b'v@@')

    def testProtocols(self):
        objc.protocolNamed('GKLocalPlayerListener')

    def testConstants(self):
        self.assertIsInstance(GameKit.GKPlayerAuthenticationDidChangeNotificationName, unicode)


if __name__ == "__main__":
    main()
