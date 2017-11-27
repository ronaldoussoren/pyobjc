from PyObjCTools.TestSupport import *

import Security

class TestSecIdentity (TestCase):

    @min_os_level('10.6')
    def test_constants_10_6(self):
        self.assertIsInstance(Security.kSecIdentityDomainDefault, unicode)
        self.assertIsInstance(Security.kSecIdentityDomainKerberosKDC, unicode)

    def test_functions(self):
        self.assertIsInstance(Security.SecIdentityGetTypeID(), (int, long))

        self.assertResultHasType(Security.SecIdentityCreateWithCertificate, objc._C_INT)
        self.assertArgHasType(Security.SecIdentityCreateWithCertificate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCreateWithCertificate, 1, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCreateWithCertificate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecIdentityCreateWithCertificate, 2)

        self.assertResultHasType(Security.SecIdentityCopyCertificate, objc._C_INT)
        self.assertArgHasType(Security.SecIdentityCopyCertificate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCopyCertificate, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecIdentityCopyCertificate, 1)

        self.assertResultHasType(Security.SecIdentityCopyPrivateKey, objc._C_INT)
        self.assertArgHasType(Security.SecIdentityCopyPrivateKey, 0, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCopyPrivateKey, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecIdentityCopyPrivateKey, 1)

        self.assertFalse(hasattr(Security, 'SecIdentityCopyPreference'))

        self.assertResultHasType(Security.SecIdentityCopyPreferred, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecIdentityCopyPreferred, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCopyPreferred, 0, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCopyPreferred, 1, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCopyPreferred, 2, objc._C_ID)

        self.assertFalse(hasattr(Security, 'SecIdentitySetPreference'))

        self.assertResultHasType(Security.SecIdentitySetPreferred, objc._C_INT)
        self.assertArgHasType(Security.SecIdentitySetPreferred, 0, objc._C_ID)
        self.assertArgHasType(Security.SecIdentitySetPreferred, 1, objc._C_ID)
        self.assertArgHasType(Security.SecIdentitySetPreferred, 2, objc._C_ID)

        self.assertResultHasType(Security.SecIdentityCopySystemIdentity, objc._C_INT)
        self.assertArgHasType(Security.SecIdentityCopySystemIdentity, 0, objc._C_ID)
        self.assertArgHasType(Security.SecIdentityCopySystemIdentity, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecIdentityCopySystemIdentity, 1)
        self.assertArgHasType(Security.SecIdentityCopySystemIdentity, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecIdentityCopySystemIdentity, 2)

        self.assertResultHasType(Security.SecIdentitySetSystemIdentity, objc._C_INT)
        self.assertArgHasType(Security.SecIdentitySetSystemIdentity, 0, objc._C_ID)
        self.assertArgHasType(Security.SecIdentitySetSystemIdentity, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecIdentitySetSystemIdentity, 1)

if __name__ == "__main__":
    main()
