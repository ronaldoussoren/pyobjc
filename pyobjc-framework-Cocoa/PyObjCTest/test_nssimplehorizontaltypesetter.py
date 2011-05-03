from PyObjCTools.TestSupport import *
from AppKit import *

if is32Bit():
    class TestNSSimpleHorizontalTypesetterHelper (NSSimpleHorizontalTypesetter):
        def willSetLineFragmentRect_forGlyphRange_usedRect_(self, a, b, c): return 1

class TestNSSimpleHorizontalTypesetter (TestCase):
    @onlyOn32Bit
    def testConstants(self):
        self.assertEqual(NSLayoutNotDone, 0)
        self.assertEqual(NSLayoutDone, 1)
        self.assertEqual(NSLayoutCantFit, 2)
        self.assertEqual(NSLayoutOutOfGlyphs, 3)

        self.assertEqual(NSGlyphLayoutAtAPoint, 0)
        self.assertEqual(NSGlyphLayoutAgainstAPoint, 1)
        self.assertEqual(NSGlyphLayoutWithPrevious, 2)

        self.assertEqual(NSLayoutLeftToRight, 0)
        self.assertEqual(NSLayoutRightToLeft, 1)

        self.assertEqual(NSBaselineNotSet, -1.0)
        self.assertEqual(NumGlyphsToGetEachTime, 20)

    @onlyOn32Bit
    def testMethods(self):
        self.assertArgIsOut(NSSimpleHorizontalTypesetter.layoutGlyphsInLayoutManager_startingAtGlyphIndex_maxNumberOfLineFragments_nextGlyphIndex_, 3)
        self.assertArgIsInOut(NSSimpleHorizontalTypesetter.layoutGlyphsInHorizontalLineFragment_baseline_, 1)
        self.assertArgIsInOut(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 2)
        self.assertArgHasType(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 2, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 0, b'N^'+NSRect.__typestr__)

if __name__ == "__main__":
    main()
