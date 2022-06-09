from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEVPNConnection(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEVPNStatus)
        self.assertIsEnumType(NetworkExtension.NEVPNConnectionError)

    def testConstants(self):
        self.assertEqual(NetworkExtension.NEVPNStatusInvalid, 0)
        self.assertEqual(NetworkExtension.NEVPNStatusDisconnected, 1)
        self.assertEqual(NetworkExtension.NEVPNStatusConnecting, 2)
        self.assertEqual(NetworkExtension.NEVPNStatusConnected, 3)
        self.assertEqual(NetworkExtension.NEVPNStatusReasserting, 4)
        self.assertEqual(NetworkExtension.NEVPNStatusDisconnecting, 5)

        self.assertEqual(NetworkExtension.NEVPNConnectionErrorOverslept, 1)
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorNoNetworkAvailable, 2)
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorUnrecoverableNetworkChange, 3
        )
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorConfigurationFailed, 4)
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorServerAddressResolutionFailed, 5
        )
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorServerNotResponding, 6)
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorServerDead, 7)
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorAuthenticationFailed, 8)
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorClientCertificateInvalid, 9
        )
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorClientCertificateNotYetValid, 10
        )
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorClientCertificateExpired, 11
        )
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorPluginFailed, 12)
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorConfigurationNotFound, 13)
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorPluginDisabled, 14)
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorNegotiationFailed, 15)
        self.assertEqual(NetworkExtension.NEVPNConnectionErrorServerDisconnected, 16)
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorServerCertificateInvalid, 17
        )
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorServerCertificateNotYetValid, 18
        )
        self.assertEqual(
            NetworkExtension.NEVPNConnectionErrorServerCertificateExpired, 19
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(NetworkExtension.NEVPNStatusDidChangeNotification, str)
        self.assertIsInstance(NetworkExtension.NEVPNConnectionStartOptionUsername, str)
        self.assertIsInstance(NetworkExtension.NEVPNConnectionStartOptionPassword, str)

    @min_os_level("13.0")
    def testConstants13_0(self):
        self.assertIsInstance(NetworkExtension.NEVPNConnectionErrorDomain, str)

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEVPNConnection.startVPNTunnelAndReturnError_
        )
        self.assertArgIsOut(
            NetworkExtension.NEVPNConnection.startVPNTunnelAndReturnError_, 0
        )

        self.assertResultIsBOOL(
            NetworkExtension.NEVPNConnection.startVPNTunnelWithOptions_andReturnError_
        )
        self.assertArgIsOut(
            NetworkExtension.NEVPNConnection.startVPNTunnelWithOptions_andReturnError_,
            1,
        )

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsBlock(
            NetworkExtension.NEVPNConnection.fetchLastDisconnectErrorWithCompletionHandler_,
            0,
            b"v@",
        )
