from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKEventListener (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKChallengeListener')


if __name__ == "__main__":
    main()
