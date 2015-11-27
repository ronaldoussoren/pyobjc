from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter

    class TestGKError (TestCase):
        @min_os_level('10.8')
        def testConstants10_8(self):
            self.assertEqual(GameCenter.GKSendDataReliable, 0)
            self.assertEqual(GameCenter.GKSendDataUnreliable, 1)

            self.assertEqual(GameCenter.GKSessionModeServer, 0)
            self.assertEqual(GameCenter.GKSessionModeClient, 1)
            self.assertEqual(GameCenter.GKSessionModePeer, 2)

            self.assertEqual(GameCenter.GKPeerStateAvailable, 0)
            self.assertEqual(GameCenter.GKPeerStateUnavailable, 1)
            self.assertEqual(GameCenter.GKPeerStateConnected, 2)
            self.assertEqual(GameCenter.GKPeerStateDisconnected, 3)
            self.assertEqual(GameCenter.GKPeerStateConnecting, 4)

            self.assertEqual(GameCenter.GKVoiceChatServiceInternalError, 32000)
            self.assertEqual(GameCenter.GKVoiceChatServiceNoRemotePacketsError, 32001)
            self.assertEqual(GameCenter.GKVoiceChatServiceUnableToConnectError, 32002)
            self.assertEqual(GameCenter.GKVoiceChatServiceRemoteParticipantHangupError, 32003)
            self.assertEqual(GameCenter.GKVoiceChatServiceInvalidCallIDError, 32004)
            self.assertEqual(GameCenter.GKVoiceChatServiceAudioUnavailableError, 32005)
            self.assertEqual(GameCenter.GKVoiceChatServiceUninitializedClientError, 32006)
            self.assertEqual(GameCenter.GKVoiceChatServiceClientMissingRequiredMethodsError, 32007)
            self.assertEqual(GameCenter.GKVoiceChatServiceRemoteParticipantBusyError, 32008)
            self.assertEqual(GameCenter.GKVoiceChatServiceRemoteParticipantCancelledError, 32009)
            self.assertEqual(GameCenter.GKVoiceChatServiceRemoteParticipantResponseInvalidError, 32010)
            self.assertEqual(GameCenter.GKVoiceChatServiceRemoteParticipantDeclinedInviteError, 32011)
            self.assertEqual(GameCenter.GKVoiceChatServiceMethodCurrentlyInvalidError, 32012)
            self.assertEqual(GameCenter.GKVoiceChatServiceNetworkConfigurationError, 32013)
            self.assertEqual(GameCenter.GKVoiceChatServiceUnsupportedRemoteVersionError, 32014)
            self.assertEqual(GameCenter.GKVoiceChatServiceOutOfMemoryError, 32015)
            self.assertEqual(GameCenter.GKVoiceChatServiceInvalidParameterError, 32016)

if __name__ == "__main__":
    main()
