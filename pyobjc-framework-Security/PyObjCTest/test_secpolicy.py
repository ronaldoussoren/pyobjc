import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestSecPolicy(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecRevocationOCSPMethod, 1 << 0)
        self.assertEqual(Security.kSecRevocationCRLMethod, 1 << 1)
        self.assertEqual(Security.kSecRevocationPreferCRL, 1 << 2)
        self.assertEqual(Security.kSecRevocationRequirePositiveResponse, 1 << 3)
        self.assertEqual(Security.kSecRevocationNetworkAccessDisabled, 1 << 4)
        self.assertEqual(
            Security.kSecRevocationUseAnyAvailableMethod,
            Security.kSecRevocationOCSPMethod | Security.kSecRevocationCRLMethod,
        )

    @min_os_level("10.7")
    def test_constants10_7(self):
        self.assertIsInstance(Security.kSecPolicyAppleX509Basic, str)
        self.assertIsInstance(Security.kSecPolicyAppleSSL, str)
        self.assertIsInstance(Security.kSecPolicyAppleSMIME, str)
        self.assertIsInstance(Security.kSecPolicyAppleEAP, str)
        self.assertIsInstance(Security.kSecPolicyAppleIPsec, str)
        # self.assertIsInstance(Security.kSecPolicyAppleiChat, str)
        self.assertIsInstance(Security.kSecPolicyApplePKINITClient, str)
        self.assertIsInstance(Security.kSecPolicyApplePKINITServer, str)
        self.assertIsInstance(Security.kSecPolicyAppleCodeSigning, str)
        self.assertIsInstance(Security.kSecPolicyMacAppStoreReceipt, str)
        self.assertIsInstance(Security.kSecPolicyAppleIDValidation, str)

        self.assertIsInstance(Security.kSecPolicyOid, str)
        self.assertIsInstance(Security.kSecPolicyName, str)
        self.assertIsInstance(Security.kSecPolicyClient, str)

        self.assertIsInstance(Security.kSecPolicyKU_DigitalSignature, str)
        self.assertIsInstance(Security.kSecPolicyKU_NonRepudiation, str)
        self.assertIsInstance(Security.kSecPolicyKU_KeyEncipherment, str)
        self.assertIsInstance(Security.kSecPolicyKU_DataEncipherment, str)
        self.assertIsInstance(Security.kSecPolicyKU_KeyAgreement, str)
        self.assertIsInstance(Security.kSecPolicyKU_KeyCertSign, str)
        self.assertIsInstance(Security.kSecPolicyKU_CRLSign, str)
        self.assertIsInstance(Security.kSecPolicyKU_EncipherOnly, str)
        self.assertIsInstance(Security.kSecPolicyKU_DecipherOnly, str)

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(Security.kSecPolicyAppleTimeStamping, str)

        self.assertIsInstance(Security.kSecPolicyRevocationFlags, str)
        self.assertIsInstance(Security.kSecPolicyTeamIdentifier, str)

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(Security.kSecPolicyAppleRevocation, str)
        self.assertIsInstance(Security.kSecPolicyApplePassbookSigning, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(Security.kSecPolicyApplePayIssuerEncryption, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecPolicyGetTypeID(), int)

        self.assertResultHasType(Security.SecPolicyCopyProperties, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCopyProperties)
        self.assertArgHasType(Security.SecPolicyCopyProperties, 0, objc._C_ID)

    @min_os_level("10.6")
    def test_functions10_6(self):
        self.assertResultHasType(Security.SecPolicyCreateBasicX509, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCopyProperties)

        self.assertResultHasType(Security.SecPolicyCreateSSL, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCreateSSL)
        self.assertArgHasType(Security.SecPolicyCreateSSL, 0, objc._C_NSBOOL)
        self.assertArgHasType(Security.SecPolicyCreateSSL, 1, objc._C_ID)

    @min_os_level("10.7")
    def test_functions10_7(self):
        self.assertFalse(hasattr(Security, "SecPolicyCreateWithOID"))
        self.assertFalse(hasattr(Security, "SecPolicyGetOID"))
        self.assertFalse(hasattr(Security, "SecPolicyGetValue"))
        self.assertFalse(hasattr(Security, "SecPolicySetValue"))
        self.assertFalse(hasattr(Security, "SecPolicySetProperties"))
        self.assertFalse(hasattr(Security, "SecPolicyGetTPHandle"))

    @min_os_level("10.9")
    def test_functions10_9(self):
        self.assertResultHasType(Security.SecPolicyCreateRevocation, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCreateRevocation)
        self.assertArgHasType(Security.SecPolicyCreateRevocation, 0, objc._C_NSUInteger)

        self.assertResultHasType(Security.SecPolicyCreateWithProperties, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCreateWithProperties)
        self.assertArgHasType(Security.SecPolicyCreateWithProperties, 0, objc._C_ID)
        self.assertArgHasType(Security.SecPolicyCreateWithProperties, 1, objc._C_ID)
