
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTypesetterHelper (NSTypesetter):
    def willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_(self, a, b, c, d): return 1
    def getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_(self, a, b, c, d, e, f): return 1
    def getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_(self, a, b, c, d, e, f, g, h): return 1

class TestNSTypesetter (TestCase):
    def testConstants(self):
        self.assertEqual(NSTypesetterZeroAdvancementAction, (1 << 0))
        self.assertEqual(NSTypesetterWhitespaceAction, (1 << 1))
        self.assertEqual(NSTypesetterHorizontalTabAction, (1 << 2))
        self.assertEqual(NSTypesetterLineBreakAction, (1 << 3))
        self.assertEqual(NSTypesetterParagraphBreakAction, (1 << 4))
        self.assertEqual(NSTypesetterContainerBreakAction, (1 << 5))

    def testMethods(self):
        self.assertArgIsOut(NSTypesetter.characterRangeForGlyphRange_actualGlyphRange_, 1)
        self.assertArgIsOut(NSTypesetter.glyphRangeForCharacterRange_actualCharacterRange_, 1)
        self.assertArgHasType(NSTypesetter.setBidiLevels_forGlyphRange_, 0, b'n^' + objc._C_CHAR_AS_INT)
        self.assertArgSizeInArg(NSTypesetter.setBidiLevels_forGlyphRange_, 0, 1)
        self.assertArgIsIn(NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1)
        self.assertArgSizeInArg(NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1, 2)
        self.assertArgIsOut(NSTypesetter.layoutGlyphsInLayoutManager_startingAtGlyphIndex_maxNumberOfLineFragments_nextGlyphIndex_, 3)
        self.assertArgIsOut(NSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_, 0)
        self.assertArgIsOut(NSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_, 1)

        self.assertResultHasType(NSTypesetter.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, objc._C_NSUInteger)
        self.assertArgHasType(NSTypesetter.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 0, NSRange.__typestr__)

        self.assertArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 0, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 1, NSRange.__typestr__)
        self.assertArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 2, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_, 3, b'N^' + objc._C_CGFloat)


        self.assertResultHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 0, NSRange.__typestr__)
        self.assertArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1, b'o^I')
        self.assertArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1, 0)

        self.assertArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2, b'o^' + objc._C_NSUInteger)
        self.assertArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2, 0)
        self.assertArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3, b'o^' + objc._C_NSUInteger)
        self.assertArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3, 0)
        self.assertArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, b'o^' + objc._C_NSBOOL)
        self.assertArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, 0)
        self.assertArgHasType(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, b'o^' + objc._C_UCHR)
        self.assertArgSizeInArg(TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, 0)

        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 0, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 1, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 2, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 3, objc._C_NSUInteger)
        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 4, NSRect.__typestr__)
        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 5, objc._C_CGFloat)
        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 6, objc._C_CGFloat)
        self.assertArgHasType(NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_, 7, objc._C_CGFloat)


    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgHasType(NSTypesetter.printingAdjustmentInLayoutManager_forNominallySpacedGlyphRange_packedGlyphs_count_, 2, b'n^v')
        self.assertArgSizeInArg(NSTypesetter.printingAdjustmentInLayoutManager_forNominallySpacedGlyphRange_packedGlyphs_count_, 2, 3)



if __name__ == "__main__":
    main()
