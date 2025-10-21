import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAVExternalSyncDevice(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVFoundation.AVExternalSyncDeviceStatus)
        self.assertEqual(AVFoundation.AVExternalSyncDeviceStatusUnavailable, 0)
        self.assertEqual(AVFoundation.AVExternalSyncDeviceStatusReady, 1)
        self.assertEqual(AVFoundation.AVExternalSyncDeviceStatusCalibrating, 2)
        self.assertEqual(AVFoundation.AVExternalSyncDeviceStatusActiveSync, 3)
        self.assertEqual(AVFoundation.AVExternalSyncDeviceStatusFreeRunSync, 4)

    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVExternalSyncDeviceDiscoverySession.isSupported
        )

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("AVExternalSyncDeviceDelegate")
