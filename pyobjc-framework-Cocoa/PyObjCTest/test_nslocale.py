import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase


class TestNSLocale(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSLocaleLanguageDirection)
        self.assertEqual(
            Foundation.NSLocaleLanguageDirectionUnknown,
            CoreFoundation.kCFLocaleLanguageDirectionUnknown,
        )
        self.assertEqual(
            Foundation.NSLocaleLanguageDirectionLeftToRight,
            CoreFoundation.kCFLocaleLanguageDirectionLeftToRight,
        )
        self.assertEqual(
            Foundation.NSLocaleLanguageDirectionRightToLeft,
            CoreFoundation.kCFLocaleLanguageDirectionRightToLeft,
        )
        self.assertEqual(
            Foundation.NSLocaleLanguageDirectionTopToBottom,
            CoreFoundation.kCFLocaleLanguageDirectionTopToBottom,
        )
        self.assertEqual(
            Foundation.NSLocaleLanguageDirectionBottomToTop,
            CoreFoundation.kCFLocaleLanguageDirectionBottomToTop,
        )

    def test_typed_enums(self):
        self.assertIsTypedEnum(Foundation.NSLocaleKey, str)

    def test_constants(self):
        self.assertIsInstance(Foundation.NSCurrentLocaleDidChangeNotification, str)
        self.assertIsInstance(Foundation.NSLocaleIdentifier, str)
        self.assertIsInstance(Foundation.NSLocaleLanguageCode, str)
        self.assertIsInstance(Foundation.NSLocaleCountryCode, str)
        self.assertIsInstance(Foundation.NSLocaleScriptCode, str)
        self.assertIsInstance(Foundation.NSLocaleVariantCode, str)
        self.assertIsInstance(Foundation.NSLocaleExemplarCharacterSet, str)
        self.assertIsInstance(Foundation.NSLocaleCalendar, str)
        self.assertIsInstance(Foundation.NSLocaleCollationIdentifier, str)
        self.assertIsInstance(Foundation.NSLocaleUsesMetricSystem, str)
        self.assertIsInstance(Foundation.NSLocaleMeasurementSystem, str)
        self.assertIsInstance(Foundation.NSLocaleDecimalSeparator, str)
        self.assertIsInstance(Foundation.NSLocaleGroupingSeparator, str)
        self.assertIsInstance(Foundation.NSLocaleCurrencySymbol, str)
        self.assertIsInstance(Foundation.NSLocaleCurrencyCode, str)
        self.assertIsInstance(Foundation.NSGregorianCalendar, str)
        self.assertIsInstance(Foundation.NSBuddhistCalendar, str)
        self.assertIsInstance(Foundation.NSChineseCalendar, str)
        self.assertIsInstance(Foundation.NSHebrewCalendar, str)
        self.assertIsInstance(Foundation.NSIslamicCalendar, str)
        self.assertIsInstance(Foundation.NSIslamicCivilCalendar, str)
        self.assertIsInstance(Foundation.NSJapaneseCalendar, str)

        self.assertIsInstance(Foundation.NSLocaleCollatorIdentifier, str)
        self.assertIsInstance(Foundation.NSLocaleQuotationBeginDelimiterKey, str)
        self.assertIsInstance(Foundation.NSLocaleQuotationEndDelimiterKey, str)
        self.assertIsInstance(
            Foundation.NSLocaleAlternateQuotationBeginDelimiterKey, str
        )
        self.assertIsInstance(Foundation.NSLocaleAlternateQuotationEndDelimiterKey, str)
        self.assertIsInstance(Foundation.NSRepublicOfChinaCalendar, str)
        self.assertIsInstance(Foundation.NSPersianCalendar, str)
        self.assertIsInstance(Foundation.NSIndianCalendar, str)
        self.assertIsInstance(Foundation.NSISO8601Calendar, str)
