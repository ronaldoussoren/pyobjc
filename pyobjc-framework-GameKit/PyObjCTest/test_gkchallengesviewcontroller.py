from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKAchievementViewController (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKChallengesViewControllerDelegate')

if __name__ == "__main__":
    main()
