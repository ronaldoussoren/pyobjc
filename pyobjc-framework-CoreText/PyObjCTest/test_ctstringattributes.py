
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTStringAttributes (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCTFontAttributeName, unicode)
        self.assertIsInstance(kCTKernAttributeName, unicode)
        self.assertIsInstance(kCTLigatureAttributeName, unicode)
        self.assertIsInstance(kCTForegroundColorAttributeName, unicode)
        self.assertIsInstance(kCTParagraphStyleAttributeName, unicode)
        self.assertIsInstance(kCTUnderlineStyleAttributeName, unicode)
        self.assertIsInstance(kCTVerticalFormsAttributeName, unicode)
        self.assertIsInstance(kCTGlyphInfoAttributeName, unicode)
        self.assertEqual(kCTUnderlineStyleNone,  0x00)
        self.assertEqual(kCTUnderlineStyleSingle,  0x01)
        self.assertEqual(kCTUnderlineStyleThick,  0x02)
        self.assertEqual(kCTUnderlineStyleDouble,  0x09)
        self.assertEqual(kCTUnderlinePatternSolid,  0x0000)
        self.assertEqual(kCTUnderlinePatternDot,  0x0100)
        self.assertEqual(kCTUnderlinePatternDash,  0x0200)
        self.assertEqual(kCTUnderlinePatternDashDot,  0x0300)
        self.assertEqual(kCTUnderlinePatternDashDotDot,  0x0400)
        self.assertEqual(kCTWritingDirectionEmbedding,  0)
        self.assertEqual(kCTWritingDirectionOverride,  2)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCTForegroundColorFromContextAttributeName, unicode)
        self.assertIsInstance(kCTSuperscriptAttributeName, unicode)
        self.assertIsInstance(kCTCharacterShapeAttributeName, unicode)
        self.assertIsInstance(kCTRunDelegateAttributeName, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCTUnderlineColorAttributeName, unicode)
        self.assertIsInstance(kCTStrokeWidthAttributeName, unicode)
        self.assertIsInstance(kCTStrokeColorAttributeName, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(kCTBaselineClassAttributeName, unicode)
        self.assertIsInstance(kCTBaselineInfoAttributeName, unicode)
        self.assertIsInstance(kCTBaselineReferenceInfoAttributeName, unicode)
        self.assertIsInstance(kCTWritingDirectionAttributeName, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(kCTLanguageAttributeName, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(kCTRubyAnnotationAttributeName, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(kCTBackgroundColorAttributeName, unicode)
        self.assertIsInstance(kCTHorizontalInVerticalFormsAttributeName, unicode)

    @min_os_level('10.13')
    def testConstants10_12(self):
        self.assertIsInstance(kCTBaselineOffsetAttributeName, unicode)

if __name__ == "__main__":
    main()
