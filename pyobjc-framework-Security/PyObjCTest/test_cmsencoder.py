from PyObjCTools.TestSupport import *

import Security

class TestCMSEncoder (TestCase):
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

    @min_os_level('10.11')
    def test_constants_10_11(self):
        self.assertIsInstance(Security.kCMSEncoderDigestAlgorithmSHA1, unicode)
        self.assertIsInstance(Security.kCMSEncoderDigestAlgorithmSHA256, unicode)

    def test_functions(self):
        self.assertIsInstance(Security.CMSEncoderGetTypeID(), (int, long))

        self.assertResultHasType(Security.CMSEncoderCreate, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCreate, 0, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.CMSEncoderCreate, 0)


        self.assertResultHasType(Security.CMSEncoderAddSigners, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderAddSigners, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderAddSigners, 1, objc._C_ID)

        self.assertResultHasType(Security.CMSEncoderCopySigners, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCopySigners, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopySigners, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.CMSEncoderCopySigners, 1)

        self.assertResultHasType(Security.CMSEncoderAddRecipients, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderAddRecipients, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderAddRecipients, 1, objc._C_ID)

        self.assertResultHasType(Security.CMSEncoderCopyRecipients, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCopyRecipients, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopyRecipients, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.CMSEncoderCopyRecipients, 1)

        self.assertResultHasType(Security.CMSEncoderSetHasDetachedContent, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderSetHasDetachedContent, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderSetHasDetachedContent, 1, objc._C_NSBOOL)

        self.assertResultHasType(Security.CMSEncoderGetHasDetachedContent, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderGetHasDetachedContent, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderGetHasDetachedContent, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)

        self.assertFalse(hasattr(Security, 'CMSEncoderSetEncapsulatedContentType'))

        self.assertResultHasType(Security.CMSEncoderSetEncapsulatedContentTypeOID, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderSetEncapsulatedContentTypeOID, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderSetEncapsulatedContentTypeOID, 1, objc._C_ID)

        self.assertResultHasType(Security.CMSEncoderCopyEncapsulatedContentType, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCopyEncapsulatedContentType, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopyEncapsulatedContentType, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.CMSEncoderCopyEncapsulatedContentType, 1)

        self.assertResultHasType(Security.CMSEncoderAddSupportingCerts, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderAddSupportingCerts, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderAddSupportingCerts, 1, objc._C_ID)

        self.assertResultHasType(Security.CMSEncoderCopySupportingCerts, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCopySupportingCerts, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopySupportingCerts, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.CMSEncoderCopySupportingCerts, 1)

        self.assertResultHasType(Security.CMSEncoderAddSignedAttributes, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderAddSignedAttributes, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderAddSignedAttributes, 1, objc._C_UINT)

        self.assertResultHasType(Security.CMSEncoderSetCertificateChainMode, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderSetCertificateChainMode, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderSetCertificateChainMode, 1, objc._C_UINT)

        self.assertResultHasType(Security.CMSEncoderGetCertificateChainMode, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderGetCertificateChainMode, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderGetCertificateChainMode, 1, objc._C_OUT + objc._C_PTR + objc._C_UINT)

        self.assertResultHasType(Security.CMSEncoderUpdateContent, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderUpdateContent, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderUpdateContent, 1, objc._C_IN + objc._C_PTR + objc._C_VOID)
        self.assertArgSizeInArg(Security.CMSEncoderUpdateContent, 1, 2)
        self.assertArgHasType(Security.CMSEncoderUpdateContent, 2, objc._C_ULNG)

        self.assertResultHasType(Security.CMSEncoderCopyEncodedContent, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCopyEncodedContent, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopyEncodedContent, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.CMSEncoderCopyEncodedContent, 1)

        self.assertFalse(hasattr(Security, 'CMSEncode'))

        self.assertResultHasType(Security.CMSEncodeContent, objc._C_INT)
        self.assertArgHasType(Security.CMSEncodeContent, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncodeContent, 1, objc._C_ID)
        self.assertArgHasType(Security.CMSEncodeContent, 2, objc._C_ID)
        self.assertArgHasType(Security.CMSEncodeContent, 3, objc._C_NSBOOL)
        self.assertArgHasType(Security.CMSEncodeContent, 4, objc._C_UINT)
        self.assertArgHasType(Security.CMSEncodeContent, 5, objc._C_IN + objc._C_PTR + objc._C_VOID)
        self.assertArgSizeInArg(Security.CMSEncodeContent, 5, 6)
        self.assertArgHasType(Security.CMSEncodeContent, 6, objc._C_ULNG)
        self.assertArgHasType(Security.CMSEncodeContent, 7, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.CMSEncodeContent, 7)

        self.assertResultHasType(Security.CMSEncoderCopySignerTimestamp, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCopySignerTimestamp, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopySignerTimestamp, 1, objc._C_ULNG)
        self.assertArgHasType(Security.CMSEncoderCopySignerTimestamp, 2, objc._C_OUT + objc._C_PTR + objc._C_DBL)

    @min_os_level('10.10')
    def test_functions_10_10(self):
        self.assertResultHasType(Security.CMSEncoderCopySignerTimestampWithPolicy, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderCopySignerTimestampWithPolicy, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopySignerTimestampWithPolicy, 1, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderCopySignerTimestampWithPolicy, 2, objc._C_ULNG)
        self.assertArgHasType(Security.CMSEncoderCopySignerTimestampWithPolicy, 3, objc._C_OUT + objc._C_PTR + objc._C_DBL)

    @min_os_level('10.11')
    def test_functions_10_11(self):
        self.assertResultHasType(Security.CMSEncoderSetSignerAlgorithm, objc._C_INT)
        self.assertArgHasType(Security.CMSEncoderSetSignerAlgorithm, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSEncoderSetSignerAlgorithm, 1, objc._C_ID)

if __name__ == "__main__":
    main()
