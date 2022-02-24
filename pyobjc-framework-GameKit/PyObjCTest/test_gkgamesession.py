import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKGameSession(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKConnectionState)
        self.assertIsEnumType(GameKit.GKTransportType)

    def testConstants(self):
        self.assertEqual(GameKit.GKConnectionStateNotConnected, 0)
        self.assertEqual(GameKit.GKConnectionStateConnected, 1)

        self.assertEqual(GameKit.GKTransportTypeUnreliable, 0)
        self.assertEqual(GameKit.GKTransportTypeReliable, 1)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertArgIsBlock(
            GameKit.GKGameSession.createSessionInContainer_withTitle_maxConnectedPlayers_completionHandler_,
            3,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.loadSessionsInContainer_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.loadSessionWithIdentifier_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.removeSessionWithIdentifier_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.getShareURLWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.loadDataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.saveData_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.setConnectionState_completionHandler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.sendData_withTransportType_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBOOL(
            GameKit.GKGameSession.sendMessageWithLocalizedFormatKey_arguments_data_toPlayers_badgePlayers_completionHandler_,
            4,
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.sendMessageWithLocalizedFormatKey_arguments_data_toPlayers_badgePlayers_completionHandler_,
            5,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKGameSession.clearBadgeForPlayers_completionHandler_, 1, b"v@"
        )
