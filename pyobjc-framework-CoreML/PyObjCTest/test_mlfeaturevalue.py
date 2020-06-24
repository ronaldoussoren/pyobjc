from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLFeatureValue(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(CoreML.MLFeatureValue.isUndefined)
        self.assertArgIsOut(CoreML.MLFeatureValue.featureValueWithDictionary_error_, 1)
        self.assertResultIsBOOL(CoreML.MLFeatureValue.isEqualToFeatureValue_)
