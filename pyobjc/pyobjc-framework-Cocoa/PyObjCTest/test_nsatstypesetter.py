
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSATSTypesetterHelper (NSATSTypesetter):
        def willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_(
                self, lineRect, glyphRange, usedRect, offset):
            return None


        def shouldBreakLineByWordBeforeCharacterAtIndex_(self, v):
            return None

        def shouldBreakLineByHyphenatingBeforeCharacterAtIndex(self, v):
            return None

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
    def testIncomplete(self):
        self.fail("Add header tests for <AppKit/NSATSTypesetter.h>")

    def testByRefArguments(self):
        o = NSATSTypesetter.alloc().init()
        m = o.lineFragmentRectForProposedRect_remainingRect_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))

        m = o.layoutParagraphAtPoint_.__metadata__()
        self.failUnless(m['arguments'][2]['type'].startswith('N^'))

        m = o.getLineFragmentRect_usedRect_forParagraphSeparatorGlyphRange_atProposedOrigin_.__metadata__()
        self.failUnless(m['arguments'][2]['type'].startswith('o^'))
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))





        o = TestNSATSTypesetterHelper.alloc().init()
        m = o.willSetLineFragmentRect_forGlyphRange_usedRect_baselineOffset_.__metadata__()
        self.failUnlessStartswith(m['arguments'][2]['type'], 'N^{')
        self.failUnlessStartswith(m['arguments'][4]['type'], 'N^{')
        self.failUnlessStartswith(m['arguments'][5]['type'], 'N^f')
        
        m = o.shouldBreakLineByWordBeforeCharacterAtIndex_.__metadata__()
        self.failUnlessEqual(m['retval']['type'], objc._C_NSBOOL)
        self.failUnlessEqual(m['arguments'][2]['type'], objc._C_UINT)

        m = o.shouldBreakLineByHyphenatingBeforeCharacterAtIndex.__metadata__()
        self.failUnlessEqual(m['retval']['type'], objc._C_NSUInteger)
        self.failUnlessEqual(m['arguments'][2]['type'], objc._C_NSUInteger)

        m = o.hyphenationFactorForGlyphAtIndex_.__metadata__()
        self.failUnlessEqual(m['retval']['type'], objc._C_FLOAT)
        self.failUnlessEqual(m['arguments'][2]['type'], objc._C_NSUInteger)

        m = o.hyphenCharacterForGlyphAtIndex_.__metadata__()
        self.failUnlessEqual(m['retval']['type'], objc._C_INT)
        self.failUnlessEqual(m['arguments'][2]['type'], objc._C_NSUInteger)

        m = o.boundingBoxForControlGlyphAtIndex_forTextContainer_proposedLineFragment_glyphPosition_characterIndex_.__metadata__()
        self.failUnlessEqual(m['retval']['type'], objc._C_INT)
        self.failUnlessEqual(m['arguments'][2]['type'], objc._C_NSUInteger)
        self.failUnlessEqual(m['arguments'][3]['type'], objc._C_ID)
        self.failUnlessStartswith(m['arguments'][4]['type'], '{')
        self.failUnlessStartswith(m['arguments'][5]['type'], '{')
        self.failUnlessStartswith(m['arguments'][6]['type'], objc._C_NSUInteger)



        m = o.characterRangeForGlyphRange_actualGlyphRange_.__metadata__()
        self.failUnlessStartswith(m['retval']['type'], '{')
        self.failUnlessStartswith(m['arguments'][2]['type'], '{')
        self.failUnlessStartswith(m['arguments'][3]['type'], 'o^{')

        m = o.glyphRangeForCharacterRange_actualCharacterRange_.__metadata__()
        self.failUnlessStartswith(m['retval']['type'], '{')
        self.failUnlessStartswith(m['arguments'][2]['type'], '{')
        self.failUnlessStartswith(m['arguments'][3]['type'], 'o^{')

        self.fail("lookup interface")
        m = o.getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_.__metadata__()
        m = o.setLineFragmentRect_forGlyphRange_usedRect_baselineOffset_.__metadata__()
        m = o.substituteGlyphsInRange_withGlyphs_.__metadata__()
        m = o.insertGlyph_atGlyphIndex_characterIndex_.__metadata__()
        m = o.deleteGlyphsInRange_.__metadata__()
        m = o.setNotShownAttribute_forGlyphRange_.__metadata__()
        m = o.setLocation_withAdvancements_forStartOfGlyphRange_.__metadata__()
        m = o.setAttachmentSize_forGlyphRange_.__metadata__()
        m = o.setBidiLevels_forGlyphRange_.__metadata__()







if __name__ == "__main__":
    main()
