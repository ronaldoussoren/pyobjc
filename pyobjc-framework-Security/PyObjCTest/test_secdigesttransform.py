import Security
from PyObjCTools.TestSupport import TestCase, expectedFailure
import objc


class TestAuthorizationDB(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecDigestMD2, str)
        self.assertIsInstance(Security.kSecDigestMD4, str)
        self.assertIsInstance(Security.kSecDigestMD5, str)
        self.assertIsInstance(Security.kSecDigestSHA1, str)
        self.assertIsInstance(Security.kSecDigestSHA2, str)
        self.assertIsInstance(Security.kSecDigestHMACMD5, str)
        self.assertIsInstance(Security.kSecDigestHMACSHA1, str)
        self.assertIsInstance(Security.kSecDigestHMACSHA2, str)
        self.assertIsInstance(Security.kSecDigestTypeAttribute, str)
        self.assertIsInstance(Security.kSecDigestLengthAttribute, str)
        self.assertIsInstance(Security.kSecDigestHMACKeyAttribute, str)

    def test_functions(self):
        self.assertResultHasType(Security.SecDigestTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecDigestTransformCreate)
        self.assertArgHasType(Security.SecDigestTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecDigestTransformCreate, 1, objc._C_NSInteger)
        self.assertArgHasType(
            Security.SecDigestTransformCreate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

    @expectedFailure
    def test_functions_missing(self):
        return  # On 10.13.4 beta the function is found, but crashes
        self.assertIsInstance(Security.SecDigestTransformGetTypeID(), int)
