import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKPublicConstants(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameKit.GKPeerConnectionState)
        self.assertEqual(GameKit.GKPeerStateAvailable, 0)
        self.assertEqual(GameKit.GKPeerStateUnavailable, 1)
        self.assertEqual(GameKit.GKPeerStateConnected, 2)
        self.assertEqual(GameKit.GKPeerStateDisconnected, 3)
        self.assertEqual(GameKit.GKPeerStateConnecting, 4)
        self.assertEqual(GameKit.GKPeerStateConnectedRelay, 5)

        self.assertIsEnumType(GameKit.GKSendDataMode)
        self.assertEqual(GameKit.GKSendDataReliable, 0)
        self.assertEqual(GameKit.GKSendDataUnreliable, 1)

        self.assertIsEnumType(GameKit.GKSessionMode)
        self.assertEqual(GameKit.GKSessionModeServer, 0)
        self.assertEqual(GameKit.GKSessionModeClient, 1)
        self.assertEqual(GameKit.GKSessionModePeer, 2)

    def test_constants(self):
        self.assertIsInstance(GameKit.GKVoiceChatServiceErrorDomain, str)
