from PyObjCTools.TestSupport import *

import objc
import GameKit

class TestGKChallengeEventHandlerHelper (GameKit.NSObject):
    def shouldShowBannerForLocallyReceivedChallenge_(self, a): return 1
    def shouldShowBannerForLocallyCompletedChallenge_(self, a): return 1
    def shouldShowBannerForRemotelyCompletedChallenge_(self, a): return 1



class TestGKChallengeEventHandler (TestCase):
    def testProtocols(self):
        objc.protocolNamed('GKChallengeEventHandlerDelegate')

    def testProtocolMethods(self):
        self.assertResultIsBOOL(TestGKChallengeEventHandlerHelper.shouldShowBannerForLocallyReceivedChallenge_)
        self.assertResultIsBOOL(TestGKChallengeEventHandlerHelper.shouldShowBannerForLocallyCompletedChallenge_)
        self.assertResultIsBOOL(TestGKChallengeEventHandlerHelper.shouldShowBannerForRemotelyCompletedChallenge_)


if __name__ == "__main__":
    main()
