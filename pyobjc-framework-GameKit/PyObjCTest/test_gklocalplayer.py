import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestGKLocalPlayerHelper(GameKit.GKLocalPlayer):
    def isUnderage(self):
        return 1


class TestGKLocalPlayer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKFriendsAuthorizationStatus)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKLocalPlayer.isAuthenticated)
        self.assertResultIsBOOL(TestGKLocalPlayerHelper.isUnderage)

        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.setDefaultLeaderboardCategoryID_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadDefaultLeaderboardCategoryIDWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadFriendsWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.authenticateWithCompletionHandler_, 0, b"v@"
        )

    @min_os_level("10.10")
    def testMethods10_9(self):
        self.assertResultIsBlock(GameKit.GKLocalPlayer.authenticateHandler, b"v@@")
        self.assertArgIsBlock(GameKit.GKLocalPlayer.setAuthenticateHandler_, 0, b"v@@")

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.setDefaultLeaderboardIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadDefaultLeaderboardIdentifierWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.generateIdentityVerificationSignatureWithCompletionHandler_,
            0,
            b"v@@@Q@",
        )
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadFriendPlayersWithCompletionHandler_, 0, b"v@@"
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadRecentPlayersWithCompletionHandler_, 0, b"v@@"
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(GameKit.GKLocalPlayer.isMultiplayerGamingRestricted)
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadChallengableFriendsWithCompletionHandler_,
            0,
            b"v@@",
        )

    @min_os_level("10.15.4")
    def testMethods10_15_4(self):
        # XXX: Header says 10.15.5
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.fetchItemsForIdentityVerificationSignature_,
            0,
            b"v@@@Q@",
        )

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            GameKit.GKLocalPlayer.isPersonalizedCommunicationRestricted
        )

    @min_os_level("11.3")
    def testMethods11_3(self):
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadFriendsAuthorizationStatus_,
            0,
            b"v" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(GameKit.GKLocalPlayer.loadFriends_, 0, b"v@@")
        self.assertArgIsBlock(
            GameKit.GKLocalPlayer.loadFriendsWithIdentifiers_completionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            GameKit.GKLocalPlayer.isPresentingFriendRequestViewController
        )

    def testProtocols(self):
        objc.protocolNamed("GKLocalPlayerListener")

    def testConstants(self):
        self.assertIsInstance(
            GameKit.GKPlayerAuthenticationDidChangeNotificationName, str
        )

        self.assertEqual(GameKit.GKAuthenticatingWithoutUI, 0)
        self.assertEqual(GameKit.GKAuthenticatingWithGreenBuddyUI, 1)
        self.assertEqual(GameKit.GKAuthenticatingWithAuthKitInvocation, 2)

        self.assertEqual(GameKit.GKFriendsAuthorizationStatusNotDetermined, 0)
        self.assertEqual(GameKit.GKFriendsAuthorizationStatusRestricted, 1)
        self.assertEqual(GameKit.GKFriendsAuthorizationStatusDenied, 2)
        self.assertEqual(GameKit.GKFriendsAuthorizationStatusAuthorized, 3)
