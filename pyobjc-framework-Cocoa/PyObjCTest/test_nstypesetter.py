
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTypesetterHelper (NSTypesetter):
    def willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_(self, a, b, c, d): return 1
    def getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_(self, a, b, c, d, e, f): return 1
    def getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_(self, a, b, c, d, e, f, g, h): return 1

class TestNSTypesetter (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTypesetterZeroAdvancementAction, (1 << 0))
        self.failUnlessEqual(NSTypesetterWhitespaceAction, (1 << 1))
        self.failUnlessEqual(NSTypesetterHorizontalTabAction, (1 << 2))
        self.failUnlessEqual(NSTypesetterLineBreakAction, (1 << 3))
        self.failUnlessEqual(NSTypesetterParagraphBreakAction, (1 << 4))
        self.failUnlessEqual(NSTypesetterContainerBreakAction, (1 << 5))

    def testMethods(self):
        self.failUnlessArgIsOut(NSTypesetter.characterRangeForGlyphRange_actualGlyphRange_, 1)
        self.failUnlessArgIsOut(NSTypesetter.glyphRangeForCharacterRange_actualCharacterRange_, 1)
        self.failUnlessArgHasType(NSTypesetter.setBidiLevels_forGlyphRange_, 0, 'n^' + objc._C_CHAR_AS_INT)
        self.failUnlessArgSizeInArg(NSTypesetter.setBidiLevels_forGlyphRange_, 0, 1)
        self.failUnlessArgIsIn(NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1)
        self.failUnlessArgSizeInArg(NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1, 2)
        self.failUnlessArgIsOut(NSTypesetter.layoutGlyphsInLayoutManager_startingAtGlyphIndex_maxNumberOfLineFragments_nextGlyphIndex_, 3)
        self.failUnlessArgIsOut(NSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_, 0)
        self.failUnlessArgIsOut(NSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_, 1)

        self.failUnlessResultHasType(NSTypesetter.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, objc._C_NSUInteger)
        self.failUnlessArgHasType(NSTypesetter.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 0, NSRange.__typestr__)

        self.failUnlessArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 0, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 1, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 2, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 3, 'N^' + objc._C_CGFloat)


        self.failUnlessResultHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 0, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1, 'o^I')
        self.failUnlessArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1, 0)

        self.failUnlessArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2, 'o^' + objc._C_NSUInteger)
        self.failUnlessArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2, 0)
        self.failUnlessArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3, 'o^' + objc._C_NSUInteger)
        self.failUnlessArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3, 0)
        self.failUnlessArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, 0)
        self.failUnlessArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, 'o^' + objc._C_UCHR)
        self.failUnlessArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, 0)

        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 0, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 1, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 2, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 3, objc._C_NSUInteger)
        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 4, NSRect.__typestr__)
        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 5, objc._C_CGFloat)
        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 6, objc._C_CGFloat)
        self.failUnlessArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 7, objc._C_CGFloat)


    @min_os_level("10.5")
    def testMethods10_5(self):
        self.failUnlessArgHasType(NSTypesetter.printingAdjustmentInLayoutManager_forNominallySpacedGlyphRange_packedGlyphs_count_, 2, 'n^v')
        self.failUnlessArgSizeInArg(NSTypesetter.printingAdjustmentInLayoutManager_forNominallySpacedGlyphRange_packedGlyphs_count_, 2, 3)



if __name__ == "__main__":
    main()
