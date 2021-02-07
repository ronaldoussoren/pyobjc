import GameKit
import objc
from PyObjCTools.TestSupport import TestCase


class TestGKGameCenterViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKGameCenterControllerDelegate")

    def testConstants(self):
        self.assertEqual(GameKit.GKGameCenterViewControllerStateDefault, -1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateLeaderboards, 0)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateAchievements, 1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateChallenges, 2)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateLocalPlayerProfile, 3)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateDashboard, 4)
