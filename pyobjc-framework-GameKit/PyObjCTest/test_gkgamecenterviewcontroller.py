import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKGameCenterViewController(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameKit.GKGameCenterViewControllerState)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateDefault, -1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateLeaderboards, 0)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateAchievements, 1)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateChallenges, 2)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateLocalPlayerProfile, 3)
        self.assertEqual(GameKit.GKGameCenterViewControllerStateDashboard, 4)
        self.assertEqual(
            GameKit.GKGameCenterViewControllerStateLocalPlayerFriendsList, 5
        )

    def test_protocols(self):
        self.assertProtocolExists("GKGameCenterControllerDelegate", GameKit)
