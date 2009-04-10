from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestStringTokenizer (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFStringTokenizerRef)

    def testFunctions(self):
        s = u"Spring eens over een boom"
        v = CFStringTokenizerCopyBestStringLanguage(s, (0, len(s)))
        self.assertEquals(v, 'nl')

        v = CFStringTokenizerGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

        self.failUnlessResultIsCFRetained(CFStringTokenizerCreate)
        tok = CFStringTokenizerCreate(
                None, s, (0, len(s)), kCFStringTokenizerUnitWord, 
                CFLocaleCopyCurrent())
        self.failUnless(isinstance(tok, CFStringTokenizerRef))

        v = CFStringTokenizerGoToTokenAtIndex(tok, 2)
        self.assertEquals(v, kCFStringTokenizerTokenNormal)

        v = CFStringTokenizerGetCurrentTokenRange(tok)
        self.assertEquals(v, CFRange(0, 6))

        v = CFStringTokenizerAdvanceToNextToken(tok)
        self.assertEquals(v, kCFStringTokenizerTokenNormal)

        v = CFStringTokenizerGetCurrentTokenRange(tok)
        self.assertEquals(v, CFRange(7, 4))

        self.failUnlessResultIsCFRetained(CFStringTokenizerCopyCurrentTokenAttribute)
        v = CFStringTokenizerCopyCurrentTokenAttribute(tok, kCFStringTokenizerAttributeLanguage)
        self.failUnless(v is None)


        s = u"A dog jumped over a log. And then some more."
        CFStringTokenizerSetString(tok, s, (0, len(s)))

        subref = []
        idx, ranges = CFStringTokenizerGetCurrentSubTokens(tok, None, 20, subref)
        self.assertEquals(idx, 0)
        self.assertEquals(ranges, ())
        self.assertEquals(subref, [])



    def testConstants(self):

        self.failUnless( kCFStringTokenizerUnitWord                           == 0 )
        self.failUnless( kCFStringTokenizerUnitSentence                       == 1 )
        self.failUnless( kCFStringTokenizerUnitParagraph                      == 2 )
        self.failUnless( kCFStringTokenizerUnitLineBreak                      == 3 )
        self.failUnless( kCFStringTokenizerUnitWordBoundary                   == 4 )
        self.failUnless( kCFStringTokenizerAttributeLatinTranscription        == 1L << 16 )
        self.failUnless( kCFStringTokenizerAttributeLanguage                  == 1L << 17 )

        self.failUnless( kCFStringTokenizerTokenNone                          == 0 )
        self.failUnless( kCFStringTokenizerTokenNormal                        == 1 )
        self.failUnless( kCFStringTokenizerTokenHasSubTokensMask              == 1L << 1 )
        self.failUnless( kCFStringTokenizerTokenHasDerivedSubTokensMask       == 1L << 2 )
        self.failUnless( kCFStringTokenizerTokenHasHasNumbersMask             == 1L << 3 )
        self.failUnless( kCFStringTokenizerTokenHasNonLettersMask             == 1L << 4 )
        self.failUnless( kCFStringTokenizerTokenIsCJWordMask                  == 1L << 5 )


if __name__ == "__main__":
    main()
