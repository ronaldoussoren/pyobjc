from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import GameCenter


class TestGKAchievementViewController(TestCase):
    @min_os_level("10.8")
    def test_classes10_8(self):
        self.assertIsInstance(GameCenter.GKAchievementViewController, objc.objc_class)

    @min_os_level("10.8")
    def test_protocols10_8(self):
        self.assertProtocolExists("GKAchievementViewControllerDelegate", GameCenter)
