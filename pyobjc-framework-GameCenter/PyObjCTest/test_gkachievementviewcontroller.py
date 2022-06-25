from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import GameCenter


class TestGKAchievementViewController(TestCase):
    @min_os_level("10.8")
    def testClasses10_8(self):
        self.assertIsInstance(GameCenter.GKAchievementViewController, objc.objc_class)

    @min_os_level("10.8")
    def testProtocols10_8(self):
        self.assertProtocolExists("GKAchievementViewControllerDelegate")
