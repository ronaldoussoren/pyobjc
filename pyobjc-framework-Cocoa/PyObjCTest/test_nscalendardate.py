import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSCalendarDate(TestCase):
    def testOutput(self):
        obj = Foundation.NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
            2008, 12, 5, 14, 15, 16, Foundation.NSTimeZone.systemTimeZone()
        )
        obj2 = Foundation.NSCalendarDate.dateWithYear_month_day_hour_minute_second_timeZone_(
            2007, 9, 8, 19, 12, 10, Foundation.NSTimeZone.systemTimeZone()
        )

        m = obj.years_months_days_hours_minutes_seconds_sinceDate_
        self.assertArgIsOut(m, 0)
        self.assertArgIsOut(m, 1)
        self.assertArgIsOut(m, 2)
        self.assertArgIsOut(m, 3)
        self.assertArgIsOut(m, 4)
        self.assertArgIsOut(m, 5)

        (
            years,
            months,
            days,
            hours,
            minutes,
            seconds,
        ) = obj.years_months_days_hours_minutes_seconds_sinceDate_(
            None, None, None, None, None, None, obj2
        )
        self.assertEqual(years, 1)
        self.assertEqual(months, 2)
        self.assertEqual(days, 26)
        self.assertEqual(hours, 19)
        self.assertEqual(minutes, 3)
        self.assertEqual(seconds, 6)
