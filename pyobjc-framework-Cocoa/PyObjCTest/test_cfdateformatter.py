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

        self.failUnlessIsInstance(kCFDateFormatterIsLenient, unicode)
        self.failUnlessIsInstance(kCFDateFormatterTimeZone, unicode)
        self.failUnlessIsInstance(kCFDateFormatterCalendarName, unicode)
        self.failUnlessIsInstance(kCFDateFormatterDefaultFormat, unicode)
        self.failUnlessIsInstance(kCFDateFormatterTwoDigitStartDate, unicode)
        self.failUnlessIsInstance(kCFDateFormatterDefaultDate, unicode)
        self.failUnlessIsInstance(kCFDateFormatterCalendar, unicode)
        self.failUnlessIsInstance(kCFDateFormatterEraSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterMonthSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterShortMonthSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterWeekdaySymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterShortWeekdaySymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterAMSymbol, unicode)
        self.failUnlessIsInstance(kCFDateFormatterPMSymbol, unicode)
        self.failUnlessIsInstance(kCFDateFormatterLongEraSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterVeryShortMonthSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterStandaloneMonthSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterShortStandaloneMonthSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterVeryShortStandaloneMonthSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterVeryShortWeekdaySymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterStandaloneWeekdaySymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterShortStandaloneWeekdaySymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterVeryShortStandaloneWeekdaySymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterQuarterSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterShortQuarterSymbols, unicode)
        self.failUnlessIsInstance(kCFDateFormatterStandaloneQuarterSymbols, unicode)
        self.failUnlessIsInstance( kCFDateFormatterShortStandaloneQuarterSymbols, unicode)
        self.failUnlessIsInstance( kCFDateFormatterGregorianStartDate, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCFDateFormatterDoesRelativeDateFormattingKey, unicode)

    @min_os_level('10.6')
    def testFunction10_6(self):
        self.failUnlessResultIsCFRetained(CFDateFormatterCreateDateFormatFromTemplate)
        r = CFDateFormatterCreateDateFormatFromTemplate(None, "%Y-%m-%d", 0, None)
        self.failUnlessIsInstance(r, unicode)
                            


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

        CFDateFormatterSetProperty(fmt, kCFDateFormatterCalendarName, u"gregorian")
        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterCalendarName)
        self.failUnlessIsInstance(v, unicode)
        self.failUnless(v == u"gregorian")

        v = CFDateFormatterCopyProperty(fmt, kCFDateFormatterIsLenient)
        self.failUnless(v is True or v is False)

        CFDateFormatterSetProperty(fmt, kCFDateFormatterIsLenient, True)
        v2 = CFDateFormatterCopyProperty(fmt, kCFDateFormatterIsLenient)
        self.failUnless(v2 is True)
        

if __name__ == "__main__":
    main()
