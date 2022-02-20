from PyObjCTools.TestSupport import TestCase, min_os_level

import SafariServices


class TestSFError(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SafariServices.SFErrorCode)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(SafariServices.SFErrorNoExtensionFound, 1)
        self.assertEqual(SafariServices.SFErrorNoAttachmentFound, 2)
        self.assertEqual(SafariServices.SFErrorLoadingInterrupted, 3)
