from PyObjCTools.TestSupport import *

import Security

class TestSecEncryptTransform (TestCase):

    def test_constants(self):
        self.assertIsInstance(Security.kSecPaddingNoneKey, unicode)
        self.assertIsInstance(Security.kSecPaddingPKCS1Key, unicode)
        self.assertIsInstance(Security.kSecPaddingPKCS5Key, unicode)
        self.assertIsInstance(Security.kSecPaddingPKCS7Key, unicode)
        self.assertIsInstance(Security.kSecPaddingOAEPKey, unicode)
        self.assertIsInstance(Security.kSecModeNoneKey, unicode)
        self.assertIsInstance(Security.kSecModeECBKey, unicode)
        self.assertIsInstance(Security.kSecModeCBCKey, unicode)
        self.assertIsInstance(Security.kSecModeCFBKey, unicode)
        self.assertIsInstance(Security.kSecModeOFBKey, unicode)
        self.assertIsInstance(Security.kSecEncryptKey, unicode)
        self.assertIsInstance(Security.kSecPaddingKey, unicode)
        self.assertIsInstance(Security.kSecIVKey, unicode)
        self.assertIsInstance(Security.kSecEncryptionMode, unicode)

    @min_os_level('10.8')
    def test_constants10_8(self):
        self.assertIsInstance(Security.kSecOAEPEncodingParametersAttributeName, unicode)

    @expectedFailure
    @min_os_level('10.8')
    def test_constants10_8_missing(self):
        self.assertIsInstance(Security.kSecOAEPMessageLengthAttributeName, unicode)
        self.assertIsInstance(Security.kSecOAEPMGF1DigestAlgorithmAttributeName, unicode)

    @min_os_level('10.7')
    def test_functions(self):
        self.assertResultHasType(Security.SecEncryptTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecEncryptTransformCreate)
        self.assertArgHasType(Security.SecEncryptTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecEncryptTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecDecryptTransformCreate, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecDecryptTransformCreate)
        self.assertArgHasType(Security.SecDecryptTransformCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecDecryptTransformCreate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

    @expectedFailure
    @min_os_level('10.7')
    def test_functions_missing(self):
        # On 10.13.4 (beta) both functions are found, but crash...
        return
        self.assertIsInstance(Security.SecDecryptTransformGetTypeID(), (int, long))
        self.assertIsInstance(Security.SecEncryptTransformGetTypeID(), (int, long))

if __name__ == "__main__":
    main()
