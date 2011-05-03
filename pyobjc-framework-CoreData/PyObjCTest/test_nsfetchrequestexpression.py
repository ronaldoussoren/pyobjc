
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSFetchRequestExpression (TestCase):

    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(NSFetchRequestExpressionType, 50)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgIsBOOL(NSFetchRequestExpression.expressionForFetch_context_countOnly_, 2)
        self.assertResultIsBOOL(NSFetchRequestExpression.isCountOnlyRequest)

if __name__ == "__main__":
    main()
