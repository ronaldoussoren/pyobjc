from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLFeatureDescription(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(CoreML.MLFeatureDescription.isOptional)
        # self.assertArgIsBOOL(CoreML.MLFeatureDescription.setOptional_, 0)
        self.assertResultIsBOOL(CoreML.MLFeatureDescription.isAllowedValue_)
