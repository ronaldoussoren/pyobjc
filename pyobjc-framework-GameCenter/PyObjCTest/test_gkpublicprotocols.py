import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKPublicProtocolsHelper(GameCenter.NSObject):
    def session_peer_didChangeState_(self, s, p, st):
        pass

    def voiceChatService_didReceiveInvitationFromParticipantID_callID_(self, v, p, c):
        pass


class TestGCAchievement(TestCase):
    @min_os_level("10.8")
    def testProtocols(self):
        self.assertProtocolExists("GKSessionDelegate")
        self.assertProtocolExists("GKVoiceChatClient")

    def test_protocol_methods(self):
        self.assertArgHasType(
            GameCenter.TestGKPublicProtocolsHelper.session_peer_didChangeState_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            GameCenter.TestGKPublicProtocolsHelper.voiceChatService_didReceiveInvitationFromParticipantID_callID_,
            2,
            objc._C_NSUInteger,
        )
