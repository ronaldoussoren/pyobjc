import CoreMediaIO
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestCMIOExtensionStreamHelper(CoreMediaIO.NSObject):
    def streamPropertiesForProperties_error_(self, a, b):
        return 1

    def setStreamProperties_error_(self, a, b):
        return 1

    def authorizedToStartStreamForClient_(self, a):
        return 1

    def startStreamAndReturnError_(self, a):
        return 1

    def stopStreamAndReturnError_(self, a):
        return 1


class TestCMIOExtensionStream(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreMediaIO.CMIOExtensionStreamDirection)
        self.assertIsEnumType(CoreMediaIO.CMIOExtensionStreamClockType)
        self.assertIsEnumType(CoreMediaIO.CMIOExtensionStreamDiscontinuityFlags)

    def test_constants(self):
        self.assertEqual(CoreMediaIO.CMIOExtensionStreamDirectionSource, 0)
        self.assertEqual(CoreMediaIO.CMIOExtensionStreamDirectionSink, 1)

        self.assertEqual(CoreMediaIO.CMIOExtensionStreamClockTypeHostTime, 0)
        self.assertEqual(
            CoreMediaIO.CMIOExtensionStreamClockTypeLinkedCoreAudioDeviceUID, 1
        )
        self.assertEqual(CoreMediaIO.CMIOExtensionStreamClockTypeCustom, 2)

        self.assertEqual(CoreMediaIO.CMIOExtensionStreamDiscontinuityFlagNone, 0)
        self.assertEqual(
            CoreMediaIO.CMIOExtensionStreamDiscontinuityFlagUnknown, 1 << 0
        )
        self.assertEqual(CoreMediaIO.CMIOExtensionStreamDiscontinuityFlagTime, 1 << 1)
        self.assertEqual(
            CoreMediaIO.CMIOExtensionStreamDiscontinuityFlagSampleDropped, 1 << 6
        )

    @min_sdk_level("12.3")
    def test_protocols(self):
        self.assertProtocolExists("CMIOExtensionStreamSource")

    def test_methods(self):
        self.assertArgHasType(
            TestCMIOExtensionStreamHelper.streamPropertiesForProperties_error_,
            1,
            b"o^@",
        )

        self.assertResultIsBOOL(
            TestCMIOExtensionStreamHelper.setStreamProperties_error_
        )
        self.assertArgHasType(
            TestCMIOExtensionStreamHelper.setStreamProperties_error_, 1, b"o^@"
        )

        self.assertResultIsBOOL(
            TestCMIOExtensionStreamHelper.authorizedToStartStreamForClient_
        )

        self.assertResultIsBOOL(
            TestCMIOExtensionStreamHelper.startStreamAndReturnError_
        )
        self.assertArgHasType(
            TestCMIOExtensionStreamHelper.startStreamAndReturnError_, 0, b"o^@"
        )

        self.assertResultIsBOOL(TestCMIOExtensionStreamHelper.stopStreamAndReturnError_)
        self.assertArgHasType(
            TestCMIOExtensionStreamHelper.stopStreamAndReturnError_, 0, b"o^@"
        )

    @min_os_level("12.3")
    def test_methods12_3(self):
        self.assertArgIsBlock(
            CoreMediaIO.CMIOExtensionStream.consumeSampleBufferFromClient_completionHandler_,
            1,
            b"v^{opaqueCMSampleBuffer=}QIZ@",
        )
