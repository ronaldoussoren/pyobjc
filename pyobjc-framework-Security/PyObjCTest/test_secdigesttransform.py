from PyObjCTools.TestSupport import *

import Security

class TestAuthorizationDB (TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecDigestMD2, unicode)
        self.assertIsInstance(Security.kSecDigestMD4, unicode)
        self.assertIsInstance(Security.kSecDigestMD5, unicode)
        self.assertIsInstance(Security.kSecDigestSHA1, unicode)
        self.assertIsInstance(Security.kSecDigestSHA2, unicode)
        self.assertIsInstance(Security.kSecDigestHMACMD5, unicode)
        self.assertIsInstance(Security.kSecDigestHMACSHA1, unicode)
        self.assertIsInstance(Security.kSecDigestHMACSHA2, unicode)
        self.assertIsInstance(Security.kSecDigestTypeAttribute, unicode)
        self.assertIsInstance(Security.kSecDigestLengthAttribute, unicode)
        self.assertIsInstance(Security.kSecDigestHMACKeyAttribute, unicode)


    def test_functions(self):
        self.assertResultHasType(Security.SecDigestTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecDigestTransformCreate)
        self.assertArgHasType(Security.SecDigestTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecDigestTransformCreate, 1, objc._C_NSInteger)
        self.assertArgHasType(Security.SecDigestTransformCreate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)

    @expectedFailure
    def test_functions_missing(self):
        return # On 10.13.4 beta the function is found, but crashes
        self.assertIsInstance(Security.SecDigestTransformGetTypeID(), (int, long))



if __name__ == "__main__":
    main()
