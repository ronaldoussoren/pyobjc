from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKGameCenterViewController (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKGameCenterControllerDelegate')

    def testConstants(self):
        self.assertEqual(GameKit.GKGameCenterViewControllerStateDefault, -1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateLeaderboards, 0)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateAchievements, 1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateChallenges, 2)

if __name__ == "__main__":
    main()
