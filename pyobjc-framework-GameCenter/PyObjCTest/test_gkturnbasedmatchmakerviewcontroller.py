from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKTurnBasedMatchmakerViewController(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            GameCenter.GKTurnBasedMatchmakerViewController.showExistingMatches
        )
        self.assertArgIsBOOL(
            GameCenter.GKTurnBasedMatchmakerViewController.setShowExistingMatches_, 0
        )

    def test_protocols10_8(self):
        self.assertProtocolExists(
            "GKTurnBasedMatchmakerViewControllerDelegate", GameCenter
        )
