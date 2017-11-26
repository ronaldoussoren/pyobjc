from PyObjCTools.TestSupport import *

import Security

class Testcssmkrapi (TestCase):

    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, 'CSSM_KR_NAME'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_PROFILE'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_WRAPPEDPRODUCT_INFO'))
        self.assertFalse(hasattr(Security, 'CSSM_KRSUBSERVICE'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_INDIV_POLICY'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_ENT_POLICY'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_LE_MAN_POLICY'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_LE_USE_POLICY'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_INDIV'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_ENT'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_LE_MAN'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_LE_USE'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_LE'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_OPTIMIZE'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_DROP_WORKFACTOR'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_POLICY_LIST_ITEM'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_POLICY_INFO'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_SetEnterpriseRecoveryPolicy'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_CreateRecoveryRegistrationContext'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_CreateRecoveryEnablementContext'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_CreateRecoveryRequestContext'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_GetPolicyInfo'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_RegistrationRequest'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_RegistrationRetrieve'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_GenerateRecoveryFields'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_ProcessRecoveryFields'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_RecoveryRequest'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_RecoveryRetrieve'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_GetRecoveredObject'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_RecoveryRequestAbort'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_QueryPolicyInfo'))
        self.assertFalse(hasattr(Security, 'CSSM_KR_PassThrough'))


if __name__ == "__main__":
    main()
