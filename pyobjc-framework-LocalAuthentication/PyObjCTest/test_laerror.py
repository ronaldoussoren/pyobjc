import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import LocalAuthentication

    class TestLAContext (TestCase):
        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(LocalAuthentication.LAErrorAuthenticationFailed, LocalAuthentication.kLAErrorAuthenticationFailed)
            self.assertEqual(LocalAuthentication.LAErrorUserCancel, LocalAuthentication.kLAErrorUserCancel)
            self.assertEqual(LocalAuthentication.LAErrorUserFallback, LocalAuthentication.kLAErrorUserFallback)
            self.assertEqual(LocalAuthentication.LAErrorSystemCancel, LocalAuthentication.kLAErrorSystemCancel)
            self.assertEqual(LocalAuthentication.LAErrorPasscodeNotSet, LocalAuthentication.kLAErrorPasscodeNotSet)
            self.assertEqual(LocalAuthentication.LAErrorTouchIDNotAvailable, LocalAuthentication.kLAErrorTouchIDNotAvailable)
            self.assertEqual(LocalAuthentication.LAErrorTouchIDNotEnrolled, LocalAuthentication.kLAErrorTouchIDNotEnrolled)
            self.assertEqual(LocalAuthentication.LAErrorTouchIDLockout, LocalAuthentication.kLAErrorTouchIDLockout)
            self.assertEqual(LocalAuthentication.LAErrorAppCancel, LocalAuthentication.kLAErrorAppCancel)
            self.assertEqual(LocalAuthentication.LAErrorInvalidContext, LocalAuthentication.kLAErrorInvalidContext)
            self.assertEqual(LocalAuthentication.LAErrorNotInteractive, LocalAuthentication.kLAErrorNotInteractive)

            self.assertEqual(LocalAuthentication.LAErrorBiometryNotAvailable, LocalAuthentication.kLAErrorBiometryNotAvailable)
            self.assertEqual(LocalAuthentication.LAErrorBiometryNotEnrolled, LocalAuthentication.kLAErrorBiometryNotEnrolled)
            self.assertEqual(LocalAuthentication.LAErrorBiometryLockout, LocalAuthentication.kLAErrorBiometryLockout)

            self.assertIsInstance(LocalAuthentication.LAErrorDomain, unicode)

if __name__ == "__main__":
    main()
