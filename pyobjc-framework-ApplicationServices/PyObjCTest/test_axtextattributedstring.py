import HIServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAXTextAttributedString(TestCase):
    def testConstants(self):
        self.assertIsInstance(HIServices.kAXFontTextAttribute, str)
        self.assertIsInstance(HIServices.kAXForegroundColorTextAttribute, str)
        self.assertIsInstance(HIServices.kAXBackgroundColorTextAttribute, str)
        self.assertIsInstance(HIServices.kAXUnderlineColorTextAttribute, str)
        self.assertIsInstance(HIServices.kAXStrikethroughColorTextAttribute, str)
        self.assertIsInstance(HIServices.kAXUnderlineTextAttribute, str)
        self.assertIsInstance(HIServices.kAXSuperscriptTextAttribute, str)
        self.assertIsInstance(HIServices.kAXStrikethroughTextAttribute, str)
        self.assertIsInstance(HIServices.kAXShadowTextAttribute, str)
        self.assertIsInstance(HIServices.kAXAttachmentTextAttribute, str)
        self.assertIsInstance(HIServices.kAXLinkTextAttribute, str)
        self.assertIsInstance(HIServices.kAXNaturalLanguageTextAttribute, str)
        self.assertIsInstance(HIServices.kAXReplacementStringTextAttribute, str)
        self.assertIsInstance(HIServices.kAXMisspelledTextAttribute, str)
        self.assertIsInstance(HIServices.kAXFontNameKey, str)
        self.assertIsInstance(HIServices.kAXFontFamilyKey, str)
        self.assertIsInstance(HIServices.kAXVisibleNameKey, str)
        self.assertIsInstance(HIServices.kAXFontSizeKey, str)
        self.assertIsInstance(HIServices.kAXForegoundColorTextAttribute, str)

        self.assertEqual(HIServices.kAXUnderlineStyleNone, 0x0)
        self.assertEqual(HIServices.kAXUnderlineStyleSingle, 0x1)
        self.assertEqual(HIServices.kAXUnderlineStyleThick, 0x2)
        self.assertEqual(HIServices.kAXUnderlineStyleDouble, 0x9)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(HIServices.kAXAutocorrectedTextAttribute, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(HIServices.kAXMarkedMisspelledTextAttribute, str)
