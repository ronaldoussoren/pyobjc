import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMorphology(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSGrammaticalGender)
        self.assertIsEnumType(Foundation.NSGrammaticalNumber)
        self.assertIsEnumType(Foundation.NSGrammaticalPartOfSpeech)

    def test_constants(self):
        self.assertEqual(Foundation.NSGrammaticalGenderNotSet, 0)
        self.assertEqual(Foundation.NSGrammaticalGenderFeminine, 1)
        self.assertEqual(Foundation.NSGrammaticalGenderMasculine, 2)
        self.assertEqual(Foundation.NSGrammaticalGenderNeuter, 3)

        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechNotSet, 0)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechDeterminer, 1)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechPronoun, 2)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechLetter, 3)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechAdverb, 4)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechParticle, 5)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechAdjective, 6)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechAdposition, 7)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechVerb, 8)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechNoun, 9)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechConjunction, 10)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechNumeral, 11)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechInterjection, 12)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechPreposition, 13)
        self.assertEqual(Foundation.NSGrammaticalPartOfSpeechAbbreviation, 14)

        self.assertEqual(Foundation.NSGrammaticalNumberNotSet, 0)
        self.assertEqual(Foundation.NSGrammaticalNumberSingular, 1)
        self.assertEqual(Foundation.NSGrammaticalNumberZero, 2)
        self.assertEqual(Foundation.NSGrammaticalNumberPlural, 3)
        self.assertEqual(Foundation.NSGrammaticalNumberPluralTwo, 4)
        self.assertEqual(Foundation.NSGrammaticalNumberPluralFew, 5)
        self.assertEqual(Foundation.NSGrammaticalNumberPluralMany, 6)

    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Foundation.NSMorphology.setCustomPronoun_forLanguage_error_
        )
        self.assertArgIsOut(
            Foundation.NSMorphology.setCustomPronoun_forLanguage_error_, 2
        )

        self.assertResultIsBOOL(
            Foundation.NSMorphologyCustomPronoun.isSupportedForLanguage_
        )

        self.assertResultIsBOOL(Foundation.NSMorphology.isUnspecified)
