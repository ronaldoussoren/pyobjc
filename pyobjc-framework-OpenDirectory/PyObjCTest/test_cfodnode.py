from PyObjCTools.TestSupport import *
import CFOpenDirectory

try:
    long
except NameError:
    long = int

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

if __name__ == "__main__":
    main()
