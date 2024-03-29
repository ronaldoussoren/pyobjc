from PyObjCTools.TestSupport import TestCase, min_os_level
import NaturalLanguage


class TestNLTagScheme(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(NaturalLanguage.NLTagScheme, str)
        self.assertIsTypedEnum(NaturalLanguage.NLTag, str)
        self.assertIsTypedEnum(NaturalLanguage.NLLanguage, str)

    def test_constants(self):
        self.assertIsInstance(NaturalLanguage.NLTagSchemeTokenType, str)
        self.assertIsInstance(NaturalLanguage.NLTagSchemeLexicalClass, str)
        self.assertIsInstance(NaturalLanguage.NLTagSchemeNameType, str)
        self.assertIsInstance(NaturalLanguage.NLTagSchemeNameTypeOrLexicalClass, str)
        self.assertIsInstance(NaturalLanguage.NLTagSchemeLemma, str)
        self.assertIsInstance(NaturalLanguage.NLTagSchemeLanguage, str)
        self.assertIsInstance(NaturalLanguage.NLTagSchemeScript, str)
        self.assertIsInstance(NaturalLanguage.NLTagWord, str)
        self.assertIsInstance(NaturalLanguage.NLTagPunctuation, str)
        self.assertIsInstance(NaturalLanguage.NLTagWhitespace, str)
        self.assertIsInstance(NaturalLanguage.NLTagOther, str)
        self.assertIsInstance(NaturalLanguage.NLTagNoun, str)
        self.assertIsInstance(NaturalLanguage.NLTagVerb, str)
        self.assertIsInstance(NaturalLanguage.NLTagAdjective, str)
        self.assertIsInstance(NaturalLanguage.NLTagAdverb, str)
        self.assertIsInstance(NaturalLanguage.NLTagPronoun, str)
        self.assertIsInstance(NaturalLanguage.NLTagDeterminer, str)
        self.assertIsInstance(NaturalLanguage.NLTagParticle, str)
        self.assertIsInstance(NaturalLanguage.NLTagPreposition, str)
        self.assertIsInstance(NaturalLanguage.NLTagNumber, str)
        self.assertIsInstance(NaturalLanguage.NLTagConjunction, str)
        self.assertIsInstance(NaturalLanguage.NLTagInterjection, str)
        self.assertIsInstance(NaturalLanguage.NLTagClassifier, str)
        self.assertIsInstance(NaturalLanguage.NLTagIdiom, str)
        self.assertIsInstance(NaturalLanguage.NLTagOtherWord, str)
        self.assertIsInstance(NaturalLanguage.NLTagSentenceTerminator, str)
        self.assertIsInstance(NaturalLanguage.NLTagOpenQuote, str)
        self.assertIsInstance(NaturalLanguage.NLTagCloseQuote, str)
        self.assertIsInstance(NaturalLanguage.NLTagOpenParenthesis, str)
        self.assertIsInstance(NaturalLanguage.NLTagCloseParenthesis, str)
        self.assertIsInstance(NaturalLanguage.NLTagWordJoiner, str)
        self.assertIsInstance(NaturalLanguage.NLTagDash, str)
        self.assertIsInstance(NaturalLanguage.NLTagOtherPunctuation, str)
        self.assertIsInstance(NaturalLanguage.NLTagParagraphBreak, str)
        self.assertIsInstance(NaturalLanguage.NLTagOtherWhitespace, str)
        self.assertIsInstance(NaturalLanguage.NLTagPersonalName, str)
        self.assertIsInstance(NaturalLanguage.NLTagPlaceName, str)
        self.assertIsInstance(NaturalLanguage.NLTagOrganizationName, str)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(NaturalLanguage.NLTagSchemeSentimentScore, str)
