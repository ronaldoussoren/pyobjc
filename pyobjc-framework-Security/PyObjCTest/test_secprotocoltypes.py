from PyObjCTools.TestSupport import *

import Security

class TestSecProtocolTypes (TestCase):

    @min_os_level('10.14')
    def test_functions(self):
        self.assertResultIsRetained(Security.sec_trust_create)
        self.assertResultIsCFRetained(Security.sec_trust_copy_ref)

        self.assertResultIsRetained(Security.sec_identity_create)
        self.assertResultIsRetained(Security.sec_identity_create_with_certificates)
        self.assertResultIsCFRetained(Security.sec_identity_copy_ref)
        self.assertResultIsCFRetained(Security.sec_identity_copy_certificates_ref)

        self.assertResultIsRetained(Security.sec_certificate_create)
        self.assertResultIsCFRetained(Security.sec_certificate_copy_ref)

if __name__ == "__main__":
    main()
