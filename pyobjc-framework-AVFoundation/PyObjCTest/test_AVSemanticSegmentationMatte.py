from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVSemanticSegmentationMatte(TestCase):
    @min_os_level("10.15")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVSemanticSegmentationMatteTypeSkin, unicode)
        self.assertIsInstance(AVFoundation.AVSemanticSegmentationMatteTypeHair, unicode)
        self.assertIsInstance(
            AVFoundation.AVSemanticSegmentationMatteTypeTeeth, unicode
        )

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsOut(
            AVFoundation.AVSemanticSegmentationMatte.semanticSegmentationMatteFromImageSourceAuxiliaryDataType_dictionaryRepresentation_error_,
            2,
        )

        self.assertArgIsOut(
            AVFoundation.AVSemanticSegmentationMatte.semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer_error_,
            1,
        )


if __name__ == "__main__":
    main()
