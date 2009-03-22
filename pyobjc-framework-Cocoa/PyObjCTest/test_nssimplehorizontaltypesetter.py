from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSimpleHorizontalTypesetterHelper (NSSimpleHorizontalTypesetter):
    def willSetLineFragmentRect_forGlyphRange_usedRect_(self, a, b, c): return 1

class TestNSSimpleHorizontalTypesetter (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSLayoutNotDone, 0)
        self.failUnlessEqual(NSLayoutDone, 1)
        self.failUnlessEqual(NSLayoutCantFit, 2)
        self.failUnlessEqual(NSLayoutOutOfGlyphs, 3)

        self.failUnlessEqual(NSGlyphLayoutAtAPoint, 0)
        self.failUnlessEqual(NSGlyphLayoutAgainstAPoint, 1)
        self.failUnlessEqual(NSGlyphLayoutWithPrevious, 2)

        self.failUnlessEqual(NSLayoutLeftToRight, 0)
        self.failUnlessEqual(NSLayoutRightToLeft, 1)

        self.failUnlessEqual(NSBaselineNotSet, -1.0)
        self.failUnlessEqual(NumGlyphsToGetEachTime, 20)

    def testMethods(self):
        self.failUnlessArgIsOut(NSSimpleHorizontalTypesetter.layoutGlyphsInLayoutManager_startingAtGlyphIndex_maxNumberOfLineFragments_nextGlyphIndex_, 3)
        self.failUnlessArgIsInOut(NSSimpleHorizontalTypesetter.layoutGlyphsInHorizontalLineFragment_baseline_, 1)
        self.failUnlessArgIsInOut(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 2)
        self.failUnlessArgHasType(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 2, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 1, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSSimpleHorizontalTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_, 0, 'N^'+NSRect.__typestr__)

if __name__ == "__main__":
    main()
