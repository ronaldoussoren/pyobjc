import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVSemanticSegmentationMatte(TestCase):
    @min_os_level("10.15")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVSemanticSegmentationMatteTypeSkin, str)
        self.assertIsInstance(AVFoundation.AVSemanticSegmentationMatteTypeHair, str)
        self.assertIsInstance(AVFoundation.AVSemanticSegmentationMatteTypeTeeth, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(AVFoundation.AVSemanticSegmentationMatteTypeGlasses, str)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsOut(
            AVFoundation.AVSemanticSegmentationMatte.semanticSegmentationMatteFromImageSourceAuxiliaryDataType_dictionaryRepresentation_error_,  # noqa: B950
            2,
        )

        self.assertArgIsOut(
            AVFoundation.AVSemanticSegmentationMatte.semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer_error_,  # noqa: B950
            1,
        )
