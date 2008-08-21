from Foundation import *
import unittest

class TestCompare (unittest.TestCase):
    def testConstants(self):
        self.assertEquals(NSCaseInsensitivePredicateOption, 0x01)
        self.assertEquals(NSDiacriticInsensitivePredicateOption, 0x02)
        self.assertEquals(NSDirectPredicateModifier, 0)
        self.assertEquals(NSAllPredicateModifier, 1)
        self.assertEquals(NSAnyPredicateModifier, 2)
        self.assertEquals(NSLessThanPredicateOperatorType, 0)
        self.assertEquals(NSLessThanOrEqualToPredicateOperatorType, 1)
        self.assertEquals(NSGreaterThanPredicateOperatorType, 2)
        self.assertEquals(NSGreaterThanOrEqualToPredicateOperatorType, 3)
        self.assertEquals(NSEqualToPredicateOperatorType, 4)
        self.assertEquals(NSNotEqualToPredicateOperatorType, 5)
        self.assertEquals(NSMatchesPredicateOperatorType, 6)
        self.assertEquals(NSLikePredicateOperatorType, 7)
        self.assertEquals(NSBeginsWithPredicateOperatorType, 8)
        self.assertEquals(NSEndsWithPredicateOperatorType, 9)
        self.assertEquals(NSInPredicateOperatorType, 10)
        self.assertEquals(NSCustomSelectorPredicateOperatorType, 11)
        self.assertEquals(NSContainsPredicateOperatorType, 99)
        self.assertEquals(NSBetweenPredicateOperatorType, 100)

if __name__ == "__main__":
    unittest.main()
