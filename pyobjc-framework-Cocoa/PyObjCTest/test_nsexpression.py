import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSExpression(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Foundation.NSExpressionType)
        self.assertEqual(Foundation.NSConstantValueExpressionType, 0)
        self.assertEqual(Foundation.NSEvaluatedObjectExpressionType, 1)
        self.assertEqual(Foundation.NSVariableExpressionType, 2)
        self.assertEqual(Foundation.NSKeyPathExpressionType, 3)
        self.assertEqual(Foundation.NSFunctionExpressionType, 4)
        self.assertEqual(Foundation.NSUnionSetExpressionType, 5)
        self.assertEqual(Foundation.NSIntersectSetExpressionType, 6)
        self.assertEqual(Foundation.NSMinusSetExpressionType, 7)
        self.assertEqual(Foundation.NSSubqueryExpressionType, 13)
        self.assertEqual(Foundation.NSAggregateExpressionType, 14)
        self.assertEqual(Foundation.NSAnyKeyExpressionType, 15)
        self.assertEqual(Foundation.NSBlockExpressionType, 19)
        self.assertEqual(Foundation.NSConditionalExpressionType, 20)

    def test_methods(self):
        self.assertArgIsBlock(
            Foundation.NSExpression.expressionForBlock_arguments_, 0, b"@@@@"
        )
        self.assertResultIsBlock(Foundation.NSExpression.expressionBlock, b"@@@@")

        self.assertArgIsPrintf(Foundation.NSExpression.expressionWithFormat_, 0)
