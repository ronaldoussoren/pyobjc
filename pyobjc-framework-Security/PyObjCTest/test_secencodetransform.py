from PyObjCTools.TestSupport import *

import Security

class TestSecEncodeTransform (TestCase):

    def test_constants(self):
        self.assertIsInstance(Security.kSecBase64Encoding, unicode)
        self.assertIsInstance(Security.kSecBase32Encoding, unicode)
        self.assertIsInstance(Security.kSecZLibEncoding, unicode)
        self.assertIsInstance(Security.kSecEncodeTypeAttribute, unicode)
        self.assertIsInstance(Security.kSecLineLength64, unicode)
        self.assertIsInstance(Security.kSecLineLength76, unicode)
        self.assertIsInstance(Security.kSecEncodeLineLengthAttribute, unicode)
        self.assertIsInstance(Security.kSecCompressionRatio, unicode)


    def test_functions(self):
        self.assertResultHasType(Security.SecEncodeTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecEncodeTransformCreate)
        self.assertArgHasType(Security.SecEncodeTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecEncodeTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

if __name__ == "__main__":
    main()
