from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter
    import objc

    class TestGKTurnBasedMatchmakerViewController (TestCase):
        @min_os_level('10.8')
        def testClasses10_8(self):
            self.assertIsInstance(GameCenter.GKTurnBasedMatchmakerViewController, objc.objc_class)

            self.assertResultIsBOOL(GameCenter.GKTurnBasedMatchmakerViewController.showExistingMatches)
            self.assertArgIsBOOL(GameCenter.GKTurnBasedMatchmakerViewController.setShowExistingMatches_, 0)

        @min_os_level('10.8')
        def testProtocols10_8(self):
            objc.protocolNamed('GKTurnBasedMatchmakerViewControllerDelegate')

if __name__ == "__main__":
    main()
