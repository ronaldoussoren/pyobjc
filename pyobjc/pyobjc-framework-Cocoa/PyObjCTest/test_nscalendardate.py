from PyObjCTools.TestSupport import *
from Foundation import *

class TestNSCalendarDate (TestCase):
    def testOutput(self):
        obj = NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
                2008, 12, 05, 14, 15, 16, NSTimeZone.systemTimeZone())
        obj2 = NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
                2007, 9, 8, 19, 12, 10, NSTimeZone.systemTimeZone())

        m = obj.years_months_days_hours_minutes_seconds_sinceDate_.__metadata__()
        self.failUnless(m['arguments'][2]['type'].startswith('o^'))
        self.failUnless(m['arguments'][3]['type'].startswith('o^'))
        self.failUnless(m['arguments'][4]['type'].startswith('o^'))
        self.failUnless(m['arguments'][5]['type'].startswith('o^'))
        self.failUnless(m['arguments'][6]['type'].startswith('o^'))
        self.failUnless(m['arguments'][7]['type'].startswith('o^'))

        years, months, days, hours, minutes, seconds = obj.years_months_days_hours_minutes_seconds_sinceDate_(None, None, None, None, None, None, obj2)
        self.assertEquals(years, 1)
        self.assertEquals(months, 2)
        self.assertEquals(days, 26)
        self.assertEquals(hours, 19)
        self.assertEquals(minutes, 3)
        self.assertEquals(seconds, 6)

if __name__ == "__main__":
    main()
