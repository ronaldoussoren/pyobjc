import VideoToolbox
from PyObjCTools.TestSupport import TestCase


class TestVTPixelTransferProperties(TestCase):
    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_ScalingMode, str)
        self.assertIsInstance(VideoToolbox.kVTScalingMode_Normal, str)
        self.assertIsInstance(
            VideoToolbox.kVTScalingMode_CropSourceToCleanAperture, str
        )
        self.assertIsInstance(VideoToolbox.kVTScalingMode_Letterbox, str)
        self.assertIsInstance(VideoToolbox.kVTScalingMode_Trim, str)
        self.assertIsInstance(
            VideoToolbox.kVTPixelTransferPropertyKey_DestinationCleanAperture, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTPixelTransferPropertyKey_DestinationPixelAspectRatio, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTPixelTransferPropertyKey_DownsamplingMode, str
        )
        self.assertIsInstance(VideoToolbox.kVTDownsamplingMode_Decimate, str)
        self.assertIsInstance(VideoToolbox.kVTDownsamplingMode_Average, str)
        self.assertIsInstance(
            VideoToolbox.kVTPixelTransferPropertyKey_DestinationColorPrimaries, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTPixelTransferPropertyKey_DestinationTransferFunction, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTPixelTransferPropertyKey_DestinationICCProfile, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTPixelTransferPropertyKey_DestinationYCbCrMatrix, str
        )
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_RealTime, str)
