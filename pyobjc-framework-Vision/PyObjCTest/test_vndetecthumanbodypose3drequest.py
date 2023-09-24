from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectHumanBodyPose3DRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectHumanBodyPose3DRequestRevision1, 1)

    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Vision.VNDetectHumanBodyPose3DRequest.initWithCompletionHandler_, 0, b"v@@"
        )

        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPose3DRequest.supportedJointNamesAndReturnError_, 0
        )

        self.assertArgIsOut(
            Vision.VNDetectHumanBodyPose3DRequest.supportedJointsGroupNamesAndReturnError_,
            0,
        )
