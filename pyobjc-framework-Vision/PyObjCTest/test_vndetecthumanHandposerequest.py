from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectHumanHandPoseRequest(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(Vision.VNHandLandmarkKeyThumbCMC, str)
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

        self.assertEqual(Vision.VNDetectHumanHandPoseRequestRevision1, 1)

    @min_os_level("10.16")
    def test_methods10_16(self):
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
