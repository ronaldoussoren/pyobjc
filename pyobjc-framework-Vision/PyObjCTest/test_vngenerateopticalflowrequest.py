from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNGenerateOpticalFlowRequest(TestCase):
    def testConstants(self):
        self.assertEqual(Vision.VNOpticalFlowGenerateLevelLow, 0)
        self.assertEqual(Vision.VNOpticalFlowGenerateLevelMedium, 1)
        self.assertEqual(Vision.VNOpticalFlowGenerateLevelHigh, 2)
        self.assertEqual(Vision.VNOpticalFlowGenerateLevelVeryHigh, 3)

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertEqual(Vision.VNGenerateOpticalFlowRequestRevision1, 1)
