from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestLocale (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFLocaleRef)

    def testGetTypeID(self):
        self.assertIsInstance(CFLocaleGetTypeID(), (int, long))
    def testInspection(self):

        locale = CFLocaleGetSystem()
        self.assertIsInstance(locale, CFLocaleRef)
        locale = CFLocaleCopyCurrent()
        self.assertIsInstance(locale, CFLocaleRef)
        idents = CFLocaleCopyAvailableLocaleIdentifiers()
        self.assertIsInstance(idents, CFArrayRef)
        codes = CFLocaleCopyISOLanguageCodes()
        self.assertIsInstance(codes, CFArrayRef)
        codes = CFLocaleCopyISOCountryCodes()
        self.assertIsInstance(codes, CFArrayRef)
        codes = CFLocaleCopyISOCurrencyCodes()
        self.assertIsInstance(codes, CFArrayRef)
        val = CFLocaleCreateCanonicalLanguageIdentifierFromString(None, "de_DE")
        self.assertIsInstance(val, unicode)
        self.assertEqual(val , 'de-DE')
        val = CFLocaleCreateCanonicalLocaleIdentifierFromString(None, "de_DE")
        self.assertIsInstance(val, unicode)
        self.assertEqual(val, 'de_DE')

        val = CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(None, 55, 75)
        self.assertIsInstance(val, unicode)
        dct = CFLocaleCreateComponentsFromLocaleIdentifier(None, "nl_NL")
        try:
            # 10.6
            self.assertEqual(dct[kCFLocaleCountryCodeKey] , 'NL')
            self.assertEqual(dct[kCFLocaleLanguageCodeKey] , 'nl')
        except NameError:
            # 10.5 and earlier
            self.assertEqual(dct["locale:country code"] , 'NL')
            self.assertEqual(dct["locale:language code"] , 'nl')
        val = CFLocaleCreateLocaleIdentifierFromComponents(None, dct)
        self.assertIsInstance(val, unicode)
        self.assertEqual(val, 'nl_NL')

        locale = CFLocaleCreate(None, "nl_NL")
        self.assertIsInstance(locale, CFLocaleRef)
        locale = CFLocaleCreateCopy(None, locale)
        self.assertIsInstance(locale, CFLocaleRef)
        ident = CFLocaleGetIdentifier(locale)
        self.assertEqual(ident , "nl_NL")
        v = CFLocaleGetValue(locale, kCFLocaleDecimalSeparator)
        self.assertEqual(v , ',')
        v = CFLocaleCopyDisplayNameForPropertyValue(locale, kCFLocaleIdentifier, "nl_NL")
        if v is not None:
            self.assertIsInstance(v, unicode)
        self.assertEqual(v , u'Nederlands (Nederland)')
    def testConstants(self):

        self.assertIsInstance( kCFLocaleIdentifier, unicode)
        self.assertIsInstance( kCFLocaleLanguageCode, unicode)
        self.assertIsInstance( kCFLocaleCountryCode, unicode)
        self.assertIsInstance( kCFLocaleScriptCode, unicode)
        self.assertIsInstance( kCFLocaleVariantCode, unicode)
        self.assertIsInstance( kCFLocaleExemplarCharacterSet, unicode)
        self.assertIsInstance( kCFLocaleCalendarIdentifier, unicode)
        self.assertIsInstance( kCFLocaleCalendar, unicode)
        self.assertIsInstance( kCFLocaleCollationIdentifier, unicode)
        self.assertIsInstance( kCFLocaleUsesMetricSystem, unicode)
        self.assertIsInstance( kCFLocaleMeasurementSystem, unicode)
        self.assertIsInstance( kCFLocaleDecimalSeparator, unicode)
        self.assertIsInstance( kCFLocaleGroupingSeparator, unicode)
        self.assertIsInstance( kCFLocaleCurrencySymbol, unicode)
        self.assertIsInstance( kCFLocaleCurrencyCode, unicode)
        self.assertIsInstance( kCFGregorianCalendar, unicode)
        self.assertIsInstance( kCFBuddhistCalendar, unicode)
        self.assertIsInstance( kCFChineseCalendar, unicode)
        self.assertIsInstance( kCFHebrewCalendar, unicode)
        self.assertIsInstance( kCFIslamicCalendar, unicode)
        self.assertIsInstance( kCFIslamicCivilCalendar, unicode)
        self.assertIsInstance( kCFJapaneseCalendar, unicode)
    @min_os_level('10.5')
    def testFunctions10_5(self):
        codes = CFLocaleCopyCommonISOCurrencyCodes()
        self.assertIsInstance(codes, CFArrayRef)
        codes = CFLocaleCopyPreferredLanguages()
        self.assertIsInstance(codes, CFArrayRef)
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance( kCFLocaleCurrentLocaleDidChangeNotification, unicode)
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFLocaleLanguageDirectionUnknown, 0)
        self.assertEqual(kCFLocaleLanguageDirectionLeftToRight, 1)
        self.assertEqual(kCFLocaleLanguageDirectionRightToLeft, 2)
        self.assertEqual(kCFLocaleLanguageDirectionTopToBottom, 3)
        self.assertEqual(kCFLocaleLanguageDirectionBottomToTop, 4)

        self.assertIsInstance(kCFLocaleCollatorIdentifier, unicode)
        self.assertIsInstance(kCFLocaleQuotationBeginDelimiterKey, unicode)
        self.assertIsInstance(kCFLocaleQuotationEndDelimiterKey, unicode)
        self.assertIsInstance(kCFLocaleAlternateQuotationBeginDelimiterKey, unicode)
        self.assertIsInstance(kCFLocaleAlternateQuotationEndDelimiterKey, unicode)
        self.assertIsInstance(kCFRepublicOfChinaCalendar, unicode)
        self.assertIsInstance(kCFPersianCalendar, unicode)
        self.assertIsInstance(kCFIndianCalendar, unicode)
        self.assertIsInstance(kCFISO8601Calendar, unicode)


    @min_os_level('10.6')
    def testFunctions10_6(self):
        v = CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier('nl_NL')
        self.assertIsInstance(v, (int, long))

        self.assertResultIsCFRetained(CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode)
        v = CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode(None, 1043)
        self.assertIsInstance(v, unicode)

        v = CFLocaleGetLanguageCharacterDirection('NL')
        self.assertEqual(v, kCFLocaleLanguageDirectionLeftToRight)

        v = CFLocaleGetLanguageLineDirection('NL')
        self.assertEqual(v, kCFLocaleLanguageDirectionTopToBottom)


if __name__ == "__main__":
    main()
