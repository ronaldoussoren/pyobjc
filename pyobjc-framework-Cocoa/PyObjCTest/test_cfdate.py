import time
import objc

import CoreFoundation
from Foundation import NSDate
from PyObjCTools.TestSupport import TestCase


class TestDate(TestCase):
    def testTypes(self):
        try:
            cls = objc.lookUpClass("__NSDate")
            self.assertIs(cls, CoreFoundation.CFDateRef)
        except objc.error:
            try:
                cls = objc.lookUpClass("__NSCFDate")
                self.assertIs(cls, CoreFoundation.CFDateRef)
            except objc.error:
                self.assertIsCFType(CoreFoundation.CFDateRef)

        try:
            cls = objc.lookUpClass("NSTimeZone")
            self.assertIs(cls, CoreFoundation.CFTimeZoneRef)
        except objc.error:
            self.assertIsCFType(CoreFoundation.CFTimeZoneRef)

    def testTypeID(self):
        v = CoreFoundation.CFDateGetTypeID()
        self.assertIsInstance(v, int)

    def testConstants(self):
        self.assertIsInstance(CoreFoundation.kCFAbsoluteTimeIntervalSince1970, float)
        self.assertIsInstance(CoreFoundation.kCFAbsoluteTimeIntervalSince1904, float)
        self.assertEqual(CoreFoundation.kCFGregorianUnitsYears, (1 << 0))
        self.assertEqual(CoreFoundation.kCFGregorianUnitsMonths, (1 << 1))
        self.assertEqual(CoreFoundation.kCFGregorianUnitsDays, (1 << 2))
        self.assertEqual(CoreFoundation.kCFGregorianUnitsHours, (1 << 3))
        self.assertEqual(CoreFoundation.kCFGregorianUnitsMinutes, (1 << 4))
        self.assertEqual(CoreFoundation.kCFGregorianUnitsSeconds, (1 << 5))
        self.assertEqual(CoreFoundation.kCFGregorianAllUnits, 0x00FFFFFF)

    def testStructs(self):
        v = CoreFoundation.CFGregorianDate()
        self.assertHasAttr(v, "year")
        self.assertHasAttr(v, "month")
        self.assertHasAttr(v, "day")
        self.assertHasAttr(v, "hour")
        self.assertHasAttr(v, "minute")
        self.assertHasAttr(v, "second")

        self.assertPickleRoundTrips(v)

        v = CoreFoundation.CFGregorianUnits()
        self.assertHasAttr(v, "years")
        self.assertHasAttr(v, "months")
        self.assertHasAttr(v, "days")
        self.assertHasAttr(v, "hours")
        self.assertHasAttr(v, "minutes")
        self.assertHasAttr(v, "seconds")

        self.assertPickleRoundTrips(v)

    def testAbsoluteTime(self):
        v = CoreFoundation.CFAbsoluteTimeGetCurrent()
        self.assertIsInstance(v, float)
        self.assertLess(
            abs(v - time.time() + CoreFoundation.kCFAbsoluteTimeIntervalSince1970), 1.0
        )

    def testCreation(self):
        now = CoreFoundation.CFAbsoluteTimeGetCurrent()
        dt = CoreFoundation.CFDateCreate(None, now)
        self.assertIsInstance(dt, NSDate)

    def testInspection(self):
        now = CoreFoundation.CFAbsoluteTimeGetCurrent()
        nowtm = time.localtime()
        dt = CoreFoundation.CFDateCreate(None, now)
        self.assertIsInstance(dt, NSDate)
        self.assertEqual(CoreFoundation.CFDateGetAbsoluteTime(dt), now)
        dt2 = CoreFoundation.CFDateCreate(None, now + 1000)
        self.assertEqual(CoreFoundation.CFDateGetTimeIntervalSinceDate(dt2, dt), 1000)
        cmp = CoreFoundation.CFDateCompare(dt, dt2, 0)
        self.assertLess(cmp, 0)
        dt = CoreFoundation.CFGregorianDate()
        dt.month = 12
        self.assertIs(
            CoreFoundation.CFGregorianDateIsValid(
                dt, CoreFoundation.kCFGregorianUnitsMonths
            ),
            True,
        )
        dt.month = 99
        self.assertIs(
            CoreFoundation.CFGregorianDateIsValid(
                dt, CoreFoundation.kCFGregorianUnitsMonths
            ),
            False,
        )
        tz = CoreFoundation.CFTimeZoneCopyDefault()
        dt.year = 2008
        dt.day = 1
        dt.month = 1
        abstime = CoreFoundation.CFGregorianDateGetAbsoluteTime(dt, tz)
        self.assertIsInstance(abstime, float)
        dt = CoreFoundation.CFAbsoluteTimeGetGregorianDate(now, tz)
        self.assertEqual(dt.year, nowtm.tm_year)
        self.assertEqual(dt.month, nowtm.tm_mon)
        self.assertEqual(dt.day, nowtm.tm_mday)
        self.assertEqual(dt.hour, nowtm.tm_hour)
        self.assertEqual(dt.minute, nowtm.tm_min)
        units = CoreFoundation.CFGregorianUnits(days=1)
        stamp = CoreFoundation.CFAbsoluteTimeAddGregorianUnits(now, tz, units)

        # XXX: This is wrong during summer time.
        self.assertIn(stamp - now, (23 * 3600, 24 * 3600, 25 * 3600))
        units = CoreFoundation.CFAbsoluteTimeGetDifferenceAsGregorianUnits(
            stamp, now, tz, CoreFoundation.kCFGregorianAllUnits
        )
        self.assertEqual(units.days, 1)
        self.assertEqual(units.seconds, 0)
        v = CoreFoundation.CFAbsoluteTimeGetDayOfWeek(now, tz)
        self.assertEqual(v, nowtm.tm_wday + 1)
        v = CoreFoundation.CFAbsoluteTimeGetDayOfYear(now, tz)
        self.assertEqual(v, nowtm.tm_yday)
        v = CoreFoundation.CFAbsoluteTimeGetWeekOfYear(now, tz)
        self.assertIsInstance(v, int)
