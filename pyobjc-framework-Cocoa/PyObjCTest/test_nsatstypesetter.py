
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

        #m = o.hyphenCharacterForGlyphAtIndex_.__metadata__()
        #self.assertEqual(m['retval']['type'], objc._C_UINT)
        #self.assertEqual(m['arguments'][2]['type'], objc._C_NSUInteger)

        #m = o.boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_.__metadata__()
        #self.assertEqual(m['retval']['type'], NSRect.__typestr__)
        #self.assertEqual(m['arguments'][2]['type'], objc._C_NSUInteger)
        #self.assertEqual(m['arguments'][3]['type'], objc._C_ID)
        #self.assertStartswith(m['arguments'][4]['type'], '{')
        #self.assertStartswith(m['arguments'][5]['type'], '{')
        #self.assertStartswith(m['arguments'][6]['type'], objc._C_NSUInteger)



        #m = o.characterRangeForGlyphRange_actualGlyphRange_.__metadata__()
        #self.assertStartswith(m['retval']['type'], '{')
        #self.assertStartswith(m['arguments'][2]['type'], '{')
        #self.assertStartswith(m['arguments'][3]['type'], 'o^{')

        m = o.glyphRangeForCharacterRange_actualCharacterRange_.__metadata__()
        self.assertStartswith(m['retval']['type'], b'{')
        self.assertStartswith(m['arguments'][2]['type'], b'{')
        self.assertStartswith(m['arguments'][3]['type'], b'o^{')

        #m = o.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_.__metadata__()
        #self.assertEqual(m['retval']['type'], objc._C_NSUInteger)
        #self.assertEqual(m['arguments'][2]['type'], NSRange.__typestr__)
        #self.assertEqual(m['arguments'][3]['type'], 'o^S')
        #self.assertEqual(m['arguments'][3]['c_array_length_in_arg'], 2)
        #self.assertEqual(m['arguments'][4]['type'], objc._C_OUT + objc._C_PTR + objc._C_NSUInteger)
        #self.assertEqual(m['arguments'][4]['c_array_length_in_arg'], 2)
        #m = o.setLineFragmentRect_forGlyphRange_usedRect_baselineOffset_.__metadata__()
        #m = o.substituteGlyphsInRange_withGlyphs_.__metadata__()
        #m = o.insertGlyph_atGlyphIndex_characterIndex_.__metadata__()
        #m = o.deleteGlyphsInRange_.__metadata__()
        #m = o.setNotShownAttribute_forGlyphRange_.__metadata__()
        #m = o.setLocation_withAdvancements_forStartOfGlyphRange_.__metadata__()
        #m = o.setAttachmentSize_forGlyphRange_.__metadata__()
        #m = o.setBidiLevels_forGlyphRange_.__metadata__()


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

    def testSubclassProtocols(self):
        self.assertResultIsBOOL(TestNSATSTypesetterHelper.shouldBreakLineByWordBeforeCharacterAtIndex_)
        self.assertResultIsBOOL(TestNSATSTypesetterHelper.shouldBreakLineByHyphenatingBeforeCharacterAtIndex_)



if __name__ == "__main__":
    main()
