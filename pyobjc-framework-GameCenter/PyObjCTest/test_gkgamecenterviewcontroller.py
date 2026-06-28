from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKGameCenterViewController(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameCenter.GKGameCenterViewControllerState)
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateDefault, -1)
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateLeaderboards, 0)
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateAchievements, 1)
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateChallenges, 2)

    def test_protocols(self):
        self.assertProtocolExists("GKGameCenterControllerDelegate", GameCenter)
