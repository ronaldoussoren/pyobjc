import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSDateFormatter(TestCase):
    def testOutput(self):
        formatter = Foundation.NSDateFormatter.alloc().init()
        formatter.setDateFormat_("yyyy/mm/dd")

        self.assertResultIsBOOL(
            Foundation.NSDateFormatter.getObjectValue_forString_range_error_
        )
        self.assertArgIsOut(
            Foundation.NSDateFormatter.getObjectValue_forString_range_error_, 0
        )
        self.assertArgIsInOut(
            Foundation.NSDateFormatter.getObjectValue_forString_range_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSDateFormatter.getObjectValue_forString_range_error_, 3
        )
        ok, val, text_range, err = formatter.getObjectValue_forString_range_error_(
            None, "2008/10/12", Foundation.NSRange(0, 10), None
        )
        self.assertTrue(ok)
        self.assertIsInstance(val, Foundation.NSDate)
        self.assertEqual(text_range, Foundation.NSRange(0, 10))
        self.assertIs(err, None)
        self.assertResultIsBOOL(
            Foundation.NSDateFormatter.getObjectValue_forString_range_error_
        )
        self.assertArgIsInOut(
            Foundation.NSDateFormatter.getObjectValue_forString_range_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSDateFormatter.getObjectValue_forString_range_error_, 3
        )

    def testConstants(self):
        self.assertEqual(
            Foundation.NSDateFormatterNoStyle, CoreFoundation.kCFDateFormatterNoStyle
        )
        self.assertEqual(
            Foundation.NSDateFormatterShortStyle,
            CoreFoundation.kCFDateFormatterShortStyle,
        )
        self.assertEqual(
            Foundation.NSDateFormatterMediumStyle,
            CoreFoundation.kCFDateFormatterMediumStyle,
        )
        self.assertEqual(
            Foundation.NSDateFormatterLongStyle,
            CoreFoundation.kCFDateFormatterLongStyle,
        )
        self.assertEqual(
            Foundation.NSDateFormatterFullStyle,
            CoreFoundation.kCFDateFormatterFullStyle,
        )

        self.assertEqual(Foundation.NSDateFormatterBehaviorDefault, 0)
        self.assertEqual(Foundation.NSDateFormatterBehavior10_0, 1000)
        self.assertEqual(Foundation.NSDateFormatterBehavior10_4, 1040)

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSDateFormatter.generatesCalendarDates)
        self.assertArgIsBOOL(Foundation.NSDateFormatter.setGeneratesCalendarDates_, 0)
        self.assertResultIsBOOL(Foundation.NSDateFormatter.isLenient)
        self.assertArgIsBOOL(Foundation.NSDateFormatter.setLenient_, 0)
        self.assertResultIsBOOL(Foundation.NSDateFormatter.isLenient)
        self.assertArgIsBOOL(
            Foundation.NSDateFormatter.initWithDateFormat_allowNaturalLanguage_, 1
        )
        self.assertResultIsBOOL(Foundation.NSDateFormatter.allowsNaturalLanguage)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Foundation.NSDateFormatter.doesRelativeDateFormatting)
        self.assertArgIsBOOL(
            Foundation.NSDateFormatter.setDoesRelativeDateFormatting_, 0
        )
