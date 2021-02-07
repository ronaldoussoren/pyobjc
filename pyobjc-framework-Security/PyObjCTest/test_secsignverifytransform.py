import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecSignVerifyTransform(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecKeyAttributeName, str)
        self.assertIsInstance(Security.kSecSignatureAttributeName, str)
        self.assertIsInstance(Security.kSecInputIsAttributeName, str)
        self.assertIsInstance(Security.kSecInputIsPlainText, str)
        self.assertIsInstance(Security.kSecInputIsDigest, str)
        self.assertIsInstance(Security.kSecInputIsRaw, str)

    def test_functions(self):
        self.assertResultHasType(Security.SecSignTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecSignTransformCreate)
        self.assertArgHasType(Security.SecSignTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecSignTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecVerifyTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecVerifyTransformCreate)
        self.assertArgHasType(Security.SecVerifyTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecVerifyTransformCreate, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecVerifyTransformCreate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
