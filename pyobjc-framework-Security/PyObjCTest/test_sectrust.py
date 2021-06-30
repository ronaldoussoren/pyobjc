import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

SecTrustCallback = b"v@I"
SecTrustWithErrorCallback = b"v@B@"


class TestSecTrusted(TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecTrustRef)

    def test_constants(self):
        self.assertEqual(Security.kSecTrustResultInvalid, 0)
        self.assertEqual(Security.kSecTrustResultProceed, 1)
        self.assertEqual(Security.kSecTrustResultConfirm, 2)
        self.assertEqual(Security.kSecTrustResultDeny, 3)
        self.assertEqual(Security.kSecTrustResultUnspecified, 4)
        self.assertEqual(Security.kSecTrustResultRecoverableTrustFailure, 5)
        self.assertEqual(Security.kSecTrustResultFatalTrustFailure, 6)
        self.assertEqual(Security.kSecTrustResultOtherError, 7)

        self.assertEqual(Security.kSecTrustOptionAllowExpired, 0x00000001)
        self.assertEqual(Security.kSecTrustOptionLeafIsCA, 0x00000002)
        self.assertEqual(Security.kSecTrustOptionFetchIssuerFromNet, 0x00000004)
        self.assertEqual(Security.kSecTrustOptionAllowExpiredRoot, 0x00000008)
        self.assertEqual(Security.kSecTrustOptionRequireRevPerCert, 0x00000010)
        self.assertEqual(Security.kSecTrustOptionUseTrustSettings, 0x00000020)
        self.assertEqual(Security.kSecTrustOptionImplicitAnchors, 0x00000040)

    @min_os_level("10.7")
    def test_constants10_7(self):
        self.assertIsInstance(Security.kSecPropertyTypeTitle, str)
        self.assertIsInstance(Security.kSecPropertyTypeError, str)

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(Security.kSecTrustEvaluationDate, str)
        self.assertIsInstance(Security.kSecTrustExtendedValidation, str)
        self.assertIsInstance(Security.kSecTrustOrganizationName, str)
        self.assertIsInstance(Security.kSecTrustResultValue, str)
        self.assertIsInstance(Security.kSecTrustRevocationChecked, str)
        self.assertIsInstance(Security.kSecTrustRevocationValidUntilDate, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(Security.kSecTrustCertificateTransparency, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(Security.kSecTrustCertificateTransparencyWhiteList, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecTrustGetTypeID(), int)

        self.assertResultHasType(Security.SecTrustCreateWithCertificates, objc._C_INT)
        self.assertArgHasType(Security.SecTrustCreateWithCertificates, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustCreateWithCertificates, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustCreateWithCertificates,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecTrustCreateWithCertificates, 2)

        self.assertResultHasType(Security.SecTrustSetPolicies, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSetPolicies, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSetPolicies, 1, objc._C_ID)

        self.assertResultHasType(Security.SecTrustCopyPolicies, objc._C_INT)
        self.assertArgHasType(Security.SecTrustCopyPolicies, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustCopyPolicies, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecTrustCopyPolicies, 1)

        self.assertResultHasType(Security.SecTrustSetAnchorCertificates, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSetAnchorCertificates, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSetAnchorCertificates, 1, objc._C_ID)

        self.assertResultHasType(
            Security.SecTrustSetAnchorCertificatesOnly, objc._C_INT
        )
        self.assertArgHasType(Security.SecTrustSetAnchorCertificatesOnly, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustSetAnchorCertificatesOnly, 1, objc._C_NSBOOL
        )

        self.assertResultHasType(
            Security.SecTrustCopyCustomAnchorCertificates, objc._C_INT
        )
        self.assertArgHasType(
            Security.SecTrustCopyCustomAnchorCertificates, 0, objc._C_ID
        )
        self.assertArgHasType(
            Security.SecTrustCopyCustomAnchorCertificates,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecTrustCopyCustomAnchorCertificates, 1)

        self.assertResultHasType(Security.SecTrustSetVerifyDate, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSetVerifyDate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSetVerifyDate, 1, objc._C_ID)

        self.assertResultHasType(Security.SecTrustGetVerifyTime, objc._C_DBL)
        self.assertArgHasType(Security.SecTrustGetVerifyTime, 0, objc._C_ID)

        self.assertResultHasType(Security.SecTrustSetKeychains, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSetKeychains, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSetKeychains, 1, objc._C_ID)

        self.assertFalse(hasattr(Security, "SecTrustSetParameters"))
        self.assertFalse(hasattr(Security, "SecTrustGetResult"))
        self.assertFalse(hasattr(Security, "SecTrustGetCssmResult"))
        self.assertFalse(hasattr(Security, "SecTrustGetCssmResultCode"))
        self.assertFalse(hasattr(Security, "SecTrustGetTPHandle"))

        self.assertResultHasType(Security.SecTrustCopyAnchorCertificates, objc._C_INT)
        self.assertArgHasType(
            Security.SecTrustCopyAnchorCertificates,
            0,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecTrustCopyAnchorCertificates, 0)

    @min_os_level("10.7")
    def test_functions_10_7(self):
        self.assertResultHasType(Security.SecTrustEvaluate, objc._C_INT)
        self.assertArgHasType(Security.SecTrustEvaluate, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustEvaluate, 1, objc._C_OUT + objc._C_PTR + objc._C_UINT
        )

        self.assertResultHasType(Security.SecTrustEvaluateAsync, objc._C_INT)
        self.assertArgHasType(Security.SecTrustEvaluateAsync, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustEvaluateAsync, 1, b"^{dispatch_queue_s}")
        self.assertArgIsBlock(Security.SecTrustEvaluateAsync, 2, SecTrustCallback)

        self.assertResultHasType(Security.SecTrustGetTrustResult, objc._C_INT)
        self.assertArgHasType(Security.SecTrustGetTrustResult, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustGetTrustResult, 1, objc._C_OUT + objc._C_PTR + objc._C_UINT
        )

        self.assertResultHasType(Security.SecTrustCopyPublicKey, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTrustCopyPublicKey)
        self.assertArgHasType(Security.SecTrustCopyPublicKey, 0, objc._C_ID)

        self.assertResultHasType(
            Security.SecTrustGetCertificateCount, objc._C_NSInteger
        )
        self.assertArgHasType(Security.SecTrustGetCertificateCount, 0, objc._C_ID)

        self.assertResultHasType(Security.SecTrustGetCertificateAtIndex, objc._C_ID)
        self.assertArgHasType(Security.SecTrustGetCertificateAtIndex, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustGetCertificateAtIndex, 1, objc._C_NSInteger
        )

        self.assertResultHasType(Security.SecTrustCopyProperties, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTrustCopyProperties)
        self.assertArgHasType(Security.SecTrustCopyProperties, 0, objc._C_ID)

        self.assertResultHasType(Security.SecTrustSetOptions, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSetOptions, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSetOptions, 1, objc._C_UINT)

    @min_os_level("10.9")
    def test_functions_10_9(self):
        self.assertResultHasType(Security.SecTrustSetNetworkFetchAllowed, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSetNetworkFetchAllowed, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustSetNetworkFetchAllowed, 1, objc._C_NSBOOL
        )

        self.assertResultHasType(Security.SecTrustGetNetworkFetchAllowed, objc._C_INT)
        self.assertArgHasType(Security.SecTrustGetNetworkFetchAllowed, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustGetNetworkFetchAllowed,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_NSBOOL,
        )

        self.assertResultHasType(Security.SecTrustCopyExceptions, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTrustCopyExceptions)
        self.assertArgHasType(Security.SecTrustCopyExceptions, 0, objc._C_ID)

        self.assertResultHasType(Security.SecTrustSetExceptions, objc._C_BOOL)
        self.assertArgHasType(Security.SecTrustSetExceptions, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSetExceptions, 1, objc._C_ID)

        self.assertResultHasType(Security.SecTrustCopyResult, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecTrustCopyResult)
        self.assertArgHasType(Security.SecTrustCopyResult, 0, objc._C_ID)

        self.assertResultHasType(Security.SecTrustSetOCSPResponse, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSetOCSPResponse, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSetOCSPResponse, 1, objc._C_ID)

    @min_os_level("10.14")
    def test_functions_10_14(self):
        self.assertResultHasType(Security.SecTrustEvaluateWithError, objc._C_BOOL)
        self.assertArgHasType(Security.SecTrustEvaluateWithError, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecTrustEvaluateWithError,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
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
