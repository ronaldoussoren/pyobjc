from PyObjCTools.TestSupport import *

import GameKit

class TestGKPublicProtocolsHelper (GameKit.NSObject):
    def session_peer_didChangeState_(self, s, p, st): pass

class TestGKPublicProtocols (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKSessionDelegate')
        objc.protocolNamed('GKVoiceChatClient')

    def testMethods(self):
        self.assertArgHasType(TestGKPublicProtocolsHelper.session_peer_didChangeState_, 2, b'i')

if __name__ == "__main__":
    main()
