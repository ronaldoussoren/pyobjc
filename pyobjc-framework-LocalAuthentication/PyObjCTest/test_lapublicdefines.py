import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import LocalAuthentication

    class TestLAPublicDefines (TestCase):
        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometrics, 1)
            self.assertEqual(LocalAuthentication.kLAPolicyDeviceOwnerAuthentication, 2)
            self.assertEqual(LocalAuthentication.kLAOptionUserFallback, 1)
            self.assertEqual(LocalAuthentication.kLAOptionAuthenticationReason, 2)
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
            self.assertEqual(LocalAuthentication.kLAErrorDomain, "com.apple.LocalAuthentication")

if __name__ == "__main__":
    main()
