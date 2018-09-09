from PyObjCTools.TestSupport import *
import VideoToolbox

class TestVTPixelTransferProperties (TestCase):
    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_ScalingMode, unicode)
        self.assertIsInstance(VideoToolbox.kVTScalingMode_Normal, unicode)
        self.assertIsInstance(VideoToolbox.kVTScalingMode_CropSourceToCleanAperture, unicode)
        self.assertIsInstance(VideoToolbox.kVTScalingMode_Letterbox, unicode)
        self.assertIsInstance(VideoToolbox.kVTScalingMode_Trim, unicode)
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_DestinationCleanAperture, unicode)
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_DestinationPixelAspectRatio, unicode)
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_DownsamplingMode, unicode)
        self.assertIsInstance(VideoToolbox.kVTDownsamplingMode_Decimate, unicode)
        self.assertIsInstance(VideoToolbox.kVTDownsamplingMode_Average, unicode)
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_DestinationColorPrimaries, unicode)
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_DestinationTransferFunction, unicode)
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_DestinationICCProfile, unicode)
        self.assertIsInstance(VideoToolbox.kVTPixelTransferPropertyKey_DestinationYCbCrMatrix, unicode)


if __name__ == "__main__":
    main()
