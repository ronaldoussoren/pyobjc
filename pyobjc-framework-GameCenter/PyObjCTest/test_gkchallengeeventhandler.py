from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import GameCenter
    import objc

    class GKChallengeEventHandlerDelegateHelper (GameCenter.NSObject):
        def shouldShowBannerForLocallyReceivedChallenge_(self, c): return 1
        def shouldShowBannerForLocallyCompletedChallenge_(self, c): return 1
        def shouldShowBannerForRemotelyCompletedChallenge_(self, c): return 1

    class TestGKChallengeEventHandler (TestCase):
        @min_os_level('10.8')
        def testClasses10_8(self):
            self.assertIsInstance(GameCenter.GKChallengeEventHandler, objc.objc_class)

        @min_os_level('10.8')
        def testProtocols10_8(self):
            objc.protocolNamed('GKChallengeEventHandlerDelegate')

            self.assertResultIsBOOL(GKChallengeEventHandlerDelegateHelper.shouldShowBannerForLocallyReceivedChallenge_)
            self.assertResultIsBOOL(GKChallengeEventHandlerDelegateHelper.shouldShowBannerForLocallyCompletedChallenge_)
            self.assertResultIsBOOL(GKChallengeEventHandlerDelegateHelper.shouldShowBannerForRemotelyCompletedChallenge_)

if __name__ == "__main__":
    main()
