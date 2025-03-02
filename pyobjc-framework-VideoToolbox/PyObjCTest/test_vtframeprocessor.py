import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessor(TestCase):
    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(
            VideoToolbox.VTFrameProcessor.startSessionWithConfiguration_error_
        )
        self.assertArgIsOut(
            VideoToolbox.VTFrameProcessor.startSessionWithConfiguration_error_, 1
        )

        self.assertResultIsBOOL(
            VideoToolbox.VTFrameProcessor.processWithParameters_error_
        )
        self.assertArgIsOut(
            VideoToolbox.VTFrameProcessor.processWithParameters_error_, 1
        )

        self.assertArgIsBlock(
            VideoToolbox.VTFrameProcessor.processWithParameters_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            VideoToolbox.VTFrameProcessor.processWithCommandBuffer_parameters_completionHandler_,
            2,
            b"v@@",
        )
