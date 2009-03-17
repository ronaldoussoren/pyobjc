
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFontDescriptor (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSFontUnknownClass, cast_int(0 << 28))
        self.failUnlessEqual(NSFontOldStyleSerifsClass, cast_int(1 << 28))
        self.failUnlessEqual(NSFontModernSerifsClass, cast_int(3 << 28))
        self.failUnlessEqual(NSFontSlabSerifsClass, cast_int(5 << 28))
        self.failUnlessEqual(NSFontSansSerifClass, cast_int(8 << 28))
        self.failUnlessEqual(NSFontScriptsClass, cast_int(10 << 28))
        self.failUnlessEqual(NSFontSymbolicClass, cast_int(12 << 28))

        self.failUnlessEqual(NSFontFamilyClassMask, cast_int(0xF0000000))

        self.failUnlessEqual(NSFontItalicTrait, (1 << 0))
        self.failUnlessEqual(NSFontBoldTrait, (1 << 1))
        self.failUnlessEqual(NSFontExpandedTrait, (1 << 5))
        self.failUnlessEqual(NSFontCondensedTrait, (1 << 6))
        self.failUnlessEqual(NSFontMonoSpaceTrait, (1 << 10))
        self.failUnlessEqual(NSFontVerticalTrait, (1 << 11))
        self.failUnlessEqual(NSFontUIOptimizedTrait, (1 << 12))


        self.failUnlessIsInstance(NSFontFamilyAttribute, unicode)
        self.failUnlessIsInstance(NSFontNameAttribute, unicode)
        self.failUnlessIsInstance(NSFontFaceAttribute, unicode)
        self.failUnlessIsInstance(NSFontSizeAttribute, unicode)
        self.failUnlessIsInstance(NSFontVisibleNameAttribute, unicode)
        self.failUnlessIsInstance(NSFontMatrixAttribute, unicode)
        self.failUnlessIsInstance(NSFontVariationAttribute, unicode)
        self.failUnlessIsInstance(NSFontCharacterSetAttribute, unicode)
        self.failUnlessIsInstance(NSFontCascadeListAttribute, unicode)
        self.failUnlessIsInstance(NSFontTraitsAttribute, unicode)
        self.failUnlessIsInstance(NSFontFixedAdvanceAttribute, unicode)
        self.failUnlessIsInstance(NSFontFeatureSettingsAttribute, unicode)
        self.failUnlessIsInstance(NSFontColorAttribute, unicode)
        self.failUnlessIsInstance(NSFontSymbolicTrait, unicode)
        self.failUnlessIsInstance(NSFontWeightTrait, unicode)
        self.failUnlessIsInstance(NSFontWidthTrait, unicode)
        self.failUnlessIsInstance(NSFontSlantTrait, unicode)
        self.failUnlessIsInstance(NSFontVariationAxisIdentifierKey, unicode)
        self.failUnlessIsInstance(NSFontVariationAxisMinimumValueKey, unicode)
        self.failUnlessIsInstance(NSFontVariationAxisMaximumValueKey, unicode)
        self.failUnlessIsInstance(NSFontVariationAxisDefaultValueKey, unicode)
        self.failUnlessIsInstance(NSFontVariationAxisNameKey, unicode)
        self.failUnlessIsInstance(NSFontFeatureTypeIdentifierKey, unicode)
        self.failUnlessIsInstance(NSFontFeatureSelectorIdentifierKey, unicode)


if __name__ == "__main__":
    main()
