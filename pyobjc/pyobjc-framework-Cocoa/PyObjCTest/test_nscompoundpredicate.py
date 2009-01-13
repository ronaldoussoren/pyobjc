from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSCompoundPredicate (TestCase):
    def testConstants(self):
        self.assertEquals(NSNotPredicateType, 0)
        self.assertEquals(NSAndPredicateType, 1)
        self.assertEquals(NSOrPredicateType, 2)

if __name__ == "__main__":
    main()

