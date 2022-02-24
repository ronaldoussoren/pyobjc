from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectHumanBodyPoseRequest(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Vision.VNHumanBodyPoseObservationJointName, str)
        self.assertIsTypedEnum(Vision.VNHumanBodyPoseObservationJointsGroupName, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Vision.VNBodyLandmarkKeyNose, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftEye, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightEye, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftEar, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightEar, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftShoulder, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightShoulder, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyNeck, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftElbow, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightElbow, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftWrist, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightWrist, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftHip, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightHip, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRoot, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftKnee, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightKnee, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyLeftAnkle, str)
        self.assertIsInstance(Vision.VNBodyLandmarkKeyRightAnkle, str)
        self.assertIsInstance(Vision.VNBodyLandmarkRegionKeyFace, str)
        self.assertIsInstance(Vision.VNBodyLandmarkRegionKeyTorso, str)
        self.assertIsInstance(Vision.VNBodyLandmarkRegionKeyLeftArm, str)
        self.assertIsInstance(Vision.VNBodyLandmarkRegionKeyRightArm, str)
        self.assertIsInstance(Vision.VNBodyLandmarkRegionKeyLeftLeg, str)
        self.assertIsInstance(Vision.VNBodyLandmarkRegionKeyRightLeg, str)

        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameNose, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameLeftEye, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRightEye, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameLeftEar, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRightEar, str)
        self.assertIsInstance(
            Vision.VNHumanBodyPoseObservationJointNameLeftShoulder, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPoseObservationJointNameRightShoulder, str
        )
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameNeck, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameLeftElbow, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRightElbow, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameLeftWrist, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRightWrist, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameLeftHip, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRightHip, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRoot, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameLeftKnee, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRightKnee, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameLeftAnkle, str)
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointNameRightAnkle, str)

        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointsGroupNameFace, str)
        self.assertIsInstance(
            Vision.VNHumanBodyPoseObservationJointsGroupNameTorso, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPoseObservationJointsGroupNameLeftArm, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPoseObservationJointsGroupNameRightArm, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPoseObservationJointsGroupNameLeftLeg, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPoseObservationJointsGroupNameRightLeg, str
        )
        self.assertIsInstance(Vision.VNHumanBodyPoseObservationJointsGroupNameAll, str)

        self.assertEqual(Vision.VNDetectHumanBodyPoseRequestRevision1, 1)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPoseRequest.supportedJointNamesForRevision_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPoseRequest.supportedJointsGroupNamesForRevision_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNHumanBodyPoseObservation.recognizedPointForJointName_error_, 1
        )
        self.assertArgIsOut(
            Vision.VNHumanBodyPoseObservation.recognizedPointsForJointsGroupName_error_,
            1,
        )
