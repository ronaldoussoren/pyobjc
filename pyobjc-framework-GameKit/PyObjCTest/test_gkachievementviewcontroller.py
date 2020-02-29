import GameKit
import objc
from PyObjCTools.TestSupport import *


class TestGKAchievementViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKAchievementViewControllerDelegate")


if __name__ == "__main__":
    main()
