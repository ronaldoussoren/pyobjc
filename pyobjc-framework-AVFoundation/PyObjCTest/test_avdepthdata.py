import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVDepthData(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVDepthDataAccuracy)
        self.assertIsEnumType(AVFoundation.AVDepthDataQuality)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVDepthDataQualityLow, 0)
        self.assertEqual(AVFoundation.AVDepthDataQualityHigh, 1)

        self.assertEqual(AVFoundation.AVDepthDataAccuracyRelative, 0)
        self.assertEqual(AVFoundation.AVDepthDataAccuracyAbsolute, 1)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(
            AVFoundation.AVDepthData.depthDataFromDictionaryRepresentation_error_,
            1,  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVDepthData.depthDataByReplacingDepthDataMapWithPixelBuffer_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVDepthData.dictionaryRepresentationForAuxiliaryDataType_,
            0,  # noqa: B950
        )
        self.assertResultIsBOOL(AVFoundation.AVDepthData.isDepthDataFiltered)
