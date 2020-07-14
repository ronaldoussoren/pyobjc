from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectHumanBodyPoseRequest(TestCase):
    @min_os_level("10.16")
    def testConstants10_16(self):

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
