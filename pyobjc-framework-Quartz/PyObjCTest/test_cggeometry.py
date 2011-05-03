
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGGeometry (TestCase):
    def testStruct(self):
        v = CGPoint()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)

        v = CGSize()
        self.assertIsInstance(v.width, float)
        self.assertIsInstance(v.height, float)

        v = CGRect()
        self.assertIsInstance(v.origin, CGPoint)
        self.assertIsInstance(v.size, CGSize)

    def testConstants(self):
        self.assertEqual(CGRectMinXEdge, 0)
        self.assertEqual(CGRectMinYEdge, 1)
        self.assertEqual(CGRectMaxXEdge, 2)
        self.assertEqual(CGRectMaxYEdge, 3)

        self.assertIsInstance(CGPointZero, CGPoint)
        self.assertEqual(CGPointZero.x, 0.0)
        self.assertEqual(CGPointZero.y, 0.0)

        self.assertIsInstance(CGSizeZero, CGSize)
        self.assertEqual(CGSizeZero.width, 0.0)
        self.assertEqual(CGSizeZero.height, 0.0)

        self.assertIsInstance(CGRectZero, CGRect)
        self.assertEqual(CGRectZero.origin, CGPointZero)
        self.assertEqual(CGRectZero.size, CGSizeZero)

        self.assertIsInstance(CGRectNull, CGRect)
        self.assertIsInstance(CGRectInfinite, CGRect)

    def testFunctions(self):
        v = CGPointMake(2.5, 3.5)
        self.assertIsInstance(v, CGPoint)
        self.assertEqual(v.x, 2.5)
        self.assertEqual(v.y, 3.5)

        v = CGSizeMake(2.5, 3.5)
        self.assertIsInstance(v, CGSize)
        self.assertEqual(v.width, 2.5)
        self.assertEqual(v.height, 3.5)

        v = CGRectMake(2.5, 3.5, 15.5, 25.5)
        self.assertIsInstance(v, CGRect)
        self.assertEqual(v.origin.x, 2.5)
        self.assertEqual(v.origin.y, 3.5)
        self.assertEqual(v.size.width, 15.5)
        self.assertEqual(v.size.height, 25.5)
        rect = v

        v = CGRectGetMinX(rect)
        self.assertEqual(v, min(rect.origin.x, rect.origin.x + rect.size.width))
        v = CGRectGetMidX(rect)
        self.assertEqual(v, rect.origin.x + (rect.size.width/2))

        v = CGRectGetMaxX(rect)
        self.assertEqual(v, max(rect.origin.x, rect.origin.x + rect.size.width))

        v = CGRectGetMinY(rect)
        self.assertEqual(v, min(rect.origin.y, rect.origin.y + rect.size.height))
        v = CGRectGetMidY(rect)
        self.assertEqual(v, rect.origin.y + (rect.size.height/2))

        v = CGRectGetMaxY(rect)
        self.assertEqual(v, max(rect.origin.y, rect.origin.y + rect.size.height))

        self.assertEqual(CGRectGetWidth(rect), abs(rect.size.width))
        self.assertEqual(CGRectGetHeight(rect), abs(rect.size.height))

        self.assertResultHasType(CGPointEqualToPoint, objc._C_BOOL)
        self.assertTrue(CGPointEqualToPoint((1, 1), (2, 2)) is False)
        self.assertTrue(CGPointEqualToPoint((1, 1), (1, 1)) is True)

        self.assertResultHasType(CGSizeEqualToSize, objc._C_BOOL)
        self.assertTrue(CGSizeEqualToSize((1, 1), (2, 2)) is False)
        self.assertTrue(CGSizeEqualToSize((1, 1), (1, 1)) is True)

        self.assertResultHasType(CGRectEqualToRect, objc._C_BOOL)
        self.assertTrue(CGRectEqualToRect(((1,1), (1,1)), ((2,2), (2,2))) is False)
        self.assertTrue(CGRectEqualToRect(((1,1), (1,1)), ((1,1), (1,1))) is True)

        v = CGRectStandardize(((90, 90), (-4, -5)))
        self.assertIsInstance(v, CGRect)
        self.assertEqual(v, CGRectMake(86, 85, 4, 5))

        self.assertResultHasType(CGRectIsEmpty, objc._C_BOOL)
        self.assertTrue(CGRectIsEmpty(rect) is False)
        self.assertTrue(CGRectIsEmpty(CGRectZero) is True)

        self.assertResultHasType(CGRectIsNull, objc._C_BOOL)
        self.assertTrue(CGRectIsNull(rect) is False)
        self.assertTrue(CGRectIsNull(CGRectNull) is True)

        self.assertResultHasType(CGRectIsInfinite, objc._C_BOOL)
        self.assertTrue(CGRectIsInfinite(rect) is False)
        self.assertTrue(CGRectIsInfinite(CGRectInfinite) is True)

        v = CGRectInset(rect, 2, 3)
        self.assertIsInstance(v, CGRect)
        self.assertEqual(v.origin.x, rect.origin.x + 2)
        self.assertEqual(v.origin.y, rect.origin.y + 3)
        self.assertEqual(v.size.width, rect.size.width - 4)
        self.assertEqual(v.size.height, rect.size.height - 6)

        v = CGRectIntegral(CGRectMake(1.5, 2.5, 3.5, 4.5))
        self.assertIsInstance(v, CGRect)
        self.assertEqual(v, ((1, 2), (4, 5)))

        v = CGRectUnion(((1,1), (4,5)), ((99,5), (40, 40)))
        self.assertIsInstance(v, CGRect)

        v = CGRectIntersection(((1,1), (4,5)), ((99,5), (40, 40)))
        self.assertIsInstance(v, CGRect)

        r = CGRectOffset(rect, 9, -5)
        self.assertIsInstance(v, CGRect)

        self.assertArgIsOut(CGRectDivide, 1)
        self.assertArgIsOut(CGRectDivide, 2)
        slice, remainder = CGRectDivide(rect, None, None, 10, CGRectMinYEdge)
        self.assertIsInstance(slice, CGRect)
        self.assertIsInstance(remainder, CGRect)

        self.assertResultHasType(CGRectContainsPoint, objc._C_BOOL)
        self.assertResultHasType(CGRectContainsRect, objc._C_BOOL)
        self.assertResultHasType(CGRectIntersectsRect, objc._C_BOOL)
        self.assertTrue(CGRectContainsPoint(rect, rect.origin) is True)
        self.assertTrue(CGRectContainsRect(rect, rect) is True)
        self.assertTrue(CGRectIntersectsRect(rect, rect) is True)

    @min_os_level('10.5')
    def testFunctions10_5(self):
        d = CGPointCreateDictionaryRepresentation((10, 5))
        self.assertIsInstance(d, CFDictionaryRef)

        ok, p = CGPointMakeWithDictionaryRepresentation(d, None)
        self.assertTrue(ok is True)
        self.assertIsInstance(p, CGPoint)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 5)

        d = CGSizeCreateDictionaryRepresentation((10, 5))
        self.assertIsInstance(d, CFDictionaryRef)

        ok, p = CGSizeMakeWithDictionaryRepresentation(d, None)
        self.assertTrue(ok is True)
        self.assertIsInstance(p, CGSize)
        self.assertEqual(p.width, 10)
        self.assertEqual(p.height, 5)

        d = CGRectCreateDictionaryRepresentation(CGRectMake(0, 10, 20, 30))
        self.assertIsInstance(d, CFDictionaryRef)

        ok, p = CGRectMakeWithDictionaryRepresentation(d, None)
        self.assertTrue(ok is True)
        self.assertIsInstance(p, CGRect)
        self.assertEqual(p, CGRectMake(0, 10, 20, 30))



if __name__ == "__main__":
    main()
