from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSExpression (TestCase):
    def testConstants(self):
        self.assertEquals(NSConstantValueExpressionType, 0)
        self.assertEquals(NSEvaluatedObjectExpressionType, 1)
        self.assertEquals(NSVariableExpressionType, 2)
        self.assertEquals(NSKeyPathExpressionType, 3)
        self.assertEquals(NSFunctionExpressionType, 4)
        self.assertEquals(NSUnionSetExpressionType, 5)
        self.assertEquals(NSIntersectSetExpressionType, 6)
        self.assertEquals(NSMinusSetExpressionType, 7)
        self.assertEquals(NSSubqueryExpressionType, 13)
        self.assertEquals(NSAggregateExpressionType, 14)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEquals(NSBlockExpressionType, 19)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsBlock(NSExpression.expressionForBlock_arguments_, 0, '@@@@')
        self.failUnlessResultIsBlock(NSExpression.expressionBlock, '@@@@')



if __name__ == "__main__":
    main()
