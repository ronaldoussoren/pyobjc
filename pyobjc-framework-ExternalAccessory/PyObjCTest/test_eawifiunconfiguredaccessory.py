from PyObjCTools.TestSupport import TestCase

import ExternalAccessory


class TestEAWiFiUnconfiguredAccessory(TestCase):
    def test_enums(self):
        self.assertIsEnumType(ExternalAccessory.EAWiFiUnconfiguredAccessoryProperties)
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryPropertySupportsAirPlay, 1 << 0
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryPropertySupportsAirPrint,
            1 << 1,
        )
        self.assertEqual(
            ExternalAccessory.EAWiFiUnconfiguredAccessoryPropertySupportsHomeKit, 1 << 2
        )
