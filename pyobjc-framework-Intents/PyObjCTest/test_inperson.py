from PyObjCTools.TestSupport import TestCase, min_os_level
import Intents


class TestINPerson(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Intents.INPersonSuggestionType)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(Intents.INPersonSuggestionTypeNone, 0)
        self.assertEqual(Intents.INPersonSuggestionTypeSocialProfile, 1)
        self.assertEqual(Intents.INPersonSuggestionTypeInstantMessageAddress, 2)

    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(Intents.INPerson.isContactSuggestion)
