from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKSession(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(GameCenter.GKSession.isAvailable)
        self.assertArgIsBOOL(GameCenter.GKSession.setAvailable_, 0)

        self.assertResultIsBOOL(
            GameCenter.GKSession.sendData_toPeers_withDataMode_error_
        )
        self.assertArgIsOut(
            GameCenter.GKSession.sendData_toPeers_withDataMode_error_, 3
        )

        self.assertResultIsBOOL(
            GameCenter.GKSession.sendDataToAllPeers_withDataMode_error_
        )
        self.assertArgIsOut(
            GameCenter.GKSession.sendDataToAllPeers_withDataMode_error_, 2
        )

        self.assertResultIsBOOL(GameCenter.GKSession.acceptConnectionFromPeer_error_)
        self.assertArgIsOut(GameCenter.GKSession.acceptConnectionFromPeer_error_, 1)
