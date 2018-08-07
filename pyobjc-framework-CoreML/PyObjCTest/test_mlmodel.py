import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLModel (TestCase):
        @min_os_level("10.13")
        def testMethods10_13(self):
            self.assertArgIsOut(CoreML.MLModel.modelWithContentsOfURL_error_, 1)
            self.assertArgIsOut(CoreML.MLModel.predictionFromFeatures_error_, 1)
            self.assertArgIsOut(CoreML.MLModel.predictionFromFeatures_options_error_, 2)


        @min_os_level("10.14")
        def testMethods10_14(self):
            self.assertArgIsOut(CoreML.MLModel.modelWithContentsOfURL_configuration_error_, 2)
            self.assertArgIsOut(CoreML.MLModel.predictionsFromBatch_options_error_, 2)

if __name__ == "__main__":
    main()
