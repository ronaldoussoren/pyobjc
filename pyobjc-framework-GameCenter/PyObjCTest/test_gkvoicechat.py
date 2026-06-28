from PyObjCTools.TestSupport import (
    TestCase,
    os_release,
    expectedFailureIf,
)
import objc

import GameCenter


class TestGKVoiceChat(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameCenter.GKVoiceChatPlayerState)
        self.assertEqual(GameCenter.GKVoiceChatPlayerConnected, 0)
        self.assertEqual(GameCenter.GKVoiceChatPlayerDisconnected, 1)
        self.assertEqual(GameCenter.GKVoiceChatPlayerSpeaking, 2)
        self.assertEqual(GameCenter.GKVoiceChatPlayerSilent, 3)
        self.assertEqual(GameCenter.GKVoiceChatPlayerConnecting, 4)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.9")
    def test_methods(self):
        self.assertArgIsBOOL(GameCenter.GKVoiceChat.setPlayer_muted_, 1)

        self.assertResultIsBlock(
            GameCenter.GKVoiceChat.playerVoiceChatStateDidChangeHandler, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKVoiceChat.setPlayerVoiceChatStateDidChangeHandler_, 0, b"v@@"
        )

        self.assertResultIsBOOL(GameCenter.GKVoiceChat.isActive)
        self.assertArgIsBOOL(GameCenter.GKVoiceChat.setActive_, 0)

        self.assertResultIsBOOL(GameCenter.GKVoiceChat.isVoIPAllowed)

        self.assertResultIsBlock(
            GameCenter.GKVoiceChat.playerStateUpdateHandler, b"v@" + objc._C_NSUInteger
        )
        self.assertArgIsBlock(
            GameCenter.GKVoiceChat.setPlayerStateUpdateHandler_,
            0,
            b"v@" + objc._C_NSUInteger,
        )

        self.assertArgIsBOOL(GameCenter.GKVoiceChat.setMute_forPlayer_, 0)
