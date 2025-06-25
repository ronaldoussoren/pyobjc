import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

SecureDownloadTrustSetupCallback = b"i@^v"
SecureDownloadTrustEvaluateCallback = b"i@i^v"

SecKeyGeneratePairBlock = b"v@@@"


class TestSecKey(TestCase):
    def testTypes(self):
        self.assertIsCFType(Security.SecKeyRef)

    def test_constants(self):
        self.assertEqual(Security.kSecKeyKeyClass, 0)
        self.assertEqual(Security.kSecKeyPrintName, 1)
        self.assertEqual(Security.kSecKeyAlias, 2)
        self.assertEqual(Security.kSecKeyPermanent, 3)
        self.assertEqual(Security.kSecKeyPrivate, 4)
        self.assertEqual(Security.kSecKeyModifiable, 5)
        self.assertEqual(Security.kSecKeyLabel, 6)
        self.assertEqual(Security.kSecKeyApplicationTag, 7)
        self.assertEqual(Security.kSecKeyKeyCreator, 8)
        self.assertEqual(Security.kSecKeyKeyType, 9)
        self.assertEqual(Security.kSecKeyKeySizeInBits, 10)
        self.assertEqual(Security.kSecKeyEffectiveKeySize, 11)
        self.assertEqual(Security.kSecKeyStartDate, 12)
        self.assertEqual(Security.kSecKeyEndDate, 13)
        self.assertEqual(Security.kSecKeySensitive, 14)
        self.assertEqual(Security.kSecKeyAlwaysSensitive, 15)
        self.assertEqual(Security.kSecKeyExtractable, 16)
        self.assertEqual(Security.kSecKeyNeverExtractable, 17)
        self.assertEqual(Security.kSecKeyEncrypt, 18)
        self.assertEqual(Security.kSecKeyDecrypt, 19)
        self.assertEqual(Security.kSecKeyDerive, 20)
        self.assertEqual(Security.kSecKeySign, 21)
        self.assertEqual(Security.kSecKeyVerify, 22)
        self.assertEqual(Security.kSecKeySignRecover, 23)
        self.assertEqual(Security.kSecKeyVerifyRecover, 24)
        self.assertEqual(Security.kSecKeyWrap, 25)
        self.assertEqual(Security.kSecKeyUnwrap, 26)

        self.assertEqual(Security.kSecCredentialTypeDefault, 0)
        self.assertEqual(Security.kSecCredentialTypeWithUI, 1)
        self.assertEqual(Security.kSecCredentialTypeNoUI, 2)

        self.assertEqual(Security.kSecPaddingNone, 0)
        self.assertEqual(Security.kSecPaddingPKCS1, 1)
        self.assertEqual(Security.kSecPaddingOAEP, 2)
        self.assertEqual(Security.kSecPaddingSigRaw, 0x4000)
        self.assertEqual(Security.kSecPaddingPKCS1MD2, 0x8000)
        self.assertEqual(Security.kSecPaddingPKCS1MD5, 0x8001)
        self.assertEqual(Security.kSecPaddingPKCS1SHA1, 0x8002)
        self.assertEqual(Security.kSecPaddingPKCS1SHA224, 0x8003)
        self.assertEqual(Security.kSecPaddingPKCS1SHA256, 0x8004)
        self.assertEqual(Security.kSecPaddingPKCS1SHA384, 0x8005)
        self.assertEqual(Security.kSecPaddingPKCS1SHA512, 0x8006)

        self.assertEqual(Security.kSecDefaultKeySize, 0)
        self.assertEqual(Security.kSec3DES192, 192)
        self.assertEqual(Security.kSecAES128, 128)
        self.assertEqual(Security.kSecAES192, 192)
        self.assertEqual(Security.kSecAES256, 256)
        self.assertEqual(Security.kSecp192r1, 192)
        self.assertEqual(Security.kSecp256r1, 256)
        self.assertEqual(Security.kSecp384r1, 384)
        self.assertEqual(Security.kSecp521r1, 521)
        self.assertEqual(Security.kSecRSAMin, 1024)
        self.assertEqual(Security.kSecRSAMax, 4096)

        self.assertEqual(Security.kSecKeyOperationTypeSign, 0)
        self.assertEqual(Security.kSecKeyOperationTypeVerify, 1)
        self.assertEqual(Security.kSecKeyOperationTypeEncrypt, 2)
        self.assertEqual(Security.kSecKeyOperationTypeDecrypt, 3)
        self.assertEqual(Security.kSecKeyOperationTypeKeyExchange, 4)

    @min_os_level("10.8")
    def test_constants_10_8(self):
        self.assertIsInstance(Security.kSecPrivateKeyAttrs, str)
        self.assertIsInstance(Security.kSecPublicKeyAttrs, str)

    @min_os_level("10.12")
    def test_constants_10_12(self):
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureRaw, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureDigestPKCS1v15Raw, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA1, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA512, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA1, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA512, str
        )
        self.assertIsInstance(Security.kSecKeyAlgorithmECDSASignatureRFC4754, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmECDSASignatureDigestX962, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmECDSASignatureDigestX962SHA1, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestX962SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestX962SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestX962SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestX962SHA512, str
        )
        self.assertIsInstance(Security.kSecKeyAlgorithmECDSASignatureMessageX962SHA1, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageX962SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageX962SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageX962SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageX962SHA512, str
        )
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionRaw, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionPKCS1, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA1, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA224, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA256, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA384, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA512, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA1AESGCM, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA224AESGCM, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA256AESGCM, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA384AESGCM, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA512AESGCM, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardX963SHA1AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardX963SHA224AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardX963SHA256AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardX963SHA384AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardX963SHA512AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorX963SHA1AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorX963SHA224AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorX963SHA256AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorX963SHA384AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorX963SHA512AESGCM, str
        )
        self.assertIsInstance(Security.kSecKeyAlgorithmECDHKeyExchangeStandard, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA1, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA512, str
        )
        self.assertIsInstance(Security.kSecKeyAlgorithmECDHKeyExchangeCofactor, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA1, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA512, str
        )

        self.assertIsInstance(Security.kSecKeyKeyExchangeParameterRequestedSize, str)
        self.assertIsInstance(Security.kSecKeyKeyExchangeParameterSharedInfo, str)

    @min_os_level("10.13")
    def test_constants_10_13(self):
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureDigestPSSSHA1, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureDigestPSSSHA224, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureDigestPSSSHA256, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureDigestPSSSHA384, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureDigestPSSSHA512, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA1, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA224, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA256, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA384, str)
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA512, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA224AESGCM,
            str,
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA256AESGCM,
            str,
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA384AESGCM,
            str,
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA512AESGCM,
            str,
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA224AESGCM,
            str,
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA256AESGCM,
            str,
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA384AESGCM,
            str,
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA512AESGCM,
            str,
        )

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(Security.kSecKeyAlgorithmECDSASignatureDigestRFC4754, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA1, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA512, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA1, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA512, str
        )

    def test_functions(self):
        self.assertIsInstance(Security.SecKeyGetTypeID(), int)

    @min_os_level("10.6")
    def test_functions_10_6(self):
        self.assertResultHasType(Security.SecKeyGetBlockSize, objc._C_ULNG)
        self.assertArgHasType(Security.SecKeyGetBlockSize, 0, objc._C_ID)

    @min_os_level("10.7")
    def test_functions_10_7(self):
        self.assertResultHasType(Security.SecKeyGenerateSymmetric, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyGenerateSymmetric)
        self.assertArgHasType(Security.SecKeyGenerateSymmetric, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyGenerateSymmetric, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyCreateFromData, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCreateFromData)
        self.assertArgHasType(Security.SecKeyCreateFromData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateFromData, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCreateFromData, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyGeneratePairAsync, objc._C_VOID)
        self.assertArgHasType(Security.SecKeyGeneratePairAsync, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyGeneratePairAsync, 1, b"^{dispatch_queue_s=}"
        )
        self.assertArgIsBlock(
            Security.SecKeyGeneratePairAsync, 2, SecKeyGeneratePairBlock
        )

        self.assertResultHasType(Security.SecKeyDeriveFromPassword, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyDeriveFromPassword)
        self.assertArgHasType(Security.SecKeyDeriveFromPassword, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyDeriveFromPassword, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyDeriveFromPassword, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyWrapSymmetric, objc._C_ID)
        self.assertArgHasType(Security.SecKeyWrapSymmetric, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyWrapSymmetric, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeyWrapSymmetric, 2, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyWrapSymmetric, 3, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyUnwrapSymmetric, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyUnwrapSymmetric, 0, objc._C_IN + objc._C_PTR + objc._C_ID
        )
        self.assertArgHasType(Security.SecKeyUnwrapSymmetric, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeyWrapSymmetric, 2, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyUnwrapSymmetric, 3, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyGeneratePair, objc._C_INT)
        self.assertArgHasType(Security.SecKeyGeneratePair, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyGeneratePair, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecKeyGeneratePair, 1)
        self.assertArgHasType(
            Security.SecKeyGeneratePair, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecKeyGeneratePair, 2)

        self.assertFalse(hasattr(Security, "SecKeyRawSign"))
        self.assertFalse(hasattr(Security, "SecKeyRawVerify"))
        self.assertFalse(hasattr(Security, "SecKeyEncrypt"))
        self.assertFalse(hasattr(Security, "SecKeyDecrypt"))

    @min_os_level("10.12")
    def test_functions_10_12(self):
        self.assertResultHasType(Security.SecKeyCreateRandomKey, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCreateRandomKey)
        self.assertArgHasType(Security.SecKeyCreateRandomKey, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCreateRandomKey, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyCreateWithData, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCreateWithData)
        self.assertArgHasType(Security.SecKeyCreateWithData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateWithData, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCreateWithData, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyCopyExternalRepresentation, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCopyExternalRepresentation)
        self.assertArgHasType(Security.SecKeyCopyExternalRepresentation, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCopyExternalRepresentation,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertResultHasType(Security.SecKeyCopyAttributes, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCopyAttributes)
        self.assertArgHasType(Security.SecKeyCopyAttributes, 0, objc._C_ID)

        self.assertResultHasType(Security.SecKeyCopyPublicKey, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCopyPublicKey)
        self.assertArgHasType(Security.SecKeyCopyPublicKey, 0, objc._C_ID)

        self.assertResultHasType(Security.SecKeyCreateSignature, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCreateSignature)
        self.assertArgHasType(Security.SecKeyCreateSignature, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateSignature, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateSignature, 2, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCreateSignature, 3, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultIsBOOL(Security.SecKeyVerifySignature)
        self.assertArgHasType(Security.SecKeyVerifySignature, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyVerifySignature, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeyVerifySignature, 2, objc._C_ID)
        self.assertArgHasType(Security.SecKeyVerifySignature, 3, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyVerifySignature, 4, objc._C_OUT + objc._C_PTR + objc._C_ID
        )

        self.assertResultHasType(Security.SecKeyCreateEncryptedData, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCreateEncryptedData)
        self.assertArgHasType(Security.SecKeyCreateEncryptedData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateEncryptedData, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateEncryptedData, 2, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCreateEncryptedData,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertResultHasType(Security.SecKeyCreateDecryptedData, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCreateDecryptedData)
        self.assertArgHasType(Security.SecKeyCreateDecryptedData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateDecryptedData, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCreateDecryptedData, 2, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCreateDecryptedData,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertResultHasType(Security.SecKeyCopyKeyExchangeResult, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecKeyCopyKeyExchangeResult)
        self.assertArgHasType(Security.SecKeyCopyKeyExchangeResult, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCopyKeyExchangeResult, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCopyKeyExchangeResult, 2, objc._C_ID)
        self.assertArgHasType(Security.SecKeyCopyKeyExchangeResult, 3, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeyCopyKeyExchangeResult,
            4,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertResultIsBOOL(Security.SecKeyIsAlgorithmSupported)
        self.assertArgHasType(Security.SecKeyIsAlgorithmSupported, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeyIsAlgorithmSupported, 1, objc._C_NSInteger)
        self.assertArgHasType(Security.SecKeyIsAlgorithmSupported, 2, objc._C_ID)

    def test_functions_deprecated(self):
        self.assertFalse(hasattr(Security, "SecKeyCreatePair"))
        self.assertFalse(hasattr(Security, "SecKeyGenerate"))
        self.assertFalse(hasattr(Security, "SecKeyGetCSSMKey"))
        self.assertFalse(hasattr(Security, "SecKeyGetCSPHandle"))
        self.assertFalse(hasattr(Security, "SecKeyGetCredentials"))
