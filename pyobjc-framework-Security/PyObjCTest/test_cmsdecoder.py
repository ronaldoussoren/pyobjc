import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCMSDecoder(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.CMSDecoderRef)

    def test_constants(self):
        self.assertEqual(Security.kCMSSignerUnsigned, 0)
        self.assertEqual(Security.kCMSSignerValid, 1)
        self.assertEqual(Security.kCMSSignerNeedsDetachedContent, 2)
        self.assertEqual(Security.kCMSSignerInvalidSignature, 3)
        self.assertEqual(Security.kCMSSignerInvalidCert, 4)
        self.assertEqual(Security.kCMSSignerInvalidIndex, 5)

    def test_functions(self):
        self.assertIsInstance(Security.CMSDecoderGetTypeID(), int)

        self.assertResultHasType(Security.CMSDecoderCreate, objc._C_INT)
        self.assertArgHasType(
            Security.CMSDecoderCreate, 0, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCreate, 0)

        self.assertResultHasType(Security.CMSDecoderUpdateMessage, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderUpdateMessage, 0, objc._C_ID)
        self.assertArgHasType(
            Security.CMSDecoderUpdateMessage, 1, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.CMSDecoderUpdateMessage, 1, 2)
        self.assertArgHasType(Security.CMSDecoderUpdateMessage, 2, objc._C_ULNG)

        self.assertResultHasType(Security.CMSDecoderFinalizeMessage, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderFinalizeMessage, 0, objc._C_ID)

        self.assertResultHasType(Security.CMSDecoderSetDetachedContent, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderSetDetachedContent, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSDecoderSetDetachedContent, 1, objc._C_ID)

        self.assertResultHasType(Security.CMSDecoderCopyDetachedContent, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderCopyDetachedContent, 0, objc._C_ID)
        self.assertArgHasType(
            Security.CMSDecoderCopyDetachedContent,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopyDetachedContent, 1)

        self.assertResultHasType(Security.CMSDecoderSetSearchKeychain, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderSetSearchKeychain, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSDecoderSetSearchKeychain, 1, objc._C_ID)

        self.assertResultHasType(Security.CMSDecoderGetNumSigners, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderGetNumSigners, 0, objc._C_ID)
        self.assertArgHasType(
            Security.CMSDecoderGetNumSigners,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertResultHasType(Security.CMSDecoderCopySignerStatus, objc._C_INT)
        # self.assertArgHasType(Security.CMSDecoderCopySignerStatus, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSDecoderCopySignerStatus, 1, objc._C_ULNG)
        self.assertArgHasType(Security.CMSDecoderCopySignerStatus, 2, objc._C_ID)
        self.assertArgHasType(Security.CMSDecoderCopySignerStatus, 3, objc._C_NSBOOL)
        self.assertArgIsOut(Security.CMSDecoderCopySignerStatus, 4)
        self.assertArgIsOut(Security.CMSDecoderCopySignerStatus, 5)
        self.assertArgIsOut(Security.CMSDecoderCopySignerStatus, 6)

        self.assertResultHasType(Security.CMSDecoderGetNumSigners, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderGetNumSigners, 0, objc._C_ID)
        self.assertArgHasType(
            Security.CMSDecoderGetNumSigners,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ULNG,
        )

        self.assertResultHasType(Security.CMSDecoderCopySignerCert, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderCopySignerCert, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSDecoderCopySignerCert, 1, objc._C_ULNG)
        self.assertArgHasType(
            Security.CMSDecoderCopySignerCert, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopySignerCert, 2)

        self.assertResultHasType(Security.CMSDecoderIsContentEncrypted, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderIsContentEncrypted, 0, objc._C_ID)
        self.assertArgHasType(
            Security.CMSDecoderIsContentEncrypted,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )

        self.assertResultHasType(
            Security.CMSDecoderCopyEncapsulatedContentType, objc._C_INT
        )
        self.assertArgHasType(
            Security.CMSDecoderCopyEncapsulatedContentType, 0, objc._C_ID
        )
        self.assertArgHasType(
            Security.CMSDecoderCopyEncapsulatedContentType,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopyEncapsulatedContentType, 1)

        self.assertResultHasType(Security.CMSDecoderCopyAllCerts, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderCopyAllCerts, 0, objc._C_ID)
        self.assertArgHasType(
            Security.CMSDecoderCopyAllCerts, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopyAllCerts, 1)

        self.assertResultHasType(Security.CMSDecoderCopyContent, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderCopyContent, 0, objc._C_ID)
        self.assertArgHasType(
            Security.CMSDecoderCopyContent, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopyContent, 1)

    @min_os_level("10.8")
    def test_functions_10_8(self):
        self.assertResultHasType(Security.CMSDecoderCopySignerSigningTime, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderCopySignerSigningTime, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSDecoderCopySignerSigningTime, 1, objc._C_ULNG)
        self.assertArgHasType(
            Security.CMSDecoderCopySignerSigningTime,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_DBL,
        )

        self.assertResultHasType(Security.CMSDecoderCopySignerTimestamp, objc._C_INT)
        self.assertArgHasType(Security.CMSDecoderCopySignerTimestamp, 0, objc._C_ID)
        self.assertArgHasType(Security.CMSDecoderCopySignerTimestamp, 1, objc._C_ULNG)
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestamp,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_DBL,
        )

        self.assertResultHasType(
            Security.CMSDecoderCopySignerTimestampCertificates, objc._C_INT
        )
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestampCertificates, 0, objc._C_ID
        )
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestampCertificates, 1, objc._C_ULNG
        )
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestampCertificates,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(
            Security.CMSDecoderCopySignerTimestampCertificates, 2
        )

    @min_os_level("10.10")
    def test_functions_10_10(self):
        self.assertResultHasType(
            Security.CMSDecoderCopySignerTimestampWithPolicy, objc._C_INT
        )
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestampWithPolicy, 0, objc._C_ID
        )
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestampWithPolicy, 1, objc._C_ID
        )
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestampWithPolicy, 2, objc._C_ULNG
        )
        self.assertArgHasType(
            Security.CMSDecoderCopySignerTimestampWithPolicy,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_DBL,
        )
