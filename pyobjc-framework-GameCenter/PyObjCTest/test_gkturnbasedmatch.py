import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter


class TestGKTurnBasedMatchHelper(GameCenter.NSObject):
    def player_receivedTurnEventForMatch_didBecomeActive_(self, p, m, a):
        pass

    def handleTurnEventForMatch_didBecomeActive_(self, m, a):
        pass


class TestGKTurnBasedMatch(TestCase):
    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(GameCenter.GKTurnBasedMatchStatusUnknown, 0)
        self.assertEqual(GameCenter.GKTurnBasedMatchStatusOpen, 1)
        self.assertEqual(GameCenter.GKTurnBasedMatchStatusEnded, 2)
        self.assertEqual(GameCenter.GKTurnBasedMatchStatusMatching, 3)

        self.assertEqual(GameCenter.GKTurnBasedParticipantStatusUnknown, 0)
        self.assertEqual(GameCenter.GKTurnBasedParticipantStatusInvited, 1)
        self.assertEqual(GameCenter.GKTurnBasedParticipantStatusDeclined, 2)
        self.assertEqual(GameCenter.GKTurnBasedParticipantStatusMatching, 3)
        self.assertEqual(GameCenter.GKTurnBasedParticipantStatusActive, 4)
        self.assertEqual(GameCenter.GKTurnBasedParticipantStatusDone, 5)

        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeNone, 0)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeQuit, 1)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeWon, 2)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeLost, 3)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeTied, 4)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeTimeExpired, 5)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeFirst, 6)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeSecond, 7)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeThird, 8)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeFourth, 9)
        self.assertEqual(GameCenter.GKTurnBasedMatchOutcomeCustomRange, 0x00FF0000)

        self.assertEqual(GameCenter.GKTurnBasedExchangeStatusUnknown, 0)
        self.assertEqual(GameCenter.GKTurnBasedExchangeStatusActive, 1)
        self.assertEqual(GameCenter.GKTurnBasedExchangeStatusComplete, 2)
        self.assertEqual(GameCenter.GKTurnBasedExchangeStatusResolved, 3)
        self.assertEqual(GameCenter.GKTurnBasedExchangeStatusCanceled, 4)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(GameCenter.GKTurnTimeoutDefault, float)
        self.assertIsInstance(GameCenter.GKTurnTimeoutNone, float)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(GameCenter.GKExchangeTimeoutDefault, float)
        self.assertIsInstance(GameCenter.GKExchangeTimeoutNone, float)

    @min_os_level("10.8")
    def testProtocols(self):
        objc.protocolNamed("GKTurnBasedEventListener")

        self.assertArgIsBOOL(
            TestGKTurnBasedMatchHelper.player_receivedTurnEventForMatch_didBecomeActive_,
            2,
        )

        objc.protocolNamed("GKTurnBasedEventHandlerDelegate")
        self.assertArgIsBOOL(
            TestGKTurnBasedMatchHelper.handleTurnEventForMatch_didBecomeActive_, 1
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.findMatchForRequest_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.loadMatchesWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.loadMatchWithID_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.acceptInviteWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.declineInviteWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.removeWithCompletionHandler_, 0, b"v@"
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.loadMatchDataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.participantQuitOutOfTurnWithOutcome_withCompletionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.endMatchInTurnWithMatchData_completionHandler_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.saveCurrentTurnWithMatchData_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.endTurnWithNextParticipant_matchData_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.participantQuitInTurnWithOutcome_nextParticipant_matchData_completionHandler_,
            3,
            b"v@",
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.rematchWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.endTurnWithNextParticipants_turnTimeout_matchData_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.participantQuitInTurnWithOutcome_nextParticipants_turnTimeout_matchData_completionHandler_,
            4,
            b"v@",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.endMatchInTurnWithMatchData_scores_achievements_completionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.saveMergedMatchData_withResolvedExchanges_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.sendExchangeToParticipants_data_localizableMessageKey_arguments_timeout_completionHandler_,
            5,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedMatch.sendReminderToParticipants_localizableMessageKey_arguments_completionHandler_,
            3,
            b"v@",
        )

        self.assertArgIsBlock(
            GameCenter.GKTurnBasedExchange.cancelWithLocalizableMessageKey_arguments_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKTurnBasedExchange.replyWithLocalizableMessageKey_arguments_data_completionHandler_,
            3,
            b"v@",
        )
