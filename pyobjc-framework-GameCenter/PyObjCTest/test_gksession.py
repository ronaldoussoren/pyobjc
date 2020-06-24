import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKSession(TestCase):
    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertIsInstance(GameCenter.GKSession, objc.objc_class)
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
