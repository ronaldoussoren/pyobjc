from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKGameSessionEventListener (TestCase):
    @min_sdk_level('10.12')
    def testProtocols(self):
        objc.protocolNamed('GKGameSessionEventListener')


if __name__ == "__main__":
    main()
