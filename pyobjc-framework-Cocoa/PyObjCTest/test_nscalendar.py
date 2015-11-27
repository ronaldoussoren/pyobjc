from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation


class TestNSCalendar (TestCase):
    def testConstants(self):
        self.assertEqual( NSEraCalendarUnit, kCFCalendarUnitEra)
        self.assertEqual( NSYearCalendarUnit, kCFCalendarUnitYear)
        self.assertEqual( NSMonthCalendarUnit, kCFCalendarUnitMonth)
        self.assertEqual( NSDayCalendarUnit, kCFCalendarUnitDay)
        self.assertEqual( NSHourCalendarUnit, kCFCalendarUnitHour)
        self.assertEqual( NSMinuteCalendarUnit, kCFCalendarUnitMinute)
        self.assertEqual( NSSecondCalendarUnit, kCFCalendarUnitSecond)
        self.assertEqual( NSWeekCalendarUnit, kCFCalendarUnitWeek)
        self.assertEqual( NSWeekdayCalendarUnit, kCFCalendarUnitWeekday)
        self.assertEqual( NSWeekdayOrdinalCalendarUnit, kCFCalendarUnitWeekdayOrdinal)

        self.assertEqual( NSWrapCalendarComponents, kCFCalendarComponentsWrap)

        self.assertEqual( NSUndefinedDateComponent, NSIntegerMax)
        self.assertEqual( NSDateComponentUndefined, NSIntegerMax)

        self.assertEqual(NSCalendarUnitEra, kCFCalendarUnitEra)
        self.assertEqual(NSCalendarUnitYear, kCFCalendarUnitYear)
        self.assertEqual(NSCalendarUnitMonth, kCFCalendarUnitMonth)
        self.assertEqual(NSCalendarUnitDay, kCFCalendarUnitDay)
        self.assertEqual(NSCalendarUnitHour, kCFCalendarUnitHour)
        self.assertEqual(NSCalendarUnitMinute, kCFCalendarUnitMinute)
        self.assertEqual(NSCalendarUnitSecond, kCFCalendarUnitSecond)
        self.assertEqual(NSCalendarUnitWeekday, kCFCalendarUnitWeekday)
        self.assertEqual(NSCalendarUnitWeekdayOrdinal, kCFCalendarUnitWeekdayOrdinal)
        self.assertEqual(NSCalendarUnitQuarter, kCFCalendarUnitQuarter)
        self.assertEqual(NSCalendarUnitWeekOfMonth, kCFCalendarUnitWeekOfMonth)
        self.assertEqual(NSCalendarUnitWeekOfYear, kCFCalendarUnitWeekOfYear)
        self.assertEqual(NSCalendarUnitYearForWeekOfYear, kCFCalendarUnitYearForWeekOfYear)
        self.assertEqual(NSCalendarUnitNanosecond, (1 << 15))
        self.assertEqual(NSCalendarUnitCalendar, (1 << 20))
        self.assertEqual(NSCalendarUnitTimeZone, (1 << 21))
        self.assertEqual(NSCalendarWrapComponents, (1 << 0))
        self.assertEqual(NSCalendarMatchStrictly, (1 << 1))
        self.assertEqual(NSCalendarSearchBackwards, (1 << 2))
        self.assertEqual(NSCalendarMatchPreviousTimePreservingSmallerUnits, (1 << 8))
        self.assertEqual(NSCalendarMatchNextTimePreservingSmallerUnits, (1 << 9))
        self.assertEqual(NSCalendarMatchNextTime, (1 << 10))
        self.assertEqual(NSCalendarMatchFirst, (1 << 12))
        self.assertEqual(NSCalendarMatchLast, (1 << 13))


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual( NSQuarterCalendarUnit, kCFCalendarUnitQuarter)

        self.assertIsInstance(NSCalendarIdentifierGregorian, unicode)
        self.assertIsInstance(NSCalendarIdentifierBuddhist, unicode)
        self.assertIsInstance(NSCalendarIdentifierChinese, unicode)
        self.assertIsInstance(NSCalendarIdentifierCoptic, unicode)
        self.assertIsInstance(NSCalendarIdentifierEthiopicAmeteMihret, unicode)
        self.assertIsInstance(NSCalendarIdentifierEthiopicAmeteAlem, unicode)
        self.assertIsInstance(NSCalendarIdentifierHebrew, unicode)
        self.assertIsInstance(NSCalendarIdentifierISO8601, unicode)
        self.assertIsInstance(NSCalendarIdentifierIndian, unicode)
        self.assertIsInstance(NSCalendarIdentifierIslamic, unicode)
        self.assertIsInstance(NSCalendarIdentifierIslamicCivil, unicode)
        self.assertIsInstance(NSCalendarIdentifierJapanese, unicode)
        self.assertIsInstance(NSCalendarIdentifierPersian, unicode)
        self.assertIsInstance(NSCalendarIdentifierRepublicOfChina, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSWeekOfMonthCalendarUnit, kCFCalendarUnitWeekOfMonth)
        self.assertEqual(NSWeekOfYearCalendarUnit, kCFCalendarUnitWeekOfYear)
        self.assertEqual(NSYearForWeekOfYearCalendarUnit, kCFCalendarUnitYearForWeekOfYear)
        self.assertEqual(NSCalendarCalendarUnit, (1 << 20))
        self.assertEqual(NSTimeZoneCalendarUnit, (1 << 21))

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSCalendarDayChangedNotification, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSCalendarIdentifierIslamicTabular, unicode)
        self.assertIsInstance(NSCalendarIdentifierIslamicUmmAlQura, unicode)


    @min_os_level('10.5')
    def testMethods10_5(self):
        obj = NSCalendar.currentCalendar()

        self.assertResultIsBOOL(NSCalendar.rangeOfUnit_startDate_interval_forDate_)
        self.assertArgIsOut(NSCalendar.rangeOfUnit_startDate_interval_forDate_, 1)
        self.assertArgIsOut(NSCalendar.rangeOfUnit_startDate_interval_forDate_, 2)

    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(NSDateComponents.isLeapMonth)
        self.assertArgIsBOOL(NSDateComponents.setLeapMonth_, 0)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsOut(NSCalendar.getEra_year_month_day_fromDate_, 0)
        self.assertArgIsOut(NSCalendar.getEra_year_month_day_fromDate_, 1)
        self.assertArgIsOut(NSCalendar.getEra_year_month_day_fromDate_, 2)
        self.assertArgIsOut(NSCalendar.getEra_year_month_day_fromDate_, 3)

        self.assertArgIsOut(NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_, 0)
        self.assertArgIsOut(NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_, 1)
        self.assertArgIsOut(NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_, 2)
        self.assertArgIsOut(NSCalendar.getEra_yearForWeekOfYear_weekOfYear_weekday_fromDate_, 3)

        self.assertArgIsOut(NSCalendar.getHour_minute_second_nanosecond_fromDate_, 0)
        self.assertArgIsOut(NSCalendar.getHour_minute_second_nanosecond_fromDate_, 1)
        self.assertArgIsOut(NSCalendar.getHour_minute_second_nanosecond_fromDate_, 2)
        self.assertArgIsOut(NSCalendar.getHour_minute_second_nanosecond_fromDate_, 3)

        self.assertResultIsBOOL(NSCalendar.isDate_equalToDate_toUnitGranularity_)
        self.assertResultIsBOOL(NSCalendar.isDate_inSameDayAsDate_)
        self.assertResultIsBOOL(NSCalendar.isDateInToday_)
        self.assertResultIsBOOL(NSCalendar.isDateInTomorrow_)
        self.assertResultIsBOOL(NSCalendar.isDateInWeekend_)
        self.assertResultIsBOOL(NSCalendar.rangeOfWeekendStartDate_interval_containingDate_)
        self.assertArgIsOut(NSCalendar.rangeOfWeekendStartDate_interval_containingDate_, 0)
        self.assertArgIsOut(NSCalendar.rangeOfWeekendStartDate_interval_containingDate_, 1)
        self.assertResultIsBOOL(NSCalendar.nextWeekendStartDate_interval_options_afterDate_)
        self.assertArgIsOut(NSCalendar.nextWeekendStartDate_interval_options_afterDate_, 0)
        self.assertArgIsOut(NSCalendar.nextWeekendStartDate_interval_options_afterDate_, 1)
        self.assertArgIsBlock(NSCalendar.enumerateDatesStartingAfterDate_matchingComponents_options_usingBlock_, 3, b'v@Zo^Z')
        self.assertResultIsBOOL(NSCalendar.date_matchesComponents_)

        self.assertResultIsBOOL(NSDateComponents.isValidDate)
        self.assertResultIsBOOL(NSDateComponents.isValidDateInCalendar_)

if __name__ == "__main__":
    main()
