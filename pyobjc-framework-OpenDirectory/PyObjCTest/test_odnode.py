from PyObjCTools.TestSupport import *

import OpenDirectory

class TestODNode (TestCase):
    def testMethods(self):
        self.assertArgIsOut(OpenDirectory.ODNode.nodeWithSession_type_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.nodeWithSession_name_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.initWithSession_type_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.initWithSession_name_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.subnodeNamesAndReturnError_, 0)
        self.assertArgIsOut(OpenDirectory.ODNode.unreachableSubnodeNamesAndReturnError_, 0)
        self.assertArgIsOut(OpenDirectory.ODNode.nodeDetailsForKeys_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODNode.supportedRecordTypesAndReturnError_, 0)
        self.assertArgIsOut(OpenDirectory.ODNode.supportedAttributesForRecordType_error_, 1)
        self.assertResultIsBOOL(OpenDirectory.ODNode.setCredentialsWithRecordType_recordName_password_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.setCredentialsWithRecordType_recordName_password_error_, 3)
        self.assertResultIsBOOL(OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_, 3)
        self.assertArgIsOut(OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_, 4)
        self.assertArgIsOut(OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_, 5)
        self.assertResultIsBOOL(OpenDirectory.ODNode.setCredentialsUsingKerberosCache_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.setCredentialsUsingKerberosCache_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODNode.recordWithRecordType_name_attributes_error_, 3)
        self.assertArgIsOut(OpenDirectory.ODNode.customCall_sendData_error_, 2)

if __name__ == "__main__":
    main()
