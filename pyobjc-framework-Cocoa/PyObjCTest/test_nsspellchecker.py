
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSpellChecker (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSpellChecker.sharedSpellCheckerExists)
        self.failUnlessArgIsBOOL(NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_, 3)
        self.failUnlessArgIsOut(NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_, 5)
        self.failUnlessResultIsBOOL(NSSpellChecker.setLanguage_)
    
        self.failUnlessArgHasType(NSSpellChecker.completionsForPartialWordRange_inString_language_inSpellDocumentWithTag_, 0, NSRange.__typestr__)


    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsBOOL(NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_, 3)
        self.failUnlessArgIsOut(NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_, 5)
        self.failUnlessResultIsBOOL(NSSpellChecker.hasLearnedWord_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgHasType(NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_,
                1, NSRange.__typestr__)
        self.failUnlessArgIsOut(NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_, 5)
        self.failUnlessArgIsOut(NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_, 6)

        self.failUnlessArgHasType(NSSpellChecker.requestCheckingOfString_range_types_options_inSpellDocumentWithTag_completionHandler_,
                1, NSRange.__typestr__)
        self.failUnlessArgIsBlock(NSSpellChecker.requestCheckingOfString_range_types_options_inSpellDocumentWithTag_completionHandler_,
                5, 'v' + objc._C_NSInteger + '@@' + objc._C_NSInteger)

        self.failUnlessArgHasType(NSSpellChecker.menuForResult_string_options_atLocation_inView_, 3, NSPoint.__typestr__)

        self.failUnlessArgHasType(NSSpellChecker.guessesForWordRange_inString_language_inSpellDocumentWithTag_, 0, NSRange.__typestr__)

        self.failUnlessResultIsBOOL(NSSpellChecker.automaticallyIdentifiesLanguages)
        self.failUnlessArgIsBOOL(NSSpellChecker.setAutomaticallyIdentifiesLanguages_, 0)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(NSTextCheckingOrthographyKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingQuotesKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingReplacementsKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingReferenceDateKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingReferenceTimeZoneKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingDocumentURLKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingDocumentTitleKey, unicode)
        self.failUnlessIsInstance(NSTextCheckingDocumentAuthorKey, unicode)



if __name__ == "__main__":
    main()
