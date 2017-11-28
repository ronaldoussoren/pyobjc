from PyObjCTools.TestSupport import *

import Security

class TestSecTrustSettings (TestCase):

    def test_constants(self):
        self.assertEqual(Security.kSecTrustSettingsPolicy, u"kSecTrustSettingsPolicy")
        self.assertEqual(Security.kSecTrustSettingsApplication, u"kSecTrustSettingsApplication")
        self.assertEqual(Security.kSecTrustSettingsPolicyString, u"kSecTrustSettingsPolicyString")
        self.assertEqual(Security.kSecTrustSettingsKeyUsage, u"kSecTrustSettingsKeyUsage")
        self.assertEqual(Security.kSecTrustSettingsAllowedError, u"kSecTrustSettingsAllowedError")
        self.assertEqual(Security.kSecTrustSettingsResult, u"kSecTrustSettingsResult")

        self.assertEqual(Security.kSecTrustSettingsKeyUseSignature, 0x00000001)
        self.assertEqual(Security.kSecTrustSettingsKeyUseEnDecryptData, 0x00000002)
        self.assertEqual(Security.kSecTrustSettingsKeyUseEnDecryptKey, 0x00000004)
        self.assertEqual(Security.kSecTrustSettingsKeyUseSignCert, 0x00000008)
        self.assertEqual(Security.kSecTrustSettingsKeyUseSignRevocation, 0x00000010)
        self.assertEqual(Security.kSecTrustSettingsKeyUseKeyExchange, 0x00000020)
        self.assertEqual(Security.kSecTrustSettingsKeyUseAny, 0xffffffff)

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
        self.assertResultHasType(Security.SecTrustSettingsCopyTrustSettings, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSettingsCopyTrustSettings, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSettingsCopyTrustSettings, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecTrustSettingsCopyTrustSettings, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecTrustSettingsCopyTrustSettings, 2)

        self.assertResultHasType(Security.SecTrustSettingsSetTrustSettings, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSettingsSetTrustSettings, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSettingsSetTrustSettings, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecTrustSettingsSetTrustSettings, 2, objc._C_ID)

        self.assertResultHasType(Security.SecTrustSettingsRemoveTrustSettings, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSettingsRemoveTrustSettings, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSettingsRemoveTrustSettings, 1, objc._C_UINT)

        self.assertResultHasType(Security.SecTrustSettingsCopyCertificates, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSettingsCopyCertificates, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecTrustSettingsCopyCertificates, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecTrustSettingsCopyCertificates, 1)

        self.assertResultHasType(Security.SecTrustSettingsCopyModificationDate, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSettingsCopyModificationDate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecTrustSettingsCopyModificationDate, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecTrustSettingsCopyModificationDate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecTrustSettingsCopyModificationDate, 2)

        self.assertResultHasType(Security.SecTrustSettingsCreateExternalRepresentation, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSettingsCreateExternalRepresentation, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecTrustSettingsCreateExternalRepresentation, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecTrustSettingsCreateExternalRepresentation, 1)

        self.assertResultHasType(Security.SecTrustSettingsImportExternalRepresentation, objc._C_INT)
        self.assertArgHasType(Security.SecTrustSettingsImportExternalRepresentation, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecTrustSettingsImportExternalRepresentation, 1, objc._C_ID)

if __name__ == "__main__":
    main()
