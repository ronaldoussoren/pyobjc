import AppKit
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    min_sdk_level,
    expectedFailure,
    os_release,
    expectedFailureIf,
)
import objc


class TestNSLayoutManagerHelper(AppKit.NSObject):
    def layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_(  # noqa: B950
        self, a, b, c, d, e
    ):
        return 1

    def layoutManager_didCompleteLayoutForTextContainer_atEnd_(self, a, b, c):
        return 1

    def layoutOrientation(self):
        return 1

    def layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_(
        self, x, g, p, c, r
    ):
        pass

    def layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_(
        self, x, i, r
    ):
        return 1

    def layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_(
        self, x, i, r
    ):
        return 1

    def layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_(
        self, x, i, r
    ):
        return 1

    def layoutManager_shouldUseAction_forControlCharacterAtIndex_(self, x, a, i):
        return 1

    def layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_(self, x, i):
        return 1

    def layoutManager_shouldBreakLineByHyphenatingBeforeCharacterAtIndex_(self, x, i):
        return 1

    def layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_(  # noqa: B950
        self, x, i, c, f, p, i2
    ):
        return 1

    def layoutManager_textContainer_didChangeGeometryFromSize_(self, x, c, s):
        pass

    def layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_(  # noqa: B950
        self, x, fr, ur, o, c, r
    ):
        return 1


class TestNSLayoutManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSControlCharacterAction)
        self.assertIsEnumType(AppKit.NSGlyphInscription)
        self.assertIsEnumType(AppKit.NSGlyphProperty)
        self.assertIsEnumType(AppKit.NSTextLayoutOrientation)
        self.assertIsEnumType(AppKit.NSTypesetterBehavior)

    def testConstants(self):
        self.assertEqual(AppKit.NSGlyphAttributeSoft, 0)
        self.assertEqual(AppKit.NSGlyphAttributeElastic, 1)
        self.assertEqual(AppKit.NSGlyphAttributeBidiLevel, 2)
        self.assertEqual(AppKit.NSGlyphAttributeInscribe, 5)

        self.assertEqual(AppKit.NSGlyphInscribeBase, 0)
        self.assertEqual(AppKit.NSGlyphInscribeBelow, 1)
        self.assertEqual(AppKit.NSGlyphInscribeAbove, 2)
        self.assertEqual(AppKit.NSGlyphInscribeOverstrike, 3)
        self.assertEqual(AppKit.NSGlyphInscribeOverBelow, 4)

        self.assertEqual(AppKit.NSTypesetterLatestBehavior, -1)
        self.assertEqual(AppKit.NSTypesetterOriginalBehavior, 0)
        self.assertEqual(AppKit.NSTypesetterBehavior_10_2_WithCompatibility, 1)
        self.assertEqual(AppKit.NSTypesetterBehavior_10_2, 2)
        self.assertEqual(AppKit.NSTypesetterBehavior_10_3, 3)
        self.assertEqual(AppKit.NSTypesetterBehavior_10_4, 4)

        self.assertEqual(AppKit.NSTextLayoutOrientationHorizontal, 0)
        self.assertEqual(AppKit.NSTextLayoutOrientationVertical, 1)

        # OSX 10.11:
        self.assertEqual(AppKit.NSGlyphPropertyNull, 1 << 0)
        self.assertEqual(AppKit.NSGlyphPropertyControlCharacter, 1 << 1)
        self.assertEqual(AppKit.NSGlyphPropertyElastic, 1 << 2)
        self.assertEqual(AppKit.NSGlyphPropertyNonBaseCharacter, 1 << 3)

        self.assertEqual(AppKit.NSControlCharacterActionZeroAdvancement, 1 << 0)
        self.assertEqual(AppKit.NSControlCharacterActionWhitespace, 1 << 1)
        self.assertEqual(AppKit.NSControlCharacterActionHorizontalTab, 1 << 2)
        self.assertEqual(AppKit.NSControlCharacterActionLineBreak, 1 << 3)
        self.assertEqual(AppKit.NSControlCharacterActionParagraphBreak, 1 << 4)
        self.assertEqual(AppKit.NSControlCharacterActionContainerBreak, 1 << 5)

    @min_sdk_level("10.7")
    def testProtocolObjects(self):
        objc.protocolNamed("NSTextLayoutOrientationProvider")
        objc.protocolNamed("NSLayoutManagerDelegate")

    def testProtocols(self):
        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutOrientation, objc._C_NSInteger
        )

        # XXX: check interface!
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_,  # noqa: B950
            1,
            b"n^" + objc._C_USHT,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_,  # noqa: B950
            2,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_,  # noqa: B950
            3,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_,  # noqa: B950
            4,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_,  # noqa: B950
            1,
            4,
        )
        self.assertArgSizeInArg(
            TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_,  # noqa: B950
            2,
            4,
        )
        self.assertArgSizeInArg(
            TestNSLayoutManagerHelper.layoutManager_shouldGenerateGlyphs_properties_characterIndexes_forGlyphRange_,  # noqa: B950
            3,
            4,
        )

        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_lineSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            2,
            AppKit.NSRect.__typestr__,
        )

        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_paragraphSpacingBeforeGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            2,
            AppKit.NSRect.__typestr__,
        )

        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_paragraphSpacingAfterGlyphAtIndex_withProposedLineFragmentRect_,  # noqa: B950
            2,
            AppKit.NSRect.__typestr__,
        )

        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldUseAction_forControlCharacterAtIndex_,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldUseAction_forControlCharacterAtIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldUseAction_forControlCharacterAtIndex_,
            2,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_,  # noqa: B950
            objc._C_NSBOOL,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByHyphenatingBeforeCharacterAtIndex_,  # noqa: B950
            objc._C_NSBOOL,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldBreakLineByWordBeforeCharacterAtIndex_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            3,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            4,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_textContainer_didChangeGeometryFromSize_,
            2,
            AppKit.NSSize.__typestr__,
        )

        self.assertResultIsBOOL(
            TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_  # noqa: B950
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_,  # noqa: B950
            1,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_,  # noqa: B950
            2,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_,  # noqa: B950
            3,
            b"N^" + objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldSetLineFragmentRect_lineFragmentUsedRect_baselineOffset_inTextContainer_forGlyphRange_,  # noqa: B950
            5,
            AppKit.NSRange.__typestr__,
        )

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSLayoutManager.usesScreenFonts)
        self.assertArgIsBOOL(AppKit.NSLayoutManager.setUsesScreenFonts_, 0)

        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,
            0,
            1,
        )
        self.assertArgIsIn(
            AppKit.NSLayoutManager.insertGlyphs_length_forStartingGlyphAtIndex_characterIndex_,  # noqa: B950
            0,
        )

        self.assertArgIsOut(
            AppKit.NSLayoutManager.invalidateGlyphsForCharacterRange_changeInLength_actualCharacterRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.invalidateLayoutForCharacterRange_isSoft_actualCharacterRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(AppKit.NSLayoutManager.getGlyphs_range_, 0)
        self.assertArgSizeInArg(AppKit.NSLayoutManager.getGlyphs_range_, 0, 1)

        self.assertResultIsBOOL(AppKit.NSLayoutManager.showsInvisibleCharacters)
        self.assertArgIsBOOL(AppKit.NSLayoutManager.setShowsInvisibleCharacters_, 0)

        self.assertResultIsBOOL(AppKit.NSLayoutManager.showsControlCharacters)
        self.assertArgIsBOOL(AppKit.NSLayoutManager.setShowsControlCharacters_, 0)

        self.assertResultIsBOOL(AppKit.NSLayoutManager.usesFontLeading)
        self.assertArgIsBOOL(AppKit.NSLayoutManager.setUsesFontLeading_, 0)

        self.assertResultIsBOOL(AppKit.NSLayoutManager.backgroundLayoutEnabled)
        self.assertArgIsBOOL(AppKit.NSLayoutManager.setBackgroundLayoutEnabled_, 0)

        self.assertArgIsOut(
            AppKit.NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_, 1
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_, 1
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_,
            1,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.layoutRectForTextBlock_atIndex_effectiveRange_, 2
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.boundsRectForTextBlock_atIndex_effectiveRange_, 2
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.glyphRangeForCharacterRange_actualCharacterRange_, 1
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.characterRangeForGlyphRange_actualGlyphRange_, 1
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.temporaryAttributesAtCharacterIndex_effectiveRange_,
            1,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.lineFragmentRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.lineFragmentUsedRectForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.textContainerForGlyphAtIndex_effectiveRange_withoutAdditionalLayout_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getFirstUnlaidCharacterIndex_glyphIndex_, 0
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getFirstUnlaidCharacterIndex_glyphIndex_, 1
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.glyphIndexForPoint_inTextContainer_fractionOfDistanceThroughGlyph_,  # noqa: B950
            2,
        )

        self.assertResultSizeInArg(
            AppKit.NSLayoutManager.rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_,  # noqa: B950
            3,
        )
        self.assertResultSizeInArg(
            AppKit.NSLayoutManager.rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_,  # noqa: B950
            3,
        )

        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            1,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            1,
            0,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            2,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            2,
            0,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            3,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            3,
            0,
        )
        self.assertArgHasType(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            4,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_,  # noqa: B950
            4,
            0,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            1,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            1,
            0,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            2,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            2,
            0,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            3,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            3,
            0,
        )
        self.assertArgHasType(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            4,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            4,
            0,
        )
        self.assertArgHasType(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            5,
            b"o^" + objc._C_UCHR,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            5,
            0,
        )
        self.assertArgHasType(
            AppKit.NSLayoutManager.showPackedGlyphs_length_glyphRange_atPoint_font_color_printingAdjustment_,  # noqa: B950
            0,
            b"n^v",
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.showPackedGlyphs_length_glyphRange_atPoint_font_color_printingAdjustment_,  # noqa: B950
            0,
            1,
        )

        self.assertResultIsBOOL(AppKit.NSLayoutManager.isValidGlyphIndex_)

        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.setNotShownAttribute_forGlyphAtIndex_, 0
        )
        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.setDrawsOutsideLineFragment_forGlyphAtIndex_, 0
        )

        self.assertResultIsBOOL(
            AppKit.NSLayoutManager.notShownAttributeForGlyphAtIndex_
        )
        self.assertResultIsBOOL(
            AppKit.NSLayoutManager.drawsOutsideLineFragmentForGlyphAtIndex_
        )

    @min_os_level("10.11")
    def testMethods_missing_10_10(self):
        # Document, but not present on 10.10??
        self.assertArgHasType(
            AppKit.NSLayoutManager.CGGlyphAtIndex_isValidIndex_, 1, b"o^Z"
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(AppKit.NSLayoutManager.allowsNonContiguousLayout)
        self.assertArgIsBOOL(AppKit.NSLayoutManager.setAllowsNonContiguousLayout_, 0)

        self.assertResultIsBOOL(AppKit.NSLayoutManager.hasNonContiguousLayout)

        self.assertArgIsOut(
            AppKit.NSLayoutManager.invalidateGlyphsForCharacterRange_changeInLength_actualCharacterRange_,  # noqa: B950
            2,
        )
        self.assertArgHasType(
            AppKit.NSLayoutManager.glyphAtIndex_isValidIndex_, 1, b"o^" + objc._C_NSBOOL
        )

        self.assertArgIsIn(
            AppKit.NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_,
            0,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_,
            0,
            2,
        )
        self.assertArgIsIn(
            AppKit.NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_,
            1,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.setLocations_startingGlyphIndexes_count_forGlyphRange_,
            1,
            2,
        )

        self.assertArgIsOut(
            AppKit.NSLayoutManager.temporaryAttribute_atCharacterIndex_effectiveRange_,
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.temporaryAttribute_atCharacterIndex_longestEffectiveRange_inRange_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.temporaryAttributesAtCharacterIndex_longestEffectiveRange_inRange_,  # noqa: B950
            1,
        )

        self.assertArgIsBOOL(
            TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_,  # noqa: B950
            2,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSLayoutManagerHelper.layoutManager_shouldUseTemporaryAttributes_forDrawingToScreen_atCharacterIndex_effectiveRange_,  # noqa: B950
            4,
            b"o^" + AppKit.NSRange.__typestr__,
        )

        self.assertArgIsBOOL(
            TestNSLayoutManagerHelper.layoutManager_didCompleteLayoutForTextContainer_atEnd_,  # noqa: B950
            2,
        )

        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getLineFragmentInsertionPointsForCharacterAtIndex_alternatePositions_inDisplayOrder_positions_characterIndexes_,  # noqa: B950
            4,
        )

        self.assertResultIsBOOL(
            AppKit.NSLayoutManager.layoutManagerOwnsFirstResponderInWindow_
        )

    @expectedFailure
    def testMethods10_5_failon11beta(self):
        self.assertArgIsBOOL(
            AppKit.NSLayoutManager.rulerAccessoryViewForTextView_paragraphStyle_ruler_enabled_,
            3,
        )

    @expectedFailureIf(
        os_release().rsplit(".", 1)[0] in ("10.5", "10.6", "10.7", "10.8", "10.9")
    )
    @min_os_level("10.5")
    def testMethods10_5_not_available(self):
        self.assertHasAttr(
            AppKit.NSLayoutManager,
            "getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_",
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            2,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            4,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            1,
            0,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            2,
            0,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            3,
            0,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.getGlyphsInRange_glyphs_properties_characterIndexes_bidiLevels_,  # noqa: B950
            4,
            0,
        )

    @min_os_level("10.5")
    @expectedFailure
    def testMethods10_5_fail(self):
        self.fail(
            "Buffer size is non-trivial: - (AppKit.NSUInteger)getLineFragmentInsertionPointsForCharacterAtIndex:(AppKit.NSUInteger)charIndex alternatePositions:(BOOL)aFlag inDisplayOrder:(BOOL)dFlag positions:(CGFloat *)positions characterIndexes:(AppKit.NSUInteger *)charIndexes;"  # noqa: B950
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgHasType(
            AppKit.NSLayoutManager.characterIndexForPoint_inTextContainer_fractionOfDistanceBetweenInsertionPoints_,  # noqa: B950
            0,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgIsOut(
            AppKit.NSLayoutManager.characterIndexForPoint_inTextContainer_fractionOfDistanceBetweenInsertionPoints_,  # noqa: B950
            2,
        )

        self.assertArgHasType(
            AppKit.NSLayoutManager.fillBackgroundRectArray_count_forCharacterRange_color_,
            0,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.fillBackgroundRectArray_count_forCharacterRange_color_,
            0,
            1,
        )
        self.assertArgHasType(
            AppKit.NSLayoutManager.fillBackgroundRectArray_count_forCharacterRange_color_,
            2,
            AppKit.NSRange.__typestr__,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsIn(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_,  # noqa: B950
            0,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_,  # noqa: B950
            0,
            2,
        )
        self.assertArgIsIn(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_,  # noqa: B950
            1,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_matrix_attributes_inContext_,  # noqa: B950
            1,
            2,
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.setGlyphs_properties_characterIndexes_font_forGlyphRange_,
            0,
            4,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.setGlyphs_properties_characterIndexes_font_forGlyphRange_,
            1,
            4,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.setGlyphs_properties_characterIndexes_font_forGlyphRange_,
            2,
            4,
        )

        self.assertArgIsBlock(
            AppKit.NSLayoutManager.enumerateLineFragmentsForGlyphRange_usingBlock_,
            1,
            b"v"
            + AppKit.NSRect.__typestr__
            + AppKit.NSRect.__typestr__
            + b"@"
            + AppKit.NSRange.__typestr__
            + b"o^Z",
        )
        self.assertArgIsBlock(
            AppKit.NSLayoutManager.enumerateEnclosingRectsForGlyphRange_withinSelectedGlyphRange_inTextContainer_usingBlock_,  # noqa: B950
            3,
            b"v" + AppKit.NSRect.__typestr__ + b"o^Z",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(AppKit.NSLayoutManager.usesDefaultHyphenation)
        self.assertArgIsBOOL(AppKit.NSLayoutManager.setUsesDefaultHyphenation_, 0)

        self.assertArgIsIn(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_textMatrix_attributes_inContext_,  # noqa: B950
            0,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_textMatrix_attributes_inContext_,  # noqa: B950
            0,
            2,
        )
        self.assertArgIsIn(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_textMatrix_attributes_inContext_,  # noqa: B950
            1,
        )
        self.assertArgSizeInArg(
            AppKit.NSLayoutManager.showCGGlyphs_positions_count_font_textMatrix_attributes_inContext_,  # noqa: B950
            1,
            2,
        )
