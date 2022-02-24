import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSCalendar(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Foundation.NSCalendarIdentifier, str)

    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSCalendarOptions)
        self.assertIsEnumType(Foundation.NSCalendarUnit)

    def testConstants(self):
        self.assertEqual(
            Foundation.NSEraCalendarUnit, CoreFoundation.kCFCalendarUnitEra
        )
        self.assertEqual(
            Foundation.NSYearCalendarUnit, CoreFoundation.kCFCalendarUnitYear
        )
        self.assertEqual(
            Foundation.NSMonthCalendarUnit, CoreFoundation.kCFCalendarUnitMonth
        )
        self.assertEqual(
            Foundation.NSDayCalendarUnit, CoreFoundation.kCFCalendarUnitDay
        )
        self.assertEqual(
            Foundation.NSHourCalendarUnit, CoreFoundation.kCFCalendarUnitHour
        )
        self.assertEqual(
            Foundation.NSMinuteCalendarUnit, CoreFoundation.kCFCalendarUnitMinute
        )
        self.assertEqual(
            Foundation.NSSecondCalendarUnit, CoreFoundation.kCFCalendarUnitSecond
        )
        self.assertEqual(
            Foundation.NSWeekCalendarUnit, CoreFoundation.kCFCalendarUnitWeek
        )
        self.assertEqual(
            Foundation.NSWeekdayCalendarUnit, CoreFoundation.kCFCalendarUnitWeekday
        )
        self.assertEqual(
            Foundation.NSWeekdayOrdinalCalendarUnit,
            CoreFoundation.kCFCalendarUnitWeekdayOrdinal,
        )

        self.assertEqual(
            Foundation.NSWrapCalendarComponents,
            CoreFoundation.kCFCalendarComponentsWrap,
        )

        self.assertEqual(Foundation.NSUndefinedDateComponent, Foundation.NSIntegerMax)
        self.assertEqual(Foundation.NSDateComponentUndefined, Foundation.NSIntegerMax)

        self.assertEqual(
            Foundation.NSCalendarUnitEra, CoreFoundation.kCFCalendarUnitEra
        )
        self.assertEqual(
            Foundation.NSCalendarUnitYear, CoreFoundation.kCFCalendarUnitYear
        )
        self.assertEqual(
            Foundation.NSCalendarUnitMonth, CoreFoundation.kCFCalendarUnitMonth
        )
        self.assertEqual(
            Foundation.NSCalendarUnitDay, CoreFoundation.kCFCalendarUnitDay
        )
        self.assertEqual(
            Foundation.NSCalendarUnitHour, CoreFoundation.kCFCalendarUnitHour
        )
        self.assertEqual(
            Foundation.NSCalendarUnitMinute, CoreFoundation.kCFCalendarUnitMinute
        )
        self.assertEqual(
            Foundation.NSCalendarUnitSecond, CoreFoundation.kCFCalendarUnitSecond
        )
        self.assertEqual(
            Foundation.NSCalendarUnitWeekday, CoreFoundation.kCFCalendarUnitWeekday
        )
        self.assertEqual(
            Foundation.NSCalendarUnitWeekdayOrdinal,
            CoreFoundation.kCFCalendarUnitWeekdayOrdinal,
        )
        self.assertEqual(
            Foundation.NSCalendarUnitQuarter, CoreFoundation.kCFCalendarUnitQuarter
        )
        self.assertEqual(
            Foundation.NSCalendarUnitWeekOfMonth,
            CoreFoundation.kCFCalendarUnitWeekOfMonth,
        )
        self.assertEqual(
            Foundation.NSCalendarUnitWeekOfYear,
            CoreFoundation.kCFCalendarUnitWeekOfYear,
        )
        self.assertEqual(
            Foundation.NSCalendarUnitYearForWeekOfYear,
            CoreFoundation.kCFCalendarUnitYearForWeekOfYear,
        )
        self.assertEqual(Foundation.NSCalendarUnitNanosecond, (1 << 15))
        self.assertEqual(Foundation.NSCalendarUnitCalendar, (1 << 20))
        self.assertEqual(Foundation.NSCalendarUnitTimeZone, (1 << 21))
        self.assertEqual(Foundation.NSCalendarWrapComponents, (1 << 0))
        self.assertEqual(Foundation.NSCalendarMatchStrictly, (1 << 1))
        self.assertEqual(Foundation.NSCalendarSearchBackwards, (1 << 2))
        self.assertEqual(
            Foundation.NSCalendarMatchPreviousTimePreservingSmallerUnits, (1 << 8)
        )
        self.assertEqual(
            Foundation.NSCalendarMatchNextTimePreservingSmallerUnits, (1 << 9)
        )
        self.assertEqual(Foundation.NSCalendarMatchNextTime, (1 << 10))
        self.assertEqual(Foundation.NSCalendarMatchFirst, (1 << 12))
        self.assertEqual(Foundation.NSCalendarMatchLast, (1 << 13))

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(
            Foundation.NSQuarterCalendarUnit, CoreFoundation.kCFCalendarUnitQuarter
        )

        self.assertIsInstance(Foundation.NSCalendarIdentifierGregorian, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierBuddhist, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierChinese, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierCoptic, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierEthiopicAmeteMihret, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierEthiopicAmeteAlem, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierHebrew, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierISO8601, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierIndian, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierIslamic, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierIslamicCivil, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierJapanese, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierPersian, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierRepublicOfChina, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(
            Foundation.NSWeekOfMonthCalendarUnit,
            CoreFoundation.kCFCalendarUnitWeekOfMonth,
        )
        self.assertEqual(
            Foundation.NSWeekOfYearCalendarUnit,
            CoreFoundation.kCFCalendarUnitWeekOfYear,
        )
        self.assertEqual(
            Foundation.NSYearForWeekOfYearCalendarUnit,
            CoreFoundation.kCFCalendarUnitYearForWeekOfYear,
        )
        self.assertEqual(Foundation.NSCalendarCalendarUnit, (1 << 20))
        self.assertEqual(Foundation.NSTimeZoneCalendarUnit, (1 << 21))

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Foundation.NSCalendarDayChangedNotification, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Foundation.NSCalendarIdentifierIslamicTabular, str)
        self.assertIsInstance(Foundation.NSCalendarIdentifierIslamicUmmAlQura, str)

    @min_os_level("10.5")
    def testMethods10_5(self):
        Foundation.NSCalendar.currentCalendar()

        self.assertResultIsBOOL(
            Foundation.NSCalendar.rangeOfUnit_startDate_interval_forDate_
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.rangeOfUnit_startDate_interval_forDate_, 1
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.rangeOfUnit_startDate_interval_forDate_, 2
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(Foundation.NSDateComponents.isLeapMonth)
        self.assertArgIsBOOL(Foundation.NSDateComponents.setLeapMonth_, 0)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsOut(Foundation.NSCalendar.getEra_year_month_day_fromDate_, 0)
        self.assertArgIsOut(Foundation.NSCalendar.getEra_year_month_day_fromDate_, 1)
        self.assertArgIsOut(Foundation.NSCalendar.getEra_year_month_day_fromDate_, 2)
        self.assertArgIsOut(Foundation.NSCalendar.getEra_year_month_day_fromDate_, 3)

        self.assertArgIsOut(
            Foundation.NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_,
            0,
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_,
            1,
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_,
            2,
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_,
            3,
        )

        self.assertArgIsOut(
            Foundation.NSCalendar.getHour_minute_second_nanosecond_fromDate_, 0
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.getHour_minute_second_nanosecond_fromDate_, 1
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.getHour_minute_second_nanosecond_fromDate_, 2
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.getHour_minute_second_nanosecond_fromDate_, 3
        )

        self.assertResultIsBOOL(
            Foundation.NSCalendar.isDate_equalToDate_toUnitGranularity_
        )
        self.assertResultIsBOOL(Foundation.NSCalendar.isDate_inSameDayAsDate_)
        self.assertResultIsBOOL(Foundation.NSCalendar.isDateInToday_)
        self.assertResultIsBOOL(Foundation.NSCalendar.isDateInTomorrow_)
        self.assertResultIsBOOL(Foundation.NSCalendar.isDateInWeekend_)
        self.assertResultIsBOOL(
            Foundation.NSCalendar.rangeOfWeekendStartDate_interval_containingDate_
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.rangeOfWeekendStartDate_interval_containingDate_, 0
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.rangeOfWeekendStartDate_interval_containingDate_, 1
        )
        self.assertResultIsBOOL(
            Foundation.NSCalendar.nextWeekendStartDate_interval_options_afterDate_
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.nextWeekendStartDate_interval_options_afterDate_, 0
        )
        self.assertArgIsOut(
            Foundation.NSCalendar.nextWeekendStartDate_interval_options_afterDate_, 1
        )
        self.assertArgIsBlock(
            Foundation.NSCalendar.enumerateDatesStartingAfterDate_matchingComponents_options_usingBlock_,  # noqa: B950
            3,
            b"v@Zo^Z",
        )
        self.assertResultIsBOOL(Foundation.NSCalendar.date_matchesComponents_)

        self.assertResultIsBOOL(Foundation.NSDateComponents.isValidDate)
        self.assertResultIsBOOL(Foundation.NSDateComponents.isValidDateInCalendar_)
