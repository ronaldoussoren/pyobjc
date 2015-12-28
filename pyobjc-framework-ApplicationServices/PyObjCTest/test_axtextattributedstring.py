import HIServices
from PyObjCTools.TestSupport import *

class TestAXTextAttributedString (TestCase):
    def testConstants(self):
        self.assertIsInstance(HIServices.kAXFontTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXForegroundColorTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXBackgroundColorTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXUnderlineColorTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXStrikethroughColorTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXUnderlineTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXSuperscriptTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXStrikethroughTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXShadowTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXAttachmentTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXLinkTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXNaturalLanguageTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXReplacementStringTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXMisspelledTextAttribute, unicode)
        self.assertIsInstance(HIServices.kAXFontNameKey, unicode)
        self.assertIsInstance(HIServices.kAXFontFamilyKey, unicode)
        self.assertIsInstance(HIServices.kAXVisibleNameKey, unicode)
        self.assertIsInstance(HIServices.kAXFontSizeKey, unicode)
        self.assertIsInstance(HIServices.kAXForegoundColorTextAttribute, unicode)

        self.assertEqual(HIServices.kAXUnderlineStyleNone, 0x0)
        self.assertEqual(HIServices.kAXUnderlineStyleSingle, 0x1)
        self.assertEqual(HIServices.kAXUnderlineStyleThick, 0x2)
        self.assertEqual(HIServices.kAXUnderlineStyleDouble, 0x9)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(HIServices.kAXAutocorrectedTextAttribute, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(HIServices.kAXMarkedMisspelledTextAttribute, unicode)



if __name__ == "__main__":
    main()
