import Security
from PyObjCTools.TestSupport import TestCase, min_os_level

SecureDownloadTrustSetupCallback = b"i@^v"
SecureDownloadTrustEvaluateCallback = b"i@i^v"

SecKeyGeneratePairBlock = b"v@@@"


class TestSecKey(TestCase):
    def test_enums(self):
        # Unnamed enum:
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

        self.assertIsEnumType(Security.SecCredentialType)
        self.assertEqual(Security.kSecCredentialTypeDefault, 0)
        self.assertEqual(Security.kSecCredentialTypeWithUI, 1)
        self.assertEqual(Security.kSecCredentialTypeNoUI, 2)

        self.assertIsEnumType(Security.SecPadding)
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

        self.assertIsEnumType(Security.SecPadding)
        self.assertEqual(Security.kSecPaddingNone, 0)

        self.assertIsEnumType(Security.SecKeySizes)
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

        self.assertIsEnumType(Security.SecKeyOperationType)
        self.assertEqual(Security.kSecKeyOperationTypeSign, 0)
        self.assertEqual(Security.kSecKeyOperationTypeVerify, 1)
        self.assertEqual(Security.kSecKeyOperationTypeEncrypt, 2)
        self.assertEqual(Security.kSecKeyOperationTypeDecrypt, 3)
        self.assertEqual(Security.kSecKeyOperationTypeKeyExchange, 4)

    def test_constants(self):
        self.assertIsInstance(Security.kSecPrivateKeyAttrs, str)
        self.assertIsInstance(Security.kSecPublicKeyAttrs, str)

    @min_os_level("10.12")
    def test_constants_10_12(self):
        self.assertIsInstance(Security.kSecKeyAlgorithmRSASignatureRaw, str)
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureDigestPKCS1v15Raw, str
        )
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
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureDigestX962SHA1, str
        )
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
        self.assertIsInstance(
            Security.kSecKeyAlgorithmECDSASignatureMessageX962SHA1, str
        )
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
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA224AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA256AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA384AESGCM, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSAEncryptionOAEPSHA512AESGCM, str
        )
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
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA224, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA256, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA384, str
        )
        self.assertIsInstance(
            Security.kSecKeyAlgorithmRSASignatureMessagePSSSHA512, str
        )
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

    def test_types(self):
        self.assertIsCFType(Security.SecKeyRef)

    def test_functions(self):
        self.assertIsInstance(Security.SecKeyGetTypeID(), int)

        Security.SecKeyGetBlockSize

        self.assertArgIsOut(Security.SecKeyGenerateSymmetric, 1)

        self.assertArgIsOut(Security.SecKeyCreateFromData, 2)

        self.assertArgIsBlock(
            Security.SecKeyGeneratePairAsync, 2, SecKeyGeneratePairBlock
        )

        self.assertArgIsOut(Security.SecKeyDeriveFromPassword, 2)

        self.assertArgIsOut(Security.SecKeyWrapSymmetric, 3)

        self.assertArgIsIn(Security.SecKeyUnwrapSymmetric, 0)
        self.assertArgIsOut(Security.SecKeyUnwrapSymmetric, 3)

        self.assertArgIsOut(Security.SecKeyGeneratePair, 1)
        self.assertArgIsCFRetained(Security.SecKeyGeneratePair, 1)
        self.assertArgIsOut(Security.SecKeyGeneratePair, 2)
        self.assertArgIsCFRetained(Security.SecKeyGeneratePair, 2)

        self.assertFalse(hasattr(Security, "SecKeyRawSign"))
        self.assertFalse(hasattr(Security, "SecKeyRawVerify"))
        self.assertFalse(hasattr(Security, "SecKeyEncrypt"))
        self.assertFalse(hasattr(Security, "SecKeyDecrypt"))

    @min_os_level("10.12")
    def test_functions_10_12(self):
        self.assertArgIsOut(Security.SecKeyCreateRandomKey, 1)

        self.assertArgIsOut(Security.SecKeyCreateWithData, 2)

        self.assertArgIsOut(
            Security.SecKeyCopyExternalRepresentation,
            1,
        )

        Security.SecKeyCopyAttributes

        Security.SecKeyCopyPublicKey

        self.assertArgIsOut(Security.SecKeyCreateSignature, 3)

        self.assertResultIsBOOL(Security.SecKeyVerifySignature)
        self.assertArgIsOut(Security.SecKeyVerifySignature, 4)

        self.assertArgIsOut(
            Security.SecKeyCreateEncryptedData,
            3,
        )

        self.assertArgIsOut(
            Security.SecKeyCreateDecryptedData,
            3,
        )

        self.assertArgIsOut(
            Security.SecKeyCopyKeyExchangeResult,
            4,
        )

        self.assertResultIsBOOL(Security.SecKeyIsAlgorithmSupported)

    def test_functions_deprecated(self):
        self.assertFalse(hasattr(Security, "SecKeyCreatePair"))
        self.assertFalse(hasattr(Security, "SecKeyGenerate"))
        self.assertFalse(hasattr(Security, "SecKeyGetCSSMKey"))
        self.assertFalse(hasattr(Security, "SecKeyGetCSPHandle"))
        self.assertFalse(hasattr(Security, "SecKeyGetCredentials"))
