from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectHumanBodyPoseRequest(TestCase):
    @min_os_level("10.16")
    def testConstants10_16(self):

        self.assertIsInsteance(Vision.VNBodyLandmarkKeyNose, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftEye, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightEye, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftEar, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightEar, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftShoulder, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightShoulder, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyNeck, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftElbow, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightElbow, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftWrist, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightWrist, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftHip, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightHip, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRoot, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftKnee, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightKnee, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyLeftAnkle, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkKeyRightAnkle, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkRegionKeyFace, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkRegionKeyTorso, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkRegionKeyLeftArm, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkRegionKeyRightArm, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkRegionKeyLeftLeg, str)
        self.assertIsInsteance(Vision.VNBodyLandmarkRegionKeyRightLeg, str)

        self.assertEqual(Vision.VNDetectHumanBodyPoseRequestRevision1, 1)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPoseRequest.supportedRecognizedPointKeysForRevision_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPoseRequest.supportedRecognizedPointGroupKeysForRevision_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPoseRequest.supportedIdentifiedPointKeysForRevision_error_,
            1,
        )
        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPoseRequest.supportedIdentifiedPointGroupKeysForRevision_error_,
            1,
        )
