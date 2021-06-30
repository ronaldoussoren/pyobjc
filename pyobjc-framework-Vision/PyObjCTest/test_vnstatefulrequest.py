from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNStatefulRequest(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            Vision.VNStatefulRequest.initWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            Vision.VNStatefulRequest.initWithFrameAnalysisSpacing_completionHandler_,
            1,
            b"v@@",
        )
