import Security
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSecPolicy(TestCase):
    def test_enums(self):
        # Unnamed enum:
        self.assertEqual(Security.kSecRevocationOCSPMethod, 1 << 0)
        self.assertEqual(Security.kSecRevocationCRLMethod, 1 << 1)
        self.assertEqual(Security.kSecRevocationPreferCRL, 1 << 2)
        self.assertEqual(Security.kSecRevocationRequirePositiveResponse, 1 << 3)
        self.assertEqual(Security.kSecRevocationNetworkAccessDisabled, 1 << 4)
        self.assertEqual(
            Security.kSecRevocationUseAnyAvailableMethod,
            Security.kSecRevocationOCSPMethod | Security.kSecRevocationCRLMethod,
        )

    def test_constants(self):
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

        self.assertIsInstance(Security.kSecPolicyAppleTimeStamping, str)

        self.assertIsInstance(Security.kSecPolicyRevocationFlags, str)
        self.assertIsInstance(Security.kSecPolicyTeamIdentifier, str)

        self.assertIsInstance(Security.kSecPolicyAppleRevocation, str)
        self.assertIsInstance(Security.kSecPolicyApplePassbookSigning, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(Security.kSecPolicyApplePayIssuerEncryption, str)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(Security.kSecPolicyAppleSSLServer, str)
        self.assertIsInstance(Security.kSecPolicyAppleSSLClient, str)
        self.assertIsInstance(Security.kSecPolicyAppleEAPServer, str)
        self.assertIsInstance(Security.kSecPolicyAppleEAPClient, str)
        self.assertIsInstance(Security.kSecPolicyAppleIPSecServer, str)
        self.assertIsInstance(Security.kSecPolicyAppleIPSecClient, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecPolicyGetTypeID(), int)

        self.assertResultIsCFRetained(Security.SecPolicyCopyProperties)

        self.assertResultIsCFRetained(Security.SecPolicyCopyProperties)

        self.assertResultIsCFRetained(Security.SecPolicyCreateSSL)
        self.assertArgIsBOOL(Security.SecPolicyCreateSSL, 0)

        self.assertFalse(hasattr(Security, "SecPolicyCreateWithOID"))
        self.assertFalse(hasattr(Security, "SecPolicyGetOID"))
        self.assertFalse(hasattr(Security, "SecPolicyGetValue"))
        self.assertFalse(hasattr(Security, "SecPolicySetValue"))
        self.assertFalse(hasattr(Security, "SecPolicySetProperties"))
        self.assertFalse(hasattr(Security, "SecPolicyGetTPHandle"))

        self.assertResultIsCFRetained(Security.SecPolicyCreateRevocation)

        self.assertResultIsCFRetained(Security.SecPolicyCreateWithProperties)
