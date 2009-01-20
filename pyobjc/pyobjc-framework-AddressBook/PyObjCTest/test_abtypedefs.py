
from PyObjCTools.TestSupport import *
from AddressBook import *

class TestABTypedefs (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kABMultiValueMask, 0x100)

        self.failUnlessEqual(kABErrorInProperty, 0x0)
        self.failUnlessEqual(kABStringProperty, 0x1)
        self.failUnlessEqual(kABIntegerProperty, 0x2)
        self.failUnlessEqual(kABRealProperty, 0x3)
        self.failUnlessEqual(kABDateProperty, 0x4)
        self.failUnlessEqual(kABArrayProperty, 0x5)
        self.failUnlessEqual(kABDictionaryProperty, 0x6)
        self.failUnlessEqual(kABDataProperty, 0x7)
        self.failUnlessEqual(kABMultiStringProperty, kABMultiValueMask | kABStringProperty)
        self.failUnlessEqual(kABMultiIntegerProperty, kABMultiValueMask | kABIntegerProperty)
        self.failUnlessEqual(kABMultiRealProperty, kABMultiValueMask | kABRealProperty)
        self.failUnlessEqual(kABMultiDateProperty, kABMultiValueMask | kABDateProperty)
        self.failUnlessEqual(kABMultiArrayProperty, kABMultiValueMask | kABArrayProperty)
        self.failUnlessEqual(kABMultiDictionaryProperty, kABMultiValueMask | kABDictionaryProperty)
        self.failUnlessEqual(kABMultiDataProperty, kABMultiValueMask | kABDataProperty)

        self.failUnlessEqual(kABEqual, 0)
        self.failUnlessEqual(kABNotEqual, 1)
        self.failUnlessEqual(kABLessThan, 2)
        self.failUnlessEqual(kABLessThanOrEqual, 3)
        self.failUnlessEqual(kABGreaterThan, 4)
        self.failUnlessEqual(kABGreaterThanOrEqual, 5)
        self.failUnlessEqual(kABEqualCaseInsensitive, 6)
        self.failUnlessEqual(kABContainsSubString, 7)
        self.failUnlessEqual(kABContainsSubStringCaseInsensitive, 8)
        self.failUnlessEqual(kABPrefixMatch, 9)
        self.failUnlessEqual(kABPrefixMatchCaseInsensitive, 10)
        self.failUnlessEqual(kABBitsInBitFieldMatch, 11)
        self.failUnlessEqual(kABDoesNotContainSubString, 12)
        self.failUnlessEqual(kABDoesNotContainSubStringCaseInsensitive, 13)
        self.failUnlessEqual(kABNotEqualCaseInsensitive, 14)
        self.failUnlessEqual(kABSuffixMatch, 15)
        self.failUnlessEqual(kABSuffixMatchCaseInsensitive, 16)
        self.failUnlessEqual(kABWithinIntervalAroundToday, 17)
        self.failUnlessEqual(kABWithinIntervalAroundTodayYearless, 18)
        self.failUnlessEqual(kABNotWithinIntervalAroundToday, 19)
        self.failUnlessEqual(kABNotWithinIntervalAroundTodayYearless, 20)
        self.failUnlessEqual(kABWithinIntervalFromToday, 21)
        self.failUnlessEqual(kABWithinIntervalFromTodayYearless, 22)
        self.failUnlessEqual(kABNotWithinIntervalFromToday, 23)
        self.failUnlessEqual(kABNotWithinIntervalFromTodayYearless, 24)

        self.failUnlessEqual(kABSearchAnd, 0)
        self.failUnlessEqual(kABSearchOr, 1)



if __name__ == "__main__":
    main()
