from PyObjCTools.TestSupport import *
import CFOpenDirectory

try:
    long
except NameError:
    long = int

class TestCFODRecord (TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODRecordGetTypeID(), (int, long))

        self.assertResultHasType(CFOpenDirectory.ODRecordSetNodeCredentials, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentials, 3)

        self.assertResultHasType(CFOpenDirectory.ODRecordSetNodeCredentialsExtended, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentialsExtended, 4)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentialsExtended, 5)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentialsExtended, 6)

        self.assertResultHasType(CFOpenDirectory.ODRecordSetNodeCredentialsUsingKerberosCache, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordSetNodeCredentialsUsingKerberosCache, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODRecordCopyPasswordPolicy)
        self.assertArgIsOut(CFOpenDirectory.ODRecordCopyPasswordPolicy, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordVerifyPassword, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODRecordVerifyPassword, 2)

        self.assertResultHasType(CFOpenDirectory.ODRecordVerifyPasswordExtended, objc._C_BOOL)
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

if __name__ == "__main__":
    main()
