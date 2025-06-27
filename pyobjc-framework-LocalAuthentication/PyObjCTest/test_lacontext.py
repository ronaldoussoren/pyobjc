import objc

from PyObjCTools.TestSupport import TestCase, min_os_level, os_level_between
import LocalAuthentication
import Security
import Foundation


class TestLAContext(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(LocalAuthentication.LAAccessControlOperation)
        self.assertIsEnumType(LocalAuthentication.LABiometryType)
        self.assertIsEnumType(LocalAuthentication.LACredentialType)
        self.assertIsEnumType(LocalAuthentication.LAPolicy)

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
        self.assertEqual(
            LocalAuthentication.LABiometryTypeNone,
            LocalAuthentication.kLABiometryTypeNone,
        )
        self.assertEqual(LocalAuthentication.LABiometryNone, 0)
        self.assertEqual(
            LocalAuthentication.LABiometryTypeTouchID,
            LocalAuthentication.kLABiometryTypeTouchID,
        )
        self.assertEqual(
            LocalAuthentication.LABiometryTypeFaceID,
            LocalAuthentication.kLABiometryTypeFaceID,
        )
        self.assertEqual(
            LocalAuthentication.LABiometryTypeOpticID,
            LocalAuthentication.kLABiometryTypeOpticID,
        )

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
        self.assertEqual(
            LocalAuthentication.LAAccessControlOperationCreateItem,
            LocalAuthentication.kLAAccessControlOperationCreateItem,
        )
        self.assertEqual(
            LocalAuthentication.LAAccessControlOperationUseItem,
            LocalAuthentication.kLAAccessControlOperationUseItem,
        )
        self.assertEqual(
            LocalAuthentication.LAAccessControlOperationCreateKey,
            LocalAuthentication.kLAAccessControlOperationCreateKey,
        )
        self.assertEqual(
            LocalAuthentication.LAAccessControlOperationUseKeySign,
            LocalAuthentication.kLAAccessControlOperationUseKeySign,
        )

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertEqual(
            LocalAuthentication.LACredentialTypeSmartCardPIN,
            LocalAuthentication.kLACredentialSmartCardPIN,
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertEqual(
            LocalAuthentication.LAAccessControlOperationUseKeyDecrypt,
            LocalAuthentication.kLAAccessControlOperationUseKeyDecrypt,
        )
        self.assertEqual(
            LocalAuthentication.LAAccessControlOperationUseKeyKeyExchange,
            LocalAuthentication.kLAAccessControlOperationUseKeyKeyExchange,
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
            LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithCompanion,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithCompanion,
        )
        self.assertEqual(
            LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrWatch,
        )
        self.assertEqual(
            LocalAuthentication.LAPolicyDeviceOwnerAuthenticationWithBiometricsOrCompanion,
            LocalAuthentication.kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrCompanion,
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

    @min_os_level("10.11")
    def test_regr_security_types(self):
        # Issue #324
        auth_ctx = LocalAuthentication.LAContext.new()
        access_control = Security.SecAccessControlCreateWithFlags(
            None,
            Security.kSecAttrAccessibleWhenUnlocked,
            Security.kSecAccessControlUserPresence,
            None,
        )[0]

        called = False

        def callback(a, b):
            nonlocal called
            called = True

        auth_ctx.evaluateAccessControl_operation_localizedReason_reply_(
            access_control,
            LocalAuthentication.LAAccessControlOperationCreateKey,
            "test",
            callback,
        )

        loop = Foundation.NSRunLoop.currentRunLoop()
        loop.runUntilDate_(Foundation.NSDate.dateWithTimeIntervalSinceNow_(1.5))

        self.assertTrue(called)
