from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSLinguisticTagger (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(NSLinguisticTagSchemeTokenType, unicode)
        self.assertIsInstance(NSLinguisticTagSchemeLexicalClass, unicode)
        self.assertIsInstance(NSLinguisticTagSchemeNameType, unicode)
        self.assertIsInstance(NSLinguisticTagSchemeNameTypeOrLexicalClass, unicode)
        self.assertIsInstance(NSLinguisticTagSchemeLemma, unicode)
        self.assertIsInstance(NSLinguisticTagSchemeLanguage, unicode)
        self.assertIsInstance(NSLinguisticTagSchemeScript, unicode)
        self.assertIsInstance(NSLinguisticTagWord, unicode)
        self.assertIsInstance(NSLinguisticTagPunctuation, unicode)
        self.assertIsInstance(NSLinguisticTagWhitespace, unicode)
        self.assertIsInstance(NSLinguisticTagOther, unicode)
        self.assertIsInstance(NSLinguisticTagNoun, unicode)
        self.assertIsInstance(NSLinguisticTagVerb, unicode)
        self.assertIsInstance(NSLinguisticTagAdjective, unicode)
        self.assertIsInstance(NSLinguisticTagAdverb, unicode)
        self.assertIsInstance(NSLinguisticTagPronoun, unicode)
        self.assertIsInstance(NSLinguisticTagDeterminer, unicode)
        self.assertIsInstance(NSLinguisticTagParticle, unicode)
        self.assertIsInstance(NSLinguisticTagPreposition, unicode)
        self.assertIsInstance(NSLinguisticTagNumber, unicode)
        self.assertIsInstance(NSLinguisticTagConjunction, unicode)
        self.assertIsInstance(NSLinguisticTagInterjection, unicode)
        self.assertIsInstance(NSLinguisticTagClassifier, unicode)
        self.assertIsInstance(NSLinguisticTagIdiom, unicode)
        self.assertIsInstance(NSLinguisticTagOtherWord, unicode)
        self.assertIsInstance(NSLinguisticTagSentenceTerminator, unicode)
        self.assertIsInstance(NSLinguisticTagOpenQuote, unicode)
        self.assertIsInstance(NSLinguisticTagCloseQuote, unicode)
        self.assertIsInstance(NSLinguisticTagOpenParenthesis, unicode)
        self.assertIsInstance(NSLinguisticTagCloseParenthesis, unicode)
        self.assertIsInstance(NSLinguisticTagWordJoiner, unicode)
        self.assertIsInstance(NSLinguisticTagDash, unicode)
        self.assertIsInstance(NSLinguisticTagOtherPunctuation, unicode)
        self.assertIsInstance(NSLinguisticTagParagraphBreak, unicode)
        self.assertIsInstance(NSLinguisticTagOtherWhitespace, unicode)
        self.assertIsInstance(NSLinguisticTagPersonalName, unicode)
        self.assertIsInstance(NSLinguisticTagPlaceName, unicode)
        self.assertIsInstance(NSLinguisticTagOrganizationName, unicode)

        self.assertEqual(NSLinguisticTaggerOmitWords, 1 << 0)
        self.assertEqual(NSLinguisticTaggerOmitPunctuation, 1 << 1)
        self.assertEqual(NSLinguisticTaggerOmitWhitespace, 1 << 2)
        self.assertEqual(NSLinguisticTaggerOmitOther, 1 << 3)
        self.assertEqual(NSLinguisticTaggerJoinNames, 1 << 4)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertArgHasType(NSLinguisticTagger.orthographyAtIndex_effectiveRange_,
                1, b'o^' + NSRange.__typestr__)

        self.assertArgIsBlock(NSLinguisticTagger.enumerateTagsInRange_scheme_options_usingBlock_,
                3, b'v@' + NSRange.__typestr__ + NSRange.__typestr__ + b'o^' + objc._C_NSBOOL)

        self.assertArgHasType(NSLinguisticTagger.tagAtIndex_scheme_tokenRange_sentenceRange_,
                2, b'o^' + NSRange.__typestr__)
        self.assertArgHasType(NSLinguisticTagger.tagAtIndex_scheme_tokenRange_sentenceRange_,
                3, b'o^' + NSRange.__typestr__)

        self.assertArgHasType(NSLinguisticTagger.tagsInRange_scheme_options_tokenRanges_,
                3, b'o^@')

        self.assertArgHasType(NSLinguisticTagger.possibleTagsAtIndex_scheme_tokenRange_sentenceRange_scores_,
                2, b'o^' + NSRange.__typestr__)
        self.assertArgHasType(NSLinguisticTagger.possibleTagsAtIndex_scheme_tokenRange_sentenceRange_scores_,
                3, b'o^' + NSRange.__typestr__)
        self.assertArgHasType(NSLinguisticTagger.possibleTagsAtIndex_scheme_tokenRange_sentenceRange_scores_,
                4, b'o^@')

        self.assertArgIsOut(NSString.linguisticTagsInRange_scheme_options_orthography_tokenRanges_, 4)

        self.assertArgIsBlock(NSString.enumerateLinguisticTagsInRange_scheme_options_orthography_usingBlock_,
                4, b'v@' + NSRange.__typestr__ + NSRange.__typestr__ + b'o^' + objc._C_NSBOOL)

if __name__ == "__main__":
    main()
