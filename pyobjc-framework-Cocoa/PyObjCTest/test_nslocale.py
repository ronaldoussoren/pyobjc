from PyObjCTools.TestSupport import *
from Foundation import *

try:
    unicode
except NameError:
    unicode = str

class TestNSLocale (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSCurrentLocaleDidChangeNotification, unicode)
        self.assertIsInstance(NSLocaleIdentifier, unicode)
        self.assertIsInstance(NSLocaleLanguageCode, unicode)
        self.assertIsInstance(NSLocaleCountryCode, unicode)
        self.assertIsInstance(NSLocaleScriptCode, unicode)
        self.assertIsInstance(NSLocaleVariantCode, unicode)
        self.assertIsInstance(NSLocaleExemplarCharacterSet, unicode)
        self.assertIsInstance(NSLocaleCalendar, unicode)
        self.assertIsInstance(NSLocaleCollationIdentifier, unicode)
        self.assertIsInstance(NSLocaleUsesMetricSystem, unicode)
        self.assertIsInstance(NSLocaleMeasurementSystem, unicode)
        self.assertIsInstance(NSLocaleDecimalSeparator, unicode)
        self.assertIsInstance(NSLocaleGroupingSeparator, unicode)
        self.assertIsInstance(NSLocaleCurrencySymbol, unicode)
        self.assertIsInstance(NSLocaleCurrencyCode, unicode)
        self.assertIsInstance(NSGregorianCalendar, unicode)
        self.assertIsInstance(NSBuddhistCalendar, unicode)
        self.assertIsInstance(NSChineseCalendar, unicode)
        self.assertIsInstance(NSHebrewCalendar, unicode)
        self.assertIsInstance(NSIslamicCalendar, unicode)
        self.assertIsInstance(NSIslamicCivilCalendar, unicode)
        self.assertIsInstance(NSJapaneseCalendar, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSLocaleCollatorIdentifier, unicode)
        self.assertIsInstance(NSLocaleQuotationBeginDelimiterKey, unicode)
        self.assertIsInstance(NSLocaleQuotationEndDelimiterKey, unicode)
        self.assertIsInstance(NSLocaleAlternateQuotationBeginDelimiterKey, unicode)
        self.assertIsInstance(NSLocaleAlternateQuotationEndDelimiterKey, unicode)
        self.assertIsInstance(NSRepublicOfChinaCalendar, unicode)
        self.assertIsInstance(NSPersianCalendar, unicode)
        self.assertIsInstance(NSIndianCalendar, unicode)
        self.assertIsInstance(NSISO8601Calendar, unicode)

        self.assertEqual(NSLocaleLanguageDirectionUnknown, kCFLocaleLanguageDirectionUnknown)
        self.assertEqual(NSLocaleLanguageDirectionLeftToRight, kCFLocaleLanguageDirectionLeftToRight)
        self.assertEqual(NSLocaleLanguageDirectionRightToLeft, kCFLocaleLanguageDirectionRightToLeft)
        self.assertEqual(NSLocaleLanguageDirectionTopToBottom, kCFLocaleLanguageDirectionTopToBottom)
        self.assertEqual(NSLocaleLanguageDirectionBottomToTop, kCFLocaleLanguageDirectionBottomToTop)


if __name__ == "__main__":
    main()
