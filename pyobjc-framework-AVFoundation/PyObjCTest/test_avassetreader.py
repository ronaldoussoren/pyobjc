import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetReader(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AVFoundation.AVAssetReaderStatus)
        self.assertEqual(AVFoundation.AVAssetReaderStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetReaderStatusReading, 1)
        self.assertEqual(AVFoundation.AVAssetReaderStatusCompleted, 2)
        self.assertEqual(AVFoundation.AVAssetReaderStatusFailed, 3)
        self.assertEqual(AVFoundation.AVAssetReaderStatusCancelled, 4)

    def test_methods(self):
        self.assertArgIsOut(AVFoundation.AVAssetReader.assetReaderWithAsset_error_, 1)
        self.assertArgIsOut(AVFoundation.AVAssetReader.initWithAsset_error_, 1)
        self.assertResultIsBOOL(AVFoundation.AVAssetReader.canAddOutput_)
        self.assertResultIsBOOL(AVFoundation.AVAssetReader.startReading)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureSession.isMultitaskingCameraAccessSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureSession.isMultitaskingCameraAccessEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureSession.setMultitaskingCameraAccessEnabled_, 0
        )
