import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import LocalAuthentication

    class TestLAContext (TestCase):
        def testConstants(self):
            self.assertEqual(LocalAutentication.LABiometryTypeNone, 0)
            self.assertEqual(LocalAutentication.LABiometryNone, 0)
            self.assertEqual(LocalAutentication.LABiometryTypeTouchID, 1)

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

        @min_os_level("10.13")
        def testMethods(self):
            self.assertArgIsBOOL(LocalAuthentication.LAContext.setInteractionNotAllowed_, 0)
            self.assertResultIsBOOL(LocalAuthentication.LAContext.interactionNotAllowed)

            #self.assertArgIsBlock(LocalAuthentication.LAContext.withCurrentContextExecute_queue_, 0, b"v")

        @min_os_level("10.10")
        def testConstants(self):
            self.assertEqual(LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithBiometrics,
                LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometrics)
            self.assertEqual(LocalAuthentication.LAPolicyDeviceOwnerAuthentication, LocalAuthentication.kLAPolicyDeviceOwnerAuthentication)
            self.assertEqual(LocalAuthentication.LACredentialTypeApplicationPassword, 0)

        @min_os_level("10.11")
        def testConstants10_11(self):
            self.assertEqual(LocalAuthentication.LAAccessControlOperationCreateItem, 0)
            self.assertEqual(LocalAuthentication.LAAccessControlOperationUseItem, 1)
            self.assertEqual(LocalAuthentication.LAAccessControlOperationCreateKey, 2)
            self.assertEqual(LocalAuthentication.LAAccessControlOperationUseKeySign, 3)

        @min_os_level("10.12")
        def testConstants10_12(self):
            self.assertEqual(LocalAuthentication.LAAccessControlOperationUseKeyDecrypt, 4)
            self.assertEqual(LocalAuthentication.LAAccessControlOperationUseKeyKeyExchange, 5)

            self.assertIsInstance(LocalAuthentication.LATouchIDAuthenticationMaximumAllowableReuseDuration, float)

        @min_os_level('10.11')
        def testMethods10_11(self):
            self.assertResultIsBOOL(LocalAuthentication.LAContext.setCredential_type_)
            self.assertResultIsBOOL(LocalAuthentication.LAContext.isCredentialSet_)

            self.assertArgIsBlock(LocalAuthentication.LAContext.evaluatePolicy_localizedReason_reply_, 2, b"v" + objc._C_NSBOOL + b"@")

if __name__ == "__main__":
    main()
