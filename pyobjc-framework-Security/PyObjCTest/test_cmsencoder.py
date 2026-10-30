import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCMSEncoder(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.CMSEncoderRef)

    def test_constants(self):
        self.assertEqual(Security.kCMSAttrNone, 0x0000)
        self.assertEqual(Security.kCMSAttrSmimeCapabilities, 0x0001)
        self.assertEqual(Security.kCMSAttrSmimeEncryptionKeyPrefs, 0x0002)
        self.assertEqual(Security.kCMSAttrSmimeMSEncryptionKeyPrefs, 0x0004)
        self.assertEqual(Security.kCMSAttrSigningTime, 0x0008)
        self.assertEqual(Security.kCMSAttrAppleCodesigningHashAgility, 0x0010)
        self.assertEqual(Security.kCMSAttrAppleCodesigningHashAgilityV2, 0x0020)
        self.assertEqual(Security.kCMSAttrAppleExpirationTime, 0x0040)

        self.assertEqual(Security.kCMSCertificateNone, 0)
        self.assertEqual(Security.kCMSCertificateSignerOnly, 1)
        self.assertEqual(Security.kCMSCertificateChain, 2)
        self.assertEqual(Security.kCMSCertificateChainWithRoot, 3)
        self.assertEqual(Security.kCMSCertificateChainWithRootOrFail, 4)

    @min_os_level("10.11")
    def test_constants_10_11(self):
        self.assertIsInstance(Security.kCMSEncoderDigestAlgorithmSHA1, str)
        self.assertIsInstance(Security.kCMSEncoderDigestAlgorithmSHA256, str)

    def test_functions(self):
        self.assertIsInstance(Security.CMSEncoderGetTypeID(), int)

        self.assertArgIsOut(Security.CMSEncoderCreate, 0)
        self.assertArgIsCFRetained(Security.CMSEncoderCreate, 0)

        Security.CMSEncoderAddSigners

        self.assertArgIsOut(Security.CMSEncoderCopySigners, 1)
        self.assertArgIsCFRetained(Security.CMSEncoderCopySigners, 1)

        Security.CMSEncoderAddRecipients

        self.assertArgIsOut(Security.CMSEncoderCopyRecipients, 1)
        self.assertArgIsCFRetained(Security.CMSEncoderCopyRecipients, 1)

        self.assertArgIsBOOL(Security.CMSEncoderSetHasDetachedContent, 1)

        self.assertArgHasType(
            Security.CMSEncoderGetHasDetachedContent,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )

        self.assertFalse(hasattr(Security, "CMSEncoderSetEncapsulatedContentType"))

        Security.CMSEncoderSetEncapsulatedContentTypeOID

        self.assertArgIsOut(
            Security.CMSEncoderCopyEncapsulatedContentType,
            1,
        )
        self.assertArgIsCFRetained(Security.CMSEncoderCopyEncapsulatedContentType, 1)

        Security.CMSEncoderAddSupportingCerts

        self.assertArgIsOut(
            Security.CMSEncoderCopySupportingCerts,
            1,
        )
        self.assertArgIsCFRetained(Security.CMSEncoderCopySupportingCerts, 1)

        Security.CMSEncoderAddSignedAttributes

        Security.CMSEncoderSetCertificateChainMode

        self.assertArgIsOut(
            Security.CMSEncoderGetCertificateChainMode,
            1,
        )

        self.assertArgHasType(
            Security.CMSEncoderUpdateContent, 1, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.CMSEncoderUpdateContent, 1, 2)

        self.assertArgIsOut(
            Security.CMSEncoderCopyEncodedContent,
            1,
        )
        self.assertArgIsCFRetained(Security.CMSEncoderCopyEncodedContent, 1)

        self.assertFalse(hasattr(Security, "CMSEncode"))

        self.assertArgIsBOOL(Security.CMSEncodeContent, 3)
        self.assertArgHasType(
            Security.CMSEncodeContent, 5, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.CMSEncodeContent, 5, 6)
        self.assertArgIsOut(Security.CMSEncodeContent, 7)
        self.assertArgIsCFRetained(Security.CMSEncodeContent, 7)

        self.assertArgIsOut(
            Security.CMSEncoderCopySignerTimestamp,
            2,
        )

    @min_os_level("10.10")
    def test_functions_10_10(self):
        self.assertArgIsOut(
            Security.CMSEncoderCopySignerTimestampWithPolicy,
            3,
        )

    @min_os_level("10.11")
    def test_functions_10_11(self):
        Security.CMSEncoderSetSignerAlgorithm
