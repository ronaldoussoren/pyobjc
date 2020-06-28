from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModel(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(CoreML.MLModel.modelWithContentsOfURL_error_, 1)
        self.assertArgIsOut(CoreML.MLModel.predictionFromFeatures_error_, 1)
        self.assertArgIsOut(CoreML.MLModel.predictionFromFeatures_options_error_, 2)

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertArgIsOut(
            CoreML.MLModel.modelWithContentsOfURL_configuration_error_, 2
        )
        self.assertArgIsOut(CoreML.MLModel.predictionsFromBatch_options_error_, 2)

    @min_os_level("10.15")
    def testMethods10_14_missing(self):
        self.assertArgIsOut(CoreML.MLModel.predictionsFromBatch_error_, 1)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsOut(CoreML.MLModel.parameterValueForKey_error_, 1)

    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertArgIsBlock(
            CoreML.MLModel.loadContentsOfURL_configuration_completionHandler_, 2, b"v@@"
        )
