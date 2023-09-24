from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectAnimalBodyPoseRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectAnimalBodyPoseRequestRevision1, 1)

    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsOut(
            Vision.VNDetectAnimalBodyPoseRequest.supportedJointNamesAndReturnError_, 0
        )
        self.assertArgIsOut(
            Vision.VNDetectAnimalBodyPoseRequest.supportedJointsGroupNamesAndReturnError_,
            0,
        )
