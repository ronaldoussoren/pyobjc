import objc

from PyObjCTools.TestSupport import TestCase, min_sdk_level
import CoreML


class TestMLBatchProviderHelper(CoreML.NSObject):
    def count(self):
        return 1

    def featuresAtIndex_(self, i):
        return "a"


class TestMLBatchProvider(TestCase):
    @min_sdk_level("10.14")
    def testProtocols(self):
        self.assertProtocolExists("MLBatchProvider")
        self.assertProtocolExists("MLFeatureProvider")

    def testMethods(self):
        self.assertResultHasType(TestMLBatchProviderHelper.count, objc._C_NSInteger)
        self.assertArgHasType(
            TestMLBatchProviderHelper.featuresAtIndex_, 0, objc._C_NSInteger
        )
