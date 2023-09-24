import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVExternalStorageDevice(TestCase):
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
