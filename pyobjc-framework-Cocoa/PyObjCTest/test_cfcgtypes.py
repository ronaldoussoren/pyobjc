import CoreFoundation
import sys
from PyObjCTools.TestSupport import TestCase


class TestCFGGTypes(TestCase):
    def test_constants(self):
        self.assertEqual(CoreFoundation.CGFLOAT_MIN, sys.float_info.min)
        self.assertEqual(CoreFoundation.CGFLOAT_MAX, sys.float_info.max)
        self.assertEqual(CoreFoundation.CGFLOAT_EPSILON, sys.float_info.epsilon)

        self.assertEqual(CoreFoundation.CGRectMinXEdge, 0)
        self.assertEqual(CoreFoundation.CGRectMinYEdge, 1)
        self.assertEqual(CoreFoundation.CGRectMaxXEdge, 2)
        self.assertEqual(CoreFoundation.CGRectMaxYEdge, 3)

    def test_structs_types(self):
        v = CoreFoundation.CGPoint()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)

        v = CoreFoundation.CGSize()
        self.assertIsInstance(v.width, float)
        self.assertIsInstance(v.height, float)

        v = CoreFoundation.CGVector()
        self.assertIsInstance(v.dx, float)
        self.assertIsInstance(v.dy, float)

        v = CoreFoundation.CGRect()
        self.assertIsInstance(v.origin, CoreFoundation.CGPoint)
        self.assertIsInstance(v.size, CoreFoundation.CGSize)

        v = CoreFoundation.CGAffineTransform()
        self.assertIsInstance(v.a, float)
        self.assertIsInstance(v.b, float)
        self.assertIsInstance(v.c, float)
        self.assertIsInstance(v.d, float)
        self.assertIsInstance(v.tx, float)
        self.assertIsInstance(v.ty, float)

        v = CoreFoundation.CGAffineTransformComponents()
        self.assertIsInstance(v.scale, CoreFoundation.CGSize)
        self.assertIsInstance(v.horizontalShear, float)
        self.assertIsInstance(v.rotation, float)
        self.assertIsInstance(v.translation, CoreFoundation.CGVector)
