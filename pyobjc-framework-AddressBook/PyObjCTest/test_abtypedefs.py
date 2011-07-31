
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABTypedefs (TestCase):
    def testConstants(self):
        self.assertEqual(kABMultiValueMask, 0x100)

        self.assertEqual(kABErrorInProperty, 0x0)
        self.assertEqual(kABStringProperty, 0x1)
        self.assertEqual(kABIntegerProperty, 0x2)
        self.assertEqual(kABRealProperty, 0x3)
        self.assertEqual(kABDateProperty, 0x4)
        self.assertEqual(kABArrayProperty, 0x5)
        self.assertEqual(kABDictionaryProperty, 0x6)
        self.assertEqual(kABDataProperty, 0x7)
        self.assertEqual(kABDateComponentsProperty, 0x8)

        self.assertEqual(kABMultiStringProperty, kABMultiValueMask | kABStringProperty)
        self.assertEqual(kABMultiIntegerProperty, kABMultiValueMask | kABIntegerProperty)
        self.assertEqual(kABMultiRealProperty, kABMultiValueMask | kABRealProperty)
        self.assertEqual(kABMultiDateProperty, kABMultiValueMask | kABDateProperty)
        self.assertEqual(kABMultiArrayProperty, kABMultiValueMask | kABArrayProperty)
        self.assertEqual(kABMultiDictionaryProperty, kABMultiValueMask | kABDictionaryProperty)
        self.assertEqual(kABMultiDataProperty, kABMultiValueMask | kABDataProperty)
        self.assertEqual(kABMultiDateComponentsProperty, kABMultiValueMask | kABDateComponentsProperty)

        self.assertEqual(kABEqual, 0)
        self.assertEqual(kABNotEqual, 1)
        self.assertEqual(kABLessThan, 2)
        self.assertEqual(kABLessThanOrEqual, 3)
        self.assertEqual(kABGreaterThan, 4)
        self.assertEqual(kABGreaterThanOrEqual, 5)
        self.assertEqual(kABEqualCaseInsensitive, 6)
        self.assertEqual(kABContainsSubString, 7)
        self.assertEqual(kABContainsSubStringCaseInsensitive, 8)
        self.assertEqual(kABPrefixMatch, 9)
        self.assertEqual(kABPrefixMatchCaseInsensitive, 10)
        self.assertEqual(kABBitsInBitFieldMatch, 11)
        self.assertEqual(kABDoesNotContainSubString, 12)
        self.assertEqual(kABDoesNotContainSubStringCaseInsensitive, 13)
        self.assertEqual(kABNotEqualCaseInsensitive, 14)
        self.assertEqual(kABSuffixMatch, 15)
        self.assertEqual(kABSuffixMatchCaseInsensitive, 16)
        self.assertEqual(kABWithinIntervalAroundToday, 17)
        self.assertEqual(kABWithinIntervalAroundTodayYearless, 18)
        self.assertEqual(kABNotWithinIntervalAroundToday, 19)
        self.assertEqual(kABNotWithinIntervalAroundTodayYearless, 20)
        self.assertEqual(kABWithinIntervalFromToday, 21)
        self.assertEqual(kABWithinIntervalFromTodayYearless, 22)
        self.assertEqual(kABNotWithinIntervalFromToday, 23)
        self.assertEqual(kABNotWithinIntervalFromTodayYearless, 24)

        self.assertEqual(kABSearchAnd, 0)
        self.assertEqual(kABSearchOr, 1)



if __name__ == "__main__":
    main()
