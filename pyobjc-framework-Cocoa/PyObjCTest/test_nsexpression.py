import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSExpression(TestCase):
    def testConstants(self):
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

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(Foundation.NSBlockExpressionType, 19)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(Foundation.NSAnyKeyExpressionType, 15)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(Foundation.NSConditionalExpressionType, 20)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBlock(
            Foundation.NSExpression.expressionForBlock_arguments_, 0, b"@@@@"
        )
        self.assertResultIsBlock(Foundation.NSExpression.expressionBlock, b"@@@@")

    @min_os_level("10.6")
    def testMethod10_6_unsupported(self):
        self.assertArgIsPrintf(Foundation.NSExpression.expressionWithFormat_, 0)
