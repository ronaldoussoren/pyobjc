
from PyObjCTools.TestSupport import *

import Security

class TestSecCertificate (TestCase):
    def test_types(self):
        self.assertIsCFType(Security.SecCertificateRef)

    def test_constants(self):
        self.assertEqual(Security.kSecKeyUsageUnspecified, 0)
        self.assertEqual(Security.kSecKeyUsageDigitalSignature, 1 << 0)
        self.assertEqual(Security.kSecKeyUsageNonRepudiation, 1 << 1)
        self.assertEqual(Security.kSecKeyUsageContentCommitment, 1 << 1)
        self.assertEqual(Security.kSecKeyUsageKeyEncipherment, 1 << 2)
        self.assertEqual(Security.kSecKeyUsageDataEncipherment, 1 << 3)
        self.assertEqual(Security.kSecKeyUsageKeyAgreement, 1 << 4)
        self.assertEqual(Security.kSecKeyUsageKeyCertSign, 1 << 5)
        self.assertEqual(Security.kSecKeyUsageCRLSign, 1 << 6)
        self.assertEqual(Security.kSecKeyUsageEncipherOnly, 1 << 7)
        self.assertEqual(Security.kSecKeyUsageDecipherOnly, 1 << 8)
        self.assertEqual(Security.kSecKeyUsageCritical, 1 << 31)
        self.assertEqual(Security.kSecKeyUsageAll, 0x7FFFFFFF)

        self.assertIsInstance(Security.kSecPropertyKeyType, unicode)
        self.assertIsInstance(Security.kSecPropertyKeyLabel, unicode)
        self.assertIsInstance(Security.kSecPropertyKeyLocalizedLabel, unicode)
        self.assertIsInstance(Security.kSecPropertyKeyValue, unicode)

        self.assertIsInstance(Security.kSecPropertyTypeWarning, unicode)
        self.assertIsInstance(Security.kSecPropertyTypeSuccess, unicode)
        self.assertIsInstance(Security.kSecPropertyTypeSection, unicode)
        self.assertIsInstance(Security.kSecPropertyTypeData, unicode)
        self.assertIsInstance(Security.kSecPropertyTypeString, unicode)
        self.assertIsInstance(Security.kSecPropertyTypeURL, unicode)
        self.assertIsInstance(Security.kSecPropertyTypeDate, unicode)

        self.assertFalse(hasattr(Security, 'kSecSubjectItemAttr'))
        self.assertFalse(hasattr(Security, 'kSecIssuerItemAttr'))
        self.assertFalse(hasattr(Security, 'kSecSerialNumberItemAttr'))
        self.assertFalse(hasattr(Security, 'kSecPublicKeyHashItemAttr'))
        self.assertFalse(hasattr(Security, 'kSecSubjectKeyIdentifierItemAttr'))
        self.assertFalse(hasattr(Security, 'kSecCertTypeItemAttr'))
        self.assertFalse(hasattr(Security, 'kSecCertEncodingItemAttr'))

    def test_functions(self):
        self.assertIsInstance(Security.SecCertificateGetTypeID(), (int, long))

        self.assertResultHasType(Security.SecCertificateCreateWithData, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCreateWithData)
        self.assertArgHasType(Security.SecCertificateCreateWithData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCreateWithData, 1, objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyData, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyData)
        self.assertArgHasType(Security.SecCertificateCopyData, 0, objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopySubjectSummary, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopySubjectSummary)
        self.assertArgHasType(Security.SecCertificateCopySubjectSummary, 0, objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyCommonName, objc._C_INT)
        self.assertArgHasType(Security.SecCertificateCopyCommonName, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyCommonName, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCertificateCopyCommonName, 1)

        self.assertResultHasType(Security.SecCertificateCopyEmailAddresses, objc._C_INT)
        self.assertArgHasType(Security.SecCertificateCopyEmailAddresses, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyEmailAddresses, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCertificateCopyEmailAddresses, 1)

        self.assertResultHasType(Security.SecCertificateCopyPublicKey, objc._C_INT)
        self.assertArgHasType(Security.SecCertificateCopyPublicKey, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyPublicKey, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecCertificateCopyPublicKey, 1)

        self.assertResultHasType(Security.SecCertificateCopySerialNumber, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopySerialNumber, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopySerialNumber, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecCertificateAddToKeychain, objc._C_INT)
        self.assertArgHasType(Security.SecCertificateAddToKeychain, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateAddToKeychain, 1, objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyPreferred, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyPreferred, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyPreferred, 1, objc._C_ID)

        self.assertResultHasType(Security.SecCertificateSetPreferred, objc._C_INT)
        self.assertArgHasType(Security.SecCertificateSetPreferred, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateSetPreferred, 1, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateSetPreferred, 2, objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyValues, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyValues)
        self.assertArgHasType(Security.SecCertificateCopyValues, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyValues, 1, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyValues, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyLongDescription, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyLongDescription)
        self.assertArgHasType(Security.SecCertificateCopyLongDescription, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyLongDescription, 1, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyLongDescription, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyShortDescription, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyShortDescription)
        self.assertArgHasType(Security.SecCertificateCopyShortDescription, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyShortDescription, 1, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyShortDescription, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyNormalizedIssuerContent, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyNormalizedIssuerContent)
        self.assertArgHasType(Security.SecCertificateCopyNormalizedIssuerContent, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyNormalizedIssuerContent, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyNormalizedSubjectContent, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyNormalizedSubjectContent)
        self.assertArgHasType(Security.SecCertificateCopyNormalizedSubjectContent, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopyNormalizedSubjectContent, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertFalse(hasattr(Security, 'SecCertificateCreateFromData'))
        self.assertFalse(hasattr(Security, 'SecCertificateGetData'))
        self.assertFalse(hasattr(Security, 'SecCertificateGetType'))
        self.assertFalse(hasattr(Security, 'SecCertificateGetSubject'))
        self.assertFalse(hasattr(Security, 'SecCertificateGetIssuer'))
        self.assertFalse(hasattr(Security, 'SecCertificateGetCLHandle'))
        self.assertFalse(hasattr(Security, 'SecCertificateGetAlgorithmID'))
        self.assertFalse(hasattr(Security, 'SecCertificateCopyPreference'))
        self.assertFalse(hasattr(Security, 'SecCertificateSetPreference'))

    @min_os_level('10.12.4')
    def test_functions_10_12_4(self):
        self.assertResultHasType(Security.SecCertificateCopyNormalizedIssuerSequence, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyNormalizedIssuerSequence)
        self.assertArgHasType(Security.SecCertificateCopyNormalizedIssuerSequence, 0, objc._C_ID)

        self.assertResultHasType(Security.SecCertificateCopyNormalizedSubjectSequence, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyNormalizedSubjectSequence)
        self.assertArgHasType(Security.SecCertificateCopyNormalizedSubjectSequence, 0, objc._C_ID)

    @min_os_level('10.13')
    def test_functions_10_13(self):
        self.assertResultHasType(Security.SecCertificateCopySerialNumberData, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopySerialNumberData)
        self.assertArgHasType(Security.SecCertificateCopySerialNumberData, 0, objc._C_ID)
        self.assertArgHasType(Security.SecCertificateCopySerialNumberData, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)

    @min_os_level('10.14')
    def test_functions_10_14(self):
        self.assertResultHasType(Security.SecCertificateCopyKey, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecCertificateCopyKey)
        self.assertArgHasType(Security.SecCertificateCopyKey, 0, objc._C_ID)

if __name__ == "__main__":
    main()
