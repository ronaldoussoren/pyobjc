import CoreText
from PyObjCTools.TestSupport import TestCase, cast_uint


class TestCTFontTraits(TestCase):
    def test_enum(self):
        self.assertEqual(CoreText.kCTFontClassMaskShift, 28)

        self.assertIsEnumType(CoreText.CTFontSymbolicTraits)
        self.assertEqual(CoreText.kCTFontTraitItalic, (1 << 0))
        self.assertEqual(CoreText.kCTFontTraitBold, (1 << 1))
        self.assertEqual(CoreText.kCTFontTraitExpanded, (1 << 5))
        self.assertEqual(CoreText.kCTFontTraitCondensed, (1 << 6))
        self.assertEqual(CoreText.kCTFontTraitMonoSpace, (1 << 10))
        self.assertEqual(CoreText.kCTFontTraitVertical, (1 << 11))
        self.assertEqual(CoreText.kCTFontTraitUIOptimized, (1 << 12))
        self.assertEqual(CoreText.kCTFontTraitColorGlyphs, (1 << 13))
        self.assertEqual(CoreText.kCTFontTraitComposite, (1 << 14))
        self.assertEqual(CoreText.kCTFontItalicTrait, cast_uint(1 << 0))
        self.assertEqual(CoreText.kCTFontBoldTrait, cast_uint(1 << 1))
        self.assertEqual(CoreText.kCTFontExpandedTrait, cast_uint(1 << 5))
        self.assertEqual(CoreText.kCTFontCondensedTrait, cast_uint(1 << 6))
        self.assertEqual(CoreText.kCTFontMonoSpaceTrait, cast_uint(1 << 10))
        self.assertEqual(CoreText.kCTFontVerticalTrait, cast_uint(1 << 11))
        self.assertEqual(CoreText.kCTFontUIOptimizedTrait, cast_uint(1 << 12))
        self.assertEqual(
            CoreText.kCTFontClassMaskTrait,
            cast_uint(15 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontTraitClassMask, (15 << CoreText.kCTFontClassMaskShift)
        )

        self.assertEqual(
            CoreText.kCTFontClassUnknown, (0 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassOldStyleSerifs, (1 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassTransitionalSerifs,
            (2 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontClassModernSerifs, (3 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassClarendonSerifs, (4 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassSlabSerifs, (5 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassFreeformSerifs, (7 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassSansSerif, (8 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassOrnamentals, (9 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassScripts, (10 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontClassSymbolic, (12 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(CoreText.kCTFontTraitColorGlyphs, 1 << 13)
        self.assertEqual(CoreText.kCTFontTraitComposite, 1 << 14)

        self.assertEqual(
            CoreText.kCTFontColorGlyphsTrait, CoreText.kCTFontTraitColorGlyphs
        )

        self.assertEqual(CoreText.kCTFontCompositeTrait, CoreText.kCTFontTraitComposite)

        self.assertIsEnumType(CoreText.CTFontStylisticClass)
        self.assertEqual(
            CoreText.kCTFontUnknownClass, cast_uint(0 << CoreText.kCTFontClassMaskShift)
        )

        self.assertEqual(
            CoreText.kCTFontUnknownClass, cast_uint(0 << CoreText.kCTFontClassMaskShift)
        )
        self.assertEqual(
            CoreText.kCTFontOldStyleSerifsClass,
            cast_uint(1 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontTransitionalSerifsClass,
            (2 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontModernSerifsClass,
            cast_uint(3 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontClarendonSerifsClass,
            cast_uint(4 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontSlabSerifsClass,
            cast_uint(5 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontFreeformSerifsClass,
            cast_uint(7 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontSansSerifClass,
            cast_uint(8 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontOrnamentalsClass,
            cast_uint(9 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontScriptsClass,
            cast_uint(10 << CoreText.kCTFontClassMaskShift),
        )
        self.assertEqual(
            CoreText.kCTFontSymbolicClass,
            cast_uint(12 << CoreText.kCTFontClassMaskShift),
        )

    def test_constants(self):
        self.assertIsInstance(CoreText.kCTFontSymbolicTrait, str)
        self.assertIsInstance(CoreText.kCTFontWeightTrait, str)
        self.assertIsInstance(CoreText.kCTFontWidthTrait, str)
        self.assertIsInstance(CoreText.kCTFontSlantTrait, str)
