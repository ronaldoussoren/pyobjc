from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLDictionaryFeatureProvider(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(
            CoreML.MLDictionaryFeatureProvider.initWithDictionary_error_, 1
        )
