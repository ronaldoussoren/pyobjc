import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSSpellServerHelper(Foundation.NSObject):
    def spellServer_findMisspelledWordInString_language_wordCount_countOnly_(
        self, a, b, c, d, e
    ):
        return 1

    def spellServer_suggestGuessesForWord_inLanguage_(self, a, b, c):
        return 1

    def spellServer_suggestCompletionsForPartialWordRange_inString_language_(
        self, a, b, c, d
    ):
        return 1

    def spellServer_checkGrammarInString_language_details_(self, a, b, c, d):
        return 1

    def spellServer_checkString_offset_types_options_orthography_wordCount_(
        self, a, b, c, d, e, f, g
    ):
        return 1


class TestNSSpellServer(TestCase):
    def testConstants(self):
        self.assertIsInstance(Foundation.NSGrammarRange, str)
        self.assertIsInstance(Foundation.NSGrammarUserDescription, str)
        self.assertIsInstance(Foundation.NSGrammarCorrections, str)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSSpellServer.registerLanguage_byVendor_)
        self.assertResultIsBOOL(
            Foundation.NSSpellServer.isWordInUserDictionaries_caseSensitive_
        )
        self.assertArgIsBOOL(
            Foundation.NSSpellServer.isWordInUserDictionaries_caseSensitive_, 1
        )

    def testDelegate(self):
        self.assertResultHasType(
            TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_,  # noqa: B950
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_,  # noqa: B950
            3,
            b"o^" + objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_,  # noqa: B950
            4,
            objc._C_NSBOOL,
        )

        self.assertArgHasType(
            TestNSSpellServerHelper.spellServer_suggestCompletionsForPartialWordRange_inString_language_,  # noqa: B950
            1,
            Foundation.NSRange.__typestr__,
        )

        self.assertResultHasType(
            TestNSSpellServerHelper.spellServer_checkGrammarInString_language_details_,
            Foundation.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestNSSpellServerHelper.spellServer_checkGrammarInString_language_details_,
            3,
            b"o^@",
        )

    @min_os_level("10.6")
    def testDelegate10_6(self):
        self.assertArgHasType(
            TestNSSpellServerHelper.spellServer_checkString_offset_types_options_orthography_wordCount_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSSpellServerHelper.spellServer_checkString_offset_types_options_orthography_wordCount_,  # noqa: B950
            3,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSSpellServerHelper.spellServer_checkString_offset_types_options_orthography_wordCount_,  # noqa: B950
            6,
            b"o^" + objc._C_NSInteger,
        )

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("NSSpellServerDelegate")
