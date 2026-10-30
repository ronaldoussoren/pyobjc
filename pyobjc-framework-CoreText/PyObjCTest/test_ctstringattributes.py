import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCTStringAttributes(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreText.CTUnderlineStyle)
        self.assertEqual(CoreText.kCTUnderlineStyleNone, 0x00)
        self.assertEqual(CoreText.kCTUnderlineStyleSingle, 0x01)
        self.assertEqual(CoreText.kCTUnderlineStyleThick, 0x02)
        self.assertEqual(CoreText.kCTUnderlineStyleDouble, 0x09)

        self.assertIsEnumType(CoreText.CTUnderlineStyleModifiers)
        self.assertEqual(CoreText.kCTUnderlinePatternSolid, 0x0000)
        self.assertEqual(CoreText.kCTUnderlinePatternDot, 0x0100)
        self.assertEqual(CoreText.kCTUnderlinePatternDash, 0x0200)
        self.assertEqual(CoreText.kCTUnderlinePatternDashDot, 0x0300)
        self.assertEqual(CoreText.kCTUnderlinePatternDashDotDot, 0x0400)

        # Unnamed enum:
        self.assertEqual(CoreText.kCTWritingDirectionEmbedding, 0)
        self.assertEqual(CoreText.kCTWritingDirectionOverride, 2)

    def test_constants(self):
        self.assertIsInstance(CoreText.kCTFontAttributeName, str)
        self.assertIsInstance(CoreText.kCTKernAttributeName, str)
        self.assertIsInstance(CoreText.kCTLigatureAttributeName, str)
        self.assertIsInstance(CoreText.kCTForegroundColorAttributeName, str)
        self.assertIsInstance(CoreText.kCTParagraphStyleAttributeName, str)
        self.assertIsInstance(CoreText.kCTUnderlineStyleAttributeName, str)
        self.assertIsInstance(CoreText.kCTVerticalFormsAttributeName, str)
        self.assertIsInstance(CoreText.kCTGlyphInfoAttributeName, str)

        self.assertIsInstance(CoreText.kCTForegroundColorFromContextAttributeName, str)
        self.assertIsInstance(CoreText.kCTSuperscriptAttributeName, str)
        self.assertIsInstance(CoreText.kCTCharacterShapeAttributeName, str)
        self.assertIsInstance(CoreText.kCTRunDelegateAttributeName, str)

        self.assertIsInstance(CoreText.kCTUnderlineColorAttributeName, str)
        self.assertIsInstance(CoreText.kCTStrokeWidthAttributeName, str)
        self.assertIsInstance(CoreText.kCTStrokeColorAttributeName, str)

        self.assertIsInstance(CoreText.kCTBaselineClassAttributeName, str)
        self.assertIsInstance(CoreText.kCTBaselineInfoAttributeName, str)
        self.assertIsInstance(CoreText.kCTBaselineReferenceInfoAttributeName, str)
        self.assertIsInstance(CoreText.kCTWritingDirectionAttributeName, str)

        self.assertIsInstance(CoreText.kCTLanguageAttributeName, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(CoreText.kCTRubyAnnotationAttributeName, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(CoreText.kCTBackgroundColorAttributeName, str)
        self.assertIsInstance(CoreText.kCTHorizontalInVerticalFormsAttributeName, str)
        self.assertIsInstance(CoreText.kCTTrackingAttributeName, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(CoreText.kCTBaselineOffsetAttributeName, str)

    @min_os_level("15.0")
    def test_constants15_0(self):
        self.assertIsInstance(CoreText.kCTAdaptiveImageProviderAttributeName, str)
