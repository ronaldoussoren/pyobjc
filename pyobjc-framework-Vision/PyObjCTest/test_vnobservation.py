from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision
from objc import simd


class TestVNObservation(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Vision.VNHumanBodyPose3DObservationHeightEstimation)
        self.assertEqual(
            Vision.VNHumanBodyPose3DObservationHeightEstimationReference, 0
        )
        self.assertEqual(Vision.VNHumanBodyPose3DObservationHeightEstimationMeasured, 1)

    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(Vision.VNRecognizedPointGroupKeyAll, str)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultHasType(
            Vision.VNImageHomographicAlignmentObservation.warpTransform,
            simd.simd_float3x3.__typestr__,
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

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(Vision.VNBarcodeObservation.isGS1DataCarrier)
        self.assertResultIsBOOL(Vision.VNBarcodeObservation.isColorInverted)

        self.assertArgIsOut(
            Vision.VNInstanceMaskObservation.generateMaskForInstances_error_, 1
        )

        self.assertArgIsBOOL(
            Vision.VNInstanceMaskObservation.generateMaskedImageOfInstances_fromRequestHandler_croppedToInstancesExtent_error_,
            2,
        )
        self.assertArgIsOut(
            Vision.VNInstanceMaskObservation.generateMaskedImageOfInstances_fromRequestHandler_croppedToInstancesExtent_error_,
            3,
        )

        self.assertArgIsOut(
            Vision.VNInstanceMaskObservation.generateScaledMaskForImageForInstances_fromRequestHandler_error_,
            2,
        )

        self.assertArgIsOut(
            Vision.VNAnimalBodyPoseObservation.recognizedPointForJointName_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNAnimalBodyPoseObservation.recognizedPointsForJointsGroupName_error_,
            1,
        )

        self.assertArgIsOut(
            Vision.VNRecognizedPoints3DObservation.recognizedPointForKey_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNRecognizedPoints3DObservation.recognizedPointsForGroupKey_error_, 1
        )

        self.assertArgIsOut(
            Vision.VNHumanBodyPose3DObservation.recognizedPointsForJointsGroupName_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNHumanBodyPose3DObservation.recognizedPointForJointName_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNHumanBodyPose3DObservation.pointInImageForJointName_error_, 1
        )

        self.assertResultIsBOOL(
            Vision.VNHumanBodyPose3DObservation.getCameraRelativePosition_forJointName_error_
        )
        self.assertArgIsOut(
            Vision.VNHumanBodyPose3DObservation.getCameraRelativePosition_forJointName_error_,
            0,
        )
        self.assertArgIsOut(
            Vision.VNHumanBodyPose3DObservation.getCameraRelativePosition_forJointName_error_,
            2,
        )
