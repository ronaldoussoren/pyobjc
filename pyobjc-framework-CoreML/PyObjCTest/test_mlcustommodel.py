import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLCustomModelHelper (CoreML.NSObject):
        def initWithModelDescription_parameterDictionary_error_(self, a, b, c): return 1
        def predictionFromFeatures_options_error_(self, a, b, c): return 1
        def predictionsFromBatch_options_error_(self, a, b, c): return 1


    class TestMLCustomModel (TestCase):
        @min_sdk_level('10.14')
        def testProtocols(self):
            objc.protocolNamed('MLCustomModel')

        def testMethods(self):
            self.assertArgHasType(TestMLCustomModelHelper.initWithModelDescription_parameterDictionary_error_, 2, b"o^@")
            self.assertArgHasType(TestMLCustomModelHelper.predictionFromFeatures_options_error_, 2, b"o^@")
            self.assertArgHasType(TestMLCustomModelHelper.predictionsFromBatch_options_error_, 2, b"o^@")

if __name__ == "__main__":
    main()
