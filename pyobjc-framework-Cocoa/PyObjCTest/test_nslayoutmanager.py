
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLayoutManagerHelper (NSObject):
    def layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_(self, a, b, c, d, e): return 1
    def layoutManager_didCompleteLayoutForTextContainer_atEnd_(self, a, b, c): return 1

class TestNSLayoutManager (TestCase):
    def testConstants(self):
        self.assertEqual(NSGlyphAttributeSoft, 0)
        self.assertEqual(NSGlyphAttributeElastic, 1)
        self.assertEqual(NSGlyphAttributeBidiLevel, 2)
        self.assertEqual(NSGlyphAttributeInscribe, 5)
        self.assertEqual(NSGlyphInscribeBase, 0)
        self.assertEqual(NSGlyphInscribeBelow, 1)
        self.assertEqual(NSGlyphInscribeAbove, 2)
        self.assertEqual(NSGlyphInscribeOverstrike, 3)
        self.assertEqual(NSGlyphInscribeOverBelow, 4)
        self.assertEqual(NSTypesetterLatestBehavior, -1)
        self.assertEqual(NSTypesetterOriginalBehavior, 0)
        self.assertEqual(NSTypesetterBehavior_10_2_WithCompatibility, 1)
        self.assertEqual(NSTypesetterBehavior_10_2, 2)
        self.assertEqual(NSTypesetterBehavior_10_3, 3)
        self.assertEqual(NSTypesetterBehavior_10_4, 4)

    def testMethods(self):
        self.assertArgIsOut(NSLayoutManager.invalidateGlyphsForCharacterRange_changeInLength_actualCharacterRange_, 2)
        self.assertArgIsOut(NSLayoutManager.invalidateLayoutForCharacterRange_isSoft_actualCharacterRange_, 2)
        self.assertArgIsOut(NSLayoutManager.getGlyphs_range_, 0)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphs_range_, 0, 1)

        self.assertArgIsOut(NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_, 1)
        self.assertArgIsOut(NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_, 1)
        self.assertArgIsOut(NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_, 1)
        self.assertArgIsOut(NSLayoutManager.layoutRectForTextBlock_atIndex_effectiveRange_, 2)
        self.assertArgIsOut(NSLayoutManager.boundsRectForTextBlock_atIndex_effectiveRange_, 2)
        self.assertArgIsOut(NSLayoutManager.glyphRangeForCharacterRange_actualCharacterRange_, 1)
        self.assertArgIsOut(NSLayoutManager.characterRangeForGlyphRange_actualGlyphRange_, 1)
        self.assertArgIsOut(NSLayoutManager.temporaryAttributesAtCharacterIndex_effectiveRange_, 1)
        self.assertArgIsOut(NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 1)
        self.assertArgIsBOOL(NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 2)
        self.assertArgIsOut(NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 1)
        self.assertArgIsBOOL(NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 2)
        self.assertArgIsOut(NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 1)
        self.assertArgIsBOOL(NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_, 2)
        self.assertArgIsOut(NSLayoutManager.getFirstUnlaidCharacterIndex_glyphIndex_, 0)
        self.assertArgIsOut(NSLayoutManager.getFirstUnlaidCharacterIndex_glyphIndex_, 1)
        self.assertArgIsOut(NSLayoutManager.glyphIndexForPoint_inTextContainer_fractionOfDistanceThroughGlyph_, 2)

        self.assertResultSizeInArg(NSLayoutManager.rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_, 3)
        self.assertArgIsOut(NSLayoutManager.rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_, 3)
        self.assertResultSizeInArg(NSLayoutManager.rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_, 3)
        self.assertArgIsOut(NSLayoutManager.rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_, 3)

        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 1)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 1, 0)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 2)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 2, 0)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 3)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 3, 0)
        self.assertArgHasType(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 4, b'o^' + objc._C_NSBOOL)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_, 4, 0)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 1, 0)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 2, 0)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 3, 0)
        self.assertArgHasType(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, b'o^' + objc._C_NSBOOL)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 4, 0)
        self.assertArgHasType(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, b'o^' + objc._C_UCHR)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_, 5, 0)
        self.assertArgHasType(NSLayoutManager.showPackedGlyphs_length_glyphRange_atPoint_font_color_printingAdjustment_, 0, b'n^v')
        self.assertArgSizeInArg(NSLayoutManager.showPackedGlyphs_length_glyphRange_atPoint_font_color_printingAdjustment_, 0, 1)


    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsOut(NSLayoutManager.invalidateGlyphsForCharacterRange_changeInLength_actualCharacterRange_, 2)
        self.assertArgHasType(NSLayoutManager.glyphAtIndex_isValidIndex_, 1, b'o^' + objc._C_NSBOOL)

        self.assertArgIsIn(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 0)
        self.assertArgSizeInArg(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 0, 2)
        self.assertArgIsIn(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 1)
        self.assertArgSizeInArg(NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_, 1, 2)

        self.assertArgIsOut(NSLayoutManager.temporaryAttribute_atCharacterIndex_effectiveRange_, 2)
        self.assertArgIsOut(NSLayoutManager.temporaryAttribute_atCharacterIndex_longestEffectiveRange_inRange_, 2)
        self.assertArgIsOut(NSLayoutManager.temporaryAttributesAtCharacterIndex_longestEffectiveRange_inRange_, 1)

        self.assertArgIsBOOL(TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_, 2)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_, 3, objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_, 4, b'o^' + NSRange.__typestr__)

        self.assertArgIsBOOL(TestNSLayoutManagerHelper.layoutManager_didCompleteLayoutForTextContainer_atEnd_, 2)

        self.assertArgIsBOOL(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 1)
        self.assertArgIsBOOL(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 2)
        self.assertArgIsOut(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 3)
        self.assertArgIsOut(NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_, 4)

    @min_os_level('10.5')
    @expectedFailure
    def testMethods10_5_fail(self):
        self.fail("Buffer size is non-trivial: - (NSUInteger)getLineFragmentInsertionPointsForCharacterAtIndex:(NSUInteger)charIndex alternatePositions:(BOOL)aFlag inDisplayOrder:(BOOL)dFlag positions:(CGFloat *)positions characterIndexes:(NSUInteger *)charIndexes;")


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgHasType(NSLayoutManager.characterIndexForPoint_inTextContainer_fractionOfDistanceBetweenInsertionPoints_, 0, NSPoint.__typestr__)
        self.assertArgIsOut(NSLayoutManager.characterIndexForPoint_inTextContainer_fractionOfDistanceBetweenInsertionPoints_, 2)

        self.assertArgHasType(NSLayoutManager.fillBackgroundRectArray_count_forCharacterRange_color_,
                0, b'N^' + NSRect.__typestr__)
        self.assertArgSizeInArg(NSLayoutManager.fillBackgroundRectArray_count_forCharacterRange_color_, 0, 1)
        self.assertArgHasType(NSLayoutManager.fillBackgroundRectArray_count_forCharacterRange_color_,
                2, NSRange.__typestr__)





if __name__ == "__main__":
    main()
