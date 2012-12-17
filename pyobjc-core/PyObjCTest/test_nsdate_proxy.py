from PyObjCTools.TestSupport import *
from PyObjCTest.fnd import NSDateFormatter, NSArray, NSDate
import datetime

class TestNSDateProxy (TestCase):
    # Test for proxied datetime.date and datetime.datetime objects,
    # these have a custom proxy class.

    def testFormattingForDate(self):
        # This is jus a round-about way of testing that the right proxy
        # object is created
        formatter = NSDateFormatter.alloc().initWithDateFormat_allowNaturalLanguage_(
                "%Y-%m-%d", True)

        date = datetime.date.today()

        value = formatter.stringFromDate_(NSDate.date())
        self.assertEqual(value, date.strftime('%Y-%m-%d'))

        value = formatter.stringFromDate_(date)
        self.assertEqual(value, date.strftime('%Y-%m-%d'))


    def testFormattingForDateTime(self):
        # This is jus a round-about way of testing that the right proxy
        # object is created
        formatter = NSDateFormatter.alloc().initWithDateFormat_allowNaturalLanguage_(
                "%Y-%m-%d %H:%M:%S", True)

        date = datetime.datetime.now()

        value = formatter.stringFromDate_(date)
        self.assertEqual(value, date.strftime('%Y-%m-%d %H:%M:%S'))


if __name__ == "__main__":
    main()
