from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import NaturalLanguage

    class TestNLTagScheme (TestCase):
        def test_constants(self):
            self.assertIsInstance(NaturalLanguage.NLTagSchemeTokenType, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagSchemeLexicalClass, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagSchemeNameType, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagSchemeNameTypeOrLexicalClass, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagSchemeLemma, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagSchemeLanguage, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagSchemeScript, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagWord, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagPunctuation, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagWhitespace, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagOther, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagNoun, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagVerb, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagAdjective, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagAdverb, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagPronoun, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagDeterminer, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagParticle, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagPreposition, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagNumber, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagConjunction, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagInterjection, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagClassifier, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagIdiom, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagOtherWord, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagSentenceTerminator, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagOpenQuote, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagCloseQuote, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagOpenParenthesis, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagCloseParenthesis, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagWordJoiner, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagDash, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagOtherPunctuation, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagParagraphBreak, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagOtherWhitespace, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagPersonalName, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagPlaceName, unicode)
            self.assertIsInstance(NaturalLanguage.NLTagOrganizationName, unicode)



if __name__ == "__main__":
    main()
