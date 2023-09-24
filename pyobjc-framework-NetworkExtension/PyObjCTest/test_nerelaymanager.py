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

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(NetworkExtension.NERelayErrorDomain, str)
        self.assertIsInstance(
            NetworkExtension.NERelayConfigurationDidChangeNotification, str
        )

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
