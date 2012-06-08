from PyObjCTools.TestSupport import *
import time
from CoreFoundation import *
from Foundation import NSDate


try:
    long
except NameError:
    long = int


class TestDate (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFDateRef)
        self.assertIsCFType(CFTimeZoneRef)

    def testTypeID(self):
        v = CFDateGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testConstants(self):
        self.assertIsInstance(kCFAbsoluteTimeIntervalSince1970, float)
        self.assertIsInstance(kCFAbsoluteTimeIntervalSince1904, float)
        self.assertEqual(kCFGregorianUnitsYears , (1 << 0))
        self.assertEqual(kCFGregorianUnitsMonths , (1 << 1))
        self.assertEqual(kCFGregorianUnitsDays , (1 << 2))
        self.assertEqual(kCFGregorianUnitsHours , (1 << 3))
        self.assertEqual(kCFGregorianUnitsMinutes , (1 << 4))
        self.assertEqual(kCFGregorianUnitsSeconds , (1 << 5))
        self.assertEqual(kCFGregorianAllUnits , 0x00FFFFFF)

    def testStructs(self):
        v = CFGregorianDate()
        self.assertHasAttr(v, 'year')
        self.assertHasAttr(v, 'month')
        self.assertHasAttr(v, 'day')
        self.assertHasAttr(v, 'hour')
        self.assertHasAttr(v, 'minute')
        self.assertHasAttr(v, 'second')

        v = CFGregorianUnits()
        self.assertHasAttr(v, 'years')
        self.assertHasAttr(v, 'months')
        self.assertHasAttr(v, 'days')
        self.assertHasAttr(v, 'hours')
        self.assertHasAttr(v, 'minutes')
        self.assertHasAttr(v, 'seconds')

    def testAbsoluteTime(self):
        v = CFAbsoluteTimeGetCurrent()
        self.assertIsInstance(v, float)
        self.assertLessThan(abs(v - time.time() + kCFAbsoluteTimeIntervalSince1970) , 1.0)

    def testCreation(self):
        now = CFAbsoluteTimeGetCurrent()
        dt = CFDateCreate(None, now)
        self.assertIsInstance(dt, NSDate)

    def testInspection(self):
        now = CFAbsoluteTimeGetCurrent()
        nowtm = time.localtime()
        dt = CFDateCreate(None, now)
        self.assertIsInstance(dt, NSDate)
        self.assertEqual(CFDateGetAbsoluteTime(dt) , now)
        dt2 = CFDateCreate(None, now + 1000)
        self.assertEqual(CFDateGetTimeIntervalSinceDate(dt2, dt) , 1000)
        cmp = CFDateCompare(dt, dt2, 0)
        self.assertLessThan(cmp , 0)
        dt = CFGregorianDate()
        dt.month = 12
        self.assertIs(CFGregorianDateIsValid(dt, kCFGregorianUnitsMonths), True)
        dt.month = 99
        self.assertIs(CFGregorianDateIsValid(dt, kCFGregorianUnitsMonths), False)
        tz = CFTimeZoneCopyDefault()
        dt.year = 2008
        dt.day = 1
        dt.month = 1
        abstime = CFGregorianDateGetAbsoluteTime(dt, tz)
        self.assertIsInstance(abstime, float)
        dt = CFAbsoluteTimeGetGregorianDate(now, tz)
        self.assertEqual(dt.year , nowtm.tm_year)
        self.assertEqual(dt.month , nowtm.tm_mon)
        self.assertEqual(dt.day , nowtm.tm_mday)
        self.assertEqual(dt.hour , nowtm.tm_hour)
        self.assertEqual(dt.minute , nowtm.tm_min)
        units = CFGregorianUnits(days = 1)
        stamp = CFAbsoluteTimeAddGregorianUnits(now, tz, units)
        self.assertEqual(stamp - now , 24 * 3600)
        units = CFAbsoluteTimeGetDifferenceAsGregorianUnits(stamp, now, tz, kCFGregorianAllUnits)
        self.assertEqual(units.days , 1)
        self.assertEqual(units.seconds , 0)
        v = CFAbsoluteTimeGetDayOfWeek(now, tz)
        self.assertEqual(v , nowtm.tm_wday+1)
        v = CFAbsoluteTimeGetDayOfYear(now, tz)
        self.assertEqual(v , nowtm.tm_yday)
        v = CFAbsoluteTimeGetWeekOfYear(now, tz)
        self.assertIsInstance(v, (int, long))

if __name__ == "__main__":
    main()
