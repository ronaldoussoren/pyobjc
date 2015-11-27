from PyObjCTools.TestSupport import *
import CFOpenDirectory

class TestCFODNode (TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODNodeGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCreateWithNodeType)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCreateWithNodeType, 3)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCreateWithName)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCreateWithName, 3)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCreateCopy)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCreateCopy, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopySubnodeNames)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopySubnodeNames, 1)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopyUnreachableSubnodeNames)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopyUnreachableSubnodeNames, 1)

        CFOpenDirectory.ODNodeGetName  # No test beyond existance

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopyDetails)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopyDetails, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopySupportedRecordTypes)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopySupportedRecordTypes, 1)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopySupportedAttributes)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopySupportedAttributes, 2)

        self.assertResultHasType(CFOpenDirectory.ODNodeSetCredentials, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeSetCredentials, 4)

        self.assertResultHasType(CFOpenDirectory.ODNodeSetCredentialsExtended, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeSetCredentialsExtended, 6)

        self.assertResultHasType(CFOpenDirectory.ODNodeSetCredentialsUsingKerberosCache, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeSetCredentialsUsingKerberosCache, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCreateRecord)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCreateRecord, 4)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopyRecord)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopyRecord, 4)

        self.assertArgIsOut(CFOpenDirectory.ODNodeCustomCall, 3)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsOut(CFOpenDirectory.ODNodeCustomFunction, 3)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopyPolicies)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopyPolicies, 1)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopySupportedPolicies)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopySupportedPolicies, 1)

        self.assertResultHasType(CFOpenDirectory.ODNodeSetPolicies, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeSetPolicies, 2)

        self.assertResultHasType(CFOpenDirectory.ODNodeSetPolicy, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeSetPolicy, 3)

        self.assertResultHasType(CFOpenDirectory.ODNodeRemovePolicy, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeRemovePolicy, 2)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultHasType(CFOpenDirectory.ODNodeAddAccountPolicy, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeAddAccountPolicy, 3)

        self.assertResultHasType(CFOpenDirectory.ODNodeRemoveAccountPolicy, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeRemoveAccountPolicy, 3)

        self.assertResultHasType(CFOpenDirectory.ODNodeSetAccountPolicies, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodeSetAccountPolicies, 2)

        self.assertResultIsCFRetained(CFOpenDirectory.ODNodeCopyAccountPolicies)
        self.assertArgIsOut(CFOpenDirectory.ODNodeCopyAccountPolicies, 1)

        self.assertResultHasType(CFOpenDirectory.ODNodePasswordContentCheck, objc._C_BOOL)
        self.assertArgIsOut(CFOpenDirectory.ODNodePasswordContentCheck, 3)

if __name__ == "__main__":
    main()
