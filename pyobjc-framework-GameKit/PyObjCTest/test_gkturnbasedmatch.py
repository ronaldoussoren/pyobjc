import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKTurnBasedMatchHelper(GameKit.NSObject):
    def player_receivedTurnEventForMatch_didBecomeActive_(self, p, m, a):
        pass

    def handleTurnEventForMatch_didBecomeActive_(self, m, a):
        pass


class TestGKTurnBasedMatch(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKTurnBasedExchangeStatus)
        self.assertIsEnumType(GameKit.GKTurnBasedMatchOutcome)
        self.assertIsEnumType(GameKit.GKTurnBasedMatchStatus)
        self.assertIsEnumType(GameKit.GKTurnBasedParticipantStatus)

    def testConstants(self):
        self.assertEqual(GameKit.GKTurnBasedMatchStatusUnknown, 0)
        self.assertEqual(GameKit.GKTurnBasedMatchStatusOpen, 1)
        self.assertEqual(GameKit.GKTurnBasedMatchStatusEnded, 2)
        self.assertEqual(GameKit.GKTurnBasedMatchStatusMatching, 3)

        self.assertEqual(GameKit.GKTurnBasedParticipantStatusUnknown, 0)
        self.assertEqual(GameKit.GKTurnBasedParticipantStatusInvited, 1)
        self.assertEqual(GameKit.GKTurnBasedParticipantStatusDeclined, 2)
        self.assertEqual(GameKit.GKTurnBasedParticipantStatusMatching, 3)
        self.assertEqual(GameKit.GKTurnBasedParticipantStatusActive, 4)
        self.assertEqual(GameKit.GKTurnBasedParticipantStatusDone, 5)

        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeNone, 0)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeQuit, 1)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeWon, 2)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeLost, 3)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeTied, 4)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeTimeExpired, 5)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeFirst, 6)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeSecond, 7)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeThird, 8)
        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeFourth, 9)

        self.assertEqual(GameKit.GKTurnBasedMatchOutcomeCustomRange, 0x00FF0000)

        self.assertEqual(GameKit.GKTurnBasedExchangeStatusUnknown, 0)
        self.assertEqual(GameKit.GKTurnBasedExchangeStatusActive, 1)
        self.assertEqual(GameKit.GKTurnBasedExchangeStatusComplete, 2)
        self.assertEqual(GameKit.GKTurnBasedExchangeStatusResolved, 3)
        self.assertEqual(GameKit.GKTurnBasedExchangeStatusCanceled, 4)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(GameKit.GKExchangeTimeoutDefault, float)
        self.assertIsInstance(GameKit.GKExchangeTimeoutNone, float)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(GameKit.GKTurnTimeoutDefault, float)
        self.assertIsInstance(GameKit.GKTurnTimeoutNone, float)

    def testProtocols(self):
        self.assertProtocolExists("GKTurnBasedEventListener")
        self.assertProtocolExists("GKTurnBasedEventHandlerDelegate")

    def testMethods(self):
        self.assertArgIsBOOL(
            TestGKTurnBasedMatchHelper.player_receivedTurnEventForMatch_didBecomeActive_,
            2,
        )
        self.assertArgIsBOOL(
            TestGKTurnBasedMatchHelper.handleTurnEventForMatch_didBecomeActive_, 1
        )

        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.findMatchForRequest_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.loadMatchesWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.removeWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.loadMatchDataWithCompletionHandler_, 0, b"v@@"
        )

        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.endMatchInTurnWithMatchData_completionHandler_,
            1,
            b"v@",
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.loadMatchWithID_withCompletionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.acceptInviteWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.declineInviteWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.saveCurrentTurnWithMatchData_completionHandler_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.endTurnWithNextParticipant_matchData_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.participantQuitInTurnWithOutcome_nextParticipant_matchData_completionHandler_,
            3,
            b"v@",
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.rematchWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.endTurnWithNextParticipants_turnTimeout_matchData_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.participantQuitInTurnWithOutcome_nextParticipants_turnTimeout_matchData_completionHandler_,
            4,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.participantQuitOutOfTurnWithOutcome_withCompletionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.endMatchInTurnWithMatchData_completionHandler_,
            1,
            b"v@",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.endMatchInTurnWithMatchData_scores_achievements_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.saveMergedMatchData_withResolvedExchanges_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.sendExchangeToParticipants_data_localizableMessageKey_arguments_timeout_completionHandler_,
            5,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedMatch.sendReminderToParticipants_localizableMessageKey_arguments_completionHandler_,
            3,
            b"v@",
        )

        self.assertArgIsBlock(
            GameKit.GKTurnBasedExchange.cancelWithLocalizableMessageKey_arguments_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameKit.GKTurnBasedExchange.replyWithLocalizableMessageKey_arguments_data_completionHandler_,
            3,
            b"v@",
        )
