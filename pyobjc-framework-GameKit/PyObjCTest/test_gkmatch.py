import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestGKMatchHelper(GameKit.NSObject):
    def match_player_didChangeConnectionState_(self, m, p, s):
        pass

    def match_player_didChangeState_(self, m, p, s):
        pass

    def match_shouldReinviteDisconnectedPlayer_(self, m, p):
        return 1

    def match_shouldReinvitePlayer_(self, m, p):
        return 1


class TestGKMatch(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKMatchSendDataMode)
        self.assertIsEnumType(GameKit.GKPlayerConnectionState)

    def testConstants(self):
        self.assertEqual(GameKit.GKMatchSendDataReliable, 0)
        self.assertEqual(GameKit.GKMatchSendDataUnreliable, 1)

        self.assertEqual(GameKit.GKPlayerStateUnknown, 0)
        self.assertEqual(GameKit.GKPlayerStateConnected, 1)
        self.assertEqual(GameKit.GKPlayerStateDisconnected, 2)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKMatch.sendData_toPlayers_dataMode_error_)
        self.assertArgIsOut(GameKit.GKMatch.sendData_toPlayers_dataMode_error_, 3)

        self.assertResultIsBOOL(
            GameKit.GKMatch.sendDataToAllPlayers_withDataMode_error_
        )
        self.assertArgIsOut(GameKit.GKMatch.sendDataToAllPlayers_withDataMode_error_, 2)

    def testProtocolMethods(self):
        self.assertArgHasType(
            GameKit.TestGKMatchHelper.match_player_didChangeConnectionState_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            GameKit.TestGKMatchHelper.match_player_didChangeState_, 2, objc._C_NSInteger
        )
        self.assertResultIsBOOL(
            GameKit.TestGKMatchHelper.match_shouldReinviteDisconnectedPlayer_
        )
        self.assertResultIsBOOL(GameKit.TestGKMatchHelper.match_shouldReinvitePlayer_)

    @min_os_level("10.10")
    def testMethods10_9(self):
        self.assertArgIsBlock(GameKit.GKMatch.rematchWithCompletionHandler_, 0, b"v@@")
        self.assertArgIsBlock(
            GameKit.GKMatch.chooseBestHostPlayerWithCompletionHandler_, 0, b"v@"
        )

        self.assertResultIsBOOL(GameKit.GKMatch.sendData_toPlayers_withDataMode_error_)
        self.assertArgIsOut(GameKit.GKMatch.sendData_toPlayers_withDataMode_error_, 3)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            GameKit.GKMatch.chooseBestHostingPlayerWithCompletionHandler_, 0, b"v@"
        )

    def testProtocols(self):
        self.assertProtocolExists("GKMatchDelegate")
