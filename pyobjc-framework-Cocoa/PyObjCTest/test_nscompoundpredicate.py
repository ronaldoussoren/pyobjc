import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSCompoundPredicate(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSCompoundPredicateType)

    def testConstants(self):
        self.assertEqual(Foundation.NSNotPredicateType, 0)
        self.assertEqual(Foundation.NSAndPredicateType, 1)
        self.assertEqual(Foundation.NSOrPredicateType, 2)
