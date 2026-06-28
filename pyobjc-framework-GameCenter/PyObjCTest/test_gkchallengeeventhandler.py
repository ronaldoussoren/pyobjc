from PyObjCTools.TestSupport import TestCase

import GameCenter


class GKChallengeEventHandlerDelegateHelper(GameCenter.NSObject):
    def shouldShowBannerForLocallyReceivedChallenge_(self, c):
        return 1

    def shouldShowBannerForLocallyCompletedChallenge_(self, c):
        return 1

    def shouldShowBannerForRemotelyCompletedChallenge_(self, c):
        return 1


class TestGKChallengeEventHandler(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKChallengeEventHandlerDelegate", GameCenter)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(
            GKChallengeEventHandlerDelegateHelper.shouldShowBannerForLocallyReceivedChallenge_
        )
        self.assertResultIsBOOL(
            GKChallengeEventHandlerDelegateHelper.shouldShowBannerForLocallyCompletedChallenge_
        )
        self.assertResultIsBOOL(
            GKChallengeEventHandlerDelegateHelper.shouldShowBannerForRemotelyCompletedChallenge_
        )
