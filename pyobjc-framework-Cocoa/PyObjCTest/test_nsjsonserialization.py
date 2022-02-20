import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSJSONSerialization(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSJSONReadingOptions)
        self.assertIsEnumType(Foundation.NSJSONWritingOptions)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Foundation.NSJSONReadingMutableContainers, (1 << 0))
        self.assertEqual(Foundation.NSJSONReadingMutableLeaves, (1 << 1))
        self.assertEqual(Foundation.NSJSONReadingAllowFragments, (1 << 2))
        self.assertEqual(Foundation.NSJSONReadingFragmentsAllowed, (1 << 2))
        self.assertEqual(Foundation.NSJSONReadingJSON5Allowed, (1 << 3))
        self.assertEqual(Foundation.NSJSONReadingTopLevelDictionaryAssumed, (1 << 4))

        self.assertEqual(Foundation.NSJSONWritingPrettyPrinted, (1 << 0))
        self.assertEqual(Foundation.NSJSONWritingSortedKeys, (1 << 1))
        self.assertEqual(Foundation.NSJSONWritingFragmentsAllowed, (1 << 2))
        self.assertEqual(Foundation.NSJSONWritingWithoutEscapingSlashes, (1 << 3))

    @min_os_level("10.7")
    def testMethod10_7(self):
        self.assertResultIsBOOL(Foundation.NSJSONSerialization.isValidJSONObject_)
        self.assertArgIsOut(
            Foundation.NSJSONSerialization.dataWithJSONObject_options_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSJSONSerialization.JSONObjectWithData_options_error_, 2
        )
        self.assertArgIsOut(
            Foundation.NSJSONSerialization.writeJSONObject_toStream_options_error_, 3
        )
        self.assertArgIsOut(
            Foundation.NSJSONSerialization.JSONObjectWithStream_options_error_, 2
        )
