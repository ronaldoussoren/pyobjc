from PyObjCTools.TestSupport import TestCase

import ExternalAccessory


class TestEAWiFiUnconfiguredAccessoryBrowser(TestCase):
    def test_enums(self):
        self.assertIsEnumType(ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserState)
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateWiFiUnavailable, 0
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateStopped, 1
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateSearching, 2
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateConfiguring, 3
        )

        self.assertIsEnumType(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatus
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatusSuccess, 0
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatusUserCancelledConfiguration,
            1,
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatusFailed, 2
        )

    def test_protocols(self):
        self.assertProtocolExists(
            "EAWiFiUnconfiguredAccessoryBrowserDelegate", ExternalAccessory
        )
