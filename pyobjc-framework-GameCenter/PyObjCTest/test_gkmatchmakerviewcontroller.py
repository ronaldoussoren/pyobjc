from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKMatchmakerViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKMatchmakerViewControllerDelegate", GameCenter)

    def test_methods(self):
        self.assertResultIsBOOL(GameCenter.GKMatchmakerViewController.isHosted)
        self.assertArgIsBOOL(GameCenter.GKMatchmakerViewController.setHosted_, 0)
        self.assertArgIsBOOL(
            GameCenter.GKMatchmakerViewController.setHostedPlayer_connected_, 1
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertArgIsBOOL(
            GameCenter.GKMatchmakerViewController.setHostedPlayer_didConnect_, 1
        )
