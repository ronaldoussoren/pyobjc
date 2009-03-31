
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLayoutManagerHelper (NSObject):
    def layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_(self, a, b, c, d, e): return 1
    def layoutManager_didCompleteLayoutForTextContainer_atEnd_(self, a, b, c): return 1

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
        self.failUnlessArgIsOut(NSLayoutManager.invalidateGlyphsForCharacterRange_changeInLength_actualCharacterRange_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.invalidateLayoutForCharacterRange_isSoft_actualCharacterRange_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.getGlyphs_range_, 0)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphs_range_, 0, 1)

        self.failUnlessArgIsOut(NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_, 1)
        self.failUnlessArgIsOut(NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_, 1)
        self.failUnlessArgIsOut(NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_, 1)
        self.failUnlessArgIsOut(NSLayoutManager.layoutRectForTextBlock_atIndex_effectiveRange_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.boundsRectForTextBlock_atIndex_effectiveRange_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.glyphRangeForCharacterRange_actualCharacterRange_, 1)
        self.failUnlessArgIsOut(NSLayoutManager.characterRangeForGlyphRange_actualGlyphRange_, 1)
        self.failUnlessArgIsOut(NSLayoutManager.temporaryAttributesAtCharacterIndex_effectiveRange_, 1)
        self.failUnlessArgIsOut(NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 1)
        self.failUnlessArgIsBOOL(NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 1)
        self.failUnlessArgIsBOOL(NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 1)
        self.failUnlessArgIsBOOL(NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.getFirstUnlaidCharacterIndex_glyphIndex_, 0)
        self.failUnlessArgIsOut(NSLayoutManager.getFirstUnlaidCharacterIndex_glyphIndex_, 1)
        self.failUnlessArgIsOut(NSLayoutManager.glyphIndexForPoint_inTextContainer_fractionOfDistanceThroughGlyph_, 2)

        self.failUnlessResultSizeInArg(NSLayoutManager.rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_, 3)
        self.failUnlessArgIsOut(NSLayoutManager.rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_, 3)
        self.failUnlessResultSizeInArg(NSLayoutManager.rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_, 3)
        self.failUnlessArgIsOut(NSLayoutManager.rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_, 3)

        self.failUnlessArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 1)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 1, 0)
        self.failUnlessArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 2)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 2, 0)
        self.failUnlessArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 3)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 3, 0)
        self.failUnlessArgHasType(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 4, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 4, 0)
        self.failUnlessArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1, 0)
        self.failUnlessArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2, 0)
        self.failUnlessArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3, 0)
        self.failUnlessArgHasType(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, 'o^' + objc._C_NSBOOL)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, 0)
        self.failUnlessArgHasType(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, 'o^' + objc._C_UCHR)
        self.failUnlessArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, 0)
        self.failUnlessArgHasType(NSLayoutManager.showPackedGlyphs_length_glyphRange_atPoint_font_color_printingAdjustment_, 0, 'n^v')
        self.failUnlessArgSizeInArg(NSLayoutManager.showPackedGlyphs_length_glyphRange_atPoint_font_color_printingAdjustment_, 0, 1)


    @min_os_level("10.5")
    def testMethods10_5(self):
        self.failUnlessArgIsOut(NSLayoutManager.invalidateGlyphsForCharacterRange_changeInLength_actualCharacterRange_, 2)
        self.failUnlessArgHasType(NSLayoutManager.glyphAtIndex_isValidIndex_, 1, 'o^' + objc._C_NSBOOL)

        self.failUnlessArgIsIn(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 0)
        self.failUnlessArgSizeInArg(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 0, 2)
        self.failUnlessArgIsIn(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 1)
        self.failUnlessArgSizeInArg(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 1, 2)

        self.failUnlessArgIsOut(NSLayoutManager.temporaryAttribute_atCharacterIndex_effectiveRange_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.temporaryAttribute_atCharacterIndex_longestEffectiveRange_inRange_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.temporaryAttributesAtCharacterIndex_longestEffectiveRange_inRange_, 1)

        self.failUnlessArgIsBOOL(TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_, 2)
        self.failUnlessArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_, 3, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_, 4, 'o^' + NSRange.__typestr__)

        self.failUnlessArgIsBOOL(TestNSLayoutManagerHelper.layoutManager_didCompleteLayoutForTextContainer_atEnd_, 2)

        self.failUnlessArgIsBOOL(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 1)
        self.failUnlessArgIsBOOL(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 2)
        self.failUnlessArgIsOut(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 3)
        self.failUnlessArgIsOut(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 4)

    @min_os_level('10.5')
    @expectedFailure
    def testMethods10_5_fail(self):
        self.fail("Buffer size is non-trivial: - (NSUInteger)getLineFragmentInsertionPointsForCharacterAtIndex:(NSUInteger)charIndex alternatePositions:(BOOL)aFlag inDisplayOrder:(BOOL)dFlag positions:(CGFloat *)positions characterIndexes:(NSUInteger *)charIndexes;")



if __name__ == "__main__":
    main()
