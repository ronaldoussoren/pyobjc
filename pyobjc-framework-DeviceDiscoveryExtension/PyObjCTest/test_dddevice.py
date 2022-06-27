from PyObjCTools.TestSupport import TestCase
import DeviceDiscoveryExtension


class TestDDDevice(TestCase):
    def test_constants(self):
        # self.assertIsTypedEnum(DeviceDiscoveryExtension.DDDeviceProtocolString, str)

        self.assertIsInstance(
            DeviceDiscoveryExtension.DDDeviceProtocolStringInvalid, str
        )
        self.assertIsInstance(DeviceDiscoveryExtension.DDDeviceProtocolStringDIAL, str)

        self.assertIsEnumType(DeviceDiscoveryExtension.DDDeviceFlags)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceFlagsNone, 0)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceFlagsSupportsAudio, 1 << 1)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceFlagsSupportsVideo, 1 << 2)

        self.assertIsEnumType(DeviceDiscoveryExtension.DDDeviceProtocol)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceProtocolInvalid, 0)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceProtocolDIAL, 1)

        self.assertIsEnumType(DeviceDiscoveryExtension.DDDeviceCategory)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceCategoryHiFiSpeaker, 0)
        self.assertEqual(
            DeviceDiscoveryExtension.DDDeviceCategoryHiFiSpeakerMultiple, 1
        )
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceCategoryTVWithMediaBox, 2)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceCategoryTV, 3)

        self.assertIsEnumType(DeviceDiscoveryExtension.DDDeviceState)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceStateInvalid, 0)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceStateActivating, 10)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceStateActivated, 20)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceStateAuthorized, 25)
        self.assertEqual(DeviceDiscoveryExtension.DDDeviceStateInvalidating, 30)

    def test_functions(self):
        # DeviceDiscoveryExtension.DDDeviceFlagsToString
        DeviceDiscoveryExtension.DDDeviceProtocolToString
        DeviceDiscoveryExtension.DDDeviceCategoryToString
        DeviceDiscoveryExtension.DDDeviceStateToString
