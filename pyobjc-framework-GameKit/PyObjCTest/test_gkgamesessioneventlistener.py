from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKGameSessionEventListener (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKGameSessionEventListener')


if __name__ == "__main__":
    main()
