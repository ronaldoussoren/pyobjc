from PyObjCTools.TestSupport import TestCase
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
