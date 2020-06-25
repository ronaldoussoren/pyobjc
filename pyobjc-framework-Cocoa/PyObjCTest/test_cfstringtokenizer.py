import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestStringTokenizer(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFStringTokenizerRef)

    def testFunctions(self):
        s = "Spring eens over een boom"
        v = CoreFoundation.CFStringTokenizerCopyBestStringLanguage(s, (0, len(s)))
        self.assertEqual(v, "nl")

        v = CoreFoundation.CFStringTokenizerGetTypeID()
        self.assertIsInstance(v, int)
        self.assertResultIsCFRetained(CoreFoundation.CFStringTokenizerCreate)
        tok = CoreFoundation.CFStringTokenizerCreate(
            None,
            s,
            (0, len(s)),
            CoreFoundation.kCFStringTokenizerUnitWord,
            CoreFoundation.CFLocaleCopyCurrent(),
        )
        self.assertIsInstance(tok, CoreFoundation.CFStringTokenizerRef)
        v = CoreFoundation.CFStringTokenizerGoToTokenAtIndex(tok, 2)
        self.assertEqual(v, CoreFoundation.kCFStringTokenizerTokenNormal)

        v = CoreFoundation.CFStringTokenizerGetCurrentTokenRange(tok)
        self.assertEqual(v, CoreFoundation.CFRange(0, 6))

        v = CoreFoundation.CFStringTokenizerAdvanceToNextToken(tok)
        self.assertEqual(v, CoreFoundation.kCFStringTokenizerTokenNormal)

        v = CoreFoundation.CFStringTokenizerGetCurrentTokenRange(tok)
        self.assertEqual(v, CoreFoundation.CFRange(7, 4))

        self.assertResultIsCFRetained(
            CoreFoundation.CFStringTokenizerCopyCurrentTokenAttribute
        )
        v = CoreFoundation.CFStringTokenizerCopyCurrentTokenAttribute(
            tok, CoreFoundation.kCFStringTokenizerAttributeLanguage
        )
        # self.assertIs(v, None)

        s = "A dog jumped over a log. And then some more."
        CoreFoundation.CFStringTokenizerSetString(tok, s, (0, len(s)))

        subref = []
        idx, ranges = CoreFoundation.CFStringTokenizerGetCurrentSubTokens(
            tok, None, 20, subref
        )
        self.assertEqual(idx, 0)
        self.assertEqual(ranges, ())
        self.assertEqual(subref, [])

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFStringTokenizerUnitWord, 0)
        self.assertEqual(CoreFoundation.kCFStringTokenizerUnitSentence, 1)
        self.assertEqual(CoreFoundation.kCFStringTokenizerUnitParagraph, 2)
        self.assertEqual(CoreFoundation.kCFStringTokenizerUnitLineBreak, 3)
        self.assertEqual(CoreFoundation.kCFStringTokenizerUnitWordBoundary, 4)
        self.assertEqual(
            CoreFoundation.kCFStringTokenizerAttributeLatinTranscription, 1 << 16
        )
        self.assertEqual(CoreFoundation.kCFStringTokenizerAttributeLanguage, 1 << 17)
        self.assertEqual(CoreFoundation.kCFStringTokenizerTokenNone, 0)
        self.assertEqual(CoreFoundation.kCFStringTokenizerTokenNormal, 1)
        self.assertEqual(CoreFoundation.kCFStringTokenizerTokenHasSubTokensMask, 1 << 1)
        self.assertEqual(
            CoreFoundation.kCFStringTokenizerTokenHasDerivedSubTokensMask, 1 << 2
        )
        self.assertEqual(
            CoreFoundation.kCFStringTokenizerTokenHasHasNumbersMask, 1 << 3
        )
        self.assertEqual(
            CoreFoundation.kCFStringTokenizerTokenHasNonLettersMask, 1 << 4
        )
        self.assertEqual(CoreFoundation.kCFStringTokenizerTokenIsCJWordMask, 1 << 5)
