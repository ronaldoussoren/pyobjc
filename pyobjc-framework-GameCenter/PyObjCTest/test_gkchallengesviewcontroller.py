import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure

import GameCenter


class TestGKChallengesViewController(TestCase):
    @expectedFailure
    @min_os_level("10.8")
    def test_classes10_8(self):
        self.assertIsInstance(GameCenter.GKChallengesViewController, objc.objc_class)

    @min_os_level("10.8")
    def test_protocols10_8(self):
        self.assertProtocolExists("GKChallengesViewControllerDelegate", GameCenter)
