import objc
from PyObjCTools.TestSupport import TestCase, min_os_level
import MultipeerConnectivity


class TestMCSessionHelper(MultipeerConnectivity.NSObject):
    def session_didReceiveCertificate_fromPeer_certificateHandler_(self, s, c, p, h):
        pass

    def session_peer_didChangeState_(self, session, peer, state):
        pass


class TestMCSession(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(MultipeerConnectivity.MCSession, objc.objc_class)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBOOL(
            MultipeerConnectivity.MCSession.sendData_toPeers_withMode_error_
        )
        self.assertArgIsBlock(
            MultipeerConnectivity.MCSession.sendResourceAtURL_withName_toPeer_withCompletionHandler_,
            3,
            b"v@",
        )
        self.assertArgIsOut(
            MultipeerConnectivity.MCSession.startStreamWithName_toPeer_error_, 2
        )

        self.assertArgIsBlock(
            MultipeerConnectivity.MCSession.nearbyConnectionDataForPeer_withCompletionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("MCSessionDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMCSessionHelper.session_peer_didChangeState_, 2, objc._C_NSUInteger
        )

        self.assertArgIsBlock(
            TestMCSessionHelper.session_didReceiveCertificate_fromPeer_certificateHandler_,
            3,
            b"v" + objc._C_NSBOOL,
        )

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(MultipeerConnectivity.MCSessionSendDataReliable, 0)
        self.assertEqual(MultipeerConnectivity.MCSessionSendDataUnreliable, 1)
        self.assertEqual(MultipeerConnectivity.MCSessionStateNotConnected, 0)
        self.assertEqual(MultipeerConnectivity.MCSessionStateConnecting, 1)
        self.assertEqual(MultipeerConnectivity.MCSessionStateConnected, 2)
        self.assertEqual(MultipeerConnectivity.MCEncryptionOptional, 0)
        self.assertEqual(MultipeerConnectivity.MCEncryptionRequired, 1)
        self.assertEqual(MultipeerConnectivity.MCEncryptionNone, 2)
        self.assertIsInstance(MultipeerConnectivity.kMCSessionMinimumNumberOfPeers, int)
        self.assertIsInstance(MultipeerConnectivity.kMCSessionMaximumNumberOfPeers, int)
