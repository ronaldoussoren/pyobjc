from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter
    import objc

    class TestGKPublicProtocolsHelper (GameCenter.NSObject):
        def session_peer_didChangeState_(self, s, p, st): pass

        def voiceChatService_didReceiveInvitationFromParticipantID_callID_(self, v, p, c): pass


    class TestGCAchievement (TestCase):
        @min_os_level('10.8')
        def testProtocols(self):
            objc.protocolNamed('GKSessionDelegate')

            self.assertArgHasType(GameCenter.TestGKPublicProtocolsHelper.session_peer_didChangeState_, 2, objc._C_NSUInteger)

            objc.protocolNamed('GKVoiceChatClient')
            self.assertArgHasType(GameCenter.TestGKPublicProtocolsHelper.voiceChatService_didReceiveInvitationFromParticipantID_callID_, 2, objc._C_NSUInteger)

if __name__ == "__main__":
    main()
