from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSExpression (TestCase):
    def testConstants(self):
        self.assertEqual(NSConstantValueExpressionType, 0)
        self.assertEqual(NSEvaluatedObjectExpressionType, 1)
        self.assertEqual(NSVariableExpressionType, 2)
        self.assertEqual(NSKeyPathExpressionType, 3)
        self.assertEqual(NSFunctionExpressionType, 4)
        self.assertEqual(NSUnionSetExpressionType, 5)
        self.assertEqual(NSIntersectSetExpressionType, 6)
        self.assertEqual(NSMinusSetExpressionType, 7)
        self.assertEqual(NSSubqueryExpressionType, 13)
        self.assertEqual(NSAggregateExpressionType, 14)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSBlockExpressionType, 19)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBlock(NSExpression.expressionForBlock_arguments_, 0, b'@@@@')
        self.assertResultIsBlock(NSExpression.expressionBlock, b'@@@@')

    @expectedFailure
    @min_os_level('10.6')
    def testMethod10_6_unsupported(self):
        # There is no documentation for this method, it is therefore unclear what kind
        # of format string is used
        self.fail('expressionWithFormat:fmt, ...')



if __name__ == "__main__":
    main()
