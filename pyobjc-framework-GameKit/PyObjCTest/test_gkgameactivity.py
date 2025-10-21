from PyObjCTools.TestSupport import TestCase, min_os_level
import GameKit


class TestGKGameActivity(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsOut(
            GameKit.GKGameActivity.startWithDefinition_partyCode_error_, 2
        )
        self.assertArgIsOut(GameKit.GKGameActivity.startWithDefinition_error_, 1)
        self.assertResultIsBOOL(GameKit.GKGameActivity.isValidPartyCode_)

        self.assertArgIsBlock(
            GameKit.GKGameActivity.findMatchWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKGameActivity.findPlayersForHostedMatchWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKGameActivity.checkPendingGameActivityExistenceWithCompletionHandler_,
            0,
            b"vZ",
        )
