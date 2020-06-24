from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLPredictionOptions(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(CoreML.MLPredictionOptions.usesCPUOnly)
        self.assertArgIsBOOL(CoreML.MLPredictionOptions.setUsesCPUOnly_, 0)
