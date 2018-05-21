
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSFontDescriptor (TestCase):
    def testConvenience(self):
        v = NSFontDescriptor.fontDescriptorWithName_size_("Courier", 12)
        d = v[NSFontNameAttribute]
        self.assertEqual(v.get(NSFontNameAttribute), d)
        self.assertEqual(v.get('no-such-name'), None)
        with self.assertRaises(KeyError):
            v['no-such-name']


    def testConstants(self):
        self.assertEqual(NSFontUnknownClass, (0 << 28))
        self.assertEqual(NSFontOldStyleSerifsClass, (1 << 28))
        self.assertEqual(NSFontTransitionalSerifsClass, (2 << 28))
        self.assertEqual(NSFontModernSerifsClass, (3 << 28))
        self.assertEqual(NSFontClarendonSerifsClass, (4 << 28))
        self.assertEqual(NSFontSlabSerifsClass, (5 << 28))
        self.assertEqual(NSFontFreeformSerifsClass, (7 << 28))
        self.assertEqual(NSFontSansSerifClass, (8 << 28))
        self.assertEqual(NSFontOrnamentalsClass, (9 << 28))
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

        self.assertEqual(NSFontDescriptorTraitItalic, 1 << 0)
        self.assertEqual(NSFontDescriptorTraitBold, 1 << 1)
        self.assertEqual(NSFontDescriptorTraitExpanded, 1 << 5)
        self.assertEqual(NSFontDescriptorTraitCondensed, 1 << 6)
        self.assertEqual(NSFontDescriptorTraitMonoSpace, 1 << 10)
        self.assertEqual(NSFontDescriptorTraitVertical, 1 << 11)
        self.assertEqual(NSFontDescriptorTraitUIOptimized, 1 << 12)
        self.assertEqual(NSFontDescriptorTraitTightLeading, 1 << 15)
        self.assertEqual(NSFontDescriptorTraitLooseLeading, 1 << 16)
        self.assertEqual(NSFontDescriptorClassMask, 0xF0000000)

        self.assertEqual(NSFontDescriptorClassUnknown, 0 << 28)
        self.assertEqual(NSFontDescriptorClassOldStyleSerifs, 1 << 28)
        self.assertEqual(NSFontDescriptorClassTransitionalSerifs, 2 << 28)
        self.assertEqual(NSFontDescriptorClassModernSerifs, 3 << 28)
        self.assertEqual(NSFontDescriptorClassClarendonSerifs, 4 << 28)
        self.assertEqual(NSFontDescriptorClassSlabSerifs, 5 << 28)
        self.assertEqual(NSFontDescriptorClassFreeformSerifs, 7 << 28)
        self.assertEqual(NSFontDescriptorClassSansSerif, 8 << 28)
        self.assertEqual(NSFontDescriptorClassOrnamentals, 9 << 28)
        self.assertEqual(NSFontDescriptorClassScripts, 10 << 28)
        self.assertEqual(NSFontDescriptorClassSymbolic, 12 << 28)


    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(NSFontWeightUltraLight, float)
        self.assertIsInstance(NSFontWeightThin, float)
        self.assertIsInstance(NSFontWeightLight, float)
        self.assertIsInstance(NSFontWeightRegular, float)
        self.assertIsInstance(NSFontWeightMedium, float)
        self.assertIsInstance(NSFontWeightSemibold, float)
        self.assertIsInstance(NSFontWeightBold, float)
        self.assertIsInstance(NSFontWeightHeavy, float)
        self.assertIsInstance(NSFontWeightBlack, float)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertResultIsBOOL(NSFontDescriptor.requiresFontAssetRequest)


if __name__ == "__main__":
    main()
