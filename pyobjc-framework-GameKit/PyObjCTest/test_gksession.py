import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKSession(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKSession.isAvailable)
        self.assertArgIsBOOL(GameKit.GKSession.setAvailable_, 0)

        self.assertResultIsBOOL(GameKit.GKSession.sendData_toPeers_withDataMode_error_)
        self.assertArgIsOut(GameKit.GKSession.sendData_toPeers_withDataMode_error_, 3)

        self.assertResultIsBOOL(
            GameKit.GKSession.sendDataToAllPeers_withDataMode_error_
        )
        self.assertArgIsOut(GameKit.GKSession.sendDataToAllPeers_withDataMode_error_, 2)

        self.assertResultIsBOOL(GameKit.GKSession.acceptConnectionFromPeer_error_)
        self.assertArgIsOut(GameKit.GKSession.acceptConnectionFromPeer_error_, 1)
