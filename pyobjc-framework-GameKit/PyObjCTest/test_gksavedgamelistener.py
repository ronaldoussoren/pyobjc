from PyObjCTools.TestSupport import *

import GameKit

class TestGKSavedGameListener (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKSavedGameListener')

if __name__ == "__main__":
    main()
