import Security
from PyObjCTools.TestSupport import TestCase


class TestSecTrustSettings(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecTrustSettingsPolicy, "kSecTrustSettingsPolicy")
        self.assertEqual(
            Security.kSecTrustSettingsApplication, "kSecTrustSettingsApplication"
        )
        self.assertEqual(
            Security.kSecTrustSettingsPolicyString, "kSecTrustSettingsPolicyString"
        )
        self.assertEqual(
            Security.kSecTrustSettingsKeyUsage, "kSecTrustSettingsKeyUsage"
        )
        self.assertEqual(
            Security.kSecTrustSettingsAllowedError, "kSecTrustSettingsAllowedError"
        )
        self.assertEqual(Security.kSecTrustSettingsResult, "kSecTrustSettingsResult")

        self.assertEqual(Security.kSecTrustSettingsKeyUseSignature, 0x00000001)
        self.assertEqual(Security.kSecTrustSettingsKeyUseEnDecryptData, 0x00000002)
        self.assertEqual(Security.kSecTrustSettingsKeyUseEnDecryptKey, 0x00000004)
        self.assertEqual(Security.kSecTrustSettingsKeyUseSignCert, 0x00000008)
        self.assertEqual(Security.kSecTrustSettingsKeyUseSignRevocation, 0x00000010)
        self.assertEqual(Security.kSecTrustSettingsKeyUseKeyExchange, 0x00000020)
        self.assertEqual(Security.kSecTrustSettingsKeyUseAny, 0xFFFFFFFF)

        self.assertEqual(Security.kSecTrustSettingsResultInvalid, 0)
        self.assertEqual(Security.kSecTrustSettingsResultTrustRoot, 1)
        self.assertEqual(Security.kSecTrustSettingsResultTrustAsRoot, 2)
        self.assertEqual(Security.kSecTrustSettingsResultDeny, 3)
        self.assertEqual(Security.kSecTrustSettingsResultUnspecified, 4)

        self.assertEqual(Security.kSecTrustSettingsDomainUser, 0)
        self.assertEqual(Security.kSecTrustSettingsDomainAdmin, 1)
        self.assertEqual(Security.kSecTrustSettingsDomainSystem, 2)

        self.assertEqual(Security.kSecTrustSettingsDefaultRootCertSetting, -1)

    def test_functions(self):
        self.assertArgIsOut(
            Security.SecTrustSettingsCopyTrustSettings,
            2,
        )
        self.assertArgIsCFRetained(Security.SecTrustSettingsCopyTrustSettings, 2)

        Security.SecTrustSettingsSetTrustSettings

        Security.SecTrustSettingsRemoveTrustSettings

        self.assertArgIsOut(
            Security.SecTrustSettingsCopyCertificates,
            1,
        )
        self.assertArgIsCFRetained(Security.SecTrustSettingsCopyCertificates, 1)

        self.assertArgIsOut(
            Security.SecTrustSettingsCopyModificationDate,
            2,
        )
        self.assertArgIsCFRetained(Security.SecTrustSettingsCopyModificationDate, 2)

        self.assertArgIsOut(
            Security.SecTrustSettingsCreateExternalRepresentation,
            1,
        )
        self.assertArgIsCFRetained(
            Security.SecTrustSettingsCreateExternalRepresentation, 1
        )

        Security.SecTrustSettingsImportExternalRepresentation
