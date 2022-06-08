from PyObjCTools.TestSupport import TestCase, min_os_level
import ShazamKit


class TestSHSignatureGeneratorr(TestCase):
    def test_classes(self):
        ShazamKit.SHSignatureGenerator

    def test_methods(self):
        self.assertResultIsBOOL(
            ShazamKit.SHSignatureGenerator.appendBuffer_atTime_error_
        )
        self.assertArgIsOut(
            ShazamKit.SHSignatureGenerator.appendBuffer_atTime_error_, 2
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            ShazamKit.SHSignatureGenerator.generateSignatureFromAsset_completionHandler_,
            1,
            b"v@@",
        )
