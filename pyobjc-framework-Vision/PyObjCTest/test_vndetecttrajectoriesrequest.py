from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNDetectTrajectoriesRequest(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertEqual(Vision.VNDetectTrajectoriesRequestRevision1, 1)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertArgIsBlock(
            Vision.VNDetectTrajectoriesRequest.initWithFrameAnalysisSpacing_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNDetectTrajectoriesRequest.initWithFrameAnalysisSpacing_trajectoryLength_completionHandler_,
            2,
            b"v@@",
        )
