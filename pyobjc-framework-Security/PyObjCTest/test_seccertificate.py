import Security
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestSecCertificate(TestCase):
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

        self.assertIsInstance(Security.kSecPropertyKeyType, str)
        self.assertIsInstance(Security.kSecPropertyKeyLabel, str)
        self.assertIsInstance(Security.kSecPropertyKeyLocalizedLabel, str)
        self.assertIsInstance(Security.kSecPropertyKeyValue, str)

        self.assertIsInstance(Security.kSecPropertyTypeWarning, str)
        self.assertIsInstance(Security.kSecPropertyTypeSuccess, str)
        self.assertIsInstance(Security.kSecPropertyTypeSection, str)
        self.assertIsInstance(Security.kSecPropertyTypeData, str)
        self.assertIsInstance(Security.kSecPropertyTypeString, str)
        self.assertIsInstance(Security.kSecPropertyTypeURL, str)
        self.assertIsInstance(Security.kSecPropertyTypeDate, str)

        self.assertFalse(hasattr(Security, "kSecSubjectItemAttr"))
        self.assertFalse(hasattr(Security, "kSecIssuerItemAttr"))
        self.assertFalse(hasattr(Security, "kSecSerialNumberItemAttr"))
        self.assertFalse(hasattr(Security, "kSecPublicKeyHashItemAttr"))
        self.assertFalse(hasattr(Security, "kSecSubjectKeyIdentifierItemAttr"))
        self.assertFalse(hasattr(Security, "kSecCertTypeItemAttr"))
        self.assertFalse(hasattr(Security, "kSecCertEncodingItemAttr"))

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Security.kSecPropertyTypeArray, str)
        self.assertIsInstance(Security.kSecPropertyTypeNumber, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecCertificateGetTypeID(), int)

        self.assertResultIsCFRetained(Security.SecCertificateCreateWithData)

        self.assertResultIsCFRetained(Security.SecCertificateCopyData)

        self.assertResultIsCFRetained(Security.SecCertificateCopySubjectSummary)

        self.assertArgIsOut(
            Security.SecCertificateCopyCommonName,
            1,
        )
        self.assertArgIsCFRetained(Security.SecCertificateCopyCommonName, 1)

        self.assertArgIsOut(
            Security.SecCertificateCopyEmailAddresses,
            1,
        )
        self.assertArgIsCFRetained(Security.SecCertificateCopyEmailAddresses, 1)

        # "SEC_SUFFIX_LEGACYMAC" on arm64
        self.assertArgIsOut(
            Security.SecCertificateCopyPublicKey,
            1,
        )
        self.assertArgIsCFRetained(Security.SecCertificateCopyPublicKey, 1)

        # "SEC_SUFFIX_LEGACYMAC" on arm64
        self.assertArgIsOut(
            Security.SecCertificateCopySerialNumber,
            1,
        )

        Security.SecCertificateAddToKeychain

        Security.SecCertificateCopyPreferred

        Security.SecCertificateSetPreferred

        self.assertResultIsCFRetained(Security.SecCertificateCopyValues)
        self.assertArgIsOut(Security.SecCertificateCopyValues, 2)
        self.assertArgIsCFRetained(Security.SecCertificateCopyValues, 2)

        self.assertResultIsCFRetained(Security.SecCertificateCopyLongDescription)
        self.assertArgIsOut(
            Security.SecCertificateCopyLongDescription,
            2,
        )
        self.assertArgIsCFRetained(
            Security.SecCertificateCopyLongDescription,
            2,
        )

        self.assertResultIsCFRetained(Security.SecCertificateCopyShortDescription)
        self.assertArgIsOut(
            Security.SecCertificateCopyShortDescription,
            2,
        )
        self.assertArgIsCFRetained(
            Security.SecCertificateCopyShortDescription,
            2,
        )

        self.assertResultIsCFRetained(
            Security.SecCertificateCopyNormalizedIssuerContent
        )
        self.assertArgIsOut(
            Security.SecCertificateCopyNormalizedIssuerContent,
            1,
        )
        self.assertArgIsCFRetained(
            Security.SecCertificateCopyNormalizedIssuerContent,
            1,
        )

        self.assertResultIsCFRetained(
            Security.SecCertificateCopyNormalizedSubjectContent
        )
        self.assertArgIsOut(
            Security.SecCertificateCopyNormalizedSubjectContent,
            1,
        )
        self.assertArgIsCFRetained(
            Security.SecCertificateCopyNormalizedSubjectContent,
            1,
        )

        self.assertFalse(hasattr(Security, "SecCertificateCreateFromData"))
        self.assertFalse(hasattr(Security, "SecCertificateGetData"))
        self.assertFalse(hasattr(Security, "SecCertificateGetType"))
        self.assertFalse(hasattr(Security, "SecCertificateGetSubject"))
        self.assertFalse(hasattr(Security, "SecCertificateGetIssuer"))
        self.assertFalse(hasattr(Security, "SecCertificateGetCLHandle"))
        self.assertFalse(hasattr(Security, "SecCertificateGetAlgorithmID"))
        self.assertFalse(hasattr(Security, "SecCertificateCopyPreference"))
        self.assertFalse(hasattr(Security, "SecCertificateSetPreference"))

    @min_os_level("10.12.4")
    def test_functions_10_12_4(self):
        self.assertResultIsCFRetained(
            Security.SecCertificateCopyNormalizedIssuerSequence
        )

        self.assertResultIsCFRetained(
            Security.SecCertificateCopyNormalizedSubjectSequence
        )

    @min_os_level("10.13")
    def test_functions_10_13(self):
        self.assertResultIsCFRetained(Security.SecCertificateCopySerialNumberData)
        self.assertArgIsOut(
            Security.SecCertificateCopySerialNumberData,
            1,
        )
        self.assertArgIsCFRetained(
            Security.SecCertificateCopySerialNumberData,
            1,
        )

    @min_os_level("10.14")
    def test_functions_10_14(self):
        self.assertResultIsCFRetained(Security.SecCertificateCopyKey)

    @min_os_level("15.0")
    def test_functions15_0(self):
        self.assertResultIsCFRetained(Security.SecCertificateCopyNotValidBeforeDate)
        self.assertResultIsCFRetained(Security.SecCertificateCopyNotValidAfterDate)
