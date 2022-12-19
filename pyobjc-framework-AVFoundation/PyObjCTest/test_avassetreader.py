import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetReader(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVSampleBufferRequestDirection)
        self.assertIsEnumType(AVFoundation.AVSampleBufferRequestMode)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(AVFoundation.AVAssetReaderStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetReaderStatusReading, 1)
        self.assertEqual(AVFoundation.AVAssetReaderStatusCompleted, 2)
        self.assertEqual(AVFoundation.AVAssetReaderStatusFailed, 3)
        self.assertEqual(AVFoundation.AVAssetReaderStatusCancelled, 4)

    @min_os_level("10.7")
    def testMethods(self):
        self.assertArgIsOut(AVFoundation.AVAssetReader.assetReaderWithAsset_error_, 1)
        self.assertArgIsOut(AVFoundation.AVAssetReader.initWithAsset_error_, 1)
        self.assertResultIsBOOL(AVFoundation.AVAssetReader.canAddOutput_)
        self.assertResultIsBOOL(AVFoundation.AVAssetReader.startReading)

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureSession.isMultitaskingCameraAccessSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureSession.isMultitaskingCameraAccessEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureSession.setMultitaskingCameraAccessEnabled_, 0
        )
