from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSDateFormatter (TestCase):
    def testOutput(self):
        formatter = NSDateFormatter.alloc().init()
        formatter.setDateFormat_("yyyy/mm/dd")

        self.assertArgIsOut(NSDateFormatter.getObjectValue_forString_range_error_, 0)
        self.assertArgIsInOut(NSDateFormatter.getObjectValue_forString_range_error_, 2)
        self.assertArgIsOut(NSDateFormatter.getObjectValue_forString_range_error_, 3)
        ok, val, range, err = formatter.getObjectValue_forString_range_error_(
                None, "2008/10/12", NSRange(0, 10), None)
        self.assertTrue(ok)
        self.assertIsInstance(val, NSDate)
        self.assertEqual(range , NSRange(0, 10))
        self.assertIs(err, None)
        self.assertResultIsBOOL(NSDateFormatter.getObjectValue_forString_range_error_)
        self.assertArgIsInOut(NSDateFormatter.getObjectValue_forString_range_error_, 2)
        self.assertArgIsOut(NSDateFormatter.getObjectValue_forString_range_error_, 3)

    def testConstants(self):
        self.assertEqual(NSDateFormatterNoStyle, kCFDateFormatterNoStyle)
        self.assertEqual(NSDateFormatterShortStyle, kCFDateFormatterShortStyle)
        self.assertEqual(NSDateFormatterMediumStyle, kCFDateFormatterMediumStyle)
        self.assertEqual(NSDateFormatterLongStyle, kCFDateFormatterLongStyle)
        self.assertEqual(NSDateFormatterFullStyle, kCFDateFormatterFullStyle)

        self.assertEqual(NSDateFormatterBehaviorDefault, 0)
        self.assertEqual(NSDateFormatterBehavior10_0, 1000)
        self.assertEqual(NSDateFormatterBehavior10_4, 1040)

    def testMethods(self):
        self.assertResultIsBOOL(NSDateFormatter.generatesCalendarDates)
        self.assertArgIsBOOL(NSDateFormatter.setGeneratesCalendarDates_, 0)
        self.assertResultIsBOOL(NSDateFormatter.isLenient)
        self.assertArgIsBOOL(NSDateFormatter.setLenient_, 0)
        self.assertResultIsBOOL(NSDateFormatter.isLenient)
        self.assertArgIsBOOL(NSDateFormatter.initWithDateFormat_allowNaturalLanguage_, 1)
        self.assertResultIsBOOL(NSDateFormatter.allowsNaturalLanguage)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSDateFormatter.doesRelativeDateFormatting)
        self.assertArgIsBOOL(NSDateFormatter.setDoesRelativeDateFormatting_, 0)



if __name__ == "__main__":
    main()
