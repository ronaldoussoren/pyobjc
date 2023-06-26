from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTrackOpticalFlowRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNTrackOpticalFlowRequestRevision1, 1)

        self.assertIsEnumType(Vision.VNTrackOpticalFlowRequestComputationAccuracy)
        self.assertEqual(Vision.VNTrackOpticalFlowRequestComputationAccuracyLow, 0)
        self.assertEqual(Vision.VNTrackOpticalFlowRequestComputationAccuracyMedium, 1)
        self.assertEqual(Vision.VNTrackOpticalFlowRequestComputationAccuracyHigh, 2)
        self.assertEqual(Vision.VNTrackOpticalFlowRequestComputationAccuracyVeryHigh, 3)

    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Vision.VNTrackOpticalFlowRequest.initWithCompletionHandler_, 0, b"v@@"
        )
        self.assertResultIsBOOL(Vision.VNTrackOpticalFlowRequest.keepNetworkOutput)
        self.assertArgIsBOOL(Vision.VNTrackOpticalFlowRequest.setKeepNetworkOutput_, 0)
