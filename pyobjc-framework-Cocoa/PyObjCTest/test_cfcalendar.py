import datetime
import objc

import CoreFoundation
from PyObjCTools.TestSupport import TestCase, NoObjCClass

NSCalendar = objc.lookUpClass("NSCalendar")
NSLocale = objc.lookUpClass("NSLocale")


class TestCFCalendarVariadic(TestCase):
    def test_cfcalendar_compose_absolute_time(self):
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

    def test_cfcalendar_add_components(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFGregorianCalendar
        )
        self.assertIsInstance(calendar, NSCalendar)

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
            calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at, float)

        with self.assertRaisesRegex(TypeError, "Expecting at least 4 arguments, got 0"):
            CoreFoundation.CFCalendarAddComponents()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFCalendarAddComponents(NoObjCClass(), at, 0, b"yH", 2, 3)

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            CoreFoundation.CFCalendarAddComponents(None, "tomorrow", 0, b"yH", 2, 3)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            CoreFoundation.CFCalendarAddComponents(None, at, "nil", b"yH", 2, 3)

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'str'"):
            CoreFoundation.CFCalendarAddComponents(None, at, 0, "yH", 2, 3)

        with self.assertRaisesRegex(TypeError, "Expecting 6 arguments, got 5"):
            success, at2 = CoreFoundation.CFCalendarAddComponents(
                calendar, at, 0, b"yH", 2
            )

        with self.assertRaisesRegex(TypeError, "Expecting 6 arguments, got 7"):
            success, at2 = CoreFoundation.CFCalendarAddComponents(
                calendar, at, 0, b"yH", 2, 3, 4
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            success, at2 = CoreFoundation.CFCalendarAddComponents(
                calendar, at, 0, b"yH", "two", 3
            )

        with self.assertRaisesRegex(
            TypeError, "At most 20 characters supported in componentDesc"
        ):
            success, at2 = CoreFoundation.CFCalendarAddComponents(
                calendar,
                at,
                0,
                b"yHMSSSSSSSSSSSSSSSSSSS",
                1,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
            )

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

    def test_cfcalendar_decompose_absolute_time(self):
        calendar = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFGregorianCalendar
        )
        self.assertTrue(calendar is not None)

        with self.assertRaisesRegex(TypeError, "Expecting at least 3 arguments, got 0"):
            CoreFoundation.CFCalendarComposeAbsoluteTime()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFCalendarComposeAbsoluteTime(
                NoObjCClass(), None, b"yMdHms", 1965, 1, 6, 14, 10, 0
            )

        with self.assertRaisesRegex(ValueError, "'at' must be None"):
            CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, 42, b"yMdHms", 1965, 1, 6, 14, 10, 0
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'str'"):
            CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'int', got 'str'"):
            CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", "last year", 1, 6, 14, 10, 0
            )

        with self.assertRaisesRegex(TypeError, "Expecting 9 arguments, got 8"):
            CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", "last year", 1, 6, 14, 10
            )

        with self.assertRaisesRegex(TypeError, "Expecting 9 arguments, got 10"):
            CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", "last year", 1, 6, 14, 10, 0, 23
            )

        with self.assertRaisesRegex(
            TypeError, "At most 20 characters supported in componentDesc"
        ):
            CoreFoundation.CFCalendarComposeAbsoluteTime(
                calendar,
                None,
                b"yMdHmsssssssssssssssssssss",
                "last year",
                1,
                6,
                14,
                10,
                0,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
                3,
            )

        success, at = CoreFoundation.CFCalendarComposeAbsoluteTime(
            calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0
        )
        self.assertEqual(success, True)
        self.assertIsInstance(at, float)

        with self.assertRaisesRegex(TypeError, "Expecting at least 3 arguments, got 0"):
            CoreFoundation.CFCalendarDecomposeAbsoluteTime()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFCalendarDecomposeAbsoluteTime(NoObjCClass(), at, b"yMdHms")

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            CoreFoundation.CFCalendarDecomposeAbsoluteTime(calendar, str(at), b"yMdHms")

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'str'"):
            CoreFoundation.CFCalendarDecomposeAbsoluteTime(calendar, at, "yMdHms")

        with self.assertRaisesRegex(TypeError, "Expecting 9 arguments, got 4"):
            CoreFoundation.CFCalendarDecomposeAbsoluteTime(
                calendar, at, b"yMdHms", None
            )

        with self.assertRaisesRegex(ValueError, "placeholder must be None"):
            CoreFoundation.CFCalendarDecomposeAbsoluteTime(
                calendar, at, b"yMdHms", None, None, None, None, 40, None
            )

        with self.assertRaisesRegex(
            TypeError, "At most 20 characters supported in componentDesc"
        ):
            CoreFoundation.CFCalendarDecomposeAbsoluteTime(
                calendar, at, b"yMdHmsSwagFFFFFFFFFFFFF"
            )

        success, y, M, d, H, m, s = CoreFoundation.CFCalendarDecomposeAbsoluteTime(
            calendar, at, b"yMdHms"
        )
        self.assertEqual(y, 1965)
        self.assertEqual(M, 1)
        self.assertEqual(d, 6)
        self.assertEqual(H, 14)
        self.assertEqual(m, 10)
        self.assertEqual(s, 0)

        success, y, M, d, H, m, s = CoreFoundation.CFCalendarDecomposeAbsoluteTime(
            calendar, at, b"yMdHms", None, None, None, None, None, None
        )
        self.assertEqual(y, 1965)
        self.assertEqual(M, 1)
        self.assertEqual(d, 6)
        self.assertEqual(H, 14)
        self.assertEqual(m, 10)
        self.assertEqual(s, 0)

        # XXX: See https://github.com/apple-oss-distributions/CF/blob/main/CFCalendar.c#L308
        #      for valid values for components

        # 'T' is not valid, behaviour is undocumented
        ok, *fields = CoreFoundation.CFCalendarDecomposeAbsoluteTime(
            calendar, at, b"TTT"
        )
        self.assertIsInstance(ok, bool)
        self.assertEqual(len(fields), 3)

    def test_cfcalendar_get_component_difference(self):
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

        with self.assertRaisesRegex(TypeError, "Expecting at least 5 arguments, got 0"):
            CoreFoundation.CFCalendarGetComponentDifference()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFCalendarGetComponentDifference(
                NoObjCClass(), at1, at2, 0, b"yM"
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            CoreFoundation.CFCalendarGetComponentDifference(
                calendar, str(at1), at2, 0, b"yM"
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'double', got 'str'"):
            CoreFoundation.CFCalendarGetComponentDifference(
                calendar, at1, str(at2), 0, b"yM"
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'unsigned long long', got 'str'"
        ):
            CoreFoundation.CFCalendarGetComponentDifference(
                calendar, at1, at2, str(0), b"yM"
            )

        with self.assertRaisesRegex(ValueError, "depythonifying 'charptr', got 'str'"):
            CoreFoundation.CFCalendarGetComponentDifference(calendar, at1, at2, 0, "yM")

        with self.assertRaisesRegex(
            TypeError, "At most 20 characters supported in componentDesc"
        ):
            CoreFoundation.CFCalendarGetComponentDifference(
                calendar, at1, at2, 0, b"yMMMMMMMMMMMMMMMMMMMMMMMMM"
            )

        with self.assertRaisesRegex(TypeError, "Expecting 5 arguments, got 6"):
            CoreFoundation.CFCalendarGetComponentDifference(
                calendar, at1, at2, 0, b"yM", None
            )

        with self.assertRaisesRegex(ValueError, "placeholder must be None"):
            CoreFoundation.CFCalendarGetComponentDifference(
                calendar, at1, at2, 0, b"yM", None, 42
            )

        success, y, M = CoreFoundation.CFCalendarGetComponentDifference(
            calendar, at1, at2, 0, b"yM"
        )
        self.assertEqual(success, True)
        self.assertEqual(y, 2)
        self.assertEqual(M, 1)

        success, y, M = CoreFoundation.CFCalendarGetComponentDifference(
            calendar, at1, at2, 0, b"yM", None, None
        )
        self.assertEqual(success, True)
        self.assertEqual(y, 2)
        self.assertEqual(M, 1)

    def test_typeid(self):
        v = CoreFoundation.CFCalendarGetTypeID()
        self.assertIsInstance(v, int)

    def test_creation(self):
        cal = CoreFoundation.CFCalendarCopyCurrent()
        self.assertIsInstance(cal, NSCalendar)
        cal = CoreFoundation.CFCalendarCreateWithIdentifier(
            None, CoreFoundation.kCFBuddhistCalendar
        )
        self.assertIsInstance(cal, NSCalendar)

    def test_inspect(self):
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

    def test_mutation(self):
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

    def test_constants(self):
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

        self.assertEqual(CoreFoundation.kCFCalendarUnitQuarter, 1 << 11)

        self.assertEqual(CoreFoundation.kCFCalendarUnitWeekOfMonth, 1 << 12)
        self.assertEqual(CoreFoundation.kCFCalendarUnitWeekOfYear, 1 << 13)
        self.assertEqual(CoreFoundation.kCFCalendarUnitYearForWeekOfYear, 1 << 14)
        self.assertEqual(CoreFoundation.kCFCalendarUnitDayOfYear, 1 << 16)
