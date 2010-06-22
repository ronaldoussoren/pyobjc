from PyObjCTools.TestSupport import *
from CoreFoundation import *
import datetime

class TestCFCalendarVariadic (TestCase):
    def testTypes(self):
        self.assertIsCFType(CFCalendarRef)

    def testCFCalendarComposeAbsoluteTime(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.assertIsInstance(calendar, CFCalendarRef)

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, b"")
        self.assertEqual(success, True)
        self.assert_(isinstance(at, float))

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEqual(success, True)
        self.assert_(isinstance(at, float))

    def testCFCalendarAddComponents(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.assertIsInstance(calendar, CFCalendarRef)

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEqual(success, True)
        self.assert_(isinstance(at, float))

        success, at2 = CFCalendarAddComponents(
                calendar, at, 0, b"yH", 2, 3)
        self.assertEqual(success, True)
        self.assert_(isinstance(at2, float))

        success, y, H = CFCalendarGetComponentDifference(
                calendar, at, at2, 0, b"yH")
        self.assertEqual(success, True)
        self.assertEqual(y, 2)
        self.assertEqual(H, 3)


    def testCFCalendarDecomposeAbsoluteTime(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEqual(success, True)
        self.assert_(isinstance(at, float))

        success, y, M, d, H, m, s = CFCalendarDecomposeAbsoluteTime(
                calendar, at, b"yMdHms")
        self.assertEqual(y, 1965)
        self.assertEqual(M, 1)
        self.assertEqual(d, 6)
        self.assertEqual(H, 14)
        self.assertEqual(m, 10)
        self.assertEqual(s, 0)

    def testCFCalendarGetComponentDifference(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at1 = CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEqual(success, True)
        self.assert_(isinstance(at1, float))

        success, at2 = CFCalendarComposeAbsoluteTime(
                calendar, None, b"yMdHms", 1967, 2, 6, 14, 10, 0)
        self.assertEqual(success, True)
        self.assert_(isinstance(at2, float))

        success, y, M = CFCalendarGetComponentDifference(
                calendar, at1, at2, 0, b"yM")
        self.assertEqual(success, True)
        self.assertEqual(y, 2)
        self.assertEqual(M, 1)

    def testTypeID(self):
        v = CFCalendarGetTypeID()
        self.assertIsInstance(v, (int, long))

    def testCreation(self):
        cal = CFCalendarCopyCurrent()
        self.assertIsInstance(cal, CFCalendarRef)
        cal = CFCalendarCreateWithIdentifier(None, kCFBuddhistCalendar)
        self.assertIsInstance(cal, CFCalendarRef)

    def testInspection(self):
        cal = CFCalendarCreateWithIdentifier(None, kCFGregorianCalendar)
        self.assertIsInstance(cal, CFCalendarRef)
        name = CFCalendarGetIdentifier(cal)
        self.assertEqual(name , kCFGregorianCalendar)
        locale = CFCalendarCopyLocale(cal)
        self.assertIsInstance(locale, CFLocaleRef)
        timezone = CFCalendarCopyTimeZone(cal)
        self.assertIsInstance(timezone, CFTimeZoneRef)
        weekday = CFCalendarGetFirstWeekday(cal)
        self.assertLessEqual(0 <= weekday , 7)
        num = CFCalendarGetMinimumDaysInFirstWeek(cal)
        self.assertLessEqual(0 <= num , 7)
        rng = CFCalendarGetMinimumRangeOfUnit(cal, kCFCalendarUnitEra)
        self.assertIsInstance(rng, CFRange)
        rng = CFCalendarGetMaximumRangeOfUnit(cal, kCFCalendarUnitEra)
        self.assertIsInstance(rng, CFRange)
        m = datetime.date.today()
        if m.month in (1,3,5,7,8,10,12):
            monthLength=31
        elif m.month in (4, 6, 9, 11):
            monthLength=30
        else:
            if m.year % 4 == 0:
                # Yes this is wrong, but the next time this fails in
                # in 2100. 
                monthLength = 29
            else:
                monthLength = 28
        rng = CFCalendarGetRangeOfUnit(cal, kCFCalendarUnitDay, kCFCalendarUnitMonth, CFAbsoluteTimeGetCurrent())
        self.assertIsInstance(rng, CFRange)
        self.assertEqual(rng.location, 1)
        self.assertEqual(rng.length, monthLength)


        v = CFCalendarGetOrdinalityOfUnit(cal, kCFCalendarUnitDay, kCFCalendarUnitYear, CFAbsoluteTimeGetCurrent())
        self.assertIsInstance(v, (int, long))
        ok, startp, tip = CFCalendarGetTimeRangeOfUnit(cal, kCFCalendarUnitDay, CFAbsoluteTimeGetCurrent(), None, None)
        self.assertIs(ok, True)
        self.assertIsInstance(startp, float)
        self.assertIsInstance(tip, float)
        self.assertEqual(tip , 86400.0)

    def testMutation(self):
        cal = CFCalendarCreateWithIdentifier(None, kCFBuddhistCalendar)

        loc = CFLocaleCreate(None, u"mr_IN")
        self.assertIsInstance(loc, CFLocaleRef)
        id1 = CFLocaleGetIdentifier(loc)

        orig_loc = CFCalendarCopyLocale(cal)
        self.assertIsInstance(orig_loc, CFLocaleRef)
        orig_id = CFLocaleGetIdentifier(orig_loc)
        CFCalendarSetLocale(cal, loc)
        new_loc = CFCalendarCopyLocale(cal)
        self.assertIsInstance(new_loc, CFLocaleRef)
        new_id = CFLocaleGetIdentifier(new_loc)

        self.assertEqual(new_id , id1)
        self.assertNotEqual(orig_id , id1)
        tz = CFTimeZoneCreateWithName(None, u"Pacific/Wallis", True)
        self.assertIsInstance(tz, CFTimeZoneRef)
        orig_zone = CFCalendarCopyTimeZone(cal)
        self.assertIsInstance(orig_zone, CFTimeZoneRef)
        CFCalendarSetTimeZone(cal, tz)
        new_zone = CFCalendarCopyTimeZone(cal)
        self.assertIsInstance(new_zone, CFTimeZoneRef)
        self.assertEqual(CFTimeZoneGetName(new_zone) , u'Pacific/Wallis' )
        weekday = CFCalendarGetFirstWeekday(cal)
        weekday = weekday + 2 % 7
        CFCalendarSetFirstWeekday(cal, weekday)
        new = CFCalendarGetFirstWeekday(cal)
        self.assertEqual(new , weekday)
        num = CFCalendarGetMinimumDaysInFirstWeek(cal)
        if num == 1:
            num = 2
        else:
            num = 1

        CFCalendarSetMinimumDaysInFirstWeek(cal, num)
        num2 = CFCalendarGetMinimumDaysInFirstWeek(cal)
        self.assertEqual(num2 , num)

    def testConstants(self):
        self.assertEqual(kCFCalendarUnitEra , (1 << 1) )
        self.assertEqual(kCFCalendarUnitYear , (1 << 2) )
        self.assertEqual(kCFCalendarUnitMonth , (1 << 3) )
        self.assertEqual(kCFCalendarUnitDay , (1 << 4) )
        self.assertEqual(kCFCalendarUnitHour , (1 << 5) )
        self.assertEqual(kCFCalendarUnitMinute , (1 << 6) )
        self.assertEqual(kCFCalendarUnitSecond , (1 << 7) )
        self.assertEqual(kCFCalendarUnitWeek , (1 << 8) )
        self.assertEqual(kCFCalendarUnitWeekday , (1 << 9) )
        self.assertEqual(kCFCalendarUnitWeekdayOrdinal , (1 << 10) )
        self.assertEqual(kCFCalendarComponentsWrap , (1 << 0) )

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(kCFCalendarUnitQuarter, 1<<11)


if __name__ == "__main__":
    main()
