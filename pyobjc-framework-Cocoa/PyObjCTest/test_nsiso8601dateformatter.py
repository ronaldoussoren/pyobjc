from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSISO8601DateFormatter (TestCase):
    @min_os_level('10.12')
    def testConstants(self):
        self.assertEqual(NSISO8601DateFormatWithYear, kCFISO8601DateFormatWithYear)
        self.assertEqual(NSISO8601DateFormatWithMonth, kCFISO8601DateFormatWithMonth)
        self.assertEqual(NSISO8601DateFormatWithWeekOfYear, kCFISO8601DateFormatWithWeekOfYear)
        self.assertEqual(NSISO8601DateFormatWithDay, kCFISO8601DateFormatWithDay)
        self.assertEqual(NSISO8601DateFormatWithTime, kCFISO8601DateFormatWithTime)
        self.assertEqual(NSISO8601DateFormatWithTimeZone, kCFISO8601DateFormatWithTimeZone)
        self.assertEqual(NSISO8601DateFormatWithSpaceBetweenDateAndTime, kCFISO8601DateFormatWithSpaceBetweenDateAndTime)
        self.assertEqual(NSISO8601DateFormatWithDashSeparatorInDate, kCFISO8601DateFormatWithDashSeparatorInDate)
        self.assertEqual(NSISO8601DateFormatWithColonSeparatorInTime, kCFISO8601DateFormatWithColonSeparatorInTime)
        self.assertEqual(NSISO8601DateFormatWithColonSeparatorInTimeZone, kCFISO8601DateFormatWithColonSeparatorInTimeZone)
        self.assertEqual(NSISO8601DateFormatWithFullDate, kCFISO8601DateFormatWithFullDate)
        self.assertEqual(NSISO8601DateFormatWithFullTime, kCFISO8601DateFormatWithFullTime)
        self.assertEqual(NSISO8601DateFormatWithInternetDateTime, kCFISO8601DateFormatWithInternetDateTime)

    @min_os_level('10.13')
    def testConstants(self):
        self.assertEqual(NSISO8601DateFormatWithFractionalSeconds, kCFISO8601DateFormatWithFractionalSeconds)

if __name__ == "__main__":
    main()
