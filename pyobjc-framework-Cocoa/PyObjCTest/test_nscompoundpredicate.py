from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSCompoundPredicate (TestCase):
    def testConstants(self):
        self.assertEqual(NSNotPredicateType, 0)
        self.assertEqual(NSAndPredicateType, 1)
        self.assertEqual(NSOrPredicateType, 2)

if __name__ == "__main__":
    main()
