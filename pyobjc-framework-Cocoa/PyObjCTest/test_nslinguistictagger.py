from PyObjCTools.TestSupport import *
from Foundation import *

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

        self.assertEqual(NSLinguisticTaggerUnitWord, 0)
        self.assertEqual(NSLinguisticTaggerUnitSentence, 1)
        self.assertEqual(NSLinguisticTaggerUnitParagraph, 2)
        self.assertEqual(NSLinguisticTaggerUnitDocument, 3)



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

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgHasType(NSLinguisticTagger.enumerateTagsInRange_unit_scheme_options_usingBlock_, 0, NSRange.__typestr__)
        self.assertArgIsBlock(NSLinguisticTagger.enumerateTagsInRange_unit_scheme_options_usingBlock_, 4, b'v@' + NSRange.__typestr__ + b'o^Z')
        self.assertArgHasType(NSLinguisticTagger.tagAtIndex_unit_scheme_tokenRange_, 3, b'o^' + NSRange.__typestr__)


        self.assertArgHasType(NSLinguisticTagger.tagsInRange_unit_scheme_options_tokenRanges_, 0, NSRange.__typestr__)
        self.assertArgIsOut(NSLinguisticTagger.tagsInRange_unit_scheme_options_tokenRanges_, 4)
        self.assertArgIsOut(NSLinguisticTagger.tagForString_atIndex_unit_scheme_orthography_tokenRange_, 5)
        self.assertArgHasType(NSLinguisticTagger.tagsForString_range_unit_scheme_options_orthography_tokenRanges_, 1, NSRange.__typestr__)
        self.assertArgIsOut(NSLinguisticTagger.tagsForString_range_unit_scheme_options_orthography_tokenRanges_, 6)
        self.assertArgHasType(NSLinguisticTagger.enumerateTagsForString_range_unit_scheme_options_orthography_usingBlock_, 1, NSRange.__typestr__)
        self.assertArgIsBlock(NSLinguisticTagger.enumerateTagsForString_range_unit_scheme_options_orthography_usingBlock_, 6, b'v@' + NSRange.__typestr__ + b'o^Z')


if __name__ == "__main__":
    main()
