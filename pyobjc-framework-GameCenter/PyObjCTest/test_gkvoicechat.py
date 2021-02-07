from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)
import objc

import GameCenter


class TestGKVoiceChat(TestCase):
    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(GameCenter.GKVoiceChatPlayerConnected, 0)
        self.assertEqual(GameCenter.GKVoiceChatPlayerDisconnected, 1)
        self.assertEqual(GameCenter.GKVoiceChatPlayerSpeaking, 2)
        self.assertEqual(GameCenter.GKVoiceChatPlayerSilent, 3)
        self.assertEqual(GameCenter.GKVoiceChatPlayerConnecting, 4)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.9")
    @min_os_level("10.8")
    def testMethods10_8(self):
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
