import objc
from PyObjCTools.TestSupport import TestCase

import ExternalAccessory


class TestEAWiFiUnconfiguredAccessoryBrowser(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserState)
        self.assertIsEnumType(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatus
        )

    def testProtocols(self):
        objc.protocolNamed("EAWiFiUnconfiguredAccessoryBrowserDelegate")

    def testConstants(self):
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

    def testMethods(self):
        # Not on macOS:
        # self.assertArgIsBlock(ExternalAccessory.EAAccessoryManager.showBluetoothAccessoryPickerWithNameFilter_completion_, 1, b'v@')   # noqa: B950
        pass
