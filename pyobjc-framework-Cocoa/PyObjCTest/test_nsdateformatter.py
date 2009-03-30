from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSDateFormatter (TestCase):
    def testOutput(self):
        formatter = NSDateFormatter.alloc().init()
        formatter.setDateFormat_("yyyy/mm/dd")

        ok, val, range, err = formatter.getObjectValue_forString_range_error_(
                None, "2008/10/12", NSRange(0, 10), None)
        self.failUnless(ok)
        self.failUnless(isinstance(val, NSDate))
        self.failUnless(range == NSRange(0, 10))
        self.failUnless(err is None)

        self.failUnlessResultIsBOOL(NSDateFormatter.getObjectValue_forString_range_error_)
        self.failUnlessArgIsInOut(NSDateFormatter.getObjectValue_forString_range_error_, 2)
        self.failUnlessArgIsOut(NSDateFormatter.getObjectValue_forString_range_error_, 3)

    def testConstants(self):
        self.assertEquals(NSDateFormatterNoStyle, kCFDateFormatterNoStyle)
        self.assertEquals(NSDateFormatterShortStyle, kCFDateFormatterShortStyle)
        self.assertEquals(NSDateFormatterMediumStyle, kCFDateFormatterMediumStyle)
        self.assertEquals(NSDateFormatterLongStyle, kCFDateFormatterLongStyle)
        self.assertEquals(NSDateFormatterFullStyle, kCFDateFormatterFullStyle)

        self.assertEquals(NSDateFormatterBehaviorDefault, 0)
        self.assertEquals(NSDateFormatterBehavior10_0, 1000)
        self.assertEquals(NSDateFormatterBehavior10_4, 1040)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSDateFormatter.generatesCalendarDates)
        self.failUnlessArgIsBOOL(NSDateFormatter.setGeneratesCalendarDates_, 0)
        self.failUnlessResultIsBOOL(NSDateFormatter.isLenient)
        self.failUnlessArgIsBOOL(NSDateFormatter.setLenient_, 0)
        self.failUnlessResultIsBOOL(NSDateFormatter.isLenient)
        self.failUnlessArgIsBOOL(NSDateFormatter.initWithDateFormat_allowNaturalLanguage_, 1)
        self.failUnlessResultIsBOOL(NSDateFormatter.allowsNaturalLanguage)


if __name__ == "__main__":
    main()
