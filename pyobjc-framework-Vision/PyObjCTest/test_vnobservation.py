from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision
from objc import simd


class TestVNObservation(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(Vision.VNRecognizedPointGroupKeyAll, str)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgHasType(
            Vision.VNImageHomographicAlignmentObservation.warpTransform,
            simd.matrix_float3x3.__typestr__,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
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
        self.assertResultHasType(
            Vision.VNTrajectoryObservation.equationCoefficients,
            simd.simd_float3.__typestr__,
        )

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
