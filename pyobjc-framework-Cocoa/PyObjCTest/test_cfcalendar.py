import datetime
import objc

import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level

NSCalendar = objc.lookUpClass("NSCalendar")
NSLocale = objc.lookUpClass("NSLocale")


class TestCFCalendarVariadic(TestCase):
    def testCFCalendarComposeAbsoluteTime(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFGregorianCalendar
        )
        self.assertIsInstance(calendar, NSCalendar)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(calendar, None, b"")
        self.assertEqual(success, True)
        self.assertIsInstance(at, float)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
            calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at, float)

    def testCFCalendarAddComponents(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFGregorianCalendar
        )
        self.assertIsInstance(calendar, NSCalendar)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
            calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at, float)

        success, at2 = CoreFoundation.CFCalendarAddComponents(
            calendar, at, 0, b"yH", 2, 3
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at2, float)

        success, y, H = CoreFoundation.CFCalendarGetComponentDifference(
            calendar, at, at2, 0, b"yH"
        )
        self.assertEqual(success, True)
        self.assertEqual(y, 2)
        self.assertEqual(H, 3)

    def testCFCalendarDecomposeAbsoluteTime(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFGregorianCalendar
        )
        self.assertTrue(calendar is not None)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
            calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at, float)

        success, y, M, d, H, m, s = CoreFoundation.CFCalendarDecomposeAbsoluteTime(
            calendar, at, b"yMdHms"
        )
        self.assertEqual(y, 1965)
        self.assertEqual(M, 1)
        self.assertEqual(d, 6)
        self.assertEqual(H, 14)
        self.assertEqual(m, 10)
        self.assertEqual(s, 0)

    def testCFCalendarGetComponentDifference(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFGregorianCalendar
        )
        self.assertTrue(calendar is not None)

        success, at1 = CoreFoundation.CFCalendarComposeAbsoluteTime(
            calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at1, float)

        success, at2 = CoreFoundation.CFCalendarComposeAbsoluteTime(
            calendar, None, b"yMdHms", 1967, 2, 6, 14, 10, 0
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at2, float)

        success, y, M = CoreFoundation.CFCalendarGetComponentDifference(
            calendar, at1, at2, 0, b"yM"
        )
        self.assertEqual(success, True)
        self.assertEqual(y, 2)
        self.assertEqual(M, 1)

    def testTypeID(self):
        v = CoreFoundation.CFCalendarGetTypeID()
        self.assertIsInstance(v, int)

    def testCreation(self):
        cal = CoreFoundation.CFCalendarCopyCurrent()
        self.assertIsInstance(cal, NSCalendar)
        cal = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFBuddhistCalendar
        )
        self.assertIsInstance(cal, NSCalendar)

    def testInspection(self):
        cal = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFGregorianCalendar
        )
        self.assertIsInstance(cal, NSCalendar)
        name = CoreFoundation.CFCalendarGetIdentifier(cal)
        self.assertEqual(name, CoreFoundation.kCFGregorianCalendar)
        locale = CoreFoundation.CFCalendarCopyLocale(cal)
        self.assertIsInstance(locale, NSLocale)
        timezone = CoreFoundation.CFCalendarCopyTimeZone(cal)
        self.assertIsInstance(timezone, CoreFoundation.CFTimeZoneRef)
        weekday = CoreFoundation.CFCalendarGetFirstWeekday(cal)
        self.assertLessEqual(0 <= weekday, 7)
        num = CoreFoundation.CFCalendarGetMinimumDaysInFirstWeek(cal)
        self.assertLessEqual(0 <= num, 7)
        rng = CoreFoundation.CFCalendarGetMinimumRangeOfUnit(
            cal, CoreFoundation.kCFCalendarUnitEra
        )
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        rng = CoreFoundation.CFCalendarGetMaximumRangeOfUnit(
            cal, CoreFoundation.kCFCalendarUnitEra
        )
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        m = datetime.date.today()
        if m.month in (1, 3, 5, 7, 8, 10, 12):
            monthLength = 31
        elif m.month in (4, 6, 9, 11):
            monthLength = 30
        else:
            if m.year % 4 == 0:
                # Yes this is wrong, but the next time this fails in
                # in 2100.
                monthLength = 29
            else:
                monthLength = 28
        rng = CoreFoundation.CFCalendarGetRangeOfUnit(
            cal,
            CoreFoundation.kCFCalendarUnitDay,
            CoreFoundation.kCFCalendarUnitMonth,
            CoreFoundation.CFAbsoluteTimeGetCurrent(),
        )
        self.assertIsInstance(rng, CoreFoundation.CFRange)
        self.assertEqual(rng.location, 1)
        self.assertEqual(rng.length, monthLength)

        v = CoreFoundation.CFCalendarGetOrdinalityOfUnit(
            cal,
            CoreFoundation.kCFCalendarUnitDay,
            CoreFoundation.kCFCalendarUnitYear,
            CoreFoundation.CFAbsoluteTimeGetCurrent(),
        )
        self.assertIsInstance(v, int)
        ok, startp, tip = CoreFoundation.CFCalendarGetTimeRangeOfUnit(
            cal,
            CoreFoundation.kCFCalendarUnitDay,
            CoreFoundation.CFAbsoluteTimeGetCurrent(),
            None,
            None,
        )
        self.assertIs(ok, True)
        self.assertIsInstance(startp, float)
        self.assertIsInstance(tip, float)
        self.assertIn(tip, (86400.0, 90000.0, 82800))  # 1 day, remove DST, add DST

    def testMutation(self):
        cal = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFBuddhistCalendar
        )

        loc = CoreFoundation.CFLocaleCreate(None, "mr_IN")
        self.assertIsInstance(loc, NSLocale)
        id1 = CoreFoundation.CFLocaleGetIdentifier(loc)

        orig_loc = CoreFoundation.CFCalendarCopyLocale(cal)
        self.assertIsInstance(orig_loc, NSLocale)
        orig_id = CoreFoundation.CFLocaleGetIdentifier(orig_loc)
        CoreFoundation.CFCalendarSetLocale(cal, loc)
        new_loc = CoreFoundation.CFCalendarCopyLocale(cal)
        self.assertIsInstance(new_loc, NSLocale)
        new_id = CoreFoundation.CFLocaleGetIdentifier(new_loc)

        self.assertEqual(new_id, id1)
        self.assertNotEqual(orig_id, id1)
        tz = CoreFoundation.CFTimeZoneCreateWithName(None, "Pacific/Wallis", True)
        self.assertIsInstance(tz, CoreFoundation.CFTimeZoneRef)
        orig_zone = CoreFoundation.CFCalendarCopyTimeZone(cal)
        self.assertIsInstance(orig_zone, CoreFoundation.CFTimeZoneRef)
        CoreFoundation.CFCalendarSetTimeZone(cal, tz)
        new_zone = CoreFoundation.CFCalendarCopyTimeZone(cal)
        self.assertIsInstance(new_zone, CoreFoundation.CFTimeZoneRef)
        self.assertEqual(CoreFoundation.CFTimeZoneGetName(new_zone), "Pacific/Wallis")
        weekday = CoreFoundation.CFCalendarGetFirstWeekday(cal)
        weekday = weekday + 2 % 7
        CoreFoundation.CFCalendarSetFirstWeekday(cal, weekday)
        new = CoreFoundation.CFCalendarGetFirstWeekday(cal)
        self.assertEqual(new, weekday)
        num = CoreFoundation.CFCalendarGetMinimumDaysInFirstWeek(cal)
        if num == 1:
            num = 2
        else:
            num = 1

        CoreFoundation.CFCalendarSetMinimumDaysInFirstWeek(cal, num)
        num2 = CoreFoundation.CFCalendarGetMinimumDaysInFirstWeek(cal)
        self.assertEqual(num2, num)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFCalendarUnitEra, 1 << 1)
        self.assertEqual(CoreFoundation.kCFCalendarUnitYear, 1 << 2)
        self.assertEqual(CoreFoundation.kCFCalendarUnitMonth, 1 << 3)
        self.assertEqual(CoreFoundation.kCFCalendarUnitDay, 1 << 4)
        self.assertEqual(CoreFoundation.kCFCalendarUnitHour, 1 << 5)
        self.assertEqual(CoreFoundation.kCFCalendarUnitMinute, 1 << 6)
        self.assertEqual(CoreFoundation.kCFCalendarUnitSecond, 1 << 7)
        self.assertEqual(CoreFoundation.kCFCalendarUnitWeek, 1 << 8)
        self.assertEqual(CoreFoundation.kCFCalendarUnitWeekday, 1 << 9)
        self.assertEqual(CoreFoundation.kCFCalendarUnitWeekdayOrdinal, 1 << 10)
        self.assertEqual(CoreFoundation.kCFCalendarComponentsWrap, 1 << 0)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(CoreFoundation.kCFCalendarUnitQuarter, 1 << 11)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(CoreFoundation.kCFCalendarUnitWeekOfMonth, 1 << 12)
        self.assertEqual(CoreFoundation.kCFCalendarUnitWeekOfYear, 1 << 13)
        self.assertEqual(CoreFoundation.kCFCalendarUnitYearForWeekOfYear, 1 << 14)
