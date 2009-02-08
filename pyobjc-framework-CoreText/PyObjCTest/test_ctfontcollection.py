
from PyObjCTools.TestSupport import *
from CoreText import *

class TestCTFontCollection (TestCase):
    def testTypes(self):
        self.failUnlessIsInstance(CTFontCollectionRef, objc.objc_class)

    def testConstants(self):
        self.failUnlessIsInstance(kCTFontCollectionRemoveDuplicatesOption, unicode)

    def testFunctions(self):

        v = CTFontCollectionCreateWithFontDescriptors([
            CTFontDescriptorCreateWithNameAndSize("Optima Bold", 14),
            ], None)
        self.failUnlessIsInstance(v, CTFontCollectionRef)

        col = CTFontCollectionCreateFromAvailableFonts(None)
        self.failUnlessIsInstance(col, CTFontCollectionRef)

        self.failUnlessResultIsCFRetained(CTFontCollectionCreateMatchingFontDescriptors)
        v = CTFontCollectionCreateMatchingFontDescriptors(col)
        self.failUnlessIsInstance(v, CFArrayRef)

        def compare(a, b, ctx):
            self.failUnlessIsInstance(a, CTFontDescriptorRef)
            self.failUnlessIsInstance(b, CTFontDescriptorRef)
            self.failUnlessEqual(ctx, "foo")
            return 0
        self.failUnlessResultIsCFRetained(CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback)
        v = CTFontCollectionCreateMatchingFontDescriptorsSortedWithCallback(
                col, compare, "foo")
        self.failUnlessIsInstance(v, CFArrayRef)

        v = CTFontCollectionGetTypeID()
        self.failUnlessIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
