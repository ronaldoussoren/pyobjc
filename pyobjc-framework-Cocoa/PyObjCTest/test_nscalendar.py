from PyObjCTools.TestSupport import *

from Foundation import *
import Foundation


class TestNSCalendar (TestCase):
    def testConstants(self):
        self.assertEquals( NSEraCalendarUnit, kCFCalendarUnitEra)
        self.assertEquals( NSYearCalendarUnit, kCFCalendarUnitYear)
        self.assertEquals( NSMonthCalendarUnit, kCFCalendarUnitMonth)
        self.assertEquals( NSDayCalendarUnit, kCFCalendarUnitDay)
        self.assertEquals( NSHourCalendarUnit, kCFCalendarUnitHour)
        self.assertEquals( NSMinuteCalendarUnit, kCFCalendarUnitMinute)
        self.assertEquals( NSSecondCalendarUnit, kCFCalendarUnitSecond)
        self.assertEquals( NSWeekCalendarUnit, kCFCalendarUnitWeek)
        self.assertEquals( NSWeekdayCalendarUnit, kCFCalendarUnitWeekday)
        self.assertEquals( NSWeekdayOrdinalCalendarUnit, kCFCalendarUnitWeekdayOrdinal)

        self.assertEquals( NSWrapCalendarComponents, kCFCalendarComponentsWrap)

        self.assertEquals( NSUndefinedDateComponent, NSIntegerMax)

    @min_os_level('10.5')
    def testMethods10_5(self):
        obj = NSCalendar.currentCalendar()

        self.failUnlessResultIsBOOL(NSCalendar.rangeOfUnit_startDate_interval_forDate_)
        self.failUnlessArgIsOut(NSCalendar.rangeOfUnit_startDate_interval_forDate_, 1)
        self.failUnlessArgIsOut(NSCalendar.rangeOfUnit_startDate_interval_forDate_, 2)


if __name__ == "__main__":
    main()
