from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNERelayManager(TestCase):
    def test_constants(self):
        self.assertIsEnumType(NetworkExtension.NERelayManagerError)
        self.assertEqual(NetworkExtension.NERelayManagerErrorConfigurationInvalid, 1)
        self.assertEqual(NetworkExtension.NERelayManagerErrorConfigurationDisabled, 2)
        self.assertEqual(NetworkExtension.NERelayManagerErrorConfigurationStale, 3)
        self.assertEqual(
            NetworkExtension.NERelayManagerErrorConfigurationCannotBeRemoved, 4
        )

        self.assertIsEnumType(NetworkExtension.NERelayManagerClientError)
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorNone, 1)
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorDNSFailed, 2)
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorServerUnreachable, 3)
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorServerDisconnected, 4)
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorCertificateMissing, 5)
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorCertificateInvalid, 6)
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorCertificateExpired, 7)
        self.assertEqual(
            NetworkExtension.NERelayManagerClientErrorServerCertificateInvalid, 8
        )
        self.assertEqual(
            NetworkExtension.NERelayManagerClientErrorServerCertificateExpired, 9
        )
        self.assertEqual(NetworkExtension.NERelayManagerClientErrorOther, 10)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(NetworkExtension.NERelayErrorDomain, str)
        self.assertIsInstance(
            NetworkExtension.NERelayConfigurationDidChangeNotification, str
        )

    @min_os_level("15.0")
    def test_constants15_0(self):
        self.assertIsInstance(NetworkExtension.NERelayClientErrorDomain, str)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            NetworkExtension.NERelayManager.loadFromPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NERelayManager.removeFromPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NERelayManager.saveToPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )

        self.assertResultIsBOOL(NetworkExtension.NERelayManager.isEnabled)
        self.assertArgIsBOOL(NetworkExtension.NERelayManager.setEnabled_, 0)

        self.assertArgIsBlock(
            NetworkExtension.NERelayManager.loadAllManagersFromPreferencesWithCompletionHandler_,
            0,
            b"v@@",
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertArgIsBlock(
            NetworkExtension.NERelayManager.getLastClientErrors_completionHandler_,
            1,
            b"v@",
        )

    @min_os_level("15.4")
    def test_methods15_4(self):
        self.assertResultIsBOOL(NetworkExtension.NERelayManager.isUIToggleEnabled)
        self.assertArgIsBOOL(NetworkExtension.NERelayManager.setUIToggleEnabled_, 0)
