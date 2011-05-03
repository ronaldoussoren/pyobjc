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

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual( NSQuarterCalendarUnit, kCFCalendarUnitQuarter)

    @min_os_level('10.5')
    def testMethods10_5(self):
        obj = NSCalendar.currentCalendar()

        self.assertResultIsBOOL(NSCalendar.rangeOfUnit_startDate_interval_forDate_)
        self.assertArgIsOut(NSCalendar.rangeOfUnit_startDate_interval_forDate_, 1)
        self.assertArgIsOut(NSCalendar.rangeOfUnit_startDate_interval_forDate_, 2)


if __name__ == "__main__":
    main()
