from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestLocale (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFLocaleRef)

    def testGetTypeID(self):
        self.failUnless(isinstance(CFLocaleGetTypeID(), (int, long)))

    def testInspection(self):

        locale = CFLocaleGetSystem()
        self.failUnless(isinstance(locale, CFLocaleRef))

        locale = CFLocaleCopyCurrent()
        self.failUnless(isinstance(locale, CFLocaleRef))

        idents = CFLocaleCopyAvailableLocaleIdentifiers()
        self.failUnless(isinstance(idents, CFArrayRef))

        codes = CFLocaleCopyISOLanguageCodes()
        self.failUnless(isinstance(codes, CFArrayRef))

        codes = CFLocaleCopyISOCountryCodes()
        self.failUnless(isinstance(codes, CFArrayRef))

        codes = CFLocaleCopyISOCurrencyCodes()
        self.failUnless(isinstance(codes, CFArrayRef))



        val = CFLocaleCreateCanonicalLanguageIdentifierFromString(None, "de_DE")
        self.failUnless(isinstance(val, unicode))
        self.failUnless(val == 'de-DE')

        val = CFLocaleCreateCanonicalLocaleIdentifierFromString(None, "de_DE")
        self.failUnless(isinstance(val, unicode))
        self.assertEquals(val, 'de_DE')

        val = CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes(None, 55, 75)
        self.failUnless(isinstance(val, unicode))

        dct = CFLocaleCreateComponentsFromLocaleIdentifier(None, "nl_NL")
        self.failUnless(dct["locale:country code"] == 'NL')
        self.failUnless(dct["locale:language code"] == 'nl')

        val = CFLocaleCreateLocaleIdentifierFromComponents(None, dct)
        self.failUnless(isinstance(val, unicode))
        self.assertEquals(val, 'nl_NL')

        locale = CFLocaleCreate(None, "nl_NL")
        self.failUnless(isinstance(locale, CFLocaleRef))

        locale = CFLocaleCreateCopy(None, locale)
        self.failUnless(isinstance(locale, CFLocaleRef))

        ident = CFLocaleGetIdentifier(locale)
        self.failUnless(ident == "nl_NL")

        v = CFLocaleGetValue(locale, kCFLocaleDecimalSeparator)
        self.failUnless(v == ',')

        v = CFLocaleCopyDisplayNameForPropertyValue(locale, kCFLocaleIdentifier, "nl_NL")
        self.failUnless(v is None or isinstance(v, unicode))
        self.failUnless(v == u'Nederlands (Nederland)')


    def testConstants(self):

        self.failUnless(isinstance( kCFLocaleIdentifier, unicode))
        self.failUnless(isinstance( kCFLocaleLanguageCode, unicode))
        self.failUnless(isinstance( kCFLocaleCountryCode, unicode))
        self.failUnless(isinstance( kCFLocaleScriptCode, unicode))
        self.failUnless(isinstance( kCFLocaleVariantCode, unicode))
        self.failUnless(isinstance( kCFLocaleExemplarCharacterSet, unicode))
        self.failUnless(isinstance( kCFLocaleCalendarIdentifier, unicode))
        self.failUnless(isinstance( kCFLocaleCalendar, unicode))
        self.failUnless(isinstance( kCFLocaleCollationIdentifier, unicode))
        self.failUnless(isinstance( kCFLocaleUsesMetricSystem, unicode))
        self.failUnless(isinstance( kCFLocaleMeasurementSystem, unicode))
        self.failUnless(isinstance( kCFLocaleDecimalSeparator, unicode))
        self.failUnless(isinstance( kCFLocaleGroupingSeparator, unicode))
        self.failUnless(isinstance( kCFLocaleCurrencySymbol, unicode))
        self.failUnless(isinstance( kCFLocaleCurrencyCode, unicode))
        self.failUnless(isinstance( kCFGregorianCalendar, unicode))
        self.failUnless(isinstance( kCFBuddhistCalendar, unicode))
        self.failUnless(isinstance( kCFChineseCalendar, unicode))
        self.failUnless(isinstance( kCFHebrewCalendar, unicode))
        self.failUnless(isinstance( kCFIslamicCalendar, unicode))
        self.failUnless(isinstance( kCFIslamicCivilCalendar, unicode))
        self.failUnless(isinstance( kCFJapaneseCalendar, unicode))

    @min_os_level('10.5')
    def testFunctions10_5(self):
        codes = CFLocaleCopyCommonISOCurrencyCodes()
        self.failUnless(isinstance(codes, CFArrayRef))

        codes = CFLocaleCopyPreferredLanguages()
        self.failUnless(isinstance(codes, CFArrayRef))

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnless(isinstance( kCFLocaleCurrentLocaleDidChangeNotification, unicode))

if __name__ == "__main__":
    main()
