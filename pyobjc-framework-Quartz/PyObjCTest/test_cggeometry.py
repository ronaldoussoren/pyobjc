from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCGGeometry(TestCase):
    def testStruct(self):
        v = Quartz.CGPoint()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)

        v = Quartz.CGSize()
        self.assertIsInstance(v.width, float)
        self.assertIsInstance(v.height, float)

        v = Quartz.CGRect()
        self.assertIsInstance(v.origin, Quartz.CGPoint)
        self.assertIsInstance(v.size, Quartz.CGSize)

        v = Quartz.CGVector()
        self.assertIsInstance(v.dx, float)
        self.assertIsInstance(v.dy, float)

    def testConstants(self):
        self.assertEqual(Quartz.CGRectMinXEdge, 0)
        self.assertEqual(Quartz.CGRectMinYEdge, 1)
        self.assertEqual(Quartz.CGRectMaxXEdge, 2)
        self.assertEqual(Quartz.CGRectMaxYEdge, 3)

        self.assertIsInstance(Quartz.CGPointZero, Quartz.CGPoint)
        self.assertEqual(Quartz.CGPointZero.x, 0.0)
        self.assertEqual(Quartz.CGPointZero.y, 0.0)

        self.assertIsInstance(Quartz.CGSizeZero, Quartz.CGSize)
        self.assertEqual(Quartz.CGSizeZero.width, 0.0)
        self.assertEqual(Quartz.CGSizeZero.height, 0.0)

        self.assertIsInstance(Quartz.CGRectZero, Quartz.CGRect)
        self.assertEqual(Quartz.CGRectZero.origin, Quartz.CGPointZero)
        self.assertEqual(Quartz.CGRectZero.size, Quartz.CGSizeZero)

        self.assertIsInstance(Quartz.CGRectNull, Quartz.CGRect)
        self.assertIsInstance(Quartz.CGRectInfinite, Quartz.CGRect)

    def testFunctions(self):
        v = Quartz.CGPointMake(2.5, 3.5)
        self.assertIsInstance(v, Quartz.CGPoint)
        self.assertEqual(v.x, 2.5)
        self.assertEqual(v.y, 3.5)

        v = Quartz.CGSizeMake(2.5, 3.5)
        self.assertIsInstance(v, Quartz.CGSize)
        self.assertEqual(v.width, 2.5)
        self.assertEqual(v.height, 3.5)

        v = Quartz.CGRectMake(2.5, 3.5, 15.5, 25.5)
        self.assertIsInstance(v, Quartz.CGRect)
        self.assertEqual(v.origin.x, 2.5)
        self.assertEqual(v.origin.y, 3.5)
        self.assertEqual(v.size.width, 15.5)
        self.assertEqual(v.size.height, 25.5)
        rect = v

        v = Quartz.CGRectGetMinX(rect)
        self.assertEqual(v, min(rect.origin.x, rect.origin.x + rect.size.width))
        v = Quartz.CGRectGetMidX(rect)
        self.assertEqual(v, rect.origin.x + (rect.size.width / 2))

        v = Quartz.CGRectGetMaxX(rect)
        self.assertEqual(v, max(rect.origin.x, rect.origin.x + rect.size.width))

        v = Quartz.CGRectGetMinY(rect)
        self.assertEqual(v, min(rect.origin.y, rect.origin.y + rect.size.height))
        v = Quartz.CGRectGetMidY(rect)
        self.assertEqual(v, rect.origin.y + (rect.size.height / 2))

        v = Quartz.CGRectGetMaxY(rect)
        self.assertEqual(v, max(rect.origin.y, rect.origin.y + rect.size.height))

        self.assertEqual(Quartz.CGRectGetWidth(rect), abs(rect.size.width))
        self.assertEqual(Quartz.CGRectGetHeight(rect), abs(rect.size.height))

        self.assertResultHasType(Quartz.CGPointEqualToPoint, objc._C_BOOL)
        self.assertTrue(Quartz.CGPointEqualToPoint((1, 1), (2, 2)) is False)
        self.assertTrue(Quartz.CGPointEqualToPoint((1, 1), (1, 1)) is True)

        self.assertResultHasType(Quartz.CGSizeEqualToSize, objc._C_BOOL)
        self.assertTrue(Quartz.CGSizeEqualToSize((1, 1), (2, 2)) is False)
        self.assertTrue(Quartz.CGSizeEqualToSize((1, 1), (1, 1)) is True)

        self.assertResultHasType(Quartz.CGRectEqualToRect, objc._C_BOOL)
        self.assertTrue(
            Quartz.CGRectEqualToRect(((1, 1), (1, 1)), ((2, 2), (2, 2))) is False
        )
        self.assertTrue(
            Quartz.CGRectEqualToRect(((1, 1), (1, 1)), ((1, 1), (1, 1))) is True
        )

        v = Quartz.CGRectStandardize(((90, 90), (-4, -5)))
        self.assertIsInstance(v, Quartz.CGRect)
        self.assertEqual(v, Quartz.CGRectMake(86, 85, 4, 5))

        self.assertResultHasType(Quartz.CGRectIsEmpty, objc._C_BOOL)
        self.assertTrue(Quartz.CGRectIsEmpty(rect) is False)
        self.assertTrue(Quartz.CGRectIsEmpty(Quartz.CGRectZero) is True)

        self.assertResultHasType(Quartz.CGRectIsNull, objc._C_BOOL)
        self.assertTrue(Quartz.CGRectIsNull(rect) is False)
        self.assertTrue(Quartz.CGRectIsNull(Quartz.CGRectNull) is True)

        self.assertResultHasType(Quartz.CGRectIsInfinite, objc._C_BOOL)
        self.assertTrue(Quartz.CGRectIsInfinite(rect) is False)
        self.assertTrue(Quartz.CGRectIsInfinite(Quartz.CGRectInfinite) is True)

        v = Quartz.CGRectInset(rect, 2, 3)
        self.assertIsInstance(v, Quartz.CGRect)
        self.assertEqual(v.origin.x, rect.origin.x + 2)
        self.assertEqual(v.origin.y, rect.origin.y + 3)
        self.assertEqual(v.size.width, rect.size.width - 4)
        self.assertEqual(v.size.height, rect.size.height - 6)

        v = Quartz.CGRectIntegral(Quartz.CGRectMake(1.5, 2.5, 3.5, 4.5))
        self.assertIsInstance(v, Quartz.CGRect)
        self.assertEqual(v, ((1, 2), (4, 5)))

        v = Quartz.CGRectUnion(((1, 1), (4, 5)), ((99, 5), (40, 40)))
        self.assertIsInstance(v, Quartz.CGRect)

        v = Quartz.CGRectIntersection(((1, 1), (4, 5)), ((99, 5), (40, 40)))
        self.assertIsInstance(v, Quartz.CGRect)

        Quartz.CGRectOffset(rect, 9, -5)
        self.assertIsInstance(v, Quartz.CGRect)

        self.assertArgIsOut(Quartz.CGRectDivide, 1)
        self.assertArgIsOut(Quartz.CGRectDivide, 2)
        slice_value, remainder = Quartz.CGRectDivide(
            rect, None, None, 10, Quartz.CGRectMinYEdge
        )
        self.assertIsInstance(slice_value, Quartz.CGRect)
        self.assertIsInstance(remainder, Quartz.CGRect)

        self.assertResultHasType(Quartz.CGRectContainsPoint, objc._C_BOOL)
        self.assertResultHasType(Quartz.CGRectContainsRect, objc._C_BOOL)
        self.assertResultHasType(Quartz.CGRectIntersectsRect, objc._C_BOOL)
        self.assertTrue(Quartz.CGRectContainsPoint(rect, rect.origin) is True)
        self.assertTrue(Quartz.CGRectContainsRect(rect, rect) is True)
        self.assertTrue(Quartz.CGRectIntersectsRect(rect, rect) is True)

    @min_os_level("10.5")
    def testFunctions10_5(self):
        d = Quartz.CGPointCreateDictionaryRepresentation((10, 5))
        self.assertIsInstance(d, Quartz.CFDictionaryRef)

        ok, p = Quartz.CGPointMakeWithDictionaryRepresentation(d, None)
        self.assertTrue(ok is True)
        self.assertIsInstance(p, Quartz.CGPoint)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 5)

        d = Quartz.CGSizeCreateDictionaryRepresentation((10, 5))
        self.assertIsInstance(d, Quartz.CFDictionaryRef)

        ok, p = Quartz.CGSizeMakeWithDictionaryRepresentation(d, None)
        self.assertTrue(ok is True)
        self.assertIsInstance(p, Quartz.CGSize)
        self.assertEqual(p.width, 10)
        self.assertEqual(p.height, 5)

        d = Quartz.CGRectCreateDictionaryRepresentation(
            Quartz.CGRectMake(0, 10, 20, 30)
        )
        self.assertIsInstance(d, Quartz.CFDictionaryRef)

        ok, p = Quartz.CGRectMakeWithDictionaryRepresentation(d, None)
        self.assertTrue(ok is True)
        self.assertIsInstance(p, Quartz.CGRect)
        self.assertEqual(p, Quartz.CGRectMake(0, 10, 20, 30))

    @min_os_level("10.9")
    def testFunctions10_9(self):
        v = Quartz.CGVectorMake(2.5, 3.5)
        self.assertIsInstance(v, Quartz.CGVector)
        self.assertEqual(v.dx, 2.5)
        self.assertEqual(v.dy, 3.5)
