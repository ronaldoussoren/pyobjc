
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGlyphGeneratorHelper (NSObject):
    def insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_(self, glyphs, length, glyphIndex, charIndex):
        self.glyphs = (glyphs, length, glyphIndex, charIndex)

    def setIntAttribute_value_forGlyphAtIndex_(self, a, v, g): pass


class TestNSGlyphGenerator (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSShowControlGlyphs, (1 << 0))
        self.failUnlessEqual(NSShowInvisibleGlyphs, (1 << 1))
        self.failUnlessEqual(NSWantsBidiLevels, (1 << 2))

    def testProtocols(self):
        self.failUnlessArgHasType(TestNSGlyphGeneratorHelper.setIntAttribute_value_forGlyphAtIndex_, 0, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSGlyphGeneratorHelper.setIntAttribute_value_forGlyphAtIndex_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSGlyphGeneratorHelper.setIntAttribute_value_forGlyphAtIndex_, 2, objc._C_NSUInteger)

        o = TestNSGlyphGeneratorHelper.alloc().init()
        o.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_(
                [0, 1, 2, 3, 4], 5, 3, 8)
        self.failUnlessEqual(o.glyphs, ([0, 1, 2, 3, 4], 5, 3, 8))
        self.failUnlessArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            0, 'n^I')
        self.failUnlessArgSizeInArg(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            0, 1)
        self.failUnlessArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            1, objc._C_NSUInteger)
        self.failUnlessArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            2, objc._C_NSUInteger)
        self.failUnlessArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            3, objc._C_NSUInteger)

    def testMethods(self):
        self.failUnlessArgIsOut(
                NSGlyphGenerator.generateGlyphsForGlyphStorage_desiredNumberOfCharacters_glyphIndex_characterIndex_, 2)
        self.failUnlessArgIsOut(
                NSGlyphGenerator.generateGlyphsForGlyphStorage_desiredNumberOfCharacters_glyphIndex_characterIndex_, 3)


if __name__ == "__main__":
    main()
