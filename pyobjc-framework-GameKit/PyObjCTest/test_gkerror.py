from PyObjCTools.TestSupport import *

import GameKit

class TestGKError (TestCase):

    def testConstants(self):
        self.assertEqual(GameKit.GKErrorUnknown, 1)
        self.assertEqual(GameKit.GKErrorCancelled, 2)
        self.assertEqual(GameKit.GKErrorCommunicationsFailure, 3)
        self.assertEqual(GameKit.GKErrorUserDenied, 4)
        self.assertEqual(GameKit.GKErrorInvalidCredentials, 5)
        self.assertEqual(GameKit.GKErrorNotAuthenticated, 6)
        self.assertEqual(GameKit.GKErrorAuthenticationInProgress, 7)
        self.assertEqual(GameKit.GKErrorInvalidPlayer, 8)
        self.assertEqual(GameKit.GKErrorScoreNotSet, 9)
        self.assertEqual(GameKit.GKErrorParentalControlsBlocked, 10)
        self.assertEqual(GameKit.GKErrorPlayerStatusExceedsMaximumLength, 11)
        self.assertEqual(GameKit.GKErrorPlayerStatusInvalid, 12)
        self.assertEqual(GameKit.GKErrorMatchRequestInvalid, 13)
        self.assertEqual(GameKit.GKErrorUnderage, 14)
        self.assertEqual(GameKit.GKErrorGameUnrecognized, 15)
        self.assertEqual(GameKit.GKErrorNotSupported, 16)
        self.assertEqual(GameKit.GKErrorInvalidParameter, 17)
        self.assertEqual(GameKit.GKErrorUnexpectedConnection, 18)
        self.assertEqual(GameKit.GKErrorChallengeInvalid, 19)
        self.assertEqual(GameKit.GKErrorTurnBasedMatchDataTooLarge, 20)
        self.assertEqual(GameKit.GKErrorTurnBasedTooManySessions, 21)
        self.assertEqual(GameKit.GKErrorTurnBasedInvalidParticipant, 22)
        self.assertEqual(GameKit.GKErrorTurnBasedInvalidTurn, 23)
        self.assertEqual(GameKit.GKErrorTurnBasedInvalidState, 24)
        self.assertEqual(GameKit.GKErrorInvitationsDisabled, 25)
        self.assertEqual(GameKit.GKErrorPlayerPhotoFailure, 26)
        self.assertEqual(GameKit.GKErrorUbiquityContainerUnavailable, 27)
        self.assertEqual(GameKit.GKErrorMatchNotConnected, 28)
        self.assertEqual(GameKit.GKErrorGameSessionRequestInvalid, 29)
        self.assertEqual(GameKit.GKErrorRestrictedToAutomatch, 30)

        self.assertEqual(GameKit.GKTournamentErrorUnknown, 1)
        self.assertEqual(GameKit.GKTournamentErrorInvalidTournament, 2)
        self.assertEqual(GameKit.GKTournamentErrorRegistrationNotOpen, 3)
        self.assertEqual(GameKit.GKTournamentErrorPlayerNotRegistered, 4)
        self.assertEqual(GameKit.GKTournamentErrorInvalidTournamentState, 5)
        self.assertEqual(GameKit.GKTournamentErrorInvalidParticipantState, 6)
        self.assertEqual(GameKit.GKTournamentErrorAlreadyRegistered, 7)
        self.assertEqual(GameKit.GKTournamentErrorDeviceConflict, 8)
        self.assertEqual(GameKit.GKTournamentErrorLocalPlayerCustomTournamentLimit, 9)
        self.assertEqual(GameKit.GKTournamentErrorNotEnoughPlayers, 10)
        self.assertEqual(GameKit.GKTournamentErrorCheatingDetected, 11)
        self.assertEqual(GameKit.GKTournamentErrorInvalidTryToken, 12)
        self.assertEqual(GameKit.GKTournamentErrorNetworkError, 13)
        self.assertEqual(GameKit.GKTournamentErrorNotSignedIntoICloud, 14)
        self.assertEqual(GameKit.GKTournamentErrorCKServerRecordChanged, 15)



if __name__ == "__main__":
    main()
