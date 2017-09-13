from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKLeaderboardViewController (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKLeaderboardViewControllerDelegate')


if __name__ == "__main__":
    main()
