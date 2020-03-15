import Foundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSLinguisticTagger(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(Foundation.NSLinguisticTagSchemeTokenType, str)
        self.assertIsInstance(Foundation.NSLinguisticTagSchemeLexicalClass, str)
        self.assertIsInstance(Foundation.NSLinguisticTagSchemeNameType, str)
        self.assertIsInstance(
            Foundation.NSLinguisticTagSchemeNameTypeOrLexicalClass, str
        )
        self.assertIsInstance(Foundation.NSLinguisticTagSchemeLemma, str)
        self.assertIsInstance(Foundation.NSLinguisticTagSchemeLanguage, str)
        self.assertIsInstance(Foundation.NSLinguisticTagSchemeScript, str)
        self.assertIsInstance(Foundation.NSLinguisticTagWord, str)
        self.assertIsInstance(Foundation.NSLinguisticTagPunctuation, str)
        self.assertIsInstance(Foundation.NSLinguisticTagWhitespace, str)
        self.assertIsInstance(Foundation.NSLinguisticTagOther, str)
        self.assertIsInstance(Foundation.NSLinguisticTagNoun, str)
        self.assertIsInstance(Foundation.NSLinguisticTagVerb, str)
        self.assertIsInstance(Foundation.NSLinguisticTagAdjective, str)
        self.assertIsInstance(Foundation.NSLinguisticTagAdverb, str)
        self.assertIsInstance(Foundation.NSLinguisticTagPronoun, str)
        self.assertIsInstance(Foundation.NSLinguisticTagDeterminer, str)
        self.assertIsInstance(Foundation.NSLinguisticTagParticle, str)
        self.assertIsInstance(Foundation.NSLinguisticTagPreposition, str)
        self.assertIsInstance(Foundation.NSLinguisticTagNumber, str)
        self.assertIsInstance(Foundation.NSLinguisticTagConjunction, str)
        self.assertIsInstance(Foundation.NSLinguisticTagInterjection, str)
        self.assertIsInstance(Foundation.NSLinguisticTagClassifier, str)
        self.assertIsInstance(Foundation.NSLinguisticTagIdiom, str)
        self.assertIsInstance(Foundation.NSLinguisticTagOtherWord, str)
        self.assertIsInstance(Foundation.NSLinguisticTagSentenceTerminator, str)
        self.assertIsInstance(Foundation.NSLinguisticTagOpenQuote, str)
        self.assertIsInstance(Foundation.NSLinguisticTagCloseQuote, str)
        self.assertIsInstance(Foundation.NSLinguisticTagOpenParenthesis, str)
        self.assertIsInstance(Foundation.NSLinguisticTagCloseParenthesis, str)
        self.assertIsInstance(Foundation.NSLinguisticTagWordJoiner, str)
        self.assertIsInstance(Foundation.NSLinguisticTagDash, str)
        self.assertIsInstance(Foundation.NSLinguisticTagOtherPunctuation, str)
        self.assertIsInstance(Foundation.NSLinguisticTagParagraphBreak, str)
        self.assertIsInstance(Foundation.NSLinguisticTagOtherWhitespace, str)
        self.assertIsInstance(Foundation.NSLinguisticTagPersonalName, str)
        self.assertIsInstance(Foundation.NSLinguisticTagPlaceName, str)
        self.assertIsInstance(Foundation.NSLinguisticTagOrganizationName, str)

        self.assertEqual(Foundation.NSLinguisticTaggerOmitWords, 1 << 0)
        self.assertEqual(Foundation.NSLinguisticTaggerOmitPunctuation, 1 << 1)
        self.assertEqual(Foundation.NSLinguisticTaggerOmitWhitespace, 1 << 2)
        self.assertEqual(Foundation.NSLinguisticTaggerOmitOther, 1 << 3)
        self.assertEqual(Foundation.NSLinguisticTaggerJoinNames, 1 << 4)

        self.assertEqual(Foundation.NSLinguisticTaggerUnitWord, 0)
        self.assertEqual(Foundation.NSLinguisticTaggerUnitSentence, 1)
        self.assertEqual(Foundation.NSLinguisticTaggerUnitParagraph, 2)
        self.assertEqual(Foundation.NSLinguisticTaggerUnitDocument, 3)

    @min_os_level("10.7")
    def testMethods(self):
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.orthographyAtIndex_effectiveRange_,
            1,
            b"o^" + Foundation.NSRange.__typestr__,
        )

        self.assertArgIsBlock(
            Foundation.NSLinguisticTagger.enumerateTagsInRange_scheme_options_usingBlock_,
            3,
            b"v@"
            + Foundation.NSRange.__typestr__
            + Foundation.NSRange.__typestr__
            + b"o^"
            + objc._C_NSBOOL,
        )

        self.assertArgHasType(
            Foundation.NSLinguisticTagger.tagAtIndex_scheme_tokenRange_sentenceRange_,
            2,
            b"o^" + Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.tagAtIndex_scheme_tokenRange_sentenceRange_,
            3,
            b"o^" + Foundation.NSRange.__typestr__,
        )

        self.assertArgHasType(
            Foundation.NSLinguisticTagger.tagsInRange_scheme_options_tokenRanges_,
            3,
            b"o^@",
        )

        self.assertArgHasType(
            Foundation.NSLinguisticTagger.possibleTagsAtIndex_scheme_tokenRange_sentenceRange_scores_,  # noqa: B950
            2,
            b"o^" + Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.possibleTagsAtIndex_scheme_tokenRange_sentenceRange_scores_,  # noqa: B950
            3,
            b"o^" + Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.possibleTagsAtIndex_scheme_tokenRange_sentenceRange_scores_,  # noqa: B950
            4,
            b"o^@",
        )

        self.assertArgIsOut(
            Foundation.NSString.linguisticTagsInRange_scheme_options_orthography_tokenRanges_,  # noqa: B950
            4,
        )

        self.assertArgIsBlock(
            Foundation.NSString.enumerateLinguisticTagsInRange_scheme_options_orthography_usingBlock_,  # noqa: B950
            4,
            b"v@"
            + Foundation.NSRange.__typestr__
            + Foundation.NSRange.__typestr__
            + b"o^"
            + objc._C_NSBOOL,
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.enumerateTagsInRange_unit_scheme_options_usingBlock_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            Foundation.NSLinguisticTagger.enumerateTagsInRange_unit_scheme_options_usingBlock_,
            4,
            b"v@" + Foundation.NSRange.__typestr__ + b"o^Z",
        )
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.tagAtIndex_unit_scheme_tokenRange_,
            3,
            b"o^" + Foundation.NSRange.__typestr__,
        )

        self.assertArgHasType(
            Foundation.NSLinguisticTagger.tagsInRange_unit_scheme_options_tokenRanges_,
            0,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsOut(
            Foundation.NSLinguisticTagger.tagsInRange_unit_scheme_options_tokenRanges_,
            4,
        )
        self.assertArgIsOut(
            Foundation.NSLinguisticTagger.tagForString_atIndex_unit_scheme_orthography_tokenRange_,  # noqa: B950
            5,
        )
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.tagsForString_range_unit_scheme_options_orthography_tokenRanges_,  # noqa: B950
            1,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsOut(
            Foundation.NSLinguisticTagger.tagsForString_range_unit_scheme_options_orthography_tokenRanges_,  # noqa: B950
            6,
        )
        self.assertArgHasType(
            Foundation.NSLinguisticTagger.enumerateTagsForString_range_unit_scheme_options_orthography_usingBlock_,  # noqa: B950
            1,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            Foundation.NSLinguisticTagger.enumerateTagsForString_range_unit_scheme_options_orthography_usingBlock_,  # noqa: B950
            6,
            b"v@" + Foundation.NSRange.__typestr__ + b"o^Z",
        )
