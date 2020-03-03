import AddressBook
from PyObjCTools.TestSupport import TestCase


class TestABTypedefs(TestCase):
    def testConstants(self):
        self.assertEqual(AddressBook.kABMultiValueMask, 0x100)

        self.assertEqual(AddressBook.kABErrorInProperty, 0x0)
        self.assertEqual(AddressBook.kABStringProperty, 0x1)
        self.assertEqual(AddressBook.kABIntegerProperty, 0x2)
        self.assertEqual(AddressBook.kABRealProperty, 0x3)
        self.assertEqual(AddressBook.kABDateProperty, 0x4)
        self.assertEqual(AddressBook.kABArrayProperty, 0x5)
        self.assertEqual(AddressBook.kABDictionaryProperty, 0x6)
        self.assertEqual(AddressBook.kABDataProperty, 0x7)
        self.assertEqual(AddressBook.kABDateComponentsProperty, 0x8)

        self.assertEqual(
            AddressBook.kABMultiStringProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABStringProperty,
        )
        self.assertEqual(
            AddressBook.kABMultiIntegerProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABIntegerProperty,
        )
        self.assertEqual(
            AddressBook.kABMultiRealProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABRealProperty,
        )
        self.assertEqual(
            AddressBook.kABMultiDateProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABDateProperty,
        )
        self.assertEqual(
            AddressBook.kABMultiArrayProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABArrayProperty,
        )
        self.assertEqual(
            AddressBook.kABMultiDictionaryProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABDictionaryProperty,
        )
        self.assertEqual(
            AddressBook.kABMultiDataProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABDataProperty,
        )
        self.assertEqual(
            AddressBook.kABMultiDateComponentsProperty,
            AddressBook.kABMultiValueMask | AddressBook.kABDateComponentsProperty,
        )

        self.assertEqual(AddressBook.kABEqual, 0)
        self.assertEqual(AddressBook.kABNotEqual, 1)
        self.assertEqual(AddressBook.kABLessThan, 2)
        self.assertEqual(AddressBook.kABLessThanOrEqual, 3)
        self.assertEqual(AddressBook.kABGreaterThan, 4)
        self.assertEqual(AddressBook.kABGreaterThanOrEqual, 5)
        self.assertEqual(AddressBook.kABEqualCaseInsensitive, 6)
        self.assertEqual(AddressBook.kABContainsSubString, 7)
        self.assertEqual(AddressBook.kABContainsSubStringCaseInsensitive, 8)
        self.assertEqual(AddressBook.kABPrefixMatch, 9)
        self.assertEqual(AddressBook.kABPrefixMatchCaseInsensitive, 10)
        self.assertEqual(AddressBook.kABBitsInBitFieldMatch, 11)
        self.assertEqual(AddressBook.kABDoesNotContainSubString, 12)
        self.assertEqual(AddressBook.kABDoesNotContainSubStringCaseInsensitive, 13)
        self.assertEqual(AddressBook.kABNotEqualCaseInsensitive, 14)
        self.assertEqual(AddressBook.kABSuffixMatch, 15)
        self.assertEqual(AddressBook.kABSuffixMatchCaseInsensitive, 16)
        self.assertEqual(AddressBook.kABWithinIntervalAroundToday, 17)
        self.assertEqual(AddressBook.kABWithinIntervalAroundTodayYearless, 18)
        self.assertEqual(AddressBook.kABNotWithinIntervalAroundToday, 19)
        self.assertEqual(AddressBook.kABNotWithinIntervalAroundTodayYearless, 20)
        self.assertEqual(AddressBook.kABWithinIntervalFromToday, 21)
        self.assertEqual(AddressBook.kABWithinIntervalFromTodayYearless, 22)
        self.assertEqual(AddressBook.kABNotWithinIntervalFromToday, 23)
        self.assertEqual(AddressBook.kABNotWithinIntervalFromTodayYearless, 24)

        self.assertEqual(AddressBook.kABSearchAnd, 0)
        self.assertEqual(AddressBook.kABSearchOr, 1)
