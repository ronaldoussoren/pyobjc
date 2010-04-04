from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSComparisonPredicate (TestCase):
    def testConstants(self):
        self.assertEqual(NSCaseInsensitivePredicateOption, 1)
        self.assertEqual(NSDiacriticInsensitivePredicateOption, 2)

        self.assertEqual(NSDirectPredicateModifier, 0)
        self.assertEqual(NSAllPredicateModifier, 1)
        self.assertEqual(NSAnyPredicateModifier, 2)

        self.assertEqual(NSLessThanPredicateOperatorType, 0)
        self.assertEqual(NSLessThanOrEqualToPredicateOperatorType, 1)
        self.assertEqual(NSGreaterThanPredicateOperatorType, 2)
        self.assertEqual(NSGreaterThanOrEqualToPredicateOperatorType, 3)
        self.assertEqual(NSEqualToPredicateOperatorType, 4)
        self.assertEqual(NSNotEqualToPredicateOperatorType, 5)
        self.assertEqual(NSMatchesPredicateOperatorType, 6)
        self.assertEqual(NSLikePredicateOperatorType, 7)
        self.assertEqual(NSBeginsWithPredicateOperatorType, 8)
        self.assertEqual(NSEndsWithPredicateOperatorType, 9)
        self.assertEqual(NSInPredicateOperatorType, 10)
        self.assertEqual(NSCustomSelectorPredicateOperatorType, 11)
        self.assertEqual(NSContainsPredicateOperatorType, 99)
        self.assertEqual(NSBetweenPredicateOperatorType, 100)

    def testMethods(self):
        self.assertArgIsSEL(NSComparisonPredicate.predicateWithLeftExpression_rightExpression_customSelector_, 2, objc._C_NSBOOL + b'@:@')
        self.assertArgIsSEL(NSComparisonPredicate.initWithLeftExpression_rightExpression_customSelector_, 2, objc._C_NSBOOL + b'@:@')

if __name__ == "__main__":
    main()

