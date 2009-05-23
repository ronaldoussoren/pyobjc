from PyObjCTools.TestSupport import *
from CoreFoundation import *

class TestCFCalendarVariadic (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CFCalendarRef)

    def testCFCalendarComposeAbsoluteTime(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.failUnlessIsInstance(calendar, CFCalendarRef)

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, '')
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

    def testCFCalendarAddComponents(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.failUnlessIsInstance(calendar, CFCalendarRef)

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

        success, at2 = CFCalendarAddComponents(
                calendar, at, 0, "yH", 2, 3)
        self.assertEquals(success, True)
        self.assert_(isinstance(at2, float))

        success, y, H = CFCalendarGetComponentDifference(
                calendar, at, at2, 0, "yH")
        self.assertEquals(success, True)
        self.assertEquals(y, 2)
        self.assertEquals(H, 3)


    def testCFCalendarDecomposeAbsoluteTime(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at = CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at, float))

        success, y, M, d, H, m, s = CFCalendarDecomposeAbsoluteTime(
                calendar, at, "yMdHms")
        self.assertEquals(y, 1965)
        self.assertEquals(M, 1)
        self.assertEquals(d, 6)
        self.assertEquals(H, 14)
        self.assertEquals(m, 10)
        self.assertEquals(s, 0)

    def testCFCalendarGetComponentDifference(self):
        calendar = CFCalendarCreateWithIdentifier(
                None, kCFGregorianCalendar)
        self.assert_(calendar is not None)

        success, at1 = CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1965, 1, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at1, float))

        success, at2 = CFCalendarComposeAbsoluteTime(
                calendar, None, "yMdHms", 1967, 2, 6, 14, 10, 0)
        self.assertEquals(success, True)
        self.assert_(isinstance(at2, float))

        success, y, M = CFCalendarGetComponentDifference(
                calendar, at1, at2, 0, "yM")
        self.assertEquals(success, True)
        self.assertEquals(y, 2)
        self.assertEquals(M, 1)

    def testTypeID(self):
        v = CFCalendarGetTypeID()
        self.failUnless(isinstance(v, (int, long)))

    def testCreation(self):
        cal = CFCalendarCopyCurrent()
        self.failUnless( isinstance(cal, CFCalendarRef) )

        cal = CFCalendarCreateWithIdentifier(None, kCFBuddhistCalendar)
        self.failUnless( isinstance(cal, CFCalendarRef) )


    def testInspection(self):
        cal = CFCalendarCreateWithIdentifier(None, kCFBuddhistCalendar)
        self.failUnless( isinstance(cal, CFCalendarRef) )

        name = CFCalendarGetIdentifier(cal)
        self.failUnless(name == kCFBuddhistCalendar)

        locale = CFCalendarCopyLocale(cal)
        self.failUnless( isinstance(locale, CFLocaleRef) )

        timezone = CFCalendarCopyTimeZone(cal)
        self.failUnless( isinstance(timezone, CFTimeZoneRef) )

        weekday = CFCalendarGetFirstWeekday(cal)
        self.failUnless(0 <= weekday <= 7)

        num = CFCalendarGetMinimumDaysInFirstWeek(cal)
        self.failUnless(0 <= num <= 7)

    
        rng = CFCalendarGetMinimumRangeOfUnit(cal, kCFCalendarUnitEra)
        self.failUnless(isinstance(rng, CFRange))

        rng = CFCalendarGetMaximumRangeOfUnit(cal, kCFCalendarUnitEra)
        self.failUnless(isinstance(rng, CFRange))

        rng = CFCalendarGetRangeOfUnit(cal, kCFCalendarUnitDay, kCFCalendarUnitYear, CFAbsoluteTimeGetCurrent())
        self.failUnless(isinstance(rng, CFRange))
        self.failUnlessEqual(rng.location, 1)
        self.failUnlessEqual(rng.length, 365)


        v = CFCalendarGetOrdinalityOfUnit(cal, kCFCalendarUnitDay, kCFCalendarUnitYear, CFAbsoluteTimeGetCurrent())
        self.failUnless( isinstance(v, (int, long)) )

        ok, startp, tip = CFCalendarGetTimeRangeOfUnit(cal, kCFCalendarUnitDay, CFAbsoluteTimeGetCurrent(), None, None)
        self.failUnless(ok is True)
        self.failUnless(isinstance(startp, float))
        self.failUnless(isinstance(tip, float))
        self.failUnless(tip == 86400.0)


    def testMutation(self):
        cal = CFCalendarCreateWithIdentifier(None, kCFBuddhistCalendar)

        loc = CFLocaleCreate(None, u"mr_IN")
        self.failUnless(isinstance(loc, CFLocaleRef))
        id1 = CFLocaleGetIdentifier(loc)

        orig_loc = CFCalendarCopyLocale(cal)
        self.failUnless(isinstance(orig_loc, CFLocaleRef))
        orig_id = CFLocaleGetIdentifier(orig_loc)
        CFCalendarSetLocale(cal, loc)
        new_loc = CFCalendarCopyLocale(cal)
        self.failUnless(isinstance(new_loc, CFLocaleRef))
        new_id = CFLocaleGetIdentifier(new_loc)

        self.failUnless(new_id == id1)
        self.failIf(orig_id == id1)

        tz = CFTimeZoneCreateWithName(None, u"Pacific/Wallis", True)
        self.failUnless(isinstance(tz, CFTimeZoneRef))
        orig_zone = CFCalendarCopyTimeZone(cal)
        self.failUnless(isinstance(orig_zone, CFTimeZoneRef))

        CFCalendarSetTimeZone(cal, tz)
        new_zone = CFCalendarCopyTimeZone(cal)
        self.failUnless(isinstance(new_zone, CFTimeZoneRef))

        self.failUnless( CFTimeZoneGetName(new_zone) == u'Pacific/Wallis' )


        weekday = CFCalendarGetFirstWeekday(cal)
        weekday = weekday + 2 % 7
        CFCalendarSetFirstWeekday(cal, weekday)
        new = CFCalendarGetFirstWeekday(cal)
        self.failUnless(new == weekday)

        num = CFCalendarGetMinimumDaysInFirstWeek(cal)
        if num == 1:
            num = 2
        else:
            num = 1

        CFCalendarSetMinimumDaysInFirstWeek(cal, num)
        num2 = CFCalendarGetMinimumDaysInFirstWeek(cal)
        self.failUnless(num2 == num)


    def testConstants(self):
        self.failUnless( kCFCalendarUnitEra == (1 << 1) )
        self.failUnless( kCFCalendarUnitYear == (1 << 2) )
        self.failUnless( kCFCalendarUnitMonth == (1 << 3) )
        self.failUnless( kCFCalendarUnitDay == (1 << 4) )
        self.failUnless( kCFCalendarUnitHour == (1 << 5) )
        self.failUnless( kCFCalendarUnitMinute == (1 << 6) )
        self.failUnless( kCFCalendarUnitSecond == (1 << 7) )
        self.failUnless( kCFCalendarUnitWeek == (1 << 8) )
        self.failUnless( kCFCalendarUnitWeekday == (1 << 9) )
        self.failUnless( kCFCalendarUnitWeekdayOrdinal == (1 << 10) )

        self.failUnless( kCFCalendarComponentsWrap == (1 << 0) )


if __name__ == "__main__":
    main()
