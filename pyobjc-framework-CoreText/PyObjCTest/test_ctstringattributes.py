import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCTStringAttributes(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreText.kCTFontAttributeName, str)
        self.assertIsInstance(CoreText.kCTKernAttributeName, str)
        self.assertIsInstance(CoreText.kCTLigatureAttributeName, str)
        self.assertIsInstance(CoreText.kCTForegroundColorAttributeName, str)
        self.assertIsInstance(CoreText.kCTParagraphStyleAttributeName, str)
        self.assertIsInstance(CoreText.kCTUnderlineStyleAttributeName, str)
        self.assertIsInstance(CoreText.kCTVerticalFormsAttributeName, str)
        self.assertIsInstance(CoreText.kCTGlyphInfoAttributeName, str)
        self.assertEqual(CoreText.kCTUnderlineStyleNone, 0x00)
        self.assertEqual(CoreText.kCTUnderlineStyleSingle, 0x01)
        self.assertEqual(CoreText.kCTUnderlineStyleThick, 0x02)
        self.assertEqual(CoreText.kCTUnderlineStyleDouble, 0x09)
        self.assertEqual(CoreText.kCTUnderlinePatternSolid, 0x0000)
        self.assertEqual(CoreText.kCTUnderlinePatternDot, 0x0100)
        self.assertEqual(CoreText.kCTUnderlinePatternDash, 0x0200)
        self.assertEqual(CoreText.kCTUnderlinePatternDashDot, 0x0300)
        self.assertEqual(CoreText.kCTUnderlinePatternDashDotDot, 0x0400)
        self.assertEqual(CoreText.kCTWritingDirectionEmbedding, 0)
        self.assertEqual(CoreText.kCTWritingDirectionOverride, 2)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(CoreText.kCTForegroundColorFromContextAttributeName, str)
        self.assertIsInstance(CoreText.kCTSuperscriptAttributeName, str)
        self.assertIsInstance(CoreText.kCTCharacterShapeAttributeName, str)
        self.assertIsInstance(CoreText.kCTRunDelegateAttributeName, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(CoreText.kCTUnderlineColorAttributeName, str)
        self.assertIsInstance(CoreText.kCTStrokeWidthAttributeName, str)
        self.assertIsInstance(CoreText.kCTStrokeColorAttributeName, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(CoreText.kCTBaselineClassAttributeName, str)
        self.assertIsInstance(CoreText.kCTBaselineInfoAttributeName, str)
        self.assertIsInstance(CoreText.kCTBaselineReferenceInfoAttributeName, str)
        self.assertIsInstance(CoreText.kCTWritingDirectionAttributeName, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(CoreText.kCTLanguageAttributeName, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CoreText.kCTRubyAnnotationAttributeName, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CoreText.kCTBackgroundColorAttributeName, str)
        self.assertIsInstance(CoreText.kCTHorizontalInVerticalFormsAttributeName, str)
        self.assertIsInstance(CoreText.kCTTrackingAttributeName, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreText.kCTBaselineOffsetAttributeName, str)
