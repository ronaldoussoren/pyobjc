from PyObjCTools.TestSupport import TestCase, min_os_level

import NaturalLanguage


class TestNLScript(TestCase):
    @min_os_level("14.0")
    def test_constants(self):
        self.assertIsTypedEnum(NaturalLanguage.NLScript, str)

        self.assertIsInstance(NaturalLanguage.NLScriptUndetermined, str)
        self.assertIsInstance(NaturalLanguage.NLScriptArabic, str)
        self.assertIsInstance(NaturalLanguage.NLScriptArmenian, str)
        self.assertIsInstance(NaturalLanguage.NLScriptBengali, str)
        self.assertIsInstance(NaturalLanguage.NLScriptCanadianAboriginalSyllabics, str)
        self.assertIsInstance(NaturalLanguage.NLScriptCherokee, str)
        self.assertIsInstance(NaturalLanguage.NLScriptCyrillic, str)
        self.assertIsInstance(NaturalLanguage.NLScriptDevanagari, str)
        self.assertIsInstance(NaturalLanguage.NLScriptEthiopic, str)
        self.assertIsInstance(NaturalLanguage.NLScriptGeorgian, str)
        self.assertIsInstance(NaturalLanguage.NLScriptGreek, str)
        self.assertIsInstance(NaturalLanguage.NLScriptGujarati, str)
        self.assertIsInstance(NaturalLanguage.NLScriptGurmukhi, str)
        self.assertIsInstance(NaturalLanguage.NLScriptHebrew, str)
        self.assertIsInstance(NaturalLanguage.NLScriptJapanese, str)
        self.assertIsInstance(NaturalLanguage.NLScriptKannada, str)
        self.assertIsInstance(NaturalLanguage.NLScriptKhmer, str)
        self.assertIsInstance(NaturalLanguage.NLScriptKorean, str)
        self.assertIsInstance(NaturalLanguage.NLScriptLao, str)
        self.assertIsInstance(NaturalLanguage.NLScriptLatin, str)
        self.assertIsInstance(NaturalLanguage.NLScriptMalayalam, str)
        self.assertIsInstance(NaturalLanguage.NLScriptMongolian, str)
        self.assertIsInstance(NaturalLanguage.NLScriptMyanmar, str)
        self.assertIsInstance(NaturalLanguage.NLScriptOriya, str)
        self.assertIsInstance(NaturalLanguage.NLScriptSimplifiedChinese, str)
        self.assertIsInstance(NaturalLanguage.NLScriptSinhala, str)
        self.assertIsInstance(NaturalLanguage.NLScriptTamil, str)
        self.assertIsInstance(NaturalLanguage.NLScriptTelugu, str)
        self.assertIsInstance(NaturalLanguage.NLScriptThai, str)
        self.assertIsInstance(NaturalLanguage.NLScriptTibetan, str)
        self.assertIsInstance(NaturalLanguage.NLScriptTraditionalChinese, str)
