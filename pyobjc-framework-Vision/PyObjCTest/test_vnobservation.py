from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNObservation(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(Vision.VNRecognizedPointGroupKeyAll, str)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(
            Vision.VNClassificationObservation.hasMinimumRecall_forPrecision_
        )
        self.assertResultIsBOOL(
            Vision.VNClassificationObservation.hasMinimumPrecision_forRecall_
        )

        self.assertArgIsOut(Vision.VNRecognizedText.boundingBoxForRange_error_, 1)

        self.assertResultIsBOOL(
            Vision.VNFeaturePrintObservation.computeDistance_toFeaturePrintObservation_error_  # noqa: B950
        )
        self.assertArgIsOut(
            Vision.VNFeaturePrintObservation.computeDistance_toFeaturePrintObservation_error_,  # noqa: B950
            2,
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsOut(Vision.VNContoursObservation.contourAtIndex_error_, 1)
        self.assertArgIsOut(Vision.VNContoursObservation.contourAtIndexPath_error_, 1)

        self.assertArgIsOut(
            Vision.VNRecognizedPointsObservation.recognizedPointsForGroupKey_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNRecognizedPointsObservation.keypointsMultiArrayAndReturnError_, 0
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(Vision.VNHumanObservation.upperBodyOnly)
