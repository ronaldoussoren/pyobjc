import objc
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)

import GameCenter


class TestGKMatchmaker(TestCase):
    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertEqual(GameCenter.GKInviteRecipientResponseAccepted, 0)
        self.assertEqual(GameCenter.GKInviteRecipientResponseDeclined, 1)
        self.assertEqual(GameCenter.GKInviteRecipientResponseFailed, 2)
        self.assertEqual(GameCenter.GKInviteRecipientResponseIncompatible, 3)
        self.assertEqual(GameCenter.GKInviteRecipientResponseUnableToConnect, 4)
        self.assertEqual(GameCenter.GKInviteRecipientResponseNoAnswer, 5)

        self.assertEqual(
            GameCenter.GKInviteeResponseAccepted,
            GameCenter.GKInviteRecipientResponseAccepted,
        )
        self.assertEqual(
            GameCenter.GKInviteeResponseDeclined,
            GameCenter.GKInviteRecipientResponseDeclined,
        )
        self.assertEqual(
            GameCenter.GKInviteeResponseFailed,
            GameCenter.GKInviteRecipientResponseFailed,
        )
        self.assertEqual(
            GameCenter.GKInviteeResponseIncompatible,
            GameCenter.GKInviteRecipientResponseIncompatible,
        )
        self.assertEqual(
            GameCenter.GKInviteeResponseUnableToConnect,
            GameCenter.GKInviteRecipientResponseUnableToConnect,
        )
        self.assertEqual(
            GameCenter.GKInviteeResponseNoAnswer,
            GameCenter.GKInviteRecipientResponseNoAnswer,
        )

        self.assertEqual(GameCenter.GKMatchTypePeerToPeer, 0)
        self.assertEqual(GameCenter.GKMatchTypeHosted, 1)
        self.assertEqual(GameCenter.GKMatchTypeTurnBased, 2)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.9")
    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(GameCenter.GKInvite.isHosted)

        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.matchForInvite_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.findMatchForRequest_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.addPlayersToMatch_matchRequest_completionHandler_,
            2,
            b"v@",
        )
        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.queryPlayerGroupActivity_withCompletionHandler_,
            1,
            b"v" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.queryActivityWithCompletionHandler_,
            0,
            b"v" + objc._C_NSInteger + b"@",
        )

        self.assertResultIsBlock(GameCenter.GKMatchmaker.inviteHandler, b"v@@")
        self.assertArgIsBlock(GameCenter.GKMatchmaker.setInviteHandler_, 0, b"v@@")

        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.findPlayersForHostedMatchRequest_withCompletionHandler_,
            1,
            b"v@@",
        )

    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.9")
    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.startBrowsingForNearbyPlayersWithReachableHandler_,
            0,
            b"v@Z",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBlock(
            GameCenter.GKMatchRequest.recipientResponseHandler,
            b"v@" + objc._C_NSUInteger,
        )
        self.assertResultIsBlock(
            GameCenter.GKMatchRequest.inviteeResponseHandler, b"v@" + objc._C_NSUInteger
        )

        self.assertArgIsBlock(
            GameCenter.GKMatchRequest.setRecipientResponseHandler_,
            0,
            b"v@" + objc._C_NSUInteger,
        )
        self.assertArgIsBlock(
            GameCenter.GKMatchRequest.setInviteeResponseHandler_,
            0,
            b"v@" + objc._C_NSUInteger,
        )

        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.findPlayersForHostedRequest_withCompletionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameCenter.GKMatchmaker.startBrowsingForNearbyPlayersWithHandler_, 0, b"v@Z"
        )

    @min_os_level("10.8")
    def testProtocols(self):
        self.assertProtocolExists("GKInviteEventListener")
