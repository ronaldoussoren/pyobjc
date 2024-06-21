from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import CoreML


class TestMLModel_MLState(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsOut(CoreML.MLModel.predictionFromFeatures_usingState_error_, 2)
        self.assertArgIsOut(
            CoreML.MLModel.predictionFromFeatures_usingState_options_error_, 3
        )

    @expectedFailure
    @min_os_level("15.0")
    def test_methods16_0(self):
        # XXX: Marked as 'macOS 16.0' in the headers.
        self.assertArgIsBlock(
            CoreML.MLModel.new().predictionFromFeatures_usingState_options_completionHandler_,
            3,
            b"v@@",
        )
