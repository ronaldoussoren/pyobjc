
from PyObjCTools.TestSupport import *
from AppKit import *

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

    def testStruct(self):
        self.fail("NSTypesetterGlyphInfo")

    def testFunctions(self):
        self.fail("NSGlyphInfoAtIndex")

    def testMethods(self):
        self.fail("- (void)layoutGlyphsInLayoutManager:(NSLayoutManager *)layoutManager startingAtGlyphIndex:(NSUInteger)startGlyphIndex maxNumberOfLineFragments:(NSUInteger)maxNumLines nextGlyphIndex:(NSUInteger *)nextGlyph;")
        self.fail("- (NSLayoutStatus)layoutGlyphsInHorizontalLineFragment:(NSRect *)lineFragmentRect baseline:(float *)baseline;")
        self.fail("- (void) willSetLineFragmentRect:(NSRect *)aRect forGlyphRange:(NSRange)aRange usedRect:(NSRect *)bRect;")


if __name__ == "__main__":
    main()
