import Foundation
import CoreFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSISO8601DateFormatter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSISO8601DateFormatOptions)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithYear,
            CoreFoundation.kCFISO8601DateFormatWithYear,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithMonth,
            CoreFoundation.kCFISO8601DateFormatWithMonth,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithWeekOfYear,
            CoreFoundation.kCFISO8601DateFormatWithWeekOfYear,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithDay,
            CoreFoundation.kCFISO8601DateFormatWithDay,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithTime,
            CoreFoundation.kCFISO8601DateFormatWithTime,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithTimeZone,
            CoreFoundation.kCFISO8601DateFormatWithTimeZone,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithSpaceBetweenDateAndTime,
            CoreFoundation.kCFISO8601DateFormatWithSpaceBetweenDateAndTime,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithDashSeparatorInDate,
            CoreFoundation.kCFISO8601DateFormatWithDashSeparatorInDate,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithColonSeparatorInTime,
            CoreFoundation.kCFISO8601DateFormatWithColonSeparatorInTime,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithColonSeparatorInTimeZone,
            CoreFoundation.kCFISO8601DateFormatWithColonSeparatorInTimeZone,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithFullDate,
            CoreFoundation.kCFISO8601DateFormatWithFullDate,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithFullTime,
            CoreFoundation.kCFISO8601DateFormatWithFullTime,
        )
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithInternetDateTime,
            CoreFoundation.kCFISO8601DateFormatWithInternetDateTime,
        )

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertEqual(
            Foundation.NSISO8601DateFormatWithFractionalSeconds,
            CoreFoundation.kCFISO8601DateFormatWithFractionalSeconds,
        )
