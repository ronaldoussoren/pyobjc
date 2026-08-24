import Security
from PyObjCTools.TestSupport import TestCase


class TestSecSignVerifyTransform(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecKeyAttributeName, str)
        self.assertIsInstance(Security.kSecSignatureAttributeName, str)
        self.assertIsInstance(Security.kSecInputIsAttributeName, str)
        self.assertIsInstance(Security.kSecInputIsPlainText, str)
        self.assertIsInstance(Security.kSecInputIsDigest, str)
        self.assertIsInstance(Security.kSecInputIsRaw, str)

    def test_functions(self):
        self.assertArgIsOut(Security.SecSignTransformCreate, 1)

        self.assertArgIsOut(Security.SecVerifyTransformCreate, 2)
