import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import MultipeerConnectivity


class TestMCNearbyServiceAdvertiserDelegateHelper(MultipeerConnectivity.NSObject):
    def advertiser_didReceiveInvitationFromPeer_withContext_invitationHandler_(
        self, adv, recv, ctx, hdlr
    ):
        pass


class TestMCNearbyServiceAdvertiser(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(
            MultipeerConnectivity.MCNearbyServiceAdvertiser, objc.objc_class
        )

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertIsInstance(
            objc.protocolNamed("MCNearbyServiceAdvertiserDelegate"),
            objc.formal_protocol,
        )
        self.assertArgIsBlock(
            TestMCNearbyServiceAdvertiserDelegateHelper.advertiser_didReceiveInvitationFromPeer_withContext_invitationHandler_,
            3,
            b"v" + objc._C_NSBOOL + b"@",
        )
