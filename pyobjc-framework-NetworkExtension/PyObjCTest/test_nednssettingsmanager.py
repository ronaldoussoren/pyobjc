from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEDNSSettingsManager(TestCase):
    def test_constants(self):
        self.assertEqual(
            NetworkExtension.NEDNSSettingsManagerErrorConfigurationInvalid, 1
        )
        self.assertEqual(
            NetworkExtension.NEDNSSettingsManagerErrorConfigurationDisabled, 2
        )
        self.assertEqual(
            NetworkExtension.NEDNSSettingsManagerErrorConfigurationStale, 3
        )
        self.assertEqual(
            NetworkExtension.NEDNSSettingsManagerErrorConfigurationCannotBeRemoved, 4
        )

    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(NetworkExtension.NEDNSSettingsErrorDomain, str)
        self.assertIsInstance(
            NetworkExtension.NEDNSSettingsConfigurationDidChangeNotification, str
        )

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            NetworkExtension.NEDNSSettingsManager.loadFromPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEDNSSettingsManager.removeFromPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEDNSSettingsManager.saveToPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )

        self.assertResultIsBOOL(NetworkExtension.NEDNSSettingsManager.isEnabled)
