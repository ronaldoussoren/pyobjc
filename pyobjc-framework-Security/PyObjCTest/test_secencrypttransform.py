import Security
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import objc


class TestSecEncryptTransform(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecPaddingNoneKey, str)
        self.assertIsInstance(Security.kSecPaddingPKCS1Key, str)
        self.assertIsInstance(Security.kSecPaddingPKCS5Key, str)
        self.assertIsInstance(Security.kSecPaddingPKCS7Key, str)
        self.assertIsInstance(Security.kSecPaddingOAEPKey, str)
        self.assertIsInstance(Security.kSecModeNoneKey, str)
        self.assertIsInstance(Security.kSecModeECBKey, str)
        self.assertIsInstance(Security.kSecModeCBCKey, str)
        self.assertIsInstance(Security.kSecModeCFBKey, str)
        self.assertIsInstance(Security.kSecModeOFBKey, str)
        self.assertIsInstance(Security.kSecEncryptKey, str)
        self.assertIsInstance(Security.kSecPaddingKey, str)
        self.assertIsInstance(Security.kSecIVKey, str)
        self.assertIsInstance(Security.kSecEncryptionMode, str)

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(Security.kSecOAEPEncodingParametersAttributeName, str)

    @expectedFailure
    @min_os_level("10.8")
    def test_constants10_8_missing(self):
        # Fails on 10.11
        self.assertIsInstance(Security.kSecOAEPMessageLengthAttributeName, str)
        self.assertIsInstance(Security.kSecOAEPMGF1DigestAlgorithmAttributeName, str)

    @min_os_level("10.7")
    def test_functions(self):
        self.assertResultHasType(Security.SecEncryptTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecEncryptTransformCreate)
        self.assertArgHasType(Security.SecEncryptTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecEncryptTransformCreate,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertResultHasType(Security.SecDecryptTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecDecryptTransformCreate)
        self.assertArgHasType(Security.SecDecryptTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecDecryptTransformCreate,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

    @min_os_level("10.7")
    def test_functions_missing(self):
        # On 10.13.4 (beta) both functions are found, but crash...
        return
        self.assertIsInstance(Security.SecDecryptTransformGetTypeID(), int)
        self.assertIsInstance(Security.SecEncryptTransformGetTypeID(), int)
