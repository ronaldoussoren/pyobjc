from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestDateFormatter (TestCase):
    def testTypeID(self):
        self.failUnless(isinstance(CFDateGetTypeID(), (int, long)))

    def testConstants(self):
        self.failUnless(kCFDateFormatterNoStyle == 0)
        self.failUnless(kCFDateFormatterShortStyle == 1)
        self.failUnless(kCFDateFormatterMediumStyle == 2)
        self.failUnless(kCFDateFormatterLongStyle == 3)
        self.failUnless(kCFDateFormatterFullStyle == 4)

        self.failUnless( isinstance( kCFDateFormatterIsLenient, unicode))
        self.failUnless( isinstance( kCFDateFormatterTimeZone, unicode))
        self.failUnless( isinstance( kCFDateFormatterCalendarName, unicode))
        self.failUnless( isinstance( kCFDateFormatterDefaultFormat, unicode))
        self.failUnless( isinstance( kCFDateFormatterTwoDigitStartDate, unicode))
        self.failUnless( isinstance( kCFDateFormatterDefaultDate, unicode))
        self.failUnless( isinstance( kCFDateFormatterCalendar, unicode))
        self.failUnless( isinstance( kCFDateFormatterEraSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterMonthSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterShortMonthSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterWeekdaySymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterShortWeekdaySymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterAMSymbol, unicode))
        self.failUnless( isinstance( kCFDateFormatterPMSymbol, unicode))
        self.failUnless( isinstance( kCFDateFormatterLongEraSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterVeryShortMonthSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterStandaloneMonthSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterShortStandaloneMonthSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterVeryShortStandaloneMonthSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterVeryShortWeekdaySymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterStandaloneWeekdaySymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterShortStandaloneWeekdaySymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterVeryShortStandaloneWeekdaySymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterQuarterSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterShortQuarterSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterStandaloneQuarterSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterShortStandaloneQuarterSymbols, unicode))
        self.failUnless( isinstance( kCFDateFormatterGregorianStartDate, unicode))

    def testTypes(self):
        self.failUnlessIsCFType(CFDateFormatterRef)

    def testInspection(self):
        locale = CFLocaleCopyCurrent()
        self.failUnlessIsInstance(locale, CFLocaleRef)

        date = CFDateCreate(None, CFAbsoluteTimeGetCurrent())
        self.failUnlessIsInstance(date, CFDateRef)

        self.failUnlessResultIsCFRetained(CFDateFormatterCreate)
        fmt = CFDateFormatterCreate(None, locale, kCFDateFormatterShortStyle, kCFDateFormatterLongStyle) 
        self.failUnless(isinstance(fmt, CFDateFormatterRef))

        v = CFDateFormatterGetLocale(fmt)
        self.assertEquals(CFLocaleGetIdentifier(locale), CFLocaleGetIdentifier(v))

        v = CFDateFormatterGetDateStyle(fmt)
        self.assertEquals(v, kCFDateFormatterShortStyle)

        v = CFDateFormatterGetTimeStyle(fmt)
        self.assertEquals(v, kCFDateFormatterLongStyle)

        v = CFDateFormatterGetFormat(fmt)
        self.failUnless(isinstance(v, unicode))

        CFDateFormatterSetFormat(fmt, v[:-1])
        v2 = CFDateFormatterGetFormat(fmt)
        self.assertEquals(v[:-1], v2)

        v = CFDateFormatterCreateStringWithDate(None, fmt, date)
        self.failUnless(isinstance(v, unicode))

        v = CFDateFormatterCreateStringWithAbsoluteTime(None, fmt, CFAbsoluteTimeGetCurrent())
        self.failUnless(isinstance(v, unicode))

        dt, rng = CFDateFormatterCreateDateFromString(None, fmt, v, (0, len(v)))
        self.failUnless(isinstance(dt, CFDateRef))
        self.failUnless(isinstance(rng, CFRange))

        ok, rng, abstime = CFDateFormatterGetAbsoluteTimeFromString(fmt, v, (0, len(v)), None)
        self.failUnless(ok is True)
        self.failUnless(isinstance(rng, CFRange))
        self.failUnless(isinstance(abstime, float))

        self.failUnlessResultIsCFRetained(CFDateFormatterCopyProperty)
        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterCalendarName)
        self.failUnless(isinstance(v, unicode))

        CFDateFormatterSetProperty(fmt, kCFDateFormatterCalendarName, u"samba")
        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterCalendarName)
        self.failUnless(isinstance(v, unicode))
        self.failUnless(v == u"samba")

        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterIsLenient)
        self.failUnless(v is True or v is False)

        CFDateFormatterSetProperty(fmt, kCFDateFormatterIsLenient, True)
        v2 = CFDateFormatterCopyProperty(fmt, kCFDateFormatterIsLenient)
        self.failUnless(v2 is True)
        

if __name__ == "__main__":
    main()
