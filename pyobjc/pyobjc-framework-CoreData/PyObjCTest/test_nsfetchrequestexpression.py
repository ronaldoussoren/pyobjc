
from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSFetchRequestExpression (TestCase):

    @min_os_level("10.5")
    def testConstants(self):
        self.failUnlessEqual(NSFetchRequestExpressionType, 50)

    @min_os_level("10.5")
    def testMethods(self):
        self.failUnlessArgIsBOOL(NSFetchRequestExpression.expressionForFetch_context_countOnly_, 2)
        self.failUnlessResultIsBOOL(NSFetchRequestExpression.isCountOnlyRequest)

if __name__ == "__main__":
    main()
