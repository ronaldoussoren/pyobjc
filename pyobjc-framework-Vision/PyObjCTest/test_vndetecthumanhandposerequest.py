from PyObjCTools.TestSupport import TestCase, os_level_between
import Vision


class TestVNDetectHumanHandPoseRequest(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Vision.VNHumanHandPoseObservationJointName, str)
        self.assertIsTypedEnum(Vision.VNHumanHandPoseObservationJointsGroupName, str)

    @os_level_between("11.0", "11.5")
    def test_constants11_0(self):
        # self.assertIsInstance(Vision.VNHandLandmarkKeyThumbCMC, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyThumbMP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyThumbIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyThumbTIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyIndexMCP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyIndexPIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyIndexDIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyIndexTIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyMiddleMCP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyMiddlePIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyMiddleDIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyMiddleTIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyRingMCP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyRingPIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyRingDIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyRingTIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyLittleMCP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyLittlePIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyLittleDIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkKeyLittleTIP, str)
        self.assertIsInstance(Vision.VNHandLandmarkRegionKeyThumb, str)
        self.assertIsInstance(Vision.VNHandLandmarkRegionKeyMiddleFinger, str)
        self.assertIsInstance(Vision.VNHandLandmarkRegionKeyIndexFinger, str)
        self.assertIsInstance(Vision.VNHandLandmarkRegionKeyRingFinger, str)
        self.assertIsInstance(Vision.VNHandLandmarkRegionKeyLittleFinger, str)

        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameWrist, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameThumbCMC, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameThumbMP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameThumbIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameThumbTip, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameIndexMCP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameIndexPIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameIndexDIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameIndexTip, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameMiddleMCP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameMiddlePIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameMiddleDIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameMiddleTip, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameRingMCP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameRingPIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameRingDIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameRingTip, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameLittleMCP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameLittlePIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameLittleDIP, str)
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointNameLittleTip, str)

        self.assertIsInstance(
            Vision.VNHumanHandPoseObservationJointsGroupNameThumb, str
        )
        self.assertIsInstance(
            Vision.VNHumanHandPoseObservationJointsGroupNameIndexFinger, str
        )
        self.assertIsInstance(
            Vision.VNHumanHandPoseObservationJointsGroupNameMiddleFinger, str
        )
        self.assertIsInstance(
            Vision.VNHumanHandPoseObservationJointsGroupNameRingFinger, str
        )
        self.assertIsInstance(
            Vision.VNHumanHandPoseObservationJointsGroupNameLittleFinger, str
        )
        self.assertIsInstance(Vision.VNHumanHandPoseObservationJointsGroupNameAll, str)

        self.assertEqual(Vision.VNDetectHumanHandPoseRequestRevision1, 1)

    @os_level_between("11.0", "11.5")
    def test_methods11_0(self):
        self.assertArgIsOut(
            Vision.VNDetectHumanHandPoseRequest.supportedRecognizedPointKeysForRevision_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanHandPoseRequest.supportedRecognizedPointGroupKeysForRevision_error_,
            1,
        )

        self.assertArgIsOut(
            Vision.VNDetectHumanHandPoseRequest.supportedIdentifiedPointKeysForRevision_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanHandPoseRequest.supportedIdentifiedPointGroupKeysForRevision_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanHandPoseRequest.supportedJointNamesForRevision_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanHandPoseRequest.supportedJointsGroupNamesForRevision_error_,
            1,
        )

        self.assertArgIsOut(
            Vision.VNHumanHandPoseObservation.recognizedPointForJointName_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNHumanHandPoseObservation.recognizedPointsForJointsGroupName_error_,
            1,
        )
