import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFontDescriptor(TestCase):
    def testConvenience(self):
        v = AppKit.NSFontDescriptor.fontDescriptorWithName_size_("Courier", 12)
        d = v[AppKit.NSFontNameAttribute]
        self.assertEqual(v.get(AppKit.NSFontNameAttribute), d)
        self.assertEqual(v.get("no-such-name"), None)
        with self.assertRaises(KeyError):
            v["no-such-name"]

    def testConstants(self):
        self.assertEqual(AppKit.NSFontUnknownClass, (0 << 28))
        self.assertEqual(AppKit.NSFontOldStyleSerifsClass, (1 << 28))
        self.assertEqual(AppKit.NSFontTransitionalSerifsClass, (2 << 28))
        self.assertEqual(AppKit.NSFontModernSerifsClass, (3 << 28))
        self.assertEqual(AppKit.NSFontClarendonSerifsClass, (4 << 28))
        self.assertEqual(AppKit.NSFontSlabSerifsClass, (5 << 28))
        self.assertEqual(AppKit.NSFontFreeformSerifsClass, (7 << 28))
        self.assertEqual(AppKit.NSFontSansSerifClass, (8 << 28))
        self.assertEqual(AppKit.NSFontOrnamentalsClass, (9 << 28))
        self.assertEqual(AppKit.NSFontScriptsClass, (10 << 28))
        self.assertEqual(AppKit.NSFontSymbolicClass, (12 << 28))

        self.assertEqual(AppKit.NSFontFamilyClassMask, (0xF0000000))

        self.assertEqual(AppKit.NSFontItalicTrait, (1 << 0))
        self.assertEqual(AppKit.NSFontBoldTrait, (1 << 1))
        self.assertEqual(AppKit.NSFontExpandedTrait, (1 << 5))
        self.assertEqual(AppKit.NSFontCondensedTrait, (1 << 6))
        self.assertEqual(AppKit.NSFontMonoSpaceTrait, (1 << 10))
        self.assertEqual(AppKit.NSFontVerticalTrait, (1 << 11))
        self.assertEqual(AppKit.NSFontUIOptimizedTrait, (1 << 12))

        self.assertIsInstance(AppKit.NSFontFamilyAttribute, str)
        self.assertIsInstance(AppKit.NSFontNameAttribute, str)
        self.assertIsInstance(AppKit.NSFontFaceAttribute, str)
        self.assertIsInstance(AppKit.NSFontSizeAttribute, str)
        self.assertIsInstance(AppKit.NSFontVisibleNameAttribute, str)
        self.assertIsInstance(AppKit.NSFontMatrixAttribute, str)
        self.assertIsInstance(AppKit.NSFontVariationAttribute, str)
        self.assertIsInstance(AppKit.NSFontCharacterSetAttribute, str)
        self.assertIsInstance(AppKit.NSFontCascadeListAttribute, str)
        self.assertIsInstance(AppKit.NSFontTraitsAttribute, str)
        self.assertIsInstance(AppKit.NSFontFixedAdvanceAttribute, str)
        self.assertIsInstance(AppKit.NSFontFeatureSettingsAttribute, str)
        self.assertIsInstance(AppKit.NSFontColorAttribute, str)
        self.assertIsInstance(AppKit.NSFontSymbolicTrait, str)
        self.assertIsInstance(AppKit.NSFontWeightTrait, str)
        self.assertIsInstance(AppKit.NSFontWidthTrait, str)
        self.assertIsInstance(AppKit.NSFontSlantTrait, str)
        self.assertIsInstance(AppKit.NSFontVariationAxisIdentifierKey, str)
        self.assertIsInstance(AppKit.NSFontVariationAxisMinimumValueKey, str)
        self.assertIsInstance(AppKit.NSFontVariationAxisMaximumValueKey, str)
        self.assertIsInstance(AppKit.NSFontVariationAxisDefaultValueKey, str)
        self.assertIsInstance(AppKit.NSFontVariationAxisNameKey, str)
        self.assertIsInstance(AppKit.NSFontFeatureTypeIdentifierKey, str)
        self.assertIsInstance(AppKit.NSFontFeatureSelectorIdentifierKey, str)

        self.assertEqual(AppKit.NSFontDescriptorTraitItalic, 1 << 0)
        self.assertEqual(AppKit.NSFontDescriptorTraitBold, 1 << 1)
        self.assertEqual(AppKit.NSFontDescriptorTraitExpanded, 1 << 5)
        self.assertEqual(AppKit.NSFontDescriptorTraitCondensed, 1 << 6)
        self.assertEqual(AppKit.NSFontDescriptorTraitMonoSpace, 1 << 10)
        self.assertEqual(AppKit.NSFontDescriptorTraitVertical, 1 << 11)
        self.assertEqual(AppKit.NSFontDescriptorTraitUIOptimized, 1 << 12)
        self.assertEqual(AppKit.NSFontDescriptorTraitTightLeading, 1 << 15)
        self.assertEqual(AppKit.NSFontDescriptorTraitLooseLeading, 1 << 16)
        self.assertEqual(AppKit.NSFontDescriptorClassMask, 0xF0000000)

        self.assertEqual(AppKit.NSFontDescriptorClassUnknown, 0 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassOldStyleSerifs, 1 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassTransitionalSerifs, 2 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassModernSerifs, 3 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassClarendonSerifs, 4 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassSlabSerifs, 5 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassFreeformSerifs, 7 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassSansSerif, 8 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassOrnamentals, 9 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassScripts, 10 << 28)
        self.assertEqual(AppKit.NSFontDescriptorClassSymbolic, 12 << 28)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AppKit.NSFontWeightUltraLight, float)
        self.assertIsInstance(AppKit.NSFontWeightThin, float)
        self.assertIsInstance(AppKit.NSFontWeightLight, float)
        self.assertIsInstance(AppKit.NSFontWeightRegular, float)
        self.assertIsInstance(AppKit.NSFontWeightMedium, float)
        self.assertIsInstance(AppKit.NSFontWeightSemibold, float)
        self.assertIsInstance(AppKit.NSFontWeightBold, float)
        self.assertIsInstance(AppKit.NSFontWeightHeavy, float)
        self.assertIsInstance(AppKit.NSFontWeightBlack, float)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(AppKit.NSFontDescriptorSystemDesignDefault, str)
        self.assertIsInstance(AppKit.NSFontDescriptorSystemDesignSerif, str)
        self.assertIsInstance(AppKit.NSFontDescriptorSystemDesignMonospaced, str)
        self.assertIsInstance(AppKit.NSFontDescriptorSystemDesignRounded, str)

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertIsInstance(AppKit.NSFontTextStyleLargeTitle, str)
        self.assertIsInstance(AppKit.NSFontTextStyleTitle1, str)
        self.assertIsInstance(AppKit.NSFontTextStyleTitle2, str)
        self.assertIsInstance(AppKit.NSFontTextStyleTitle3, str)
        self.assertIsInstance(AppKit.NSFontTextStyleHeadline, str)
        self.assertIsInstance(AppKit.NSFontTextStyleSubheadline, str)
        self.assertIsInstance(AppKit.NSFontTextStyleBody, str)
        self.assertIsInstance(AppKit.NSFontTextStyleCallout, str)
        self.assertIsInstance(AppKit.NSFontTextStyleFootnote, str)
        self.assertIsInstance(AppKit.NSFontTextStyleCaption1, str)
        self.assertIsInstance(AppKit.NSFontTextStyleCaption2, str)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(AppKit.NSFontDescriptor.requiresFontAssetRequest)
