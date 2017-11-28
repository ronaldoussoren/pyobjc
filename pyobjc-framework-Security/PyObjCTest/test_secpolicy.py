from PyObjCTools.TestSupport import *

import Security

class TestSecPolicy (TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecRevocationOCSPMethod, 1 << 0)
        self.assertEqual(Security.kSecRevocationCRLMethod, 1 << 1)
        self.assertEqual(Security.kSecRevocationPreferCRL, 1 << 2)
        self.assertEqual(Security.kSecRevocationRequirePositiveResponse, 1 << 3)
        self.assertEqual(Security.kSecRevocationNetworkAccessDisabled, 1 << 4)
        self.assertEqual(Security.kSecRevocationUseAnyAvailableMethod, Security.kSecRevocationOCSPMethod | Security.kSecRevocationCRLMethod)


    @min_os_level('10.7')
    def test_constants10_7(self):
        self.assertIsInstance(Security.kSecPolicyAppleX509Basic, unicode)
        self.assertIsInstance(Security.kSecPolicyAppleSSL, unicode)
        self.assertIsInstance(Security.kSecPolicyAppleSMIME, unicode)
        self.assertIsInstance(Security.kSecPolicyAppleEAP, unicode)
        self.assertIsInstance(Security.kSecPolicyAppleIPsec, unicode)
        #self.assertIsInstance(Security.kSecPolicyAppleiChat, unicode)
        self.assertIsInstance(Security.kSecPolicyApplePKINITClient, unicode)
        self.assertIsInstance(Security.kSecPolicyApplePKINITServer, unicode)
        self.assertIsInstance(Security.kSecPolicyAppleCodeSigning, unicode)
        self.assertIsInstance(Security.kSecPolicyMacAppStoreReceipt, unicode)
        self.assertIsInstance(Security.kSecPolicyAppleIDValidation, unicode)

        self.assertIsInstance(Security.kSecPolicyOid, unicode)
        self.assertIsInstance(Security.kSecPolicyName, unicode)
        self.assertIsInstance(Security.kSecPolicyClient, unicode)

        self.assertIsInstance(Security.kSecPolicyKU_DigitalSignature, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_NonRepudiation, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_KeyEncipherment, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_DataEncipherment, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_KeyAgreement, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_KeyCertSign, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_CRLSign, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_EncipherOnly, unicode)
        self.assertIsInstance(Security.kSecPolicyKU_DecipherOnly, unicode)


    @min_os_level('10.8')
    def test_constants10_8(self):
        self.assertIsInstance(Security.kSecPolicyAppleTimeStamping, unicode)

        self.assertIsInstance(Security.kSecPolicyRevocationFlags, unicode)
        self.assertIsInstance(Security.kSecPolicyTeamIdentifier, unicode)

    @min_os_level('10.9')
    def test_constants10_9(self):
        self.assertIsInstance(Security.kSecPolicyAppleRevocation, unicode)
        self.assertIsInstance(Security.kSecPolicyApplePassbookSigning, unicode)


    @min_os_level('10.11')
    def test_constants10_11(self):
        self.assertIsInstance(Security.kSecPolicyApplePayIssuerEncryption, unicode)


    def test_functions(self):
        self.assertIsInstance(Security.SecPolicyGetTypeID(), (int, long))

        self.assertResultHasType(Security.SecPolicyCopyProperties, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCopyProperties)
        self.assertArgHasType(Security.SecPolicyCopyProperties, 0, objc._C_ID)

    @min_os_level('10.6')
    def test_functions10_6(self):
        self.assertResultHasType(Security.SecPolicyCreateBasicX509, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCopyProperties)

        self.assertResultHasType(Security.SecPolicyCreateSSL, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCreateSSL)
        self.assertArgHasType(Security.SecPolicyCreateSSL, 0, objc._C_NSBOOL)
        self.assertArgHasType(Security.SecPolicyCreateSSL, 1, objc._C_ID)

    @min_os_level('10.7')
    def test_functions10_7(self):
        self.assertFalse(hasattr(Security, "SecPolicyCreateWithOID"))
        self.assertFalse(hasattr(Security, "SecPolicyGetOID"))
        self.assertFalse(hasattr(Security, "SecPolicyGetValue"))
        self.assertFalse(hasattr(Security, "SecPolicySetValue"))
        self.assertFalse(hasattr(Security, "SecPolicySetProperties"))
        self.assertFalse(hasattr(Security, "SecPolicyGetTPHandle"))

    @min_os_level('10.9')
    def test_functions10_9(self):
        self.assertResultHasType(Security.SecPolicyCreateRevocation, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCreateRevocation)
        self.assertArgHasType(Security.SecPolicyCreateRevocation, 0, objc._C_NSUInteger)

        self.assertResultHasType(Security.SecPolicyCreateWithProperties, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecPolicyCreateWithProperties)
        self.assertArgHasType(Security.SecPolicyCreateWithProperties, 0, objc._C_ID)
        self.assertArgHasType(Security.SecPolicyCreateWithProperties, 1, objc._C_ID)

if __name__ == "__main__":
    main()
