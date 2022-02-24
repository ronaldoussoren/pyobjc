import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSSpellChecker(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSTextCheckingOptionKey, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSCorrectionIndicatorType)
        self.assertIsEnumType(AppKit.NSCorrectionResponse)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSpellChecker.sharedSpellCheckerExists)
        self.assertArgIsBOOL(
            AppKit.NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AppKit.NSSpellChecker.checkSpellingOfString_startingAt_language_wrap_inSpellDocumentWithTag_wordCount_,  # noqa: B950
            5,
        )
        self.assertResultIsBOOL(AppKit.NSSpellChecker.setLanguage_)

        self.assertArgHasType(
            AppKit.NSSpellChecker.completionsForPartialWordRange_inString_language_inSpellDocumentWithTag_,  # noqa: B950
            0,
            AppKit.NSRange.__typestr__,
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsBOOL(
            AppKit.NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_,  # noqa: B950
            3,
        )
        self.assertArgIsOut(
            AppKit.NSSpellChecker.checkGrammarOfString_startingAt_language_wrap_inSpellDocumentWithTag_details_,  # noqa: B950
            5,
        )
        self.assertResultIsBOOL(AppKit.NSSpellChecker.hasLearnedWord_)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgHasType(
            AppKit.NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsOut(
            AppKit.NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_,  # noqa: B950
            5,
        )
        self.assertArgIsOut(
            AppKit.NSSpellChecker.checkString_range_types_options_inSpellDocumentWithTag_orthography_wordCount_,  # noqa: B950
            6,
        )

        self.assertArgHasType(
            AppKit.NSSpellChecker.requestCheckingOfString_range_types_options_inSpellDocumentWithTag_completionHandler_,  # noqa: B950
            1,
            AppKit.NSRange.__typestr__,
        )
        self.assertArgIsBlock(
            AppKit.NSSpellChecker.requestCheckingOfString_range_types_options_inSpellDocumentWithTag_completionHandler_,  # noqa: B950
            5,
            b"v" + objc._C_NSInteger + b"@@" + objc._C_NSInteger,
        )

        self.assertArgHasType(
            AppKit.NSSpellChecker.menuForResult_string_options_atLocation_inView_,
            3,
            AppKit.NSPoint.__typestr__,
        )

        self.assertArgHasType(
            AppKit.NSSpellChecker.guessesForWordRange_inString_language_inSpellDocumentWithTag_,
            0,
            AppKit.NSRange.__typestr__,
        )

        self.assertResultIsBOOL(AppKit.NSSpellChecker.automaticallyIdentifiesLanguages)
        self.assertArgIsBOOL(
            AppKit.NSSpellChecker.setAutomaticallyIdentifiesLanguages_, 0
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBlock(
            AppKit.NSSpellChecker.showCorrectionIndicatorOfType_primaryString_alternativeStrings_forStringInRect_view_completionHandler_,  # noqa: B950
            5,
            b"v@",
        )
        self.assertResultIsBOOL(AppKit.NSSpellChecker.isAutomaticTextReplacementEnabled)
        self.assertResultIsBOOL(
            AppKit.NSSpellChecker.isAutomaticSpellingCorrectionEnabled
        )

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            AppKit.NSSpellChecker.isAutomaticQuoteSubstitutionEnabled
        )
        self.assertResultIsBOOL(
            AppKit.NSSpellChecker.isAutomaticDashSubstitutionEnabled
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            AppKit.NSSpellChecker.preventsAutocorrectionBeforeString_language_
        )
        self.assertResultIsBOOL(AppKit.NSSpellChecker.isAutomaticCapitalizationEnabled)
        self.assertResultIsBOOL(
            AppKit.NSSpellChecker.isAutomaticPeriodSubstitutionEnabled
        )
        self.assertResultIsBOOL(AppKit.NSSpellChecker.isAutomaticTextCompletionEnabled)

        self.assertArgIsBlock(
            AppKit.NSSpellChecker.requestCandidatesForSelectedRange_inString_types_options_inSpellDocumentWithTag_completionHandler_,  # noqa: B950
            5,
            b"v" + objc._C_NSInteger + b"@",
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(AppKit.NSTextCheckingOrthographyKey, str)
        self.assertIsInstance(AppKit.NSTextCheckingQuotesKey, str)
        self.assertIsInstance(AppKit.NSTextCheckingReplacementsKey, str)
        self.assertIsInstance(AppKit.NSTextCheckingReferenceDateKey, str)
        self.assertIsInstance(AppKit.NSTextCheckingReferenceTimeZoneKey, str)
        self.assertIsInstance(AppKit.NSTextCheckingDocumentURLKey, str)
        self.assertIsInstance(AppKit.NSTextCheckingDocumentTitleKey, str)
        self.assertIsInstance(AppKit.NSTextCheckingDocumentAuthorKey, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSTextCheckingRegularExpressionsKey, str)
        self.assertIsInstance(
            AppKit.NSSpellCheckerDidChangeAutomaticSpellingCorrectionNotification, str
        )
        self.assertIsInstance(
            AppKit.NSSpellCheckerDidChangeAutomaticTextReplacementNotification, str
        )

        self.assertEqual(AppKit.NSCorrectionResponseNone, 0)
        self.assertEqual(AppKit.NSCorrectionResponseAccepted, 1)
        self.assertEqual(AppKit.NSCorrectionResponseRejected, 2)
        self.assertEqual(AppKit.NSCorrectionResponseIgnored, 3)
        self.assertEqual(AppKit.NSCorrectionResponseEdited, 4)
        self.assertEqual(AppKit.NSCorrectionResponseReverted, 5)

        self.assertEqual(AppKit.NSCorrectionIndicatorTypeDefault, 0)
        self.assertEqual(AppKit.NSCorrectionIndicatorTypeReversion, 1)
        self.assertEqual(AppKit.NSCorrectionIndicatorTypeGuesses, 2)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(
            AppKit.NSSpellCheckerDidChangeAutomaticQuoteSubstitutionNotification, str
        )
        self.assertIsInstance(
            AppKit.NSSpellCheckerDidChangeAutomaticDashSubstitutionNotification, str
        )

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSTextCheckingSelectedRangeKey, str)
        self.assertIsInstance(
            AppKit.NSSpellCheckerDidChangeAutomaticCapitalizationNotification, str
        )
        self.assertIsInstance(
            AppKit.NSSpellCheckerDidChangeAutomaticPeriodSubstitutionNotification, str
        )
        self.assertIsInstance(
            AppKit.NSSpellCheckerDidChangeAutomaticTextCompletionNotification, str
        )
