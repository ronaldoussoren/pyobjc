import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKPublicProtocolsHelper(GameKit.NSObject):
    def session_peer_didChangeState_(self, s, p, st):
        pass


class TestGKPublicProtocols(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKSessionDelegate", GameKit)
        self.assertProtocolExists("GKVoiceChatClient", GameKit)

    def test_methods(self):
        self.assertArgHasType(
            TestGKPublicProtocolsHelper.session_peer_didChangeState_, 2, b"i"
        )
