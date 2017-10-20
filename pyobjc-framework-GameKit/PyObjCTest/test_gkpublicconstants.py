from PyObjCTools.TestSupport import *

import GameKit

class TestGKPublicConstants (TestCase):

    def testConstants(self):
        self.assertEqual(GameKit.GKSendDataReliable, 0)
        self.assertEqual(GameKit.GKSendDataUnreliable, 1)

        self.assertEqual(GameKit.GKSessionModeServer, 0)
        self.assertEqual(GameKit.GKSessionModeClient, 1)
        self.assertEqual(GameKit.GKSessionModePeer, 2)

        self.assertEqual(GameKit.GKPeerStateAvailable, 0)
        self.assertEqual(GameKit.GKPeerStateUnavailable, 1)
        self.assertEqual(GameKit.GKPeerStateConnected, 2)
        self.assertEqual(GameKit.GKPeerStateDisconnected, 3)
        self.assertEqual(GameKit.GKPeerStateConnecting, 4)

if __name__ == "__main__":
    main()
