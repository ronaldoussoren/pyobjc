from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSSpellServerHelper (NSObject):
    def spellServer_findMisspelledWordInString_language_wordCount_countOnly_(self, a, b, c, d, e): return 1
    def spellServer_suggestGuessesForWord_inLanguage_(self, a, b, c): return 1
    def spellServer_suggestCompletionsForPartialWordRange_inString_language_(self, a, b, c, d): return 1
    def spellServer_checkGrammarInString_language_details_(self, a, b, c, d): return 1



class TestNSSpellServer (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSGrammarRange, unicode)
        self.failUnlessIsInstance(NSGrammarUserDescription, unicode)
        self.failUnlessIsInstance(NSGrammarCorrections, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSpellServer.registerLanguage_byVendor_)
        self.failUnlessResultIsBOOL(NSSpellServer.isWordInUserDictionaries_caseSensitive_)
        self.failUnlessArgIsBOOL(NSSpellServer.isWordInUserDictionaries_caseSensitive_, 1)

    def testDelegate(self):
        self.failUnlessResultHasType(TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_, 3, 'o^' + objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSSpellServerHelper.spellServer_findMisspelledWordInString_language_wordCount_countOnly_, 4, objc._C_NSBOOL)

        self.failUnlessArgHasType(TestNSSpellServerHelper.spellServer_suggestCompletionsForPartialWordRange_inString_language_, 1, NSRange.__typestr__)

        self.failUnlessResultHasType(TestNSSpellServerHelper.spellServer_checkGrammarInString_language_details_, NSRange.__typestr__)
        self.failUnlessArgHasType(TestNSSpellServerHelper.spellServer_checkGrammarInString_language_details_, 3, 'o^@')

if __name__ == "__main__":
    main()
