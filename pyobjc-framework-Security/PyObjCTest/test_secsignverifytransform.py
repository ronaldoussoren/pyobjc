from PyObjCTools.TestSupport import *

import Security

class TestSecSignVerifyTransform (TestCase):

    def test_constants(self):
        self.assertIsInstance(Security.kSecKeyAttributeName, unicode)
        self.assertIsInstance(Security.kSecSignatureAttributeName, unicode)
        self.assertIsInstance(Security.kSecInputIsAttributeName,unicode)
        self.assertIsInstance(Security.kSecInputIsPlainText, unicode)
        self.assertIsInstance(Security.kSecInputIsDigest, unicode)
        self.assertIsInstance(Security.kSecInputIsRaw, unicode)

    def test_functions(self):
        self.assertResultHasType(Security.SecSignTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecSignTransformCreate)
        self.assertArgHasType(Security.SecSignTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecSignTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecVerifyTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecVerifyTransformCreate)
        self.assertArgHasType(Security.SecVerifyTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecVerifyTransformCreate, 1, objc._C_ID)
        self.assertArgHasType(Security.SecVerifyTransformCreate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)

if __name__ == "__main__":
    main()
