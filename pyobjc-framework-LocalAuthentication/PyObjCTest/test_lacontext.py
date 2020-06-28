import objc

from PyObjCTools.TestSupport import TestCase, min_os_level, os_level_between
import LocalAuthentication


class TestLAContext(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(LocalAuthentication.LAContext, objc.objc_class)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(LocalAuthentication.LAContext.canEvaluatePolicy_error_)
        self.assertArgIsOut(LocalAuthentication.LAContext.canEvaluatePolicy_error_, 1)

        self.assertArgIsBlock(
            LocalAuthentication.LAContext.evaluatePolicy_localizedReason_reply_,
            2,
            b"v" + objc._C_NSBOOL + b"@",
        )

    @os_level_between("10.10", "10.15")
    def testMethods10_10_to_15(self):
        self.assertResultIsBOOL(LocalAuthentication.LAContext.isCancelButtonVisible)
        self.assertArgIsBOOL(LocalAuthentication.LAContext.setCancelButtonVisible_, 0)

        self.assertResultIsBOOL(LocalAuthentication.LAContext.isFallbackButtonVisible)
        self.assertArgIsBOOL(LocalAuthentication.LAContext.setFallbackButtonVisible_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBOOL(LocalAuthentication.LAContext.setInteractionNotAllowed_, 0)
        self.assertResultIsBOOL(LocalAuthentication.LAContext.interactionNotAllowed)

        # self.assertArgIsBlock(LocalAuthentication.LAContext.withCurrentContextExecute_queue_, 0, b"v")

    def testConstants(self):
        self.assertEqual(LocalAuthentication.LABiometryTypeNone, 0)
        self.assertEqual(LocalAuthentication.LABiometryNone, 0)
        self.assertEqual(LocalAuthentication.LABiometryTypeTouchID, 1)
        self.assertEqual(LocalAuthentication.LABiometryTypeFaceID, 2)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(
            LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithBiometrics,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometrics,
        )
        self.assertEqual(
            LocalAuthentication.LAPolicyDeviceOwnerAuthentication,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthentication,
        )
        self.assertEqual(
            LocalAuthentication.LACredentialTypeApplicationPassword,
            LocalAuthentication.kLACredentialTypeApplicationPassword,
        )

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(LocalAuthentication.LAAccessControlOperationCreateItem, 0)
        self.assertEqual(LocalAuthentication.LAAccessControlOperationUseItem, 1)
        self.assertEqual(LocalAuthentication.LAAccessControlOperationCreateKey, 2)
        self.assertEqual(LocalAuthentication.LAAccessControlOperationUseKeySign, 3)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertEqual(
            LocalAuthentication.LACredentialTypeSmartCardPIN,
            LocalAuthentication.kLACredentialSmartCardPIN,
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertEqual(LocalAuthentication.LAAccessControlOperationUseKeyDecrypt, 4)
        self.assertEqual(
            LocalAuthentication.LAAccessControlOperationUseKeyKeyExchange, 5
        )

        self.assertIsInstance(
            LocalAuthentication.LATouchIDAuthenticationMaximumAllowableReuseDuration,
            float,
        )

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertEqual(
            LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithWatch,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithWatch,
        )
        self.assertEqual(
            LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch,
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(LocalAuthentication.LAContext.setCredential_type_)
        self.assertResultIsBOOL(LocalAuthentication.LAContext.isCredentialSet_)

        self.assertArgIsBlock(
            LocalAuthentication.LAContext.evaluatePolicy_localizedReason_reply_,
            2,
            b"v" + objc._C_NSBOOL + b"@",
        )
