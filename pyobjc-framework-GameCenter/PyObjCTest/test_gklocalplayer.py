import objc
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
)

import GameCenter


class TestGKLocalPlayer(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            GameCenter.GKPlayerAuthenticationDidChangeNotificationName, str
        )

    def test_methods(self):
        self.assertIsInstance(GameCenter.GKLocalPlayer, objc.objc_class)
        self.assertResultIsBOOL(GameCenter.GKLocalPlayer.isAuthenticated)

        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.setDefaultLeaderboardCategoryID_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.loadDefaultLeaderboardCategoryIDWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.loadFriendsWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.authenticateWithCompletionHandler_, 0, b"v@"
        )

        self.assertResultIsBOOL(GameCenter.GKLocalPlayer().isUnderage)

        self.assertResultIsBlock(GameCenter.GKLocalPlayer.authenticateHandler, b"v@@")
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.setAuthenticateHandler_, 0, b"v@@"
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.loadFriendPlayersWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.setDefaultLeaderboardIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.loadDefaultLeaderboardIdentifierWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKLocalPlayer.generateIdentityVerificationSignatureWithCompletionHandler_,
            0,
            b"v@@@Q@",
        )

    @min_sdk_level("10.10")
    def test_protocols(self):
        self.assertProtocolExists("GKLocalPlayerListener", GameCenter)
