import Security
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSecIdentity(TestCase):
    def test_constants(self):
        self.assertIsInstance(Security.kSecIdentityDomainDefault, str)
        self.assertIsInstance(Security.kSecIdentityDomainKerberosKDC, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecIdentityGetTypeID(), int)

        self.assertArgIsOut(
            Security.SecIdentityCreateWithCertificate,
            2,
        )
        self.assertArgIsCFRetained(Security.SecIdentityCreateWithCertificate, 2)

        self.assertArgIsOut(
            Security.SecIdentityCopyCertificate,
            1,
        )
        self.assertArgIsCFRetained(Security.SecIdentityCopyCertificate, 1)

        self.assertArgIsOut(
            Security.SecIdentityCopyPrivateKey,
            1,
        )
        self.assertArgIsCFRetained(Security.SecIdentityCopyPrivateKey, 1)

        self.assertFalse(hasattr(Security, "SecIdentityCopyPreference"))

        Security.SecIdentityCopyPreferred

        self.assertFalse(hasattr(Security, "SecIdentitySetPreference"))

        Security.SecIdentitySetPreferred

        self.assertArgIsOut(
            Security.SecIdentityCopySystemIdentity,
            1,
        )
        self.assertArgIsCFRetained(Security.SecIdentityCopySystemIdentity, 1)
        self.assertArgIsOut(
            Security.SecIdentityCopySystemIdentity,
            2,
        )
        self.assertArgIsCFRetained(Security.SecIdentityCopySystemIdentity, 2)

    @min_os_level("10.12")
    def test_functions12_0(self):
        self.assertResultIsCFRetained(Security.SecIdentityCreate)
