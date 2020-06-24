from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLUpdateProgressHandlers(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            CoreML.MLUpdateProgressHandlers.initForEvents_progressHandler_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            CoreML.MLUpdateProgressHandlers.initForEvents_progressHandler_completionHandler_,
            2,
            b"v@",
        )
