from PyObjCTools.TestSupport import TestCase
import ShazamKit


class TestSHSignature(TestCase):
    def test_classes(self):
        ShazamKit.SHSignature

    def test_methods(self):
        self.assertArgIsOut(
            ShazamKit.SHSignature.signatureWithDataRepresentation_error_, 1
        )
        self.assertArgIsOut(ShazamKit.SHSignature.initWithDataRepresentation_error_, 1)
