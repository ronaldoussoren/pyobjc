
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLayoutManager (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSGlyphAttributeSoft, 0)
        self.failUnlessEqual(NSGlyphAttributeElastic, 1)
        self.failUnlessEqual(NSGlyphAttributeBidiLevel, 2)
        self.failUnlessEqual(NSGlyphAttributeInscribe, 5)
        self.failUnlessEqual(NSGlyphInscribeBase, 0)
        self.failUnlessEqual(NSGlyphInscribeBelow, 1)
        self.failUnlessEqual(NSGlyphInscribeAbove, 2)
        self.failUnlessEqual(NSGlyphInscribeOverstrike, 3)
        self.failUnlessEqual(NSGlyphInscribeOverBelow, 4)
        self.failUnlessEqual(NSTypesetterLatestBehavior, -1)
        self.failUnlessEqual(NSTypesetterOriginalBehavior, 0)
        self.failUnlessEqual(NSTypesetterBehavior_10_2_WithCompatibility, 1)
        self.failUnlessEqual(NSTypesetterBehavior_10_2, 2)
        self.failUnlessEqual(NSTypesetterBehavior_10_3, 3)
        self.failUnlessEqual(NSTypesetterBehavior_10_4, 4)

    def testMethods(self):
        self.fail("- (void)invalidateGlyphsForCharacterRange:(NSRange)charRange changeInLength:(NSInteger)delta actualCharacterRange:(NSRangePointer)actualCharRange;")
        self.fail("- (void)invalidateLayoutForCharacterRange:(NSRange)charRange isSoft:(BOOL)flag actualCharacterRange:(NSRangePointer)actualCharRange;")
        self.fail("- (NSUInteger)getGlyphsInRange:(NSRange)glyphRange glyphs:(NSGlyph *)glyphBuffer characterIndexes:(NSUInteger *)charIndexBuffer glyphInscriptions:(NSGlyphInscription *)inscribeBuffer elasticBits:(BOOL *)elasticBuffer;")
        self.fail("- (NSUInteger)getGlyphsInRange:(NSRange)glyphRange glyphs:(NSGlyph *)glyphBuffer characterIndexes:(NSUInteger *)charIndexBuffer glyphInscriptions:(NSGlyphInscription *)inscribeBuffer elasticBits:(BOOL *)elasticBuffer bidiLevels:(unsigned char *)bidiLevelBuffer;")
        self.fail("- (NSUInteger)getGlyphs:(NSGlyph *)glyphArray range:(NSRange)glyphRange;")
        self.fail("- (void)getFirstUnlaidCharacterIndex:(NSUInteger *)charIndex glyphIndex:(NSUInteger *)glyphIndex;")
        self.fail("- (NSTextContainer *)textContainerForGlyphAtIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange;")
        self.fail("- (NSRect)lineFragmentRectForGlyphAtIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange;")
        self.fail("- (NSRect)lineFragmentUsedRectForGlyphAtIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange;")
        self.fail("- (NSRect)lineFragmentRectForGlyphAtIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange withoutAdditionalLayout:(BOOL)flag;")
        self.fail("- (NSRect)lineFragmentUsedRectForGlyphAtIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange withoutAdditionalLayout:(BOOL)flag;")
        self.fail("- (NSTextContainer *)textContainerForGlyphAtIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange withoutAdditionalLayout:(BOOL)flag;")
        self.fail("- (NSRect)layoutRectForTextBlock:(NSTextBlock *)block atIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange;")
        self.fail("- (NSRect)boundsRectForTextBlock:(NSTextBlock *)block atIndex:(NSUInteger)glyphIndex effectiveRange:(NSRangePointer)effectiveGlyphRange;")
        self.fail("- (NSRange)glyphRangeForCharacterRange:(NSRange)charRange actualCharacterRange:(NSRangePointer)actualCharRange;")
        self.fail("- (NSRange)characterRangeForGlyphRange:(NSRange)glyphRange actualGlyphRange:(NSRangePointer)actualGlyphRange;")
        self.fail("- (NSRectArray)rectArrayForCharacterRange:(NSRange)charRange withinSelectedCharacterRange:(NSRange)selCharRange inTextContainer:(NSTextContainer *)container rectCount:(NSUInteger *)rectCount;")
        self.fail("- (NSRectArray)rectArrayForGlyphRange:(NSRange)glyphRange withinSelectedGlyphRange:(NSRange)selGlyphRange inTextContainer:(NSTextContainer *)container rectCount:(NSUInteger *)rectCount;")
        self.fail("- (NSUInteger)glyphIndexForPoint:(NSPoint)point inTextContainer:(NSTextContainer *)container fractionOfDistanceThroughGlyph:(CGFloat *)partialFraction;")
        self.fail("- (NSDictionary *)temporaryAttributesAtCharacterIndex:(NSUInteger)charIndex effectiveRange:(NSRangePointer)effectiveCharRange;")


        self.fail("- (void)showPackedGlyphs:(char *)glyphs length:(NSUInteger)glyphLen glyphRange:(NSRange)glyphRange atPoint:(NSPoint)point font:(NSFont *)font color:(NSColor *)color printingAdjustment:(NSSize)printingAdjustment;")







    @min_os_level("10.5")
    def testMethods10_5(self):
        self.fail("- (void)invalidateGlyphsForCharacterRange:(NSRange)charRange changeInLength:(NSInteger)delta actualCharacterRange:(NSRangePointer)actualCharRange;")
        self.fail("- (NSGlyph)glyphAtIndex:(NSUInteger)glyphIndex isValidIndex:(BOOL *)isValidIndex;")
        self.fail("- (void)setLocations:(NSPointArray)locations startingGlyphIndexes:(NSUInteger *)glyphIndexes count:(NSUInteger)count forGlyphRange:(NSRange)glyphRange;")
        self.fail("- (NSUInteger)getLineFragmentInsertionPointsForCharacterAtIndex:(NSUInteger)charIndex alternatePositions:(BOOL)aFlag inDisplayOrder:(BOOL)dFlag positions:(CGFloat *)positions characterIndexes:(NSUInteger *)charIndexes;")
        self.fail("- (id)temporaryAttribute:(NSString *)attrName atCharacterIndex:(NSUInteger)location effectiveRange:(NSRangePointer)range;")
        self.fail("- (id)temporaryAttribute:(NSString *)attrName atCharacterIndex:(NSUInteger)location longestEffectiveRange:(NSRangePointer)range inRange:(NSRange)rangeLimit;")
        self.fail("- (NSDictionary *)temporaryAttributesAtCharacterIndex:(NSUInteger)location longestEffectiveRange:(NSRangePointer)range inRange:(NSRange)rangeLimit;")

        self.fail("- (NSDictionary *)layoutManager:(NSLayoutManager *)layoutManager shouldUseTemporaryAttributes:(NSDictionary *)attrs forDrawingToScreen:(BOOL)toScreen atCharacterIndex:(NSUInteger)charIndex effectiveRange:(NSRangePointer)effectiveCharRange;")






if __name__ == "__main__":
    main()
