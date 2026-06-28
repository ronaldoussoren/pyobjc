import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSFetchRequestExpression(TestCase):
    def test_constants(self):
        self.assertEqual(CoreData.NSFetchRequestExpressionType, 50)

    def test_methods(self):
        self.assertArgIsBOOL(
            CoreData.NSFetchRequestExpression.expressionForFetch_context_countOnly_, 2
        )
        self.assertResultIsBOOL(CoreData.NSFetchRequestExpression.isCountOnlyRequest)
