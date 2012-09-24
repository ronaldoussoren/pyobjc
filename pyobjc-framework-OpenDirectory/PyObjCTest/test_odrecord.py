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
if __name__ == "__main__":
    main()
