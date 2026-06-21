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
    def test_protocols(self):
        self.assertProtocolExists("MLBatchProvider", CoreML)
        self.assertProtocolExists("MLFeatureProvider", CoreML)

    def test_methods(self):
        self.assertResultHasType(TestMLBatchProviderHelper.count, objc._C_NSInteger)
        self.assertArgHasType(
            TestMLBatchProviderHelper.featuresAtIndex_, 0, objc._C_NSInteger
        )
