from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKError(TestCase):
    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(GameCenter.GKErrorDomain, str)

        self.assertEqual(GameCenter.GKErrorUnknown, 1)
        self.assertEqual(GameCenter.GKErrorCancelled, 2)
        self.assertEqual(GameCenter.GKErrorCommunicationsFailure, 3)
        self.assertEqual(GameCenter.GKErrorUserDenied, 4)
        self.assertEqual(GameCenter.GKErrorInvalidCredentials, 5)
        self.assertEqual(GameCenter.GKErrorNotAuthenticated, 6)
        self.assertEqual(GameCenter.GKErrorAuthenticationInProgress, 7)
        self.assertEqual(GameCenter.GKErrorInvalidPlayer, 8)
        self.assertEqual(GameCenter.GKErrorScoreNotSet, 9)
        self.assertEqual(GameCenter.GKErrorParentalControlsBlocked, 10)
        self.assertEqual(GameCenter.GKErrorPlayerStatusExceedsMaximumLength, 11)
        self.assertEqual(GameCenter.GKErrorPlayerStatusInvalid, 12)
        self.assertEqual(GameCenter.GKErrorMatchRequestInvalid, 13)
        self.assertEqual(GameCenter.GKErrorUnderage, 14)
        self.assertEqual(GameCenter.GKErrorGameUnrecognized, 15)
        self.assertEqual(GameCenter.GKErrorNotSupported, 16)
        self.assertEqual(GameCenter.GKErrorInvalidParameter, 17)
        self.assertEqual(GameCenter.GKErrorUnexpectedConnection, 18)
        self.assertEqual(GameCenter.GKErrorChallengeInvalid, 19)
        self.assertEqual(GameCenter.GKErrorTurnBasedMatchDataTooLarge, 20)
        self.assertEqual(GameCenter.GKErrorTurnBasedTooManySessions, 21)
        self.assertEqual(GameCenter.GKErrorTurnBasedInvalidParticipant, 22)
        self.assertEqual(GameCenter.GKErrorTurnBasedInvalidTurn, 23)
        self.assertEqual(GameCenter.GKErrorTurnBasedInvalidState, 24)
        self.assertEqual(GameCenter.GKErrorInvitationsDisabled, 25)
        self.assertEqual(GameCenter.GKErrorPlayerPhotoFailure, 26)
        self.assertEqual(GameCenter.GKErrorUbiquityContainerUnavailable, 27)
