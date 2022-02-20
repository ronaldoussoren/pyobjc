import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTypesetterHelper(AppKit.NSTypesetter):
    def willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_(
        self, a, b, c, d
    ):
        return 1

    def getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_(
        self, a, b, c, d, e, f
    ):
        return 1

    def getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_(  # noqa: B950
        self, a, b, c, d, e, f, g, h
    ):
        return 1

    def shouldBreakLineByWordBeforeCharacterAtIndex_(self, i):
        return False

    def shouldBreakLineByHyphenatingBeforeCharacterAtIndex_(self, i):
        return False

    def hyphenationFactorForGlyphAtIndex_(self, i):
        return 1.0

    def hyphenCharacterForGlyphAtIndex_(self, i):
        return 1

    def boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_(  # noqa: B950
        self, i, c, f, p, idx
    ):
        pass


class TestNSTypesetter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTypesetterControlCharacterAction)

    def testConstants(self):
        self.assertEqual(AppKit.NSTypesetterZeroAdvancementAction, (1 << 0))
        self.assertEqual(AppKit.NSTypesetterWhitespaceAction, (1 << 1))
        self.assertEqual(AppKit.NSTypesetterHorizontalTabAction, (1 << 2))
        self.assertEqual(AppKit.NSTypesetterLineBreakAction, (1 << 3))
        self.assertEqual(AppKit.NSTypesetterParagraphBreakAction, (1 << 4))
        self.assertEqual(AppKit.NSTypesetterContainerBreakAction, (1 << 5))

    def testMethods(self):
        self.assertArgIsIn(AppKit.NSTypesetter.substituteGlyphsInRange_withGlyphs_, 1)
        self.assertArgSizeInArg(
            AppKit.NSTypesetter.substituteGlyphsInRange_withGlyphs_, 1, 0
        )
        self.assertArgIsIn(
            AppKit.NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1
        )
        self.assertArgSizeInArg(
            AppKit.NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1, 2
        )
        self.assertArgIsBOOL(AppKit.NSTypesetter.setNotShownAttribute_forGlyphRange_, 0)
        self.assertArgIsBOOL(
            AppKit.NSTypesetter.setDrawsOutsideLineFragment_forGlyphRange_, 0
        )
        self.assertResultIsBOOL(
            TestNSTypesetterHelper.shouldBreakLineByWordBeforeCharacterAtIndex_
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.shouldBreakLineByWordBeforeCharacterAtIndex_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            TestNSTypesetterHelper.shouldBreakLineByHyphenatingBeforeCharacterAtIndex_
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.shouldBreakLineByHyphenatingBeforeCharacterAtIndex_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestNSTypesetterHelper.hyphenationFactorForGlyphAtIndex_, objc._C_FLT
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.hyphenationFactorForGlyphAtIndex_,
            0,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestNSTypesetterHelper.boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            3,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestNSTypesetterHelper.hyphenCharacterForGlyphAtIndex_, objc._C_INT
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.hyphenCharacterForGlyphAtIndex_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgIsBOOL(AppKit.NSTypesetter.setHardInvalidation_forGlyphRange_, 0)
        self.assertResultIsBOOL(AppKit.NSTypesetter.usesFontLeading)
        self.assertArgIsBOOL(AppKit.NSTypesetter.setUsesFontLeading_, 0)
        self.assertResultIsBOOL(AppKit.NSTypesetter.bidiProcessingEnabled)
        self.assertArgIsBOOL(AppKit.NSTypesetter.setBidiProcessingEnabled_, 0)
        self.assertArgIsInOut(AppKit.NSTypesetter.layoutParagraphAtPoint_, 0)
        self.assertArgIsOut(
            AppKit.NSTypesetter.characterRangeForGlyphRange_actualGlyphRange_, 1
        )
        self.assertArgIsOut(
            AppKit.NSTypesetter.glyphRangeForCharacterRange_actualCharacterRange_, 1
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.setBidiLevels_forGlyphRange_,
            0,
            b"n^" + objc._C_CHAR_AS_INT,
        )
        self.assertArgSizeInArg(AppKit.NSTypesetter.setBidiLevels_forGlyphRange_, 0, 1)
        self.assertArgIsIn(
            AppKit.NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1
        )
        self.assertArgSizeInArg(
            AppKit.NSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1, 2
        )
        self.assertArgIsOut(
            AppKit.NSTypesetter.layoutGlyphsInLayoutManager_startingAtGlyphIndex_maxNumberOfLineFragments_nextGlyphIndex_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_,  # noqa: B950
            0,
        )
        self.assertArgIsOut(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_,  # noqa: B950
            1,
        )

        self.assertResultHasType(
            AppKit.NSTypesetter.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            0,
            AppKit.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_,  # noqa: B950
            0,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_,  # noqa: B950
            2,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_,  # noqa: B950
            3,
            b"N^" + objc._C_CGFloat,
        )

        self.assertResultHasType(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            0,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            1,
            b"o^I",
        )
        self.assertArgSizeInArg(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            1,
            0,
        )

        self.assertArgHasType(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            2,
            b"o^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            2,
            0,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            3,
            b"o^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            3,
            0,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            4,
            b"o^" + objc._C_NSBOOL,
        )
        self.assertArgSizeInArg(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            4,
            0,
        )
        self.assertArgHasType(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            5,
            b"o^" + objc._C_UCHR,
        )
        self.assertArgSizeInArg(
            TestNSTypesetterHelper.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_,  # noqa: B950
            5,
            0,
        )

        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            0,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            1,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            2,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            4,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            5,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            6,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            AppKit.NSTypesetter.getLineFragmentRect_usedRect_remainingRect_forStartingGlyphAtIndex_proposedRect_lineSpacing_paragraphSpacingBefore_paragraphSpacingAfter_,  # noqa: B950
            7,
            objc._C_CGFloat,
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgHasType(
            AppKit.NSTypesetter.printingAdjustmentInLayoutManager_forNominallySpacedGlyphRange_packedGlyphs_count_,  # noqa: B950
            2,
            b"n^v",
        )
        self.assertArgSizeInArg(
            AppKit.NSTypesetter.printingAdjustmentInLayoutManager_forNominallySpacedGlyphRange_packedGlyphs_count_,  # noqa: B950
            2,
            3,
        )
