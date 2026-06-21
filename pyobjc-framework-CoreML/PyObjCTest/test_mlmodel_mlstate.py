from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModel_MLState(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsOut(CoreML.MLModel.predictionFromFeatures_usingState_error_, 2)
        self.assertArgIsOut(
            CoreML.MLModel.predictionFromFeatures_usingState_options_error_, 3
        )

    @min_os_level("15.0")
    def test_methods16_0(self):
        self.assertArgIsBlock(
            CoreML.MLModel.new().predictionFromFeatures_usingState_options_completionHandler_,
            3,
            b"v@@",
        )
