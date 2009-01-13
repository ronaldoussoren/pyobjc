from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSLocale (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSCurrentLocaleDidChangeNotification, unicode))

        self.failUnless(isinstance(NSLocaleIdentifier, unicode))
        self.failUnless(isinstance(NSLocaleLanguageCode, unicode))
        self.failUnless(isinstance(NSLocaleCountryCode, unicode))
        self.failUnless(isinstance(NSLocaleScriptCode, unicode))
        self.failUnless(isinstance(NSLocaleVariantCode, unicode))
        self.failUnless(isinstance(NSLocaleExemplarCharacterSet, unicode))
        self.failUnless(isinstance(NSLocaleCalendar, unicode))
        self.failUnless(isinstance(NSLocaleCollationIdentifier, unicode))
        self.failUnless(isinstance(NSLocaleUsesMetricSystem, unicode))
        self.failUnless(isinstance(NSLocaleMeasurementSystem, unicode))
        self.failUnless(isinstance(NSLocaleDecimalSeparator, unicode))
        self.failUnless(isinstance(NSLocaleGroupingSeparator, unicode))
        self.failUnless(isinstance(NSLocaleCurrencySymbol, unicode))
        self.failUnless(isinstance(NSLocaleCurrencyCode, unicode))

        self.failUnless(isinstance(NSGregorianCalendar, unicode))
        self.failUnless(isinstance(NSBuddhistCalendar, unicode))
        self.failUnless(isinstance(NSChineseCalendar, unicode))
        self.failUnless(isinstance(NSHebrewCalendar, unicode))
        self.failUnless(isinstance(NSIslamicCalendar, unicode))
        self.failUnless(isinstance(NSIslamicCivilCalendar, unicode))
        self.failUnless(isinstance(NSJapaneseCalendar, unicode))


if __name__ == "__main__":
    main()
