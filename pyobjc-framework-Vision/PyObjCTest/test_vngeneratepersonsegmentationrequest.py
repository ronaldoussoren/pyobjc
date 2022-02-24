from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNGeneratePersonSegmentationRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Vision.VNGeneratePersonSegmentationRequestQualityLevel)

    def test_constants(self):
        self.assertEqual(
            Vision.VNGeneratePersonSegmentationRequestQualityLevelAccurate, 0
        )
        self.assertEqual(
            Vision.VNGeneratePersonSegmentationRequestQualityLevelBalanced, 1
        )
        self.assertEqual(Vision.VNGeneratePersonSegmentationRequestQualityLevelFast, 2)

        self.assertEqual(Vision.VNGeneratePersonSegmentationRequestRevision1, 1)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            Vision.VNGeneratePersonSegmentationRequest.initWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNGeneratePersonSegmentationRequest.initWithFrameAnalysisSpacing_completionHandler_,
            1,
            b"v@@",
        )
