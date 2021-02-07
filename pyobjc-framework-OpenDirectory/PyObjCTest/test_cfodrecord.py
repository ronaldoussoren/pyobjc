import CFOpenDirectory
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCFODRecord(TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODRecordGetTypeID(), int)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordSetNodeCredentials, objc._C_BOOL
        )
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentials, 3)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordSetNodeCredentialsExtended, objc._C_BOOL
        )
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentialsExtended, 4)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentialsExtended, 5)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentialsExtended, 6)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordSetNodeCredentialsUsingKerberosCache, objc._C_BOOL
        )
        self.assertArgIsOut(
            CFOpenDirectory.ODRecordSetNodeCredentialsUsingKerberosCache, 2
        )

        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopyPasswordPolicy)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopyPasswordPolicy, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordVerifyPassword, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordVerifyPassword, 2)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordVerifyPasswordExtended, objc._C_BOOL
        )
        self.assertArgIsOut(CFOpenDirectory.ODRecordVerifyPasswordExtended, 3)
        self.assertArgIsOut(CFOpenDirectory.ODRecordVerifyPasswordExtended, 4)
        self.assertArgIsOut(CFOpenDirectory.ODRecordVerifyPasswordExtended, 5)

        self.assertResultHasType(CFOpenDirectory.ODRecordChangePassword, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordChangePassword, 3)

        CFOpenDirectory.ODRecordGetRecordType
        CFOpenDirectory.ODRecordGetRecordName

        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopyValues)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopyValues, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordSetValue, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetValue, 3)

        self.assertResultHasType(CFOpenDirectory.ODRecordAddValue, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordAddValue, 3)

        self.assertResultHasType(CFOpenDirectory.ODRecordRemoveValue, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordRemoveValue, 3)

        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopyDetails)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopyDetails, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordSynchronize, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSynchronize, 1)

        self.assertResultHasType(CFOpenDirectory.ODRecordDelete, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordDelete, 1)

        self.assertResultHasType(CFOpenDirectory.ODRecordAddMember, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordAddMember, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordRemoveMember, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordRemoveMember, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordContainsMember, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordContainsMember, 2)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopyPolicies)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopyPolicies, 1)

        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopyEffectivePolicies)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopyEffectivePolicies, 1)

        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopySupportedPolicies)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopySupportedPolicies, 1)

        self.assertResultHasType(CFOpenDirectory.ODRecordSetPolicies, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetPolicies, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordSetPolicy, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetPolicy, 3)

        self.assertResultHasType(CFOpenDirectory.ODRecordRemovePolicy, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordRemovePolicy, 2)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultHasType(CFOpenDirectory.ODRecordAddAccountPolicy, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordAddAccountPolicy, 3)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordRemoveAccountPolicy, objc._C_BOOL
        )
        self.assertArgIsOut(CFOpenDirectory.ODRecordRemoveAccountPolicy, 3)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordSetAccountPolicies, objc._C_BOOL
        )
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetAccountPolicies, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopyAccountPolicies)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopyAccountPolicies, 1)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordAuthenticationAllowed, objc._C_BOOL
        )
        self.assertArgIsOut(CFOpenDirectory.ODRecordAuthenticationAllowed, 1)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordPasswordChangeAllowed, objc._C_BOOL
        )
        self.assertArgIsOut(CFOpenDirectory.ODRecordPasswordChangeAllowed, 2)

        self.assertResultHasType(
            CFOpenDirectory.ODRecordWillPasswordExpire, objc._C_BOOL
        )
        self.assertResultHasType(
            CFOpenDirectory.ODRecordWillAuthenticationsExpire, objc._C_BOOL
        )

        CFOpenDirectory.ODRecordSecondsUntilPasswordExpires  # No further tests
        CFOpenDirectory.ODRecordSecondsUntilAuthenticationsExpire  # No further tests
