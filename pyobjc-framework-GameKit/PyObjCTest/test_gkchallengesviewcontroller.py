import GameKit
import objc
from PyObjCTools.TestSupport import *


class TestGKAchievementViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKChallengesViewControllerDelegate")


if __name__ == "__main__":
    main()
