import CoreText
from PyObjCTools.TestSupport import TestCase
import objc


class TestCTFontCollection(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreText.CTFontCollectionCopyOptions)
        self.assertEqual(CoreText.kCTFontCollectionCopyDefaultOptions, 0)
        self.assertEqual(CoreText.kCTFontCollectionCopyUnique, 1 << 0)
        self.assertEqual(CoreText.kCTFontCollectionCopyStandardSort, 1 << 1)

    def test_constants(self):
        self.assertIsInstance(CoreText.kCTFontCollectionRemoveDuplicatesOption, str)

        self.assertIsInstance(CoreText.kCTFontCollectionIncludeDisabledFontsOption, str)
        self.assertIsInstance(
            CoreText.kCTFontCollectionDisallowAutoActivationOption, str
        )

    def test_types(self):
        self.assertIsInstance(CoreText.CTFontCollectionRef, objc.objc_class)

    def test_functions(self):
        self.assertResultIsCFRetained(
            CoreText.CTFontCollectionCreateCopyWithFontDescriptors
        )

        v = CoreText.CTFontCollectionCreateWithFontDescriptors(
            [CoreText.CTFontDescriptorCreateWithNameAndSize("Optima Bold", 14)], None
        )
        self.assertIsInstance(v, CoreText.CTFontCollectionRef)

        col = CoreText.CTFontCollectionCreateFromAvailableFonts(None)
        self.assertIsInstance(col, CoreText.CTFontCollectionRef)

        self.assertResultIsCFRetained(
            CoreText.CTFontCollectionCreateMatchingFontDescriptors
        )
        v = CoreText.CTFontCollectionCreateMatchingFontDescriptors(col)
        self.assertIsInstance(v, CoreText.CFArrayRef)

        def compare(a, b, ctx):
            self.assertIsInstance(a, CoreText.CTFontDescriptorRef)
            self.assertIsInstance(b, CoreText.CTFontDescriptorRef)
            self.assertEqual(ctx, "foo")
            return 0

        self.assertResultIsCFRetained(
            CoreText.CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback
        )
        v = CoreText.CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(
            col, compare, "foo"
        )
        self.assertIsInstance(v, CoreText.CFArrayRef)

        v = CoreText.CTFontCollectionGetTypeID()
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(CoreText.CTFontCollectionCreateMutableCopy)
        self.assertResultIsCFRetained(CoreText.CTFontCollectionCopyQueryDescriptors)
        CoreText.CTFontCollectionSetQueryDescriptors
        self.assertResultIsCFRetained(CoreText.CTFontCollectionCopyExclusionDescriptors)
        CoreText.CTFontCollectionSetExclusionDescriptors
        self.assertResultIsCFRetained(
            CoreText.CTFontCollectionCreateMatchingFontDescriptorsWithOptions
        )
        self.assertResultIsCFRetained(
            CoreText.CTFontCollectionCreateMatchingFontDescriptorsForFamily
        )
        self.assertResultIsCFRetained(CoreText.CTFontCollectionCopyFontAttribute)
        self.assertResultIsCFRetained(CoreText.CTFontCollectionCopyFontAttributes)
