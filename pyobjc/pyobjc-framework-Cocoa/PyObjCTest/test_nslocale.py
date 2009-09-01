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

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(NSLocaleCollatorIdentifier, unicode)
        self.failUnlessIsInstance(NSLocaleQuotationBeginDelimiterKey, unicode)
        self.failUnlessIsInstance(NSLocaleQuotationEndDelimiterKey, unicode)
        self.failUnlessIsInstance(NSLocaleAlternateQuotationBeginDelimiterKey, unicode)
        self.failUnlessIsInstance(NSLocaleAlternateQuotationEndDelimiterKey, unicode)
        self.failUnlessIsInstance(NSRepublicOfChinaCalendar, unicode)
        self.failUnlessIsInstance(NSPersianCalendar, unicode)
        self.failUnlessIsInstance(NSIndianCalendar, unicode)
        self.failUnlessIsInstance(NSISO8601Calendar, unicode)

        self.failUnlessEqual(NSLocaleLanguageDirectionUnknown, kCFLocaleLanguageDirectionUnknown)
        self.failUnlessEqual(NSLocaleLanguageDirectionLeftToRight, kCFLocaleLanguageDirectionLeftToRight)
        self.failUnlessEqual(NSLocaleLanguageDirectionRightToLeft, kCFLocaleLanguageDirectionRightToLeft)
        self.failUnlessEqual(NSLocaleLanguageDirectionTopToBottom, kCFLocaleLanguageDirectionTopToBottom)
        self.failUnlessEqual(NSLocaleLanguageDirectionBottomToTop, kCFLocaleLanguageDirectionBottomToTop)





if __name__ == "__main__":
    main()
