
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGlyphGeneratorHelper (NSObject):
    def insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_(self, glyphs, length, glyphIndex, charIndex):
        self.glyphs = (glyphs, length, glyphIndex, charIndex)

    def setIntAttribute_value_forGlyphAtIndex_(self, a, v, g): pass


class TestNSGlyphGenerator (TestCase):
    def testConstants(self):
        self.assertEqual(NSShowControlGlyphs, (1 << 0))
        self.assertEqual(NSShowInvisibleGlyphs, (1 << 1))
        self.assertEqual(NSWantsBidiLevels, (1 << 2))

    def testProtocols(self):
        self.assertArgHasType(TestNSGlyphGeneratorHelper.setIntAttribute_value_forGlyphAtIndex_, 0, objc._C_NSInteger)
        self.assertArgHasType(TestNSGlyphGeneratorHelper.setIntAttribute_value_forGlyphAtIndex_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSGlyphGeneratorHelper.setIntAttribute_value_forGlyphAtIndex_, 2, objc._C_NSUInteger)

        o = TestNSGlyphGeneratorHelper.alloc().init()
        o.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_(
                [0, 1, 2, 3, 4], 5, 3, 8)
        self.assertEqual(o.glyphs, ([0, 1, 2, 3, 4], 5, 3, 8))
        self.assertArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            0, b'n^I')
        self.assertArgSizeInArg(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            0, 1)
        self.assertArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            1, objc._C_NSUInteger)
        self.assertArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            2, objc._C_NSUInteger)
        self.assertArgHasType(
            TestNSGlyphGeneratorHelper.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            3, objc._C_NSUInteger)

    def testMethods(self):
        self.assertArgIsOut(
                NSGlyphGenerator.generateGlyphsForGlyphStorage_desiredNumberOfCharacters_glyphIndex_characterIndex_, 2)
        self.assertArgIsOut(
                NSGlyphGenerator.generateGlyphsForGlyphStorage_desiredNumberOfCharacters_glyphIndex_characterIndex_, 3)


if __name__ == "__main__":
    main()
