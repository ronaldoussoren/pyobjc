
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontCollection (TestCase):
    def testTypes(self):
        self.assertIsInstance(CTFontCollectionRef, objc.objc_class)

    def testConstants(self):
        self.assertIsInstance(kCTFontCollectionRemoveDuplicatesOption, unicode)

    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(kCTFontCollectionIncludeDisabledFontsOption, unicode)
        self.assertIsInstance(kCTFontCollectionDisallowAutoActivationOption, unicode)

        self.assertEqual(kCTFontCollectionCopyDefaultOptions, 0)
        self.assertEqual(kCTFontCollectionCopyUnique, 1 << 0)
        self.assertEqual(kCTFontCollectionCopyStandardSort, 1 << 1)


    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertResultIsCFRetained(CTFontCollectionCreateMutableCopy)
        self.assertResultIsCFRetained(CTFontCollectionCopyQueryDescriptors)
        CTFontCollectionSetQueryDescriptors
        self.assertResultIsCFRetained(CTFontCollectionCopyExclusionDescriptors)
        CTFontCollectionSetExclusionDescriptors
        self.assertResultIsCFRetained(CTFontCollectionCreateMatchingFontDescriptorsWithOptions)
        self.assertResultIsCFRetained(CTFontCollectionCreateMatchingFontDescriptorsForFamily)
        self.assertResultIsCFRetained(CTFontCollectionCopyFontAttribute)
        self.assertResultIsCFRetained(CTFontCollectionCopyFontAttributes)

    def testFunctions(self):
        self.assertResultIsCFRetained(CTFontCollectionCreateCopyWithFontDescriptors)

        v = CTFontCollectionCreateWithFontDescriptors([
            CTFontDescriptorCreateWithNameAndSize("Optima Bold", 14),
            ], None)
        self.assertIsInstance(v, CTFontCollectionRef)

        col = CTFontCollectionCreateFromAvailableFonts(None)
        self.assertIsInstance(col, CTFontCollectionRef)

        self.assertResultIsCFRetained(CTFontCollectionCreateMatchingFontDescriptors)
        v = CTFontCollectionCreateMatchingFontDescriptors(col)
        self.assertIsInstance(v, CFArrayRef)

        def compare(a, b, ctx):
            self.assertIsInstance(a, CTFontDescriptorRef)
            self.assertIsInstance(b, CTFontDescriptorRef)
            self.assertEqual(ctx, "foo")
            return 0
        self.assertResultIsCFRetained(CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback)
        v = CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(
                col, compare, "foo")
        self.assertIsInstance(v, CFArrayRef)

        v = CTFontCollectionGetTypeID()
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
