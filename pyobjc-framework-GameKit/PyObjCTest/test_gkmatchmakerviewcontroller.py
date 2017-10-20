from PyObjCTools.TestSupport import *

import GameKit

class TestGKMatchmakerViewController (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKMatchmakerViewController.isHosted)
        self.assertArgIsBOOL(GameKit.GKMatchmakerViewController.setHosted_, 0)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertArgIsBOOL(GameKit.GKMatchmakerViewController.setHostedPlayer_connected_, 1)


    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBOOL(GameKit.GKMatchmakerViewController.setHostedPlayer_didConnect_, 1)

    def testProtocols(self):
        objc.protocolNamed('GKMatchmakerViewControllerDelegate')

if __name__ == "__main__":
    main()
