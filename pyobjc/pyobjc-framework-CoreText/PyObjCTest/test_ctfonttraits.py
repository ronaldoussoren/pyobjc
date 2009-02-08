
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontTraits (TestCase):

    def testConstants(self):
        self.failUnlessIsInstance(kCTFontSymbolicTrait, unicode)
        self.failUnlessIsInstance(kCTFontWeightTrait, unicode)
        self.failUnlessIsInstance(kCTFontWidthTrait, unicode)
        self.failUnlessIsInstance(kCTFontSlantTrait, unicode)

	self.failUnlessEqual(kCTFontClassMaskShift, 28)

        self.failUnlessEqual(kCTFontItalicTrait, cast_int(1 << 0))
        self.failUnlessEqual(kCTFontBoldTrait, cast_int(1 << 1))
        self.failUnlessEqual(kCTFontExpandedTrait, cast_int(1 << 5))
        self.failUnlessEqual(kCTFontCondensedTrait, cast_int(1 << 6))
        self.failUnlessEqual(kCTFontMonoSpaceTrait, cast_int(1 << 10))
        self.failUnlessEqual(kCTFontVerticalTrait, cast_int(1 << 11))
        self.failUnlessEqual(kCTFontUIOptimizedTrait, cast_int(1 << 12))

        self.failUnlessEqual(kCTFontClassMaskTrait, cast_int(15 << kCTFontClassMaskShift))

        self.failUnlessEqual(kCTFontUnknownClass, cast_int(0 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontOldStyleSerifsClass, cast_int(1 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontTransitionalSerifsClass, (2 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontModernSerifsClass, cast_int(3 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontClarendonSerifsClass, cast_int(4 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontSlabSerifsClass, cast_int(5 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontFreeformSerifsClass, cast_int(7 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontSansSerifClass, cast_int(8 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontOrnamentalsClass, cast_int(9 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontScriptsClass, cast_int(10 << kCTFontClassMaskShift))
        self.failUnlessEqual(kCTFontSymbolicClass, cast_int(12 << kCTFontClassMaskShift))

if __name__ == "__main__":
    main()
