import CoreFoundation
import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestDateFormatter(TestCase):
    def testTypeID(self):
        self.assertIsInstance(CoreFoundation.CFDateGetTypeID(), int)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFDateFormatterNoStyle, 0)
        self.assertEqual(CoreFoundation.kCFDateFormatterShortStyle, 1)
        self.assertEqual(CoreFoundation.kCFDateFormatterMediumStyle, 2)
        self.assertEqual(CoreFoundation.kCFDateFormatterLongStyle, 3)
        self.assertEqual(CoreFoundation.kCFDateFormatterFullStyle, 4)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterIsLenient, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterTimeZone, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterCalendarName, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterDefaultFormat, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterTwoDigitStartDate, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterDefaultDate, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterCalendar, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterEraSymbols, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterMonthSymbols, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterShortMonthSymbols, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterWeekdaySymbols, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterShortWeekdaySymbols, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterAMSymbol, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterPMSymbol, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterLongEraSymbols, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterVeryShortMonthSymbols, str)
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterStandaloneMonthSymbols, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterShortStandaloneMonthSymbols, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterVeryShortStandaloneMonthSymbols, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterVeryShortWeekdaySymbols, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterStandaloneWeekdaySymbols, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterShortStandaloneWeekdaySymbols, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterVeryShortStandaloneWeekdaySymbols, str
        )
        self.assertIsInstance(CoreFoundation.kCFDateFormatterQuarterSymbols, str)
        self.assertIsInstance(CoreFoundation.kCFDateFormatterShortQuarterSymbols, str)
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterStandaloneQuarterSymbols, str
        )
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterShortStandaloneQuarterSymbols, str
        )
        self.assertIsInstance(CoreFoundation.kCFDateFormatterGregorianStartDate, str)

        self.assertEqual(CoreFoundation.kCFISO8601DateFormatWithYear, 1 << 0)
        self.assertEqual(CoreFoundation.kCFISO8601DateFormatWithMonth, 1 << 1)
        self.assertEqual(CoreFoundation.kCFISO8601DateFormatWithWeekOfYear, 1 << 2)
        self.assertEqual(CoreFoundation.kCFISO8601DateFormatWithDay, 1 << 4)
        self.assertEqual(CoreFoundation.kCFISO8601DateFormatWithTime, 1 << 5)
        self.assertEqual(CoreFoundation.kCFISO8601DateFormatWithTimeZone, 1 << 6)
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithSpaceBetweenDateAndTime, 1 << 7
        )
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithDashSeparatorInDate, 1 << 8
        )
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithColonSeparatorInTime, 1 << 9
        )
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithColonSeparatorInTimeZone, 1 << 10
        )
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithFractionalSeconds, 1 << 11
        )
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithFullDate,
            CoreFoundation.kCFISO8601DateFormatWithYear
            | CoreFoundation.kCFISO8601DateFormatWithMonth
            | CoreFoundation.kCFISO8601DateFormatWithDay
            | CoreFoundation.kCFISO8601DateFormatWithDashSeparatorInDate,
        )
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithFullTime,
            CoreFoundation.kCFISO8601DateFormatWithTime
            | CoreFoundation.kCFISO8601DateFormatWithColonSeparatorInTime
            | CoreFoundation.kCFISO8601DateFormatWithTimeZone
            | CoreFoundation.kCFISO8601DateFormatWithColonSeparatorInTimeZone,
        )
        self.assertEqual(
            CoreFoundation.kCFISO8601DateFormatWithInternetDateTime,
            CoreFoundation.kCFISO8601DateFormatWithFullDate
            | CoreFoundation.kCFISO8601DateFormatWithFullTime,
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(
            CoreFoundation.kCFDateFormatterDoesRelativeDateFormattingKey, str
        )

    @min_os_level("10.6")
    def testFunction10_6(self):
        self.assertResultIsCFRetained(
            CoreFoundation.CFDateFormatterCreateDateFormatFromTemplate
        )
        r = CoreFoundation.CFDateFormatterCreateDateFormatFromTemplate(
            None, "%Y-%m-%d", 0, None
        )
        self.assertIsInstance(r, str)

    @min_os_level("10.12")
    def testFunctions10_12(self):
        self.assertResultIsCFRetained(
            CoreFoundation.CFDateFormatterCreateISO8601Formatter
        )

    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFDateFormatterRef)

        self.assertIsInstance(CoreFoundation.CFDateFormatterGetTypeID(), int)

    def testInspection(self):
        locale = CoreFoundation.CFLocaleCopyCurrent()
        self.assertIsInstance(locale, objc.lookUpClass("NSLocale"))

        date = CoreFoundation.CFDateCreate(
            None, CoreFoundation.CFAbsoluteTimeGetCurrent()
        )
        self.assertIsInstance(date, Foundation.NSDate)

        self.assertResultIsCFRetained(CoreFoundation.CFDateFormatterCreate)
        fmt = CoreFoundation.CFDateFormatterCreate(
            None,
            locale,
            CoreFoundation.kCFDateFormatterShortStyle,
            CoreFoundation.kCFDateFormatterLongStyle,
        )
        self.assertIsInstance(fmt, CoreFoundation.CFDateFormatterRef)
        v = CoreFoundation.CFDateFormatterGetLocale(fmt)
        self.assertEqual(
            CoreFoundation.CFLocaleGetIdentifier(locale),
            CoreFoundation.CFLocaleGetIdentifier(v),
        )

        v = CoreFoundation.CFDateFormatterGetDateStyle(fmt)
        self.assertEqual(v, CoreFoundation.kCFDateFormatterShortStyle)

        v = CoreFoundation.CFDateFormatterGetTimeStyle(fmt)
        self.assertEqual(v, CoreFoundation.kCFDateFormatterLongStyle)

        v = CoreFoundation.CFDateFormatterGetFormat(fmt)
        self.assertIsInstance(v, str)
        CoreFoundation.CFDateFormatterSetFormat(fmt, v[:-1])
        v2 = CoreFoundation.CFDateFormatterGetFormat(fmt)
        self.assertEqual(v[:-1], v2)

        v = CoreFoundation.CFDateFormatterCreateStringWithDate(None, fmt, date)
        self.assertIsInstance(v, str)
        v = CoreFoundation.CFDateFormatterCreateStringWithAbsoluteTime(
            None, fmt, CoreFoundation.CFAbsoluteTimeGetCurrent()
        )
        self.assertIsInstance(v, str)
        dt, rng = CoreFoundation.CFDateFormatterCreateDateFromString(
            None, fmt, v, (0, len(v))
        )
        self.assertIsInstance(dt, Foundation.NSDate)
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        ok, rng, abstime = CoreFoundation.CFDateFormatterGetAbsoluteTimeFromString(
            fmt, v, (0, len(v)), None
        )
        self.assertIs(ok, True)
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        self.assertIsInstance(abstime, float)
        self.assertResultIsCFRetained(CoreFoundation.CFDateFormatterCopyProperty)
        v = CoreFoundation.CFDateFormatterCopyProperty(
            fmt, CoreFoundation.kCFDateFormatterCalendarName
        )
        self.assertIsInstance(v, str)
        CoreFoundation.CFDateFormatterSetProperty(
            fmt, CoreFoundation.kCFDateFormatterCalendarName, "gregorian"
        )
        v = CoreFoundation.CFDateFormatterCopyProperty(
            fmt, CoreFoundation.kCFDateFormatterCalendarName
        )
        self.assertIsInstance(v, str)
        self.assertEqual(v, "gregorian")
        v = CoreFoundation.CFDateFormatterCopyProperty(
            fmt, CoreFoundation.kCFDateFormatterIsLenient
        )
        self.assertTrue(v is True or v is False)
        CoreFoundation.CFDateFormatterSetProperty(
            fmt, CoreFoundation.kCFDateFormatterIsLenient, True
        )
        v2 = CoreFoundation.CFDateFormatterCopyProperty(
            fmt, CoreFoundation.kCFDateFormatterIsLenient
        )
        self.assertIs(v2, True)
