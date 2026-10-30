import Security
from PyObjCTools.TestSupport import TestCase


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

        self.assertIsInstance(Security.kSecOAEPEncodingParametersAttributeName, str)

    def test_constants10_8_missing(self):
        # Fails on 10.11
        self.assertIsInstance(Security.kSecOAEPMessageLengthAttributeName, str)
        self.assertIsInstance(Security.kSecOAEPMGF1DigestAlgorithmAttributeName, str)

    def test_functions(self):
        self.assertResultIsCFRetained(Security.SecEncryptTransformCreate)
        self.assertArgIsOut(
            Security.SecEncryptTransformCreate,
            1,
        )
        self.assertArgIsCFRetained(Security.SecEncryptTransformCreate, 1)

        self.assertResultIsCFRetained(Security.SecDecryptTransformCreate)
        self.assertArgIsOut(
            Security.SecDecryptTransformCreate,
            1,
        )
        self.assertArgIsCFRetained(Security.SecDecryptTransformCreate, 1)

        # XXX: Calling either one of these causes a hard crash
        Security.SecDecryptTransformGetTypeID
        Security.SecEncryptTransformGetTypeID
