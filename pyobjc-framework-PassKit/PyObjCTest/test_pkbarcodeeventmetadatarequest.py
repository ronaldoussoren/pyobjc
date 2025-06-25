from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKBarcodeEventMetadataRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PassKit.PKBarcodeEventConfigurationDataType)

    def test_constants(self):
        self.assertEqual(PassKit.PKBarcodeEventConfigurationDataTypeUnknown, 0)
        self.assertEqual(PassKit.PKBarcodeEventConfigurationDataTypeSigningKeyMaterial, 1)
        self.assertEqual(PassKit.PKBarcodeEventConfigurationDataTypeSigningCertificate, 2)
