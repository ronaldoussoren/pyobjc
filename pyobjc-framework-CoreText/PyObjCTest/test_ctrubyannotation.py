import CoreText
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestCTRubyAnnotation(TestCase):
    def testTypes(self):
        self.assertIsInstance(CoreText.CTRubyAnnotationRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(CoreText.kCTRubyAlignmentInvalid, 255)
        self.assertEqual(CoreText.kCTRubyAlignmentAuto, 0)
        self.assertEqual(CoreText.kCTRubyAlignmentStart, 1)
        self.assertEqual(CoreText.kCTRubyAlignmentCenter, 2)
        self.assertEqual(CoreText.kCTRubyAlignmentEnd, 3)
        self.assertEqual(CoreText.kCTRubyAlignmentDistributeLetter, 4)
        self.assertEqual(CoreText.kCTRubyAlignmentDistributeSpace, 5)
        self.assertEqual(CoreText.kCTRubyAlignmentLineEdge, 6)

        self.assertEqual(CoreText.kCTRubyOverhangInvalid, 255)
        self.assertEqual(CoreText.kCTRubyOverhangAuto, 0)
        self.assertEqual(CoreText.kCTRubyOverhangStart, 1)
        self.assertEqual(CoreText.kCTRubyOverhangEnd, 2)
        self.assertEqual(CoreText.kCTRubyOverhangNone, 3)

        self.assertEqual(CoreText.kCTRubyPositionBefore, 0)
        self.assertEqual(CoreText.kCTRubyPositionAfter, 1)
        self.assertEqual(CoreText.kCTRubyPositionInterCharacter, 2)
        self.assertEqual(CoreText.kCTRubyPositionInline, 3)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CoreText.kCTRubyAnnotationSizeFactorAttributeName, str)
        self.assertIsInstance(CoreText.kCTRubyAnnotationScaleToFitAttributeName, str)

    @min_os_level("10.10")
    def testFunctions(self):
        self.assertIsInstance(CoreText.CTRubyAnnotationGetTypeID(), int)

        self.assertResultIsCFRetained(CoreText.CTRubyAnnotationCreate)
        self.assertArgIsIn(CoreText.CTRubyAnnotationCreate, 3)
        self.assertArgIsFixedSize(
            CoreText.CTRubyAnnotationCreate, 3, CoreText.kCTRubyPositionCount
        )

        self.assertResultIsCFRetained(CoreText.CTRubyAnnotationCreateCopy)

        CoreText.CTRubyAnnotationGetAlignment

        CoreText.CTRubyAnnotationGetOverhang

        CoreText.CTRubyAnnotationGetSizeFactor

        self.assertResultIsNotCFRetained(CoreText.CTRubyAnnotationGetTextForPosition)

    @min_os_level("10.12")
    def testFunctions10_12(self):
        self.assertResultIsCFRetained(CoreText.CTRubyAnnotationCreateWithAttributes)
