import ImageCaptureCore
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    max_os_level,
)


class TestICDevice(TestCase):
    def test_enums(self):
        self.assertIsEnumType(ImageCaptureCore.ICDeviceType)
        self.assertEqual(ImageCaptureCore.ICDeviceTypeCamera, 0x00000001)
        self.assertEqual(ImageCaptureCore.ICDeviceTypeScanner, 0x00000002)

        self.assertIsEnumType(ImageCaptureCore.ICDeviceLocationType)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeLocal, 0x00000100)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeShared, 0x00000200)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeBonjour, 0x00000400)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeBluetooth, 0x00000800)

        self.assertIsEnumType(ImageCaptureCore.ICDeviceTypeMask)
        self.assertEqual(ImageCaptureCore.ICDeviceTypeMaskCamera, 0x00000001)
        self.assertEqual(ImageCaptureCore.ICDeviceTypeMaskScanner, 0x00000002)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeMaskLocal, 0x00000100)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeMaskShared, 0x00000200)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeMaskBonjour, 0x00000400)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeMaskBluetooth, 0x00000800)
        self.assertEqual(ImageCaptureCore.ICDeviceLocationTypeMaskRemote, 0x0000FE00)

    def test_typed_enums(self):
        self.assertIsTypedEnum(ImageCaptureCore.ICDeviceCapability, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICDeviceLocationOptions, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICDeviceStatus, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICDeviceTransport, str)
        self.assertIsTypedEnum(ImageCaptureCore.ICSessionOptions, str)

    def test_constants(self):
        self.assertIsInstance(ImageCaptureCore.ICTransportTypeUSB, str)
        self.assertIsInstance(ImageCaptureCore.ICTransportTypeFireWire, str)
        self.assertIsInstance(ImageCaptureCore.ICTransportTypeBluetooth, str)
        self.assertIsInstance(ImageCaptureCore.ICTransportTypeTCPIP, str)
        self.assertIsInstance(ImageCaptureCore.ICTransportTypeMassStorage, str)
        self.assertIsInstance(ImageCaptureCore.ICDeviceLocationDescriptionUSB, str)
        self.assertIsInstance(ImageCaptureCore.ICDeviceLocationDescriptionFireWire, str)
        self.assertIsInstance(
            ImageCaptureCore.ICDeviceLocationDescriptionBluetooth, str
        )
        self.assertIsInstance(
            ImageCaptureCore.ICDeviceLocationDescriptionMassStorage, str
        )
        self.assertIsInstance(ImageCaptureCore.ICButtonTypeScan, str)
        self.assertIsInstance(ImageCaptureCore.ICButtonTypeMail, str)
        self.assertIsInstance(ImageCaptureCore.ICButtonTypeCopy, str)
        self.assertIsInstance(ImageCaptureCore.ICButtonTypeWeb, str)
        self.assertIsInstance(ImageCaptureCore.ICButtonTypePrint, str)
        self.assertIsInstance(ImageCaptureCore.ICButtonTypeTransfer, str)
        self.assertIsInstance(ImageCaptureCore.ICStatusNotificationKey, str)
        self.assertIsInstance(ImageCaptureCore.ICLocalizedStatusNotificationKey, str)
        self.assertIsInstance(ImageCaptureCore.ICDeviceCanEjectOrDisconnect, str)
        self.assertIsInstance(ImageCaptureCore.ICStatusCodeKey, str)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(ImageCaptureCore.ICEnumerationChronologicalOrder, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(ImageCaptureCore.ICTransportTypeProximity, str)

    def test_methods(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICDevice.isRemote)
        self.assertResultIsBOOL(ImageCaptureCore.ICDevice.hasOpenSession)

        self.assertArgIsSEL(
            ImageCaptureCore.ICDevice.requestSendMessage_outData_maxReturnedDataSize_sendMessageDelegate_didSendMessageSelector_contextInfo_,  # noqa: B950
            4,
            b"v@:I@@^v",
        )

    @max_os_level("10.14")
    def test_methods_removed_in_10_15(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICDevice.isShared)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            ImageCaptureCore.ICDevice.requestOpenSessionWithOptions_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ImageCaptureCore.ICDevice.requestCloseSessionWithOptions_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ImageCaptureCore.ICDevice.requestEjectWithCompletion_, 0, b"v@"
        )

    def test_protocols(self):
        self.assertProtocolExists("ICDeviceDelegate", ImageCaptureCore)
