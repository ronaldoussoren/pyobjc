import Security
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)


class TestSecQWACTLSBinding(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Security.SecQWACTLSBindingError)
        self.assertEqual(Security.kSecQWACTLSBindingErrorUnavailable, 1)
        self.assertEqual(Security.kSecQWACTLSBindingErrorMalformed, 2)
        self.assertEqual(Security.kSecQWACTLSBindingErrorProfile, 3)
        self.assertEqual(Security.kSecQWACTLSBindingErrorSignature, 4)
        self.assertEqual(Security.kSecQWACTLSBindingErrorCertificate, 5)
        self.assertEqual(Security.kSecQWACTLSBindingErrorNotBound, 6)
        self.assertEqual(Security.kSecQWACTLSBindingErrorExpired, 7)

    @min_os_level("27.3")
    def test_contants27_3(self):
        self.assertIsInstance(Security.kSecQWACTLSBindingErrorDomain, str)

    @min_os_level("27.3")
    def test_functions(self):
        self.assertResultIsCFRetained(Security.SecTrustCreateAndVerifyQWACTLSBinding)
        self.assertArgIsOut(Security.SecTrustCreateAndVerifyQWACTLSBinding, 2)
        self.assertArgIsCFRetained(Security.SecTrustCreateAndVerifyQWACTLSBinding, 2)
