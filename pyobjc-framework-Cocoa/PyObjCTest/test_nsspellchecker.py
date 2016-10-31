
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSSpellChecker (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSSpellChecker.sharedSpellCheckerExists)
        self.assertArgIsBOOL(NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_, 3)
        self.assertArgIsOut(NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_, 5)
        self.assertResultIsBOOL(NSSpellChecker.setLanguage_)

        self.assertArgHasType(NSSpellChecker.completionsForPartialWordRange_inString_language_inSpellDocumentWithTag_, 0, NSRange.__typestr__)


    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsBOOL(NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_, 3)
        self.assertArgIsOut(NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_, 5)
        self.assertResultIsBOOL(NSSpellChecker.hasLearnedWord_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgHasType(NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_,
                1, NSRange.__typestr__)
        self.assertArgIsOut(NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_, 5)
        self.assertArgIsOut(NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_, 6)

        self.assertArgHasType(NSSpellChecker.requestCheckingOfString_range_types_options_inSpellDocumentWithTag_completionHandler_,
                1, NSRange.__typestr__)
        self.assertArgIsBlock(NSSpellChecker.requestCheckingOfString_range_types_options_inSpellDocumentWithTag_completionHandler_,
                5, b'v' + objc._C_NSInteger + b'@@' + objc._C_NSInteger)

        self.assertArgHasType(NSSpellChecker.menuForResult_string_options_atLocation_inView_, 3, NSPoint.__typestr__)

        self.assertArgHasType(NSSpellChecker.guessesForWordRange_inString_language_inSpellDocumentWithTag_, 0, NSRange.__typestr__)

        self.assertResultIsBOOL(NSSpellChecker.automaticallyIdentifiesLanguages)
        self.assertArgIsBOOL(NSSpellChecker.setAutomaticallyIdentifiesLanguages_, 0)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBlock(
                NSSpellChecker.showCorrectionIndicatorOfType_primaryString_alternativeStrings_forStringInRect_view_completionHandler_,
                5, b'v@')
        self.assertResultIsBOOL(NSSpellChecker.isAutomaticTextReplacementEnabled)
        self.assertResultIsBOOL(NSSpellChecker.isAutomaticSpellingCorrectionEnabled)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(NSSpellChecker.isAutomaticQuoteSubstitutionEnabled)
        self.assertResultIsBOOL(NSSpellChecker.isAutomaticDashSubstitutionEnabled)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSSpellChecker.preventsAutocorrectionBeforeString_language_)
        self.assertResultIsBOOL(NSSpellChecker.isAutomaticCapitalizationEnabled)
        self.assertResultIsBOOL(NSSpellChecker.isAutomaticPeriodSubstitutionEnabled)
        self.assertResultIsBOOL(NSSpellChecker.isAutomaticTextCompletionEnabled)

        self.assertArgIsBlock(NSSpellChecker.requestCandidatesForSelectedRange_inString_types_options_inSpellDocumentWithTag_completionHandler_, 5, b'v' + objc._C_NSInteger + b'@')


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSTextCheckingOrthographyKey, unicode)
        self.assertIsInstance(NSTextCheckingQuotesKey, unicode)
        self.assertIsInstance(NSTextCheckingReplacementsKey, unicode)
        self.assertIsInstance(NSTextCheckingReferenceDateKey, unicode)
        self.assertIsInstance(NSTextCheckingReferenceTimeZoneKey, unicode)
        self.assertIsInstance(NSTextCheckingDocumentURLKey, unicode)
        self.assertIsInstance(NSTextCheckingDocumentTitleKey, unicode)
        self.assertIsInstance(NSTextCheckingDocumentAuthorKey, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(NSTextCheckingRegularExpressionsKey, unicode)
        self.assertIsInstance(NSSpellCheckerDidChangeAutomaticSpellingCorrectionNotification, unicode)
        self.assertIsInstance(NSSpellCheckerDidChangeAutomaticTextReplacementNotification, unicode)

        self.assertEqual(NSCorrectionResponseNone, 0)
        self.assertEqual(NSCorrectionResponseAccepted, 1)
        self.assertEqual(NSCorrectionResponseRejected, 2)
        self.assertEqual(NSCorrectionResponseIgnored, 3)
        self.assertEqual(NSCorrectionResponseEdited, 4)
        self.assertEqual(NSCorrectionResponseReverted, 5)

        self.assertEqual(NSCorrectionIndicatorTypeDefault, 0)
        self.assertEqual(NSCorrectionIndicatorTypeReversion, 1)
        self.assertEqual(NSCorrectionIndicatorTypeGuesses, 2)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSSpellCheckerDidChangeAutomaticQuoteSubstitutionNotification, unicode)
        self.assertIsInstance(NSSpellCheckerDidChangeAutomaticDashSubstitutionNotification, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(NSTextCheckingSelectedRangeKey, unicode)
        self.assertIsInstance(NSSpellCheckerDidChangeAutomaticCapitalizationNotification, unicode)
        self.assertIsInstance(NSSpellCheckerDidChangeAutomaticPeriodSubstitutionNotification, unicode)
        self.assertIsInstance(NSSpellCheckerDidChangeAutomaticTextCompletionNotification, unicode)


if __name__ == "__main__":
    main()
