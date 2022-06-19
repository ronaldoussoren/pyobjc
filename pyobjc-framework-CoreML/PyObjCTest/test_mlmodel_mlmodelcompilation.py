from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModel_MLModelCompilation(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(CoreML.MLModel.compileModelAtURL_error_, 1)

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsBlock(
            CoreML.MLModel.compileModelAtURL_completionHandler_, 1, b"v@@"
        )
