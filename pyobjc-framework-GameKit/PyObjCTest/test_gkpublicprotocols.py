import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKPublicProtocolsHelper(GameKit.NSObject):
    def session_peer_didChangeState_(self, s, p, st):
        pass


class TestGKPublicProtocols(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKSessionDelegate", GameKit)
        self.assertProtocolExists("GKVoiceChatClient", GameKit)

    def testMethods(self):
        self.assertArgHasType(
            TestGKPublicProtocolsHelper.session_peer_didChangeState_, 2, b"i"
        )
