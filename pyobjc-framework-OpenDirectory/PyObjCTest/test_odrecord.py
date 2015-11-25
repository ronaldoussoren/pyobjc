from PyObjCTools.TestSupport import *

import OpenDirectory

class TestODRecord (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(OpenDirectory.ODRecord.setNodeCredentials_password_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.setNodeCredentials_password_error_, 2)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.setNodeCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.setNodeCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_, 3)
        self.assertArgIsOut(OpenDirectory.ODRecord.setNodeCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_, 4)
        self.assertArgIsOut(OpenDirectory.ODRecord.setNodeCredentialsWithRecordType_authenticationType_authenticationItems_continueItems_context_error_, 5)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.setNodeCredentialsUsingKerberosCache_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.setNodeCredentialsUsingKerberosCache_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_, 3)
        self.assertArgIsOut(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_, 4)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.synchronizeAndReturnError_)
        self.assertArgIsOut(OpenDirectory.ODRecord.synchronizeAndReturnError_, 0)

        self.assertArgIsOut(OpenDirectory.ODRecord.recordDetailsForAttributes_error_, 1)

        self.assertArgIsOut(OpenDirectory.ODRecord.valuesForAttribute_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.setValue_forAttribute_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.setValue_forAttribute_error_, 2)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.removeValuesForAttribute_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.removeValuesForAttribute_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.removeValue_fromAttribute_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.removeValue_fromAttribute_error_, 2)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.addValue_toAttribute_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.addValue_toAttribute_error_, 2)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.deleteRecordAndReturnError_)
        self.assertArgIsOut(OpenDirectory.ODRecord.deleteRecordAndReturnError_, 0)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.addMemberRecord_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.addMemberRecord_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.removeMemberRecord_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.removeMemberRecord_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.isMemberRecord_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.isMemberRecord_error_, 1)

        self.assertArgIsOut(OpenDirectory.ODRecord.passwordPolicyAndReturnError_, 0)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.verifyPassword_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.verifyPassword_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_, 2)
        self.assertArgIsOut(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_, 3)
        self.assertArgIsOut(OpenDirectory.ODRecord.verifyExtendedWithAuthenticationType_authenticationItems_continueItems_context_error_, 4)


        self.assertResultIsBOOL(OpenDirectory.ODRecord.changePassword_toPassword_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.changePassword_toPassword_error_, 2)


    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsOut(OpenDirectory.ODRecord.policiesAndReturnError_, 0)
        self.assertArgIsOut(OpenDirectory.ODRecord.effectivePoliciesAndReturnError_, 0)
        self.assertArgIsOut(OpenDirectory.ODRecord.supportedPoliciesAndReturnError_, 0)
        self.assertResultIsBOOL(OpenDirectory.ODRecord.setPolicies_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.setPolicies_error_, 1)
        self.assertResultIsBOOL(OpenDirectory.ODRecord.setPolicy_value_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.setPolicy_value_error_, 2)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.removePolicy_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.removePolicy_error_, 1)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(OpenDirectory.ODRecord.addAccountPolicy_toCategory_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.addAccountPolicy_toCategory_error_, 2)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.removeAccountPolicy_fromCategory_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.removeAccountPolicy_fromCategory_error_, 2)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.setAccountPolicies_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.setAccountPolicies_error_, 1)

        self.assertArgIsOut(OpenDirectory.ODRecord.accountPoliciesAndReturnError_, 0)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.authenticationAllowedAndReturnError_)
        self.assertArgIsOut(OpenDirectory.ODRecord.authenticationAllowedAndReturnError_, 0)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.passwordChangeAllowed_error_)
        self.assertArgIsOut(OpenDirectory.ODRecord.passwordChangeAllowed_error_, 1)

        self.assertResultIsBOOL(OpenDirectory.ODRecord.willPasswordExpire_)
        self.assertResultIsBOOL(OpenDirectory.ODRecord.willAuthenticationsExpire_)

if __name__ == "__main__":
    main()
