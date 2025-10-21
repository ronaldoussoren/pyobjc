from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision
import CoreMedia


class TestVNDetectTrajectoriesRequest(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertEqual(Vision.VNDetectTrajectoriesRequestRevision1, 1)

    @min_os_level("11.0")
    def test_methods11_0(self):
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

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultHasType(
            Vision.VNDetectTrajectoriesRequest.targetFrameTime,
            CoreMedia.CMTime.__typestr__,
        )
        self.assertArgHasType(
            Vision.VNDetectTrajectoriesRequest.setTargetFrameTime_,
            0,
            CoreMedia.CMTime.__typestr__,
        )
        self.assertArgHasType(
            Vision.VNDetectTrajectoriesRequest.initWithFrameAnalysisSpacing_completionHandler_,
            0,
            CoreMedia.CMTime.__typestr__,
        )
