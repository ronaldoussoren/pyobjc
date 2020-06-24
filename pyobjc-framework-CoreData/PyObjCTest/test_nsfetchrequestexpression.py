import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSFetchRequestExpression(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(CoreData.NSFetchRequestExpressionType, 50)

    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgIsBOOL(
            CoreData.NSFetchRequestExpression.expressionForFetch_context_countOnly_, 2
        )
        self.assertResultIsBOOL(CoreData.NSFetchRequestExpression.isCountOnlyRequest)
