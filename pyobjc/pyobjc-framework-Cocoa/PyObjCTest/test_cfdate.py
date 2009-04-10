from PyObjCTools.TestSupport import *
import time
from CoreFoundation import *


class TestDate (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFDateRef)
        self.failUnlessIsCFType(CFTimeZoneRef)

    def testTypeID(self):
        v = CFDateGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testConstants(self):
        self.failUnless(isinstance(kCFAbsoluteTimeIntervalSince1970, float))
        self.failUnless(isinstance(kCFAbsoluteTimeIntervalSince1904, float))

        self.failUnless(kCFGregorianUnitsYears == (1 << 0))
        self.failUnless(kCFGregorianUnitsMonths == (1 << 1))
        self.failUnless(kCFGregorianUnitsDays == (1 << 2))
        self.failUnless(kCFGregorianUnitsHours == (1 << 3))
        self.failUnless(kCFGregorianUnitsMinutes == (1 << 4))
        self.failUnless(kCFGregorianUnitsSeconds == (1 << 5))
        self.failUnless(kCFGregorianAllUnits == 0x00FFFFFF)

    def testStructs(self):
        v = CFGregorianDate()
        self.failUnless(hasattr(v, 'year'))
        self.failUnless(hasattr(v, 'month'))
        self.failUnless(hasattr(v, 'day'))
        self.failUnless(hasattr(v, 'hour'))
        self.failUnless(hasattr(v, 'minute'))
        self.failUnless(hasattr(v, 'second'))

        v = CFGregorianUnits()
        self.failUnless(hasattr(v, 'years'))
        self.failUnless(hasattr(v, 'months'))
        self.failUnless(hasattr(v, 'days'))
        self.failUnless(hasattr(v, 'hours'))
        self.failUnless(hasattr(v, 'minutes'))
        self.failUnless(hasattr(v, 'seconds'))


    def testAbsoluteTime(self):
        v = CFAbsoluteTimeGetCurrent()
        self.failUnless(isinstance(v, float))
        self.failUnless(abs(v - time.time() + kCFAbsoluteTimeIntervalSince1970) < 1.0)

    def testCreation(self):
        now = CFAbsoluteTimeGetCurrent()
        dt = CFDateCreate(None, now)
        self.failUnless(isinstance(dt, CFDateRef))

    def testInspection(self):
        now = CFAbsoluteTimeGetCurrent()
        nowtm = time.localtime()
        dt = CFDateCreate(None, now)
        self.failUnless(isinstance(dt, CFDateRef))
        self.failUnless(CFDateGetAbsoluteTime(dt) == now)

        dt2 = CFDateCreate(None, now + 1000)
        self.failUnless(CFDateGetTimeIntervalSinceDate(dt2, dt) == 1000)

        cmp = CFDateCompare(dt, dt2, 0)
        self.failUnless(cmp < 0)

        dt = CFGregorianDate()
        dt.month = 12
        self.failUnless(CFGregorianDateIsValid(dt, kCFGregorianUnitsMonths) is True)
        dt.month = 99
        self.failUnless(CFGregorianDateIsValid(dt, kCFGregorianUnitsMonths) is False)

        tz = CFTimeZoneCopyDefault()
        dt.year = 2008
        dt.day = 1
        dt.month = 1
        abstime = CFGregorianDateGetAbsoluteTime(dt, tz)
        self.failUnless(isinstance(abstime, float))

        dt = CFAbsoluteTimeGetGregorianDate(now, tz)
        self.failUnless(dt.year == nowtm.tm_year)
        self.failUnless(dt.month == nowtm.tm_mon)
        self.failUnless(dt.day == nowtm.tm_mday)
        self.failUnless(dt.hour == nowtm.tm_hour)
        self.failUnless(dt.minute == nowtm.tm_min)

        units = CFGregorianUnits(days = 1)
        stamp = CFAbsoluteTimeAddGregorianUnits(now, tz, units)
        self.failUnless(stamp - now == 24 * 3600)

        units = CFAbsoluteTimeGetDifferenceAsGregorianUnits(stamp, now, tz, kCFGregorianAllUnits)
        self.failUnless(units.days == 1)
        self.failUnless(units.seconds == 0)

        v = CFAbsoluteTimeGetDayOfWeek(now, tz)
        self.failUnless(v == nowtm.tm_wday+1)

        v = CFAbsoluteTimeGetDayOfYear(now, tz)
        self.failUnless(v == nowtm.tm_yday)

        v = CFAbsoluteTimeGetWeekOfYear(now, tz)
        self.failUnless(isinstance(v, (int, long)))

        

if __name__ == "__main__":
    main()
