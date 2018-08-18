import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLBatchProviderHelper (CoreML.NSObject):
        def count(self): return 1
        def featuresAtIndex_(self, i): return 'a'


    class TestMLBatchProvider (TestCase):
        @min_sdk_level('10.14')
        def testProtocols(self):
            objc.protocolNamed('MLBatchProvider')
            objc.protocolNamed('MLFeatureProvider')


        def testMethods(self):
            self.assertResultHasType(TestMLBatchProviderHelper.count, objc._C_NSInteger)
            self.assertArgHasType(TestMLBatchProviderHelper.featuresAtIndex_, 0, objc._C_NSInteger)

if __name__ == "__main__":
    main()
