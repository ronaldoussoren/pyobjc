import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKTurnBasedMatchmakerViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists(
            "GKTurnBasedMatchmakerViewControllerDelegate", GameKit
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            GameKit.GKTurnBasedMatchmakerViewController.showExistingMatches
        )
        self.assertArgIsBOOL(
            GameKit.GKTurnBasedMatchmakerViewController.setShowExistingMatches_, 0
        )
