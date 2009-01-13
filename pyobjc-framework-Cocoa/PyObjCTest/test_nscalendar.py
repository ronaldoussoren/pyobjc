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

    def testOutput(self):
        obj = NSCalendar.currentCalendar()

        m = obj.rangeOfUnit_startDate_interval_forDate_.__metadata__()
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))


if __name__ == "__main__":
    main()
