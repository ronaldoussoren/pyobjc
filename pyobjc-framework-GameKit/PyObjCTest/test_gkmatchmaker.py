from PyObjCTools.TestSupport import *

import GameKit

class TestGKMatchMaker (TestCase):

    def testConstants(self):
        self.assertEqual(GameKit.GKInviteRecipientResponseAccepted, 0)
        self.assertEqual(GameKit.GKInviteRecipientResponseDeclined, 1)
        self.assertEqual(GameKit.GKInviteRecipientResponseFailed, 2)
        self.assertEqual(GameKit.GKInviteRecipientResponseIncompatible, 3)
        self.assertEqual(GameKit.GKInviteRecipientResponseUnableToConnect, 4)
        self.assertEqual(GameKit.GKInviteRecipientResponseNoAnswer, 5)

        self.assertEqual(GameKit.GKInviteeResponseAccepted, GameKit.GKInviteRecipientResponseAccepted)
        self.assertEqual(GameKit.GKInviteeResponseDeclined, GameKit.GKInviteRecipientResponseDeclined)
        self.assertEqual(GameKit.GKInviteeResponseFailed, GameKit.GKInviteRecipientResponseFailed)
        self.assertEqual(GameKit.GKInviteeResponseIncompatible, GameKit.GKInviteRecipientResponseIncompatible)
        self.assertEqual(GameKit.GKInviteeResponseUnableToConnect, GameKit.GKInviteRecipientResponseUnableToConnect)
        self.assertEqual(GameKit.GKInviteeResponseNoAnswer, GameKit.GKInviteRecipientResponseNoAnswer)

        self.assertEqual(GameKit.GKMatchTypePeerToPeer, 0)
        self.assertEqual(GameKit.GKMatchTypeHosted, 1)
        self.assertEqual(GameKit.GKMatchTypeTurnBased, 2)


    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods(self):
        self.assertArgIsBlock(GameKit.GKMatchmaker.addPlayersToMatch_matchRequest_completionHandler_, 2, b'v@')
        self.assertArgIsBlock(GameKit.GKMatchmaker.queryPlayerGroupActivity_withCompletionHandler_, 1, b'v' + objc._C_NSInteger + b'@')
        self.assertArgIsBlock(GameKit.GKMatchmaker.queryActivityWithCompletionHandler_, 0, b'v' + objc._C_NSInteger + b'@')

    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_8(self):
	# XXX: These aren't available on 10.9, even though the SDK claims they are
        self.assertResultIsBlock(GameKit.GKMatchmaker.inviteHandler, b'v@@')
        self.assertArgIsBlock(GameKit.GKMatchmaker.setInviteHandler_, 0, b'v@@')

        self.assertArgIsBlock(GameKit.GKMatchmaker.findPlayersForHostedMatchRequest_withCompletionHandler_, 1, b'v@@')


    @onlyOn64Bit
    @min_os_level('10.10')
    def testMethods10_9(self):	
	# XXX: These aren't available on 10.9, even though the SDK claims they are
        self.assertArgIsBlock(GameKit.GKMatchmaker.matchForInvite_completionHandler_, 1, b'v@@')

        self.assertArgIsBlock(GameKit.GKMatchmaker.matchForInvite_completionHandler_, 1, b'v@@')

        self.assertArgIsBlock(GameKit.GKMatchmaker.startBrowsingForNearbyPlayersWithReachableHandler_, 0, b'v@Z')

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBlock(GameKit.GKMatchRequest.recipientResponseHandler, b'v@' + objc._C_NSInteger)
        self.assertArgIsBlock(GameKit.GKMatchRequest.setRecipientResponseHandler_, 0, b'v@' + objc._C_NSInteger)
        self.assertResultIsBlock(GameKit.GKMatchRequest.inviteeResponseHandler, b'v@' + objc._C_NSInteger)
        self.assertArgIsBlock(GameKit.GKMatchRequest.setInviteeResponseHandler_, 0, b'v@' + objc._C_NSInteger)

        self.assertArgIsBlock(GameKit.GKMatchmaker.findPlayersForHostedRequest_withCompletionHandler_, 1, b'v@@')
        self.assertArgIsBlock(GameKit.GKMatchmaker.startBrowsingForNearbyPlayersWithHandler_, 0, b'v@Z')

    def testProtocols(self):
        objc.protocolNamed('GKInviteEventListener')

if __name__ == "__main__":
    main()
