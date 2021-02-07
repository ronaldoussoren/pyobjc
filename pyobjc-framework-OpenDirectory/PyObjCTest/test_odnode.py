import OpenDirectory
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestODNode(TestCase):
    def testMethods(self):
        self.assertArgIsOut(OpenDirectory.ODNode.nodeWithSession_type_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.nodeWithSession_name_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.initWithSession_type_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.initWithSession_name_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODNode.subnodeNamesAndReturnError_, 0)
        self.assertArgIsOut(
            OpenDirectory.ODNode.unreachableSubnodeNamesAndReturnError_, 0
        )
        self.assertArgIsOut(OpenDirectory.ODNode.nodeDetailsForKeys_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODNode.supportedRecordTypesAndReturnError_, 0)
        self.assertArgIsOut(
            OpenDirectory.ODNode.supportedAttributesForRecordType_error_, 1
        )
        self.assertResultIsBOOL(
            OpenDirectory.ODNode.setCredentialsWithRecordType_recordName_password_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.setCredentialsWithRecordType_recordName_password_error_,
            3,
        )
        self.assertResultIsBOOL(
            OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_,
            3,
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_,
            4,
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.setCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_,
            5,
        )
        self.assertResultIsBOOL(
            OpenDirectory.ODNode.setCredentialsUsingKerberosCache_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.setCredentialsUsingKerberosCache_error_, 1
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.recordWithRecordType_name_attributes_error_, 3
        )
        self.assertArgIsOut(OpenDirectory.ODNode.customCall_sendData_error_, 2)

        self.assertArgIsOut(
            OpenDirectory.ODNode.createRecordWithRecordType_name_attributes_error_, 3
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsOut(OpenDirectory.ODNode.policiesAndReturnError_, 0)
        self.assertArgIsOut(OpenDirectory.ODNode.supportedPoliciesAndReturnError_, 0)
        self.assertResultIsBOOL(OpenDirectory.ODNode.setPolicies_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.setPolicies_error_, 1)
        self.assertResultIsBOOL(OpenDirectory.ODNode.setPolicy_value_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.setPolicy_value_error_, 2)
        self.assertResultIsBOOL(OpenDirectory.ODNode.removePolicy_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.removePolicy_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODNode.customFunction_payload_error_, 2)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(OpenDirectory.ODNode.addAccountPolicy_toCategory_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.addAccountPolicy_toCategory_error_, 2)
        self.assertResultIsBOOL(
            OpenDirectory.ODNode.removeAccountPolicy_fromCategory_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.removeAccountPolicy_fromCategory_error_, 2
        )
        self.assertResultIsBOOL(OpenDirectory.ODNode.setAccountPolicies_error_)
        self.assertArgIsOut(OpenDirectory.ODNode.setAccountPolicies_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODNode.accountPoliciesAndReturnError_, 0)
        self.assertResultIsBOOL(
            OpenDirectory.ODNode.passwordContentCheck_forRecordName_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODNode.passwordContentCheck_forRecordName_error_, 2
        )
