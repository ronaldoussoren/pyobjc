import Security
from PyObjCTools.TestSupport import TestCase, expectedFailure


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
        self.assertResultIsCFRetained(Security.SecDigestTransformCreate)
        self.assertArgIsOut(Security.SecDigestTransformCreate, 2)
        self.assertArgIsCFRetained(Security.SecDigestTransformCreate, 2)

    @expectedFailure
    def test_functions_missing(self):
        self.fail(
            "crashy function"
        )  # On 10.13.4 beta the function is found, but crashes
        self.assertIsInstance(Security.SecDigestTransformGetTypeID(), int)
