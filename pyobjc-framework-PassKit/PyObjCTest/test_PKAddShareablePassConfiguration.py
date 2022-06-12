from PyObjCTools.TestSupport import TestCase, min_os_level

import PassKit


class TestPKAddShareablePassConfiguration(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKAddShareablePassConfigurationPrimaryAction)

    def test_constants(self):
        self.assertEqual(PassKit.PKAddShareablePassConfigurationPrimaryActionAdd, 0)
        self.assertEqual(PassKit.PKAddShareablePassConfigurationPrimaryActionShare, 1)

    @min_os_level("12.0")
    def test_methods(self):
        self.assertArgIsBOOL(
            PassKit.PKShareablePassMetadata.initWithProvisioningCredentialIdentifier_sharingInstanceIdentifier_passThumbnailImage_ownerDisplayName_localizedDescription_accountHash_templateIdentifier_relyingPartyIdentifier_requiresUnifiedAccessCapableDevice_,  # noqa: B950
            8,
        )
        self.assertResultIsBOOL(
            PassKit.PKShareablePassMetadata.requiresUnifiedAccessCapableDevice
        )

        self.assertArgIsBlock(
            PassKit.PKAddShareablePassConfiguration.configurationForPassMetadata_provisioningPolicyIdentifier_primaryAction_completion_,  # noqa: B950
            3,
            b"v@@",
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            PassKit.PKAddShareablePassConfiguration.configurationForPassMetadata_primaryAction_completion_,
            2,
            b"v@@",
        )
