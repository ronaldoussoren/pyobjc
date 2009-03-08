
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTypesetter (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTypesetterZeroAdvancementAction, (1 << 0))
        self.failUnlessEqual(NSTypesetterWhitespaceAction, (1 << 1))
        self.failUnlessEqual(NSTypesetterHorizontalTabAction, (1 << 2))
        self.failUnlessEqual(NSTypesetterLineBreakAction, (1 << 3))
        self.failUnlessEqual(NSTypesetterParagraphBreakAction, (1 << 4))
        self.failUnlessEqual(NSTypesetterContainerBreakAction, (1 << 5))

    def testMethods(self):
        self.fail("- (void)getLineFragmentRect:(NSRectPointer)lineFragmentRect usedRect:(NSRectPointer)lineFragmentUsedRect forParagraphSeparatorGlyphRange:(NSRange)paragraphSeparatorGlyphRange atProposedOrigin:(NSPoint)lineOrigin;")
        self.fail("- (void)layoutGlyphsInLayoutManager:(NSLayoutManager *)layoutManager startingAtGlyphIndex:(NSUInteger)startGlyphIndex maxNumberOfLineFragments:(NSUInteger)maxNumLines nextGlyphIndex:(NSUInteger *)nextGlyph;")


        self.fail("- (void)willSetLineFragmentRect:(NSRectPointer)lineRect forGlyphRange:(NSRange)glyphRange usedRect:(NSRectPointer)usedRect baselineOffset:(CGFloat *)baselineOffset;")
        self.fail("- (NSRange)characterRangeForGlyphRange:(NSRange)glyphRange actualGlyphRange:(NSRangePointer)actualGlyphRange;")
        self.fail("- (NSRange)glyphRangeForCharacterRange:(NSRange)charRange actualCharacterRange:(NSRangePointer)actualCharRange;")
        self.fail("- (NSUInteger)getGlyphsInRange:(NSRange)glyphsRange glyphs:(NSGlyph *)glyphBuffer characterIndexes:(NSUInteger *)charIndexBuffer glyphInscriptions:(NSGlyphInscription *)inscribeBuffer elasticBits:(BOOL *)elasticBuffer bidiLevels:(unsigned char *)bidiLevelBuffer;")

        self.fail("- (void)getLineFragmentRect:(NSRectPointer)lineFragmentRect usedRect:(NSRectPointer)lineFragmentUsedRect remainingRect:(NSRectPointer)remainingRect forStartingGlyphAtIndex:(NSUInteger)startingGlyphIndex proposedRect:(NSRect)proposedRect lineSpacing:(CGFloat)lineSpacing paragraphSpacingBefore:(CGFloat)paragraphSpacingBefore paragraphSpacingAfter:(CGFloat)paragraphSpacingAfter;")

        self.fail("- (void)setLocation:(NSPoint)location withAdvancements:(const CGFloat *)advancements forStartOfGlyphRange:(NSRange)glyphRange;")
        self.fail("- (void)setBidiLevels:(const uint8_t *)levels forGlyphRange:(NSRange)glyphRange;")



    @min_os_level("10.5")
    def testMethods10_5(self):
        self.fail("+ (NSSize)printingAdjustmentInLayoutManager:(NSLayoutManager *)layoutMgr forNominallySpacedGlyphRange:(NSRange)nominallySpacedGlyphsRange packedGlyphs:(const unsigned char *)packedGlyphs count:(NSUInteger)packedGlyphsCount;")



if __name__ == "__main__":
    main()
