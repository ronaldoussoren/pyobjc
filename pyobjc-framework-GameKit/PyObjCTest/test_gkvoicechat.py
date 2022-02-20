import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestGKVoiceChat(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKVoiceChatPlayerState)

    def testConstants(self):
        self.assertEqual(GameKit.GKVoiceChatPlayerConnected, 0)
        self.assertEqual(GameKit.GKVoiceChatPlayerDisconnected, 1)
        self.assertEqual(GameKit.GKVoiceChatPlayerSpeaking, 2)
        self.assertEqual(GameKit.GKVoiceChatPlayerSilent, 3)
        self.assertEqual(GameKit.GKVoiceChatPlayerConnecting, 4)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBOOL(GameKit.GKVoiceChat.setPlayer_muted_, 1)

        self.assertArgIsBlock(
            GameKit.GKVoiceChat.setPlayerVoiceChatStateDidChangeHandler_,
            0,
            b"v@" + objc._C_NSInteger,
        )
        self.assertResultIsBlock(
            GameKit.GKVoiceChat.playerVoiceChatStateDidChangeHandler,
            b"v@" + objc._C_NSInteger,
        )

    @min_os_level("10.10")
    def testMethods10_8(self):
        # XXX: For some reason most of these aren't actually available when testing on 10.9
        self.assertArgIsBOOL(GameKit.GKVoiceChat.setActive_, 0)
        self.assertResultIsBOOL(GameKit.GKVoiceChat.isActive)

        self.assertResultIsBOOL(GameKit.GKVoiceChat.isVoIPAllowed)

        self.assertArgIsBlock(
            GameKit.GKVoiceChat.setPlayerStateUpdateHandler_,
            0,
            b"v@" + objc._C_NSInteger,
        )
        self.assertResultIsBlock(
            GameKit.GKVoiceChat.playerStateUpdateHandler, b"v@" + objc._C_NSInteger
        )

        self.assertArgIsBOOL(GameKit.GKVoiceChat.setMute_forPlayer_, 0)
