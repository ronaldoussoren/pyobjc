from PyObjCTools.TestSupport import TestCase, min_os_level

import PassKit


class TestPKAddIdentityDocumentConfiguration(TestCase):
    def test_constants(self):
        self.assertIsEnumType(PassKit.PKAddIdentityDocumentType)
        self.assertEqual(PassKit.PKAddIdentityDocumentTypeIDCard, 0)
        self.assertEqual(PassKit.PKAddIdentityDocumentTypeMDL, 1)
        self.assertEqual(PassKit.PKAddIdentityDocumentTypePhotoID, 2)

    @min_os_level("15.0")
    def test_methods(self):
        self.assertArgIsBlock(
            PassKit.PKAddIdentityDocumentConfiguration.configurationForMetadata_completion_,
            1,
            b"v@@",
        )
