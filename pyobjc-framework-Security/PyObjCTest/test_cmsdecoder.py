import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCMSDecoder(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Security.CMSSignerStatus)
        self.assertEqual(Security.kCMSSignerUnsigned, 0)
        self.assertEqual(Security.kCMSSignerValid, 1)
        self.assertEqual(Security.kCMSSignerNeedsDetachedContent, 2)
        self.assertEqual(Security.kCMSSignerInvalidSignature, 3)
        self.assertEqual(Security.kCMSSignerInvalidCert, 4)
        self.assertEqual(Security.kCMSSignerInvalidIndex, 5)

    def test_types(self):
        self.assertIsCFType(Security.CMSDecoderRef)

    def test_functions(self):
        self.assertIsInstance(Security.CMSDecoderGetTypeID(), int)

        self.assertArgIsOut(Security.CMSDecoderCreate, 0)
        self.assertArgIsCFRetained(Security.CMSDecoderCreate, 0)

        self.assertArgHasType(
            Security.CMSDecoderUpdateMessage, 1, objc._C_IN + objc._C_PTR + objc._C_VOID
        )
        self.assertArgSizeInArg(Security.CMSDecoderUpdateMessage, 1, 2)

        Security.CMSDecoderFinalizeMessage

        Security.CMSDecoderSetDetachedContent

        self.assertArgIsOut(
            Security.CMSDecoderCopyDetachedContent,
            1,
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopyDetachedContent, 1)

        Security.CMSDecoderSetSearchKeychain

        self.assertArgIsOut(
            Security.CMSDecoderGetNumSigners,
            1,
        )

        self.assertArgIsBOOL(Security.CMSDecoderCopySignerStatus, 3)
        self.assertArgIsOut(Security.CMSDecoderCopySignerStatus, 4)
        self.assertArgIsOut(Security.CMSDecoderCopySignerStatus, 5)
        self.assertArgIsOut(Security.CMSDecoderCopySignerStatus, 6)

        self.assertArgIsOut(
            Security.CMSDecoderGetNumSigners,
            1,
        )

        self.assertArgIsOut(Security.CMSDecoderCopySignerCert, 2)
        self.assertArgIsCFRetained(Security.CMSDecoderCopySignerCert, 2)

        self.assertArgHasType(
            Security.CMSDecoderIsContentEncrypted,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )

        self.assertArgIsOut(
            Security.CMSDecoderCopyEncapsulatedContentType,
            1,
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopyEncapsulatedContentType, 1)

        self.assertArgIsOut(
            Security.CMSDecoderCopyAllCerts, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.CMSDecoderCopyAllCerts, 1)

        self.assertArgIsOut(Security.CMSDecoderCopyContent, 1)
        self.assertArgIsCFRetained(Security.CMSDecoderCopyContent, 1)

        self.assertArgIsOut(
            Security.CMSDecoderCopySignerSigningTime,
            2,
        )

        self.assertArgIsOut(
            Security.CMSDecoderCopySignerTimestamp,
            2,
        )

        self.assertArgIsOut(
            Security.CMSDecoderCopySignerTimestampCertificates,
            2,
        )
        self.assertArgIsCFRetained(
            Security.CMSDecoderCopySignerTimestampCertificates, 2
        )

    @min_os_level("10.10")
    def test_functions_10_10(self):
        self.assertArgIsOut(
            Security.CMSDecoderCopySignerTimestampWithPolicy,
            3,
        )
