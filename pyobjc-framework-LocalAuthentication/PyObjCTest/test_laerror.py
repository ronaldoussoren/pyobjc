from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLAContext(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(LocalAuthentication.LAError)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(
            LocalAuthentication.LAErrorAuthenticationFailed,
            LocalAuthentication.kLAErrorAuthenticationFailed,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorUserCancel,
            LocalAuthentication.kLAErrorUserCancel,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorUserFallback,
            LocalAuthentication.kLAErrorUserFallback,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorSystemCancel,
            LocalAuthentication.kLAErrorSystemCancel,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorPasscodeNotSet,
            LocalAuthentication.kLAErrorPasscodeNotSet,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorTouchIDNotAvailable,
            LocalAuthentication.kLAErrorTouchIDNotAvailable,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorTouchIDNotEnrolled,
            LocalAuthentication.kLAErrorTouchIDNotEnrolled,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorTouchIDLockout,
            LocalAuthentication.kLAErrorTouchIDLockout,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorAppCancel, LocalAuthentication.kLAErrorAppCancel
        )
        self.assertEqual(
            LocalAuthentication.LAErrorInvalidContext,
            LocalAuthentication.kLAErrorInvalidContext,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorNotInteractive,
            LocalAuthentication.kLAErrorNotInteractive,
        )

        self.assertEqual(
            LocalAuthentication.LAErrorBiometryNotAvailable,
            LocalAuthentication.kLAErrorBiometryNotAvailable,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorBiometryNotEnrolled,
            LocalAuthentication.kLAErrorBiometryNotEnrolled,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorBiometryLockout,
            LocalAuthentication.kLAErrorBiometryLockout,
        )

        self.assertEqual(
            LocalAuthentication.LAErrorWatchNotAvailable,
            LocalAuthentication.kLAErrorWatchNotAvailable,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorBiometryNotPaired,
            LocalAuthentication.kLAErrorBiometryNotPaired,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorBiometryDisconnected,
            LocalAuthentication.kLAErrorBiometryDisconnected,
        )
        self.assertEqual(
            LocalAuthentication.LAErrorInvalidDimensions,
            LocalAuthentication.kLAErrorInvalidDimensions,
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(LocalAuthentication.LAErrorDomain, str)
