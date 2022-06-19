from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNGenerateOpticalFlowRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Vision.VNGenerateOpticalFlowRequestComputationAccuracy)

    def testConstants(self):
        self.assertEqual(Vision.VNGenerateOpticalFlowRequestComputationAccuracyLow, 0)
        self.assertEqual(
            Vision.VNGenerateOpticalFlowRequestComputationAccuracyMedium, 1
        )
        self.assertEqual(Vision.VNGenerateOpticalFlowRequestComputationAccuracyHigh, 2)
        self.assertEqual(
            Vision.VNGenerateOpticalFlowRequestComputationAccuracyVeryHigh, 3
        )

        self.assertEqual(Vision.VNGenerateOpticalFlowRequestRevision1, 1)
        self.assertEqual(Vision.VNGenerateOpticalFlowRequestRevision2, 2)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(Vision.VNGenerateOpticalFlowRequest.keepNetworkOutput)
        self.assertArgIsBOOL(
            Vision.VNGenerateOpticalFlowRequest.setKeepNetworkOutput_, 0
        )
