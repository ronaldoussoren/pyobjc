from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestStringTokenizer (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFStringTokenizerRef)

    def testFunctions(self):
        s = u"Spring eens over een boom"
        v = CFStringTokenizerCopyBestStringLanguage(s, (0, len(s)))
        self.assertEqual(v, 'nl')

        v = CFStringTokenizerGetTypeID()
        self.assertIsInstance(v, (int, long))
        self.assertResultIsCFRetained(CFStringTokenizerCreate)
        tok = CFStringTokenizerCreate(
                None, s, (0, len(s)), kCFStringTokenizerUnitWord, 
                CFLocaleCopyCurrent())
        self.assertIsInstance(tok, CFStringTokenizerRef)
        v = CFStringTokenizerGoToTokenAtIndex(tok, 2)
        self.assertEqual(v, kCFStringTokenizerTokenNormal)

        v = CFStringTokenizerGetCurrentTokenRange(tok)
        self.assertEqual(v, CFRange(0, 6))

        v = CFStringTokenizerAdvanceToNextToken(tok)
        self.assertEqual(v, kCFStringTokenizerTokenNormal)

        v = CFStringTokenizerGetCurrentTokenRange(tok)
        self.assertEqual(v, CFRange(7, 4))

        self.assertResultIsCFRetained(CFStringTokenizerCopyCurrentTokenAttribute)
        v = CFStringTokenizerCopyCurrentTokenAttribute(tok, kCFStringTokenizerAttributeLanguage)
        self.assertIs(v, None)
        s = u"A dog jumped over a log. And then some more."
        CFStringTokenizerSetString(tok, s, (0, len(s)))

        subref = []
        idx, ranges = CFStringTokenizerGetCurrentSubTokens(tok, None, 20, subref)
        self.assertEqual(idx, 0)
        self.assertEqual(ranges, ())
        self.assertEqual(subref, [])



    def testConstants(self):

        self.assertEqual(kCFStringTokenizerUnitWord                           , 0 )
        self.assertEqual(kCFStringTokenizerUnitSentence                       , 1 )
        self.assertEqual(kCFStringTokenizerUnitParagraph                      , 2 )
        self.assertEqual(kCFStringTokenizerUnitLineBreak                      , 3 )
        self.assertEqual(kCFStringTokenizerUnitWordBoundary                   , 4 )
        self.assertEqual(kCFStringTokenizerAttributeLatinTranscription        , 1L << 16 )
        self.assertEqual(kCFStringTokenizerAttributeLanguage                  , 1L << 17 )
        self.assertEqual(kCFStringTokenizerTokenNone                          , 0 )
        self.assertEqual(kCFStringTokenizerTokenNormal                        , 1 )
        self.assertEqual(kCFStringTokenizerTokenHasSubTokensMask              , 1L << 1 )
        self.assertEqual(kCFStringTokenizerTokenHasDerivedSubTokensMask       , 1L << 2 )
        self.assertEqual(kCFStringTokenizerTokenHasHasNumbersMask             , 1L << 3 )
        self.assertEqual(kCFStringTokenizerTokenHasNonLettersMask             , 1L << 4 )
        self.assertEqual(kCFStringTokenizerTokenIsCJWordMask                  , 1L << 5 )
if __name__ == "__main__":
    main()
