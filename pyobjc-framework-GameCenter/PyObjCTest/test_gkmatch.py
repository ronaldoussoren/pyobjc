from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter
    import objc

    class GKMatchDelegateHelper (GameCenter.NSObject):
        def match_player_didChangeConnectionState_(self, m, p, s): pass
        def match_player_didChangeState_(self, m, p, s): pass
        def match_shouldReinviteDisconnectedPlayer_(self, m, p): return 1
        def match_shouldReinvitePlayer_(self, m, p): return 1

    class TestGKError (TestCase):
        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertEqual(GameCenter.GKMatchSendDataReliable, 0)
            self.assertEqual(GameCenter.GKMatchSendDataUnreliable, 1)

            self.assertEqual(GameCenter.GKPlayerStateUnknown, 0)
            self.assertEqual(GameCenter.GKPlayerStateConnected, 1)
            self.assertEqual(GameCenter.GKPlayerStateDisconnected, 2)

        @expectedFailureIf(os_release().rsplit('.', 1)[0] == '10.9')
        @min_os_level('10.8')
        def testMethods10_8(self):
            self.assertResultIsBOOL(GameCenter.GKMatch.sendData_toPlayers_dataMode_error_)
            self.assertArgIsOut(GameCenter.GKMatch.sendData_toPlayers_dataMode_error_, 3)

            self.assertResultIsBOOL(GameCenter.GKMatch.sendDataToAllPlayers_withDataMode_error_)
            self.assertArgIsOut(GameCenter.GKMatch.sendDataToAllPlayers_withDataMode_error_, 2)

            self.assertArgIsBlock(GameCenter.GKMatch.chooseBestHostingPlayerWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(GameCenter.GKMatch.rematchWithCompletionHandler_, 0, b'v@@')

        @expectedFailureIf(os_release().rsplit('.', 1)[0] == '10.9')
        @min_os_level('10.9')
        def testMethods10_9(self):
            self.assertArgIsBlock(GameCenter.GKMatch.chooseBestHostPlayerWithCompletionHandler_, 0, b'v@')

            self.assertResultIsBOOL(GameCenter.GKMatch.sendData_toPlayers_withDataMode_error_)
            self.assertArgIsOut(GameCenter.GKMatch.sendData_toPlayers_withDataMode_error_, 3)

        @min_os_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('GKMatchDelegate')

            self.assertArgHasType(GKMatchDelegateHelper.match_player_didChangeConnectionState_, 2, objc._C_NSUInteger)
            self.assertArgHasType(GKMatchDelegateHelper.match_player_didChangeState_, 2, objc._C_NSUInteger)
            self.assertResultIsBOOL(GKMatchDelegateHelper.match_shouldReinviteDisconnectedPlayer_)
            self.assertResultIsBOOL(GKMatchDelegateHelper.match_shouldReinvitePlayer_)


if __name__ == "__main__":
    main()
