import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

SecTrustCallback = b"v@I"
SecTrustWithErrorCallback = b"v@B@"


class TestSecTrusted(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecTrustRef)

    def test_enums(self):
        self.assertIsEnumType(Security.SecTrustResultType)
        self.assertEqual(Security.kSecTrustResultInvalid, 0)
        self.assertEqual(Security.kSecTrustResultProceed, 1)
        self.assertEqual(Security.kSecTrustResultConfirm, 2)
        self.assertEqual(Security.kSecTrustResultDeny, 3)
        self.assertEqual(Security.kSecTrustResultUnspecified, 4)
        self.assertEqual(Security.kSecTrustResultRecoverableTrustFailure, 5)
        self.assertEqual(Security.kSecTrustResultFatalTrustFailure, 6)
        self.assertEqual(Security.kSecTrustResultOtherError, 7)

        self.assertIsEnumType(Security.SecTrustOptionFlags)
        self.assertEqual(Security.kSecTrustOptionAllowExpired, 0x00000001)
        self.assertEqual(Security.kSecTrustOptionLeafIsCA, 0x00000002)
        self.assertEqual(Security.kSecTrustOptionFetchIssuerFromNet, 0x00000004)
        self.assertEqual(Security.kSecTrustOptionAllowExpiredRoot, 0x00000008)
        self.assertEqual(Security.kSecTrustOptionRequireRevPerCert, 0x00000010)
        self.assertEqual(Security.kSecTrustOptionUseTrustSettings, 0x00000020)
        self.assertEqual(Security.kSecTrustOptionImplicitAnchors, 0x00000040)

    def test_constants(self):
        self.assertIsInstance(Security.kSecPropertyTypeTitle, str)
        self.assertIsInstance(Security.kSecPropertyTypeError, str)

        self.assertIsInstance(Security.kSecTrustEvaluationDate, str)
        self.assertIsInstance(Security.kSecTrustExtendedValidation, str)
        self.assertIsInstance(Security.kSecTrustOrganizationName, str)
        self.assertIsInstance(Security.kSecTrustResultValue, str)
        self.assertIsInstance(Security.kSecTrustRevocationChecked, str)
        self.assertIsInstance(Security.kSecTrustRevocationValidUntilDate, str)

    @min_os_level("10.12")
    def test_constants10_11(self):
        self.assertIsInstance(Security.kSecTrustCertificateTransparency, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(Security.kSecTrustCertificateTransparencyWhiteList, str)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(Security.kSecTrustQCStatements, str)
        self.assertIsInstance(Security.kSecTrustQWACValidation, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecTrustGetTypeID(), int)

        self.assertArgIsOut(
            Security.SecTrustCreateWithCertificates,
            2,
        )
        self.assertArgIsCFRetained(Security.SecTrustCreateWithCertificates, 2)

        Security.SecTrustSetPolicies

        self.assertArgIsOut(Security.SecTrustCopyPolicies, 1)
        self.assertArgIsCFRetained(Security.SecTrustCopyPolicies, 1)

        Security.SecTrustSetAnchorCertificates

        self.assertArgIsBOOL(Security.SecTrustSetAnchorCertificatesOnly, 1)

        self.assertArgIsOut(
            Security.SecTrustCopyCustomAnchorCertificates,
            1,
        )
        self.assertArgIsCFRetained(Security.SecTrustCopyCustomAnchorCertificates, 1)

        Security.SecTrustSetVerifyDate

        Security.SecTrustGetVerifyTime

        Security.SecTrustSetKeychains

        self.assertFalse(hasattr(Security, "SecTrustSetParameters"))
        self.assertFalse(hasattr(Security, "SecTrustGetResult"))
        self.assertFalse(hasattr(Security, "SecTrustGetCssmResult"))
        self.assertFalse(hasattr(Security, "SecTrustGetCssmResultCode"))
        self.assertFalse(hasattr(Security, "SecTrustGetTPHandle"))

        self.assertArgIsOut(
            Security.SecTrustCopyAnchorCertificates,
            0,
        )
        self.assertArgIsCFRetained(Security.SecTrustCopyAnchorCertificates, 0)

        self.assertArgIsOut(Security.SecTrustEvaluate, 1)

        self.assertArgIsBlock(Security.SecTrustEvaluateAsync, 2, SecTrustCallback)

        self.assertArgIsOut(Security.SecTrustGetTrustResult, 1)

        Security.SecTrustCopyPublicKey

        Security.SecTrustGetCertificateCount

        Security.SecTrustGetCertificateAtIndex

        Security.SecTrustCopyProperties

        Security.SecTrustSetOptions

        self.assertArgIsBOOL(Security.SecTrustSetNetworkFetchAllowed, 1)

        self.assertArgHasType(
            Security.SecTrustGetNetworkFetchAllowed,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )

        Security.SecTrustCopyExceptions

        Security.SecTrustSetExceptions

        self.assertResultIsCFRetained(Security.SecTrustCopyResult)

        Security.SecTrustSetOCSPResponse

    @min_os_level("10.14")
    def test_functions_10_14(self):
        self.assertArgIsOut(
            Security.SecTrustEvaluateWithError,
            1,
        )

    @min_os_level("10.14.2")
    def test_functions_10_14_2(self):
        Security.SecTrustSetSignedCertificateTimestamps

    @min_os_level("10.15")
    def test_functions_10_15(self):
        self.assertArgIsBlock(
            Security.SecTrustEvaluateAsyncWithError, 2, SecTrustWithErrorCallback
        )

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertResultIsCFRetained(Security.SecTrustCopyKey)

    @min_os_level("12.0")
    def test_functions12_0(self):
        self.assertResultIsCFRetained(Security.SecTrustCopyCertificateChain)
