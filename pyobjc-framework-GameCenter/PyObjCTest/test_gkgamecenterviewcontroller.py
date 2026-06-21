from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKGameCenterViewController(TestCase):
    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateDefault, -1)
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateLeaderboards, 0)
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateAchievements, 1)
        self.assertEqual(GameCenter.GKGameCenterViewControllerStateChallenges, 2)

    @min_os_level("10.9")
    def test_protocols10_9(self):
        self.assertProtocolExists("GKGameCenterControllerDelegate", GameCenter)
