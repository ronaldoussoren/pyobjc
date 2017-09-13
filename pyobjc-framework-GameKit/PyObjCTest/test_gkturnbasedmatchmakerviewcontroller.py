from PyObjCTools.TestSupport import *

import GameKit

class TestGKTurnBasedMatchmakerViewController (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKTurnBasedMatchmakerViewControllerDelegate')

    @min_os_level('10.8')
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKTurnBasedMatchmakerViewController.showExistingMatches)
        self.assertArgIsBOOL(GameKit.GKTurnBasedMatchmakerViewController.setShowExistingMatches_, 0)

if __name__ == "__main__":
    main()
