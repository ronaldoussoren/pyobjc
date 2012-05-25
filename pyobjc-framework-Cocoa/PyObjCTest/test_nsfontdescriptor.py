
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSFontDescriptor (TestCase):
    def testConstants(self):
        self.assertEqual(NSFontUnknownClass, (0 << 28))
        self.assertEqual(NSFontOldStyleSerifsClass, (1 << 28))
        self.assertEqual(NSFontModernSerifsClass, (3 << 28))
        self.assertEqual(NSFontSlabSerifsClass, (5 << 28))
        self.assertEqual(NSFontSansSerifClass, (8 << 28))
        self.assertEqual(NSFontScriptsClass, (10 << 28))
        self.assertEqual(NSFontSymbolicClass, (12 << 28))

        self.assertEqual(NSFontFamilyClassMask, (0xF0000000))

        self.assertEqual(NSFontItalicTrait, (1 << 0))
        self.assertEqual(NSFontBoldTrait, (1 << 1))
        self.assertEqual(NSFontExpandedTrait, (1 << 5))
        self.assertEqual(NSFontCondensedTrait, (1 << 6))
        self.assertEqual(NSFontMonoSpaceTrait, (1 << 10))
        self.assertEqual(NSFontVerticalTrait, (1 << 11))
        self.assertEqual(NSFontUIOptimizedTrait, (1 << 12))


        self.assertIsInstance(NSFontFamilyAttribute, unicode)
        self.assertIsInstance(NSFontNameAttribute, unicode)
        self.assertIsInstance(NSFontFaceAttribute, unicode)
        self.assertIsInstance(NSFontSizeAttribute, unicode)
        self.assertIsInstance(NSFontVisibleNameAttribute, unicode)
        self.assertIsInstance(NSFontMatrixAttribute, unicode)
        self.assertIsInstance(NSFontVariationAttribute, unicode)
        self.assertIsInstance(NSFontCharacterSetAttribute, unicode)
        self.assertIsInstance(NSFontCascadeListAttribute, unicode)
        self.assertIsInstance(NSFontTraitsAttribute, unicode)
        self.assertIsInstance(NSFontFixedAdvanceAttribute, unicode)
        self.assertIsInstance(NSFontFeatureSettingsAttribute, unicode)
        self.assertIsInstance(NSFontColorAttribute, unicode)
        self.assertIsInstance(NSFontSymbolicTrait, unicode)
        self.assertIsInstance(NSFontWeightTrait, unicode)
        self.assertIsInstance(NSFontWidthTrait, unicode)
        self.assertIsInstance(NSFontSlantTrait, unicode)
        self.assertIsInstance(NSFontVariationAxisIdentifierKey, unicode)
        self.assertIsInstance(NSFontVariationAxisMinimumValueKey, unicode)
        self.assertIsInstance(NSFontVariationAxisMaximumValueKey, unicode)
        self.assertIsInstance(NSFontVariationAxisDefaultValueKey, unicode)
        self.assertIsInstance(NSFontVariationAxisNameKey, unicode)
        self.assertIsInstance(NSFontFeatureTypeIdentifierKey, unicode)
        self.assertIsInstance(NSFontFeatureSelectorIdentifierKey, unicode)


if __name__ == "__main__":
    main()
