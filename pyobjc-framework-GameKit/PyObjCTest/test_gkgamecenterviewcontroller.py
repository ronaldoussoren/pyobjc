import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKGameCenterViewController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKGameCenterViewControllerState)

    def testProtocols(self):
        self.assertProtocolExists("GKGameCenterControllerDelegate")

    def testConstants(self):
        self.assertEqual(GameKit.GKGameCenterViewControllerStateDefault, -1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateLeaderboards, 0)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateAchievements, 1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateChallenges, 2)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateLocalPlayerProfile, 3)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateDashboard, 4)
        self.assertEqual(
            GameKit.GKGameCenterViewControllerStateLocalPlayerFriendsList, 5
        )
