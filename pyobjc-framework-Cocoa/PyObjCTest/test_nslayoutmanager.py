
from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSLayoutManagerHelper (NSObject):
    def layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_(self, a, b, c, d, e): return 1
    def layoutManager_didCompleteLayoutForTextContainer_atEnd_(self, a, b, c): return 1
    def layoutOrientation(self): return 1
    def layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_(self, l, g, p, c, r): pass
    def layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_(self, l, i, r): return 1
    def layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_(self, l, i, r): return 1
    def layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_(self, l, i, r): return 1
    def layoutManager_shouldUseAction_forControlCharacterAtIndex_(self, l, a, i): return 1
    def layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_(self, l, i): return 1
    def layoutManager_shouldBreakLineByHyphenatingBeforeCharacterAtIndex_(self, l, i): return 1
    def layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_(self, l, i, c, f, p, i2): return 1
    def layoutManager_textContainer_didChangeGeometryFromSize_(self, l, c, s): pass
    def layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_(self, l, fr, ur, o, c, r): return 1

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

        self.assertEqual(NSTextLayoutOrientationHorizontal, 0)
        self.assertEqual(NSTextLayoutOrientationVertical, 1)

        # OSX 10.11:
        self.assertEqual(NSGlyphPropertyNull, 1<<0)
        self.assertEqual(NSGlyphPropertyControlCharacter, 1 << 1)
        self.assertEqual(NSGlyphPropertyElastic, 1 << 2)
        self.assertEqual(NSGlyphPropertyNonBaseCharacter, 1 << 3)

        self.assertEqual(NSControlCharacterActionZeroAdvancement, 1 << 0)
        self.assertEqual(NSControlCharacterActionWhitespace, 1 << 1)
        self.assertEqual(NSControlCharacterActionHorizontalTab, 1 << 2)
        self.assertEqual(NSControlCharacterActionLineBreak, 1 << 3)
        self.assertEqual(NSControlCharacterActionParagraphBreak, 1 << 4)
        self.assertEqual(NSControlCharacterActionContainerBreak, 1 << 5)

    @min_sdk_level('10.7')
    def testProtocolObjects(self):
        objc.protocolNamed('NSTextLayoutOrientationProvider')
        objc.protocolNamed('NSLayoutManagerDelegate')

    def testProtocols(self):
        self.assertResultHasType(TestNSLayoutManagerHelper.layoutOrientation, objc._C_NSInteger)


        # XXX: check interface!
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_, 1, b'n^' + objc._C_USHT)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_, 2, b'n^' + objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_, 3, b'n^' + objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_, 4, NSRange.__typestr__)
        self.assertArgSizeInArg(TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_, 1, 4)
        self.assertArgSizeInArg(TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_, 2, 4)
        self.assertArgSizeInArg(TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_, 3, 4)

        self.assertResultHasType(TestNSLayoutManagerHelper.layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_, objc._C_CGFloat)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_, 2, NSRect.__typestr__)

        self.assertResultHasType(TestNSLayoutManagerHelper.layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_, objc._C_CGFloat)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_, 2, NSRect.__typestr__)

        self.assertResultHasType(TestNSLayoutManagerHelper.layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_, objc._C_CGFloat)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_, 2, NSRect.__typestr__)

        self.assertResultHasType(TestNSLayoutManagerHelper.layoutManager_shouldUseAction_forControlCharacterAtIndex_, objc._C_NSInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldUseAction_forControlCharacterAtIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldUseAction_forControlCharacterAtIndex_, 2, objc._C_NSInteger)

        self.assertResultHasType(TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_, objc._C_NSBOOL)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_, 1, objc._C_NSUInteger)

        self.assertResultHasType(TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByHyphenatingBeforeCharacterAtIndex_, objc._C_NSBOOL)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_, 1, objc._C_NSUInteger)

        self.assertResultHasType(TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_, NSRect.__typestr__)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_, 1, objc._C_NSUInteger)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_, 3, NSRect.__typestr__)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_, 4, NSPoint.__typestr__)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_, 5, objc._C_NSUInteger)

        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_textContainer_didChangeGeometryFromSize_, 2, NSSize.__typestr__)

        self.assertResultIsBOOL(TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_, 1, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_, 2, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_, 3, b'N^' + objc._C_CGFloat)
        self.assertArgHasType(TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_, 5, NSRange.__typestr__)


    def testMethods(self):
        self.assertResultIsBOOL(NSLayoutManager.usesScreenFonts)
        self.assertArgIsBOOL(NSLayoutManager.setUsesScreenFonts_, 0)

        self.assertArgSizeInArg(NSLayoutManager.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_, 0, 1)
        self.assertArgIsIn(NSLayoutManager.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_, 0)

        self.assertArgIsOut(NSLayoutManager.invalidateGlyphsForCharacterRange_changeInLength_actualCharacterRange_, 2)
        self.assertArgIsOut(NSLayoutManager.invalidateLayoutForCharacterRange_isSoft_actualCharacterRange_, 2)
        self.assertArgIsOut(NSLayoutManager.getGlyphs_range_, 0)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphs_range_, 0, 1)

        self.assertResultIsBOOL(NSLayoutManager.showsInvisibleCharacters)
        self.assertArgIsBOOL(NSLayoutManager.setShowsInvisibleCharacters_, 0)

        self.assertResultIsBOOL(NSLayoutManager.showsControlCharacters)
        self.assertArgIsBOOL(NSLayoutManager.setShowsControlCharacters_, 0)

        self.assertResultIsBOOL(NSLayoutManager.usesFontLeading)
        self.assertArgIsBOOL(NSLayoutManager.setUsesFontLeading_, 0)

        self.assertResultIsBOOL(NSLayoutManager.backgroundLayoutEnabled)
        self.assertArgIsBOOL(NSLayoutManager.setBackgroundLayoutEnabled_, 0)

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

        self.assertResultIsBOOL(NSLayoutManager.isValidGlyphIndex_)

        self.assertArgIsBOOL(NSLayoutManager.setNotShownAttribute_forGlyphAtIndex_, 0)
        self.assertArgIsBOOL(NSLayoutManager.setDrawsOutsideLineFragment_forGlyphAtIndex_, 0)

        self.assertResultIsBOOL(NSLayoutManager.notShownAttributeForGlyphAtIndex_)
        self.assertResultIsBOOL(NSLayoutManager.drawsOutsideLineFragmentForGlyphAtIndex_)


    @min_os_level('10.11')
    def testMethods_missing_10_10(self):
        # Document, but not present on 10.10??
        self.assertArgHasType(NSLayoutManager.CGGlyphAtIndex_isValidIndex_, 1, b'o^Z')


    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(NSLayoutManager.allowsNonContiguousLayout)
        self.assertArgIsBOOL(NSLayoutManager.setAllowsNonContiguousLayout_, 0)

        self.assertResultIsBOOL(NSLayoutManager.hasNonContiguousLayout)
        #self.assertArgIsBOOL(NSLayoutManager.setHasNonContiguousLayout_, 0)

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


        self.assertArgIsBOOL(NSLayoutManager.rulerAccessoryViewForTextView_paragraphStyle_ruler_enabled_, 3)
        self.assertResultIsBOOL(NSLayoutManager.layoutManagerOwnsFirstResponderInWindow_)

    @expectedFailureIf(os_release().rsplit('.', 1)[0] in ('10.5', '10.6', '10.7', '10.8', '10.9'))
    @min_os_level('10.5')
    def testMethods10_5_not_available(self):
        self.assertHasAttr(NSLayoutManager, 'getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_')
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 1)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 2)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 3)
        self.assertArgIsOut(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 4)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 1, 0)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 2, 0)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 3, 0)
        self.assertArgSizeInArg(NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_, 4, 0)

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

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsIn(NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_, 0)
        self.assertArgSizeInArg(NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_, 0, 2)
        self.assertArgIsIn(NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_, 1)
        self.assertArgSizeInArg(NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_, 1, 2)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgSizeInArg(NSLayoutManager.setGlyphs_properties_characterIndexes_font_forGlyphRange_, 0, 4)
        self.assertArgSizeInArg(NSLayoutManager.setGlyphs_properties_characterIndexes_font_forGlyphRange_, 1, 4)
        self.assertArgSizeInArg(NSLayoutManager.setGlyphs_properties_characterIndexes_font_forGlyphRange_, 2, 4)

        self.assertArgIsBlock(NSLayoutManager.enumerateLineFragmentsForGlyphRange_usingBlock_, 1, b'v' + NSRect.__typestr__ + NSRect.__typestr__ + b'@' + NSRange.__typestr__ + b'o^Z')
        self.assertArgIsBlock(NSLayoutManager.enumerateEnclosingRectsForGlyphRange_withinSelectedGlyphRange_inTextContainer_usingBlock_, 3, b'v' + NSRect.__typestr__ + b'o^Z')

        self.assertResultIsBOOL


if __name__ == "__main__":
    main()
