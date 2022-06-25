import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKPublicProtocolsHelper(GameKit.NSObject):
    def session_peer_didChangeState_(self, s, p, st):
        pass


class TestGKPublicProtocols(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKSessionDelegate")
        self.assertProtocolExists("GKVoiceChatClient")

    def testMethods(self):
        self.assertArgHasType(
            TestGKPublicProtocolsHelper.session_peer_didChangeState_, 2, b"i"
        )
