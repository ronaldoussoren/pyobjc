import GameKit
import objc
from PyObjCTools.TestSupport import *


class TestGKLeaderboardViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKLeaderboardViewControllerDelegate")


if __name__ == "__main__":
    main()
