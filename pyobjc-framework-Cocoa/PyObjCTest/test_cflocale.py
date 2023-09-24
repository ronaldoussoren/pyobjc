import CoreFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

NSLocale = objc.lookUpClass("NSLocale")
NSArray = objc.lookUpClass("NSArray")


class TestLocale(TestCase):
    def testGetTypeID(self):
        self.assertIsInstance(CoreFoundation.CFLocaleGetTypeID(), int)

    def testInspection(self):
        locale = CoreFoundation.CFLocaleGetSystem()
        self.assertIsInstance(locale, NSLocale)
        locale = CoreFoundation.CFLocaleCopyCurrent()
        self.assertIsInstance(locale, NSLocale)
        idents = CoreFoundation.CFLocaleCopyAvailableLocaleIdentifiers()
        self.assertIsInstance(idents, NSArray)
        codes = CoreFoundation.CFLocaleCopyISOLanguageCodes()
        self.assertIsInstance(codes, NSArray)
        codes = CoreFoundation.CFLocaleCopyISOCountryCodes()
        self.assertIsInstance(codes, NSArray)
        codes = CoreFoundation.CFLocaleCopyISOCurrencyCodes()
        self.assertIsInstance(codes, NSArray)
        val = CoreFoundation.CFLocaleCreateCanonicalLanguageIdentifierFromString(
            None, "de_DE"
        )
        self.assertIsInstance(val, str)
        self.assertEqual(val, "de-DE")
        val = CoreFoundation.CFLocaleCreateCanonicalLocaleIdentifierFromString(
            None, "de_DE"
        )
        self.assertIsInstance(val, str)
        self.assertEqual(val, "de_DE")

        val = CoreFoundation.CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(
            None, 55, 75
        )
        self.assertIsInstance(val, str)
        dct = CoreFoundation.CFLocaleCreateComponentsFromLocaleIdentifier(None, "nl_NL")
        self.assertEqual(dct[CoreFoundation.kCFLocaleCountryCodeKey], "NL")
        self.assertEqual(dct[CoreFoundation.kCFLocaleLanguageCodeKey], "nl")
        val = CoreFoundation.CFLocaleCreateLocaleIdentifierFromComponents(None, dct)
        self.assertIsInstance(val, str)
        self.assertEqual(val, "nl_NL")

        locale = CoreFoundation.CFLocaleCreate(None, "nl_NL")
        self.assertIsInstance(locale, NSLocale)
        locale = CoreFoundation.CFLocaleCreateCopy(None, locale)
        self.assertIsInstance(locale, NSLocale)
        ident = CoreFoundation.CFLocaleGetIdentifier(locale)
        self.assertEqual(ident, "nl_NL")
        v = CoreFoundation.CFLocaleGetValue(
            locale, CoreFoundation.kCFLocaleDecimalSeparator
        )
        self.assertEqual(v, ",")
        v = CoreFoundation.CFLocaleCopyDisplayNameForPropertyValue(
            locale, CoreFoundation.kCFLocaleIdentifier, "nl_NL"
        )
        if v is not None:
            self.assertIsInstance(v, str)
        self.assertEqual(v, "Nederlands (Nederland)")

    def testConstants(self):
        self.assertIsInstance(CoreFoundation.kCFLocaleIdentifier, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleLanguageCode, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleCountryCode, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleScriptCode, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleVariantCode, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleExemplarCharacterSet, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleCalendarIdentifier, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleCollationIdentifier, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleUsesMetricSystem, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleMeasurementSystem, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleDecimalSeparator, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleGroupingSeparator, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleCurrencySymbol, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleCurrencyCode, str)
        self.assertIsInstance(CoreFoundation.kCFGregorianCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFBuddhistCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFChineseCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFHebrewCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFIslamicCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFIslamicCivilCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFJapaneseCalendar, str)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        codes = CoreFoundation.CFLocaleCopyCommonISOCurrencyCodes()
        self.assertIsInstance(codes, NSArray)
        codes = CoreFoundation.CFLocaleCopyPreferredLanguages()
        self.assertIsInstance(codes, NSArray)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(
            CoreFoundation.kCFLocaleCurrentLocaleDidChangeNotification, str
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreFoundation.kCFLocaleLanguageDirectionUnknown, 0)
        self.assertEqual(CoreFoundation.kCFLocaleLanguageDirectionLeftToRight, 1)
        self.assertEqual(CoreFoundation.kCFLocaleLanguageDirectionRightToLeft, 2)
        self.assertEqual(CoreFoundation.kCFLocaleLanguageDirectionTopToBottom, 3)
        self.assertEqual(CoreFoundation.kCFLocaleLanguageDirectionBottomToTop, 4)

        self.assertIsInstance(CoreFoundation.kCFLocaleCollatorIdentifier, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleQuotationBeginDelimiterKey, str)
        self.assertIsInstance(CoreFoundation.kCFLocaleQuotationEndDelimiterKey, str)
        self.assertIsInstance(
            CoreFoundation.kCFLocaleAlternateQuotationBeginDelimiterKey, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFLocaleAlternateQuotationEndDelimiterKey, str
        )
        self.assertIsInstance(CoreFoundation.kCFRepublicOfChinaCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFPersianCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFIndianCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFISO8601Calendar, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(CoreFoundation.kCFIslamicTabularCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFIslamicUmmAlQuraCalendar, str)

    @min_os_level("10.6")
    def testFunctions10_6(self):
        v = CoreFoundation.CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier("nl_NL")
        self.assertIsInstance(v, int)

        self.assertResultIsCFRetained(
            CoreFoundation.CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode
        )
        v = CoreFoundation.CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(
            None, 1043
        )
        self.assertIsInstance(v, str)

        v = CoreFoundation.CFLocaleGetLanguageCharacterDirection("NL")
        self.assertEqual(v, CoreFoundation.kCFLocaleLanguageDirectionLeftToRight)

        v = CoreFoundation.CFLocaleGetLanguageLineDirection("NL")
        self.assertEqual(v, CoreFoundation.kCFLocaleLanguageDirectionTopToBottom)
