
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontTraits (TestCase):

    def testConstants(self):
        self.assertIsInstance(kCTFontSymbolicTrait, unicode)
        self.assertIsInstance(kCTFontWeightTrait, unicode)
        self.assertIsInstance(kCTFontWidthTrait, unicode)
        self.assertIsInstance(kCTFontSlantTrait, unicode)

        self.assertEqual(kCTFontClassMaskShift, 28)

        self.assertEqual(kCTFontItalicTrait, cast_int(1 << 0))
        self.assertEqual(kCTFontBoldTrait, cast_int(1 << 1))
        self.assertEqual(kCTFontExpandedTrait, cast_int(1 << 5))
        self.assertEqual(kCTFontCondensedTrait, cast_int(1 << 6))
        self.assertEqual(kCTFontMonoSpaceTrait, cast_int(1 << 10))
        self.assertEqual(kCTFontVerticalTrait, cast_int(1 << 11))
        self.assertEqual(kCTFontUIOptimizedTrait, cast_int(1 << 12))

        self.assertEqual(kCTFontClassMaskTrait, cast_int(15 << kCTFontClassMaskShift))

        self.assertEqual(kCTFontUnknownClass, cast_int(0 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontOldStyleSerifsClass, cast_int(1 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontTransitionalSerifsClass, (2 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontModernSerifsClass, cast_int(3 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontClarendonSerifsClass, cast_int(4 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontSlabSerifsClass, cast_int(5 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontFreeformSerifsClass, cast_int(7 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontSansSerifClass, cast_int(8 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontOrnamentalsClass, cast_int(9 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontScriptsClass, cast_int(10 << kCTFontClassMaskShift))
        self.assertEqual(kCTFontSymbolicClass, cast_int(12 << kCTFontClassMaskShift))

if __name__ == "__main__":
    main()
