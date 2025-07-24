from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLAPublicDefines(TestCase):
    @min_os_level("10.10")
    def testConstants(self):
        self.assertEqual(LocalAuthentication.kLABiometryTypeNone, 0)
        self.assertEqual(LocalAuthentication.kLABiometryTypeTouchID, 1 << 0)
        self.assertEqual(LocalAuthentication.kLABiometryTypeFaceID, 1 << 1)
        self.assertEqual(LocalAuthentication.kLABiometryTypeOpticID, 1 << 2)

        self.assertEqual(LocalAuthentication.kLACredentialTypeApplicationPassword, 0)
        self.assertEqual(LocalAuthentication.kLAErrorNotInteractive, -1004)

        self.assertEqual(
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometrics, 1
        )
        self.assertEqual(LocalAuthentication.kLAPolicyDeviceOwnerAuthentication, 2)
        self.assertEqual(LocalAuthentication.kLAOptionUserFallback, 1)
        self.assertEqual(LocalAuthentication.kLAOptionAuthenticationReason, 2)
        self.assertEqual(
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithWatch, 3
        )
        self.assertEqual(
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch,
            4,
        )
        self.assertEqual(
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithWristDetection,
            5,
        )
        self.assertEqual(
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithCompanion,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithWatch,
        )
        self.assertEqual(
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrCompanion,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch,
        )

        self.assertEqual(LocalAuthentication.kLACredentialTypePasscode, -1)
        self.assertEqual(LocalAuthentication.kLACredentialTypePassphrase, -2)
        self.assertEqual(LocalAuthentication.kLACredentialCTKPIN, -3)
        self.assertEqual(LocalAuthentication.kLACredentialSmartCardPIN, -3)

        self.assertEqual(LocalAuthentication.kLAErrorAuthenticationFailed, -1)
        self.assertEqual(LocalAuthentication.kLAErrorUserCancel, -2)
        self.assertEqual(LocalAuthentication.kLAErrorUserFallback, -3)
        self.assertEqual(LocalAuthentication.kLAErrorSystemCancel, -4)
        self.assertEqual(LocalAuthentication.kLAErrorPasscodeNotSet, -5)
        self.assertEqual(LocalAuthentication.kLAErrorTouchIDNotAvailable, -6)
        self.assertEqual(LocalAuthentication.kLAErrorTouchIDNotEnrolled, -7)
        self.assertEqual(LocalAuthentication.kLAErrorTouchIDLockout, -8)
        self.assertEqual(LocalAuthentication.kLAErrorAppCancel, -9)
        self.assertEqual(LocalAuthentication.kLAErrorInvalidContext, -10)
        self.assertEqual(LocalAuthentication.kLAErrorWatchNotAvailable, -11)
        self.assertEqual(LocalAuthentication.kLAErrorBiometryNotPaired, -12)
        self.assertEqual(LocalAuthentication.kLAErrorBiometryDisconnected, -13)
        self.assertEqual(LocalAuthentication.kLAErrorInvalidDimensions, -14)
        self.assertEqual(
            LocalAuthentication.kLAErrorCompanionNotAvailable,
            LocalAuthentication.kLAErrorWatchNotAvailable,
        )
        self.assertEqual(
            LocalAuthentication.kLAErrorDomain, "com.apple.LocalAuthentication"
        )

        self.assertEqual(
            LocalAuthentication.kLAErrorBiometryNotAvailable,
            LocalAuthentication.kLAErrorTouchIDNotAvailable,
        )
        self.assertEqual(
            LocalAuthentication.kLAErrorBiometryNotEnrolled,
            LocalAuthentication.kLAErrorTouchIDNotEnrolled,
        )
        self.assertEqual(
            LocalAuthentication.kLAErrorBiometryLockout,
            LocalAuthentication.kLAErrorTouchIDLockout,
        )

        self.assertEqual(LocalAuthentication.kLACompanionTypeNone, 0)
        self.assertEqual(LocalAuthentication.kLACompanionTypeWatch, 1 << 0)
        self.assertEqual(LocalAuthentication.kLACompanionTypeMac, 1 << 1)
        self.assertEqual(LocalAuthentication.kLACompanionTypeVision, 1 << 2)

        self.assertEqual(LocalAuthentication.kLAAccessControlOperationCreateItem, 0)
        self.assertEqual(LocalAuthentication.kLAAccessControlOperationUseItem, 1)
        self.assertEqual(LocalAuthentication.kLAAccessControlOperationCreateKey, 2)
        self.assertEqual(LocalAuthentication.kLAAccessControlOperationUseKeySign, 3)
        self.assertEqual(LocalAuthentication.kLAAccessControlOperationUseKeyDecrypt, 4)
        self.assertEqual(
            LocalAuthentication.kLAAccessControlOperationUseKeyKeyExchange, 5
        )
