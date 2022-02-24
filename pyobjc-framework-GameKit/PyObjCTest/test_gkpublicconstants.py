import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKPublicConstants(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKPeerConnectionState)
        self.assertIsEnumType(GameKit.GKSendDataMode)
        self.assertIsEnumType(GameKit.GKSessionMode)
        self.assertIsEnumType(GameKit.GKVoiceChatServiceError)

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
        self.assertEqual(GameKit.GKPeerStateConnectedRelay, 5)

        self.assertIsInstance(GameKit.GKVoiceChatServiceErrorDomain, str)
