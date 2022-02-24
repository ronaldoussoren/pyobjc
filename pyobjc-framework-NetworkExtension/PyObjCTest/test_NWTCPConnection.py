from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc

import NetworkExtension


class TestNWTCPConnectionHelper(NetworkExtension.NSObject):
    def shouldProvideIdentityForConnection_(self, c):
        return 1

    def provideIdentityForConnection_completionHandler_(self, c, h):
        pass

    def shouldEvaluateTrustForConnection_(self, c):
        return 1

    def evaluateTrustForConnection_peerCertificateChain_completionHandler_(
        self, c, ch, h
    ):
        pass


class TestNWTCPConnection(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NWTCPConnectionState)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(NetworkExtension.NWTCPConnectionStateInvalid, 0)
        self.assertEqual(NetworkExtension.NWTCPConnectionStateConnecting, 1)
        self.assertEqual(NetworkExtension.NWTCPConnectionStateWaiting, 2)
        self.assertEqual(NetworkExtension.NWTCPConnectionStateConnected, 3)
        self.assertEqual(NetworkExtension.NWTCPConnectionStateDisconnected, 4)
        self.assertEqual(NetworkExtension.NWTCPConnectionStateCancelled, 5)

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(NetworkExtension.NWTCPConnection.isViable)
        self.assertResultIsBOOL(NetworkExtension.NWTCPConnection.hasBetterPath)

        self.assertArgIsBlock(
            NetworkExtension.NWTCPConnection.readLength_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            NetworkExtension.NWTCPConnection.readMinimumLength_maximumLength_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NWTCPConnection.write_completionHandler_, 1, b"v@"
        )

        self.assertResultIsBOOL(
            TestNWTCPConnectionHelper.shouldProvideIdentityForConnection_
        )
        self.assertArgIsBlock(
            TestNWTCPConnectionHelper.provideIdentityForConnection_completionHandler_,
            1,
            b"v@@",
        )
        self.assertResultIsBOOL(
            TestNWTCPConnectionHelper.shouldEvaluateTrustForConnection_
        )
        self.assertArgIsBlock(
            TestNWTCPConnectionHelper.evaluateTrustForConnection_peerCertificateChain_completionHandler_,
            2,
            b"v@",
        )

    @min_sdk_level("10.11")
    def testProtocols(self):
        objc.protocolNamed("NWTCPConnectionAuthenticationDelegate")
