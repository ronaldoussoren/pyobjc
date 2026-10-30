import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVExternalStorageDevice(TestCase):
    def test_enum_types(self):
        self.assertIsTypedEnum(
            AVFoundation.AVExternalStorageDeviceReasonNotRecommendedForCaptureUse, str
        )

    @min_os_level("27.0")
    def test_constants(self):
        self.assertIsInstance(
            AVFoundation.AVExternalStorageDeviceReasonNotRecommendedForCaptureUseEncrypted,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVExternalStorageDeviceReasonNotRecommendedForCaptureUseUnsupportedFileSystem,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVExternalStorageDeviceReasonNotRecommendedForCaptureUseSlowWritingSpeed,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVExternalStorageDeviceReasonNotRecommendedForCaptureUseUnknownWritingSpeed,
            str,
        )

    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVExternalStorageDevice.isConnected)
        self.assertResultIsBOOL(
            AVFoundation.AVExternalStorageDevice.isNotRecommendedForCaptureUse
        )

        self.assertArgIsOut(
            AVFoundation.AVExternalStorageDevice.nextAvailableURLsWithPathExtensions_error_,
            1,
        )

        self.assertArgIsBlock(
            AVFoundation.AVExternalStorageDevice.requestAccessWithCompletionHandler_,
            0,
            b"vZ",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVExternalStorageDeviceDiscoverySession.isSupported
        )
