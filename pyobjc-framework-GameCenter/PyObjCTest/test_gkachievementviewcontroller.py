from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKAchievementViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKAchievementViewControllerDelegate", GameCenter)
