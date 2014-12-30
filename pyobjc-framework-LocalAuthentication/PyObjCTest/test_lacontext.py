import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import LocalAuthentication

    class TestLAContext (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(LocalAuthentication.LAContext, objc.objc_class)

        @min_os_level("10.10")
        def testMethods(self):
            self.assertResultIsBOOL(LocalAuthentication.LAContext.canEvaluatePolicy_error_)
            self.assertArgIsOut(LocalAuthentication.LAContext.canEvaluatePolicy_error_, 1)

            self.assertArgIsBlock(LocalAuthentication.LAContext.evaluatePolicy_localizedReason_reply_, 2, b"v" + objc._C_NSBOOL + b"@")

            self.assertResultIsBOOL(LocalAuthentication.LAContext.isCancelButtonVisible)
            self.assertArgIsBOOL(LocalAuthentication.LAContext.setCancelButtonVisible_, 0)

            self.assertResultIsBOOL(LocalAuthentication.LAContext.isFallbackButtonVisible)
            self.assertArgIsBOOL(LocalAuthentication.LAContext.setFallbackButtonVisible_, 0)

        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithBiometrics,
                LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometrics)


if __name__ == "__main__":
    main()
