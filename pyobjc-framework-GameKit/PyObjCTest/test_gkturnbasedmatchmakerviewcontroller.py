import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestGKTurnBasedMatchmakerViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKTurnBasedMatchmakerViewControllerDelegate")

    @min_os_level("10.8")
    def testMethods(self):
        self.assertResultIsBOOL(
            GameKit.GKTurnBasedMatchmakerViewController.showExistingMatches
        )
        self.assertArgIsBOOL(
            GameKit.GKTurnBasedMatchmakerViewController.setShowExistingMatches_, 0
        )
