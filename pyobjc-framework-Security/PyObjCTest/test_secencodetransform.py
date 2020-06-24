import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecEncodeTransform(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecBase64Encoding, str)
        self.assertIsInstance(Security.kSecBase32Encoding, str)
        self.assertIsInstance(Security.kSecZLibEncoding, str)
        self.assertIsInstance(Security.kSecEncodeTypeAttribute, str)
        self.assertIsInstance(Security.kSecLineLength64, str)
        self.assertIsInstance(Security.kSecLineLength76, str)
        self.assertIsInstance(Security.kSecEncodeLineLengthAttribute, str)
        self.assertIsInstance(Security.kSecCompressionRatio, str)

    def test_functions(self):
        self.assertResultHasType(Security.SecEncodeTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecEncodeTransformCreate)
        self.assertArgHasType(Security.SecEncodeTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecEncodeTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
