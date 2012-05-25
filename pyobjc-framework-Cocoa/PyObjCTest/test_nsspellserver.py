from Foundation import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class TestNSSpellServerHelper (NSObject):
    def spellServer_findMisspelledWordInString_language_wordCount_countOnly_(self, a, b, c, d, e): return 1
    def spellServer_suggestGuessesForWord_inLanguage_(self, a, b, c): return 1
    def spellServer_suggestCompletionsForPartialWordRange_inString_language_(self, a, b, c, d): return 1
    def spellServer_checkGrammarInString_language_details_(self, a, b, c, d): return 1

    def spellServer_checkString_offset_types_options_orthography_wordCount_(self, a, b, c, d, e, f, g): return 1



class TestNSSpellServer (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSGrammarRange, unicode)
        self.assertIsInstance(NSGrammarUserDescription, unicode)
        self.assertIsInstance(NSGrammarCorrections, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(NSSpellServer.registerLanguage_byVendor_)
        self.assertResultIsBOOL(NSSpellServer.isWordInUserDictionaries_caseSensitive_)
        self.assertArgIsBOOL(NSSpellServer.isWordInUserDictionaries_caseSensitive_, 1)

    def testDelegate(self):
        self.assertResultHasType(TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_, NSRange.__typestr__)
        self.assertArgHasType(TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_, 3, b'o^' + objc._C_NSInteger)
        self.assertArgHasType(TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_, 4, objc._C_NSBOOL)

        self.assertArgHasType(TestNSSpellServerHelper.spellServer_suggestCompletionsForPartialWordRange_inString_language_, 1, NSRange.__typestr__)

        self.assertResultHasType(TestNSSpellServerHelper.spellServer_checkGrammarInString_language_details_, NSRange.__typestr__)
        self.assertArgHasType(TestNSSpellServerHelper.spellServer_checkGrammarInString_language_details_, 3, b'o^@')

    @min_os_level('10.6')
    def testDelegate10_6(self):
        self.assertArgHasType(TestNSSpellServerHelper.spellServer_checkString_offset_types_options_orthography_wordCount_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestNSSpellServerHelper.spellServer_checkString_offset_types_options_orthography_wordCount_, 3, objc._C_NSInteger)
        self.assertArgHasType(TestNSSpellServerHelper.spellServer_checkString_offset_types_options_orthography_wordCount_, 6, b'o^' + objc._C_NSInteger)

if __name__ == "__main__":
    main()
