
from PyObjCTools.TestSupport import *
from AppKit import *


class TestNSATSTypesetterHelper (NSATSTypesetter):
    def willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_(
            self, lineRect, glyphRange, usedRect, offset):
        return None


    def shouldBreakLineByWordBeforeCharacterAtIndex_(self, v):
        return None

    def shouldBreakLineByHyphenatingBeforeCharacterAtIndex_(self, v):
        return True

    def hyphenationFactorForGlyphAtIndex_(self, v):
        return None

    def hyphenCharacterForGlyphAtIndex_(self, v):
        return None

    def boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_(self, v, v2, v3, v4, v5):
        return None

    def characterRangeForGlyphRange_actualGlyphRange_(self, v1, v2):
        pass

    def glyphRangeForCharacterRange_actualCharacterRange_(self, v1, v2):
        pass

    def getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_(self, v1, v2, v3, v4, v5):
        pass

    def setLineFragmentRect_forGlyphRange_usedRect_baselineOffset_(self, v1, v2, v3, v4):
        pass

    def substituteGlyphsInRange_withGlyphs_(self, v1, v2):
        pass

    def insertGlyph_atGlyphIndex_characterIndex_(self, v1, v2, v3):
        pass

    def deleteGlyphsInRange_(self, v1):
        pass

    def setNotShownAttribute_forGlyphRange_(self, v1, v2):
        pass

    def setLocation_withAdvancements_forStartOfGlyphRange_(self, v1, v2, v3):
        pass

    def setAttachmentSize_forGlyphRange_(self, v1, v2):
        pass

    def setBidiLevels_forGlyphRange_(self, v1, v2):
        pass


class TestNSATSTypesetter (TestCase):
    def testByRefArguments(self):
        self.assertArgIsOut(NSATSTypesetter.lineFragmentRectForProposedRect_remainingRect_, 1)
        self.assertArgIsInOut(NSATSTypesetter.layoutParagraphAtPoint_, 0)
        self.assertArgIsOut(NSATSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_, 0)
        self.assertArgIsOut(NSATSTypesetter.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_, 1)

        o = TestNSATSTypesetterHelper.alloc().init()
        m = o.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_.__metadata__()
        self.assertStartswith(m['arguments'][2]['type'], b'N^{')
        self.assertStartswith(m['arguments'][4]['type'], b'N^{')
        self.assertStartswith(m['arguments'][5]['type'], b'N^' + objc._C_CGFloat)

        m = o.shouldBreakLineByWordBeforeCharacterAtIndex_.__metadata__()
        self.assertEqual(m['retval']['type'], objc._C_NSBOOL)
        self.assertEqual(m['arguments'][2]['type'], objc._C_NSUInteger)

        m = o.shouldBreakLineByHyphenatingBeforeCharacterAtIndex_.__metadata__()
        self.assertEqual(m['retval']['type'], objc._C_NSBOOL)
        self.assertEqual(m['arguments'][2]['type'], objc._C_NSUInteger)

        m = o.hyphenationFactorForGlyphAtIndex_.__metadata__()
        self.assertEqual(m['retval']['type'], objc._C_FLT)
        self.assertEqual(m['arguments'][2]['type'], objc._C_NSUInteger)

        m = o.glyphRangeForCharacterRange_actualCharacterRange_.__metadata__()
        self.assertStartswith(m['retval']['type'], b'{')
        self.assertStartswith(m['arguments'][2]['type'], b'{')
        self.assertStartswith(m['arguments'][3]['type'], b'o^{')

        self.assertResultIsBOOL(NSATSTypesetter.usesFontLeading)
        self.assertArgIsBOOL(NSATSTypesetter.setUsesFontLeading_, 0)
        self.assertResultIsBOOL(NSATSTypesetter.bidiProcessingEnabled)
        self.assertArgIsBOOL(NSATSTypesetter.setBidiProcessingEnabled_, 0)
        self.assertArgIsBOOL(NSATSTypesetter.setHardInvalidation_forGlyphRange_, 0)
        self.assertArgIsBOOL(NSATSTypesetter.setNotShownAttribute_forGlyphRange_, 0)
        self.assertArgIsBOOL(NSATSTypesetter.setDrawsOutsideLineFragment_forGlyphRange_, 0)


        self.assertArgIsIn(NSATSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1)
        self.assertArgSizeInArg(NSATSTypesetter.setLocation_withAdvancements_forStartOfGlyphRange_, 1, 2)
        self.assertArgSizeInArg(NSATSTypesetter.setBidiLevels_forGlyphRange_, 0, 1)
        self.assertArgSizeInArg(NSATSTypesetter.setBidiLevels_forGlyphRange_, 0, 1)

        self.assertArgIsIn(NSATSTypesetter.substituteGlyphsInRange_withGlyphs_, 1)
        self.assertArgSizeInArg(NSATSTypesetter.substituteGlyphsInRange_withGlyphs_, 1, 0)

    def testSubclassProtocols(self):
        self.assertResultIsBOOL(TestNSATSTypesetterHelper.shouldBreakLineByWordBeforeCharacterAtIndex_)
        self.assertResultIsBOOL(TestNSATSTypesetterHelper.shouldBreakLineByHyphenatingBeforeCharacterAtIndex_)

        self.assertResultHasType(TestNSATSTypesetterHelper.characterRangeForGlyphRange_actualGlyphRange_,
                NSRange.__typestr__)
        self.assertArgHasType(TestNSATSTypesetterHelper.characterRangeForGlyphRange_actualGlyphRange_,
                0, NSRange.__typestr__)
        self.assertArgHasType(TestNSATSTypesetterHelper.characterRangeForGlyphRange_actualGlyphRange_,
                1, b'o^' + NSRange.__typestr__)

        self.assertArgIsBOOL(TestNSATSTypesetterHelper.setNotShownAttribute_forGlyphRange_, 0)
        self.assertArgHasType(TestNSATSTypesetterHelper.setNotShownAttribute_forGlyphRange_, 1, NSRange.__typestr__)



if __name__ == "__main__":
    main()
