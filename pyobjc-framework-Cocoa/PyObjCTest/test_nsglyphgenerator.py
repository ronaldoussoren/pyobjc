
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSGlyphGenerator (TestCase):
    def testConstants(self):
        self.failUnlesEqual(NSShowControlGlyphs, (1 << 0))
        self.failUnlesEqual(NSShowInvisibleGlyphs, (1 << 1))
        self.failUnlesEqual(NSWantsBidiLevels, (1 << 2))

    def testMethods(self):
        self.fail("- (void)insertGlyphs:(const NSGlyph *)glyphs length:(NSUInteger)length forStartingGlyphAtIndex:(NSUInteger)glyphIndex characterIndex:(NSUInteger)charIndex;")
        self.fail("- (void)generateGlyphsForGlyphStorage:(id <NSGlyphStorage>)glyphStorage desiredNumberOfCharacters:(NSUInteger)nChars glyphIndex:(NSUInteger *)glyphIndex characterIndex:(NSUInteger *)charIndex;")


if __name__ == "__main__":
    main()
