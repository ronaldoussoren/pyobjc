from PyObjCTools.TestSupport import TestCase

import SafariServices


class TestSFError(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SafariServices.SFErrorCode)
        self.assertEqual(SafariServices.SFErrorNoExtensionFound, 1)
        self.assertEqual(SafariServices.SFErrorNoAttachmentFound, 2)
        self.assertEqual(SafariServices.SFErrorLoadingInterrupted, 3)
