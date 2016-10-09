from PyObjCTools.TestSupport import *
from CoreText import *
from Quartz import *

class TestCTRubyAnnotation (TestCase):
    def testTypes(self):
        self.assertIsInstance(CTRubyAnnotationRef, objc.objc_class)

    def testConstants(self):
        self.assertEqual(kCTRubyAlignmentInvalid, 255)
        self.assertEqual(kCTRubyAlignmentAuto, 0)
        self.assertEqual(kCTRubyAlignmentStart, 1)
        self.assertEqual(kCTRubyAlignmentCenter, 2)
        self.assertEqual(kCTRubyAlignmentEnd, 3)
        self.assertEqual(kCTRubyAlignmentDistributeLetter, 4)
        self.assertEqual(kCTRubyAlignmentDistributeSpace, 5)
        self.assertEqual(kCTRubyAlignmentLineEdge, 6)

        self.assertEqual(kCTRubyOverhangInvalid, 255)
        self.assertEqual(kCTRubyOverhangAuto, 0)
        self.assertEqual(kCTRubyOverhangStart, 1)
        self.assertEqual(kCTRubyOverhangEnd, 2)
        self.assertEqual(kCTRubyOverhangNone, 3)

        self.assertEqual(kCTRubyPositionBefore, 0)
        self.assertEqual(kCTRubyPositionAfter, 1)
        self.assertEqual(kCTRubyPositionInterCharacter, 2)
        self.assertEqual(kCTRubyPositionInline, 3)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(kCTRubyAnnotationSizeFactorAttributeName, unicode)
        self.assertIsInstance(kCTRubyAnnotationScaleToFitAttributeName, unicode)

    @min_os_level('10.10')
    def testFunctions(self):
        self.assertIsInstance(CTRubyAnnotationGetTypeID(), (int, long))

        self.assertResultIsCFRetained(CTRubyAnnotationCreate)
        self.assertArgIsIn(CTRubyAnnotationCreate, 3)
        self.assertArgIsFixedSize(CTRubyAnnotationCreate, 3, kCTRubyPositionCount)

        self.assertResultIsCFRetained(CTRubyAnnotationCreateCopy)

        CTRubyAnnotationGetAlignment

        CTRubyAnnotationGetOverhang

        CTRubyAnnotationGetSizeFactor

        self.assertResultIsNotCFRetained(CTRubyAnnotationGetTextForPosition)

    @min_os_level('10.12')
    def testFunctions10_12(self):
        self.assertResultIsCFRetained(CTRubyAnnotationCreateWithAttributes)

if __name__ == "__main__":
    main()
