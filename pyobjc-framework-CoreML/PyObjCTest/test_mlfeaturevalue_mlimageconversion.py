from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLFeatureValue_MLImageConversion(TestCase):
    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(CoreML.MLFeatureValueImageOptionCropRect, str)
        self.assertIsInstance(CoreML.MLFeatureValueImageOptionCropAndScale, str)

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithImageAtURL_pixelsWide_pixelsHigh_pixelFormatType_options_error_,
            5,
        )
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithImageAtURL_constraint_options_error_,
            3,
        )
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithCGImage_pixelsWide_pixelsHigh_pixelFormatType_options_error_,
            5,
        )
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithCGImage_constraint_options_error_, 3
        )
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithImageAtURL_orientation_pixelsWide_pixelsHigh_pixelFormatType_options_error_,
            6,
        )
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithImageAtURL_orientation_constraint_options_error_,
            4,
        )
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithCGImage_orientation_pixelsWide_pixelsHigh_pixelFormatType_options_error_,
            6,
        )
        self.assertArgIsOut(
            CoreML.MLFeatureValue.featureValueWithCGImage_orientation_constraint_options_error_,
            4,
        )
