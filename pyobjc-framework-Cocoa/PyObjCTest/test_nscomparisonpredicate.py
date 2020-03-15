import Foundation
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSComparisonPredicate(TestCase):
    def testConstants(self):
        self.assertEqual(Foundation.NSCaseInsensitivePredicateOption, 1)
        self.assertEqual(Foundation.NSDiacriticInsensitivePredicateOption, 2)
        self.assertEqual(Foundation.NSNormalizedPredicateOption, 4)

        self.assertEqual(Foundation.NSDirectPredicateModifier, 0)
        self.assertEqual(Foundation.NSAllPredicateModifier, 1)
        self.assertEqual(Foundation.NSAnyPredicateModifier, 2)

        self.assertEqual(Foundation.NSLessThanPredicateOperatorType, 0)
        self.assertEqual(Foundation.NSLessThanOrEqualToPredicateOperatorType, 1)
        self.assertEqual(Foundation.NSGreaterThanPredicateOperatorType, 2)
        self.assertEqual(Foundation.NSGreaterThanOrEqualToPredicateOperatorType, 3)
        self.assertEqual(Foundation.NSEqualToPredicateOperatorType, 4)
        self.assertEqual(Foundation.NSNotEqualToPredicateOperatorType, 5)
        self.assertEqual(Foundation.NSMatchesPredicateOperatorType, 6)
        self.assertEqual(Foundation.NSLikePredicateOperatorType, 7)
        self.assertEqual(Foundation.NSBeginsWithPredicateOperatorType, 8)
        self.assertEqual(Foundation.NSEndsWithPredicateOperatorType, 9)
        self.assertEqual(Foundation.NSInPredicateOperatorType, 10)
        self.assertEqual(Foundation.NSCustomSelectorPredicateOperatorType, 11)
        self.assertEqual(Foundation.NSContainsPredicateOperatorType, 99)
        self.assertEqual(Foundation.NSBetweenPredicateOperatorType, 100)

    def testMethods(self):
        self.assertArgIsSEL(
            Foundation.NSComparisonPredicate.predicateWithLeftExpression_rightExpression_customSelector_,  # noqa: B950
            2,
            objc._C_NSBOOL + b"@:@",
        )
        self.assertArgIsSEL(
            Foundation.NSComparisonPredicate.initWithLeftExpression_rightExpression_customSelector_,  # noqa: B950
            2,
            objc._C_NSBOOL + b"@:@",
        )
        self.assertResultIsSEL(
            Foundation.NSComparisonPredicate.customSelector, objc._C_NSBOOL + b"@:@"
        )
