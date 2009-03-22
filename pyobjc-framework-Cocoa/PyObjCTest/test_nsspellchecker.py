
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSpellChecker (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSpellChecker.sharedSpellCheckerExists)
        self.failUnlessArgIsBOOL(NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_, 3)
        self.failUnlessArgIsOut(NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_, 5)
        self.failUnlessResultIsBOOL(NSSpellChecker.setLanguage_)
        self.failUnlessResultIsBOOL(NSSpellChecker.hasLearnedWord_)


    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsBOOL(NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_, 3)
        self.failUnlessArgIsOut(NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_, 5)

if __name__ == "__main__":
    main()
