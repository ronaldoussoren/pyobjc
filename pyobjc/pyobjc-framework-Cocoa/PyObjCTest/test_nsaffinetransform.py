#
# Tests for the struct-wrapper for NSAffineTransformStruct
#
from Foundation import *
from PyObjCTools.TestSupport import *
import operator

class TestNSAffineTransformStruct (TestCase):
    def testConstructor(self):
        p = NSAffineTransformStruct()
        self.assert_(isinstance(p, NSAffineTransformStruct))
        self.assertEqual(p.m11, 0)
        self.assertEqual(p.m12, 0)
        self.assertEqual(p.m21, 0)
        self.assertEqual(p.m22, 0)
        self.assertEqual(p.tX, 0)
        self.assertEqual(p.tY, 0)

        p = NSAffineTransformStruct(1,2, 3, 4, 5, 6)
        self.assert_(isinstance(p, NSAffineTransformStruct))
        self.assertEqual(p.m11, 1)
        self.assertEqual(p.m12, 2)
        self.assertEqual(p.m21, 3)
        self.assertEqual(p.m22, 4)
        self.assertEqual(p.tX, 5)
        self.assertEqual(p.tY, 6)
        self.assertEqual(p[0], 1)
        self.assertEqual(p[1], 2)
        self.assertEqual(p[2], 3)
        self.assertEqual(p[3], 4)
        self.assertEqual(p[4], 5)
        self.assertEqual(p[5], 6)

        p = NSAffineTransformStruct(tY=1,tX=2, m22=3, m21=4, m12=5, m11=6)
        self.assert_(isinstance(p, NSAffineTransformStruct))
        self.assertEqual(p.m11, 6)
        self.assertEqual(p.m12, 5)
        self.assertEqual(p.m21, 4)
        self.assertEqual(p.m22, 3)
        self.assertEqual(p.tX, 2)
        self.assertEqual(p.tY, 1)
        self.assertEqual(p[0], 6)
        self.assertEqual(p[1], 5)
        self.assertEqual(p[2], 4)
        self.assertEqual(p[3], 3)
        self.assertEqual(p[4], 2)
        self.assertEqual(p[5], 1)

        self.assertRaises(TypeError, NSAffineTransformStruct, 1, 2, 3, 4, 5, 6, 7, 8)
        self.assertRaises(TypeError, NSAffineTransformStruct, 1, 2, 3, 4, 5, 6, tY=3)
        self.assertRaises(TypeError, NSAffineTransformStruct, 1, 2, 3, 4, 5, m11=3)
        self.assertRaises(TypeError, NSAffineTransformStruct, m11=3, mXY=4)

    def testHash(self):
        p = NSAffineTransformStruct()
        self.assertRaises(TypeError, hash, p)

    def testCompare(self):
        p = NSAffineTransformStruct(1, 2, 3, 4, 5, 6)
        q = NSAffineTransformStruct(1, 2, 3, 4, 5, 7)
        P = (1, 2, 3, 4, 5, 6)
        Q = (1, 2, 3, 4, 5, 7)

        self.assert_(not (p == P[:4]))
        self.assert_((p != P[:4]))
        self.assert_(not (p <= P[:4]))
        self.assert_(not (p < P[:4]))
        self.assert_((p > P[:4]))
        self.assert_((p >= P[:4]))

        self.assert_(not (p < p))
        self.assert_(not (p < P))
        self.assert_(p < q)
        self.assert_(p < Q)

        self.assert_(p <= p)
        self.assert_(p <= P)
        self.assert_(p <= q)
        self.assert_(p <= Q)

        self.assert_(p == p)
        self.assert_(p == P)
        self.assert_(not (p == q))
        self.assert_(not (p == Q))

        self.assert_(p != q)
        self.assert_(p != Q)
        self.assert_(not(p != p))
        self.assert_(not(p != P))

        self.assert_(q >= p)
        self.assert_(q >= P)
        self.assert_(q >= q)
        self.assert_(q >= Q)

        self.assert_(not (q > q))
        self.assert_(not (q > Q))
        self.assert_(q > p)
        self.assert_(q > P)

    def testRepr(self):
        p = NSAffineTransformStruct()
        self.assertEqual(repr(p), "<NSAffineTransformStruct m11=0.0 m12=0.0 m21=0.0 m22=0.0 tX=0.0 tY=0.0>")

        p = NSAffineTransformStruct(1, 2, 3, 4, 5, 6)
        self.assertEqual(repr(p), "<NSAffineTransformStruct m11=1 m12=2 m21=3 m22=4 tX=5 tY=6>")

        p.tX = p
        self.assertEqual(repr(p), "<NSAffineTransformStruct m11=1 m12=2 m21=3 m22=4 tX=<NSAffineTransformStruct ...> tY=6>")

    def testStr(self):
        p = NSAffineTransformStruct()
        self.assertEqual(str(p), "<NSAffineTransformStruct m11=0.0 m12=0.0 m21=0.0 m22=0.0 tX=0.0 tY=0.0>")

        p = NSAffineTransformStruct(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(p), "<NSAffineTransformStruct m11=1 m12=2 m21=3 m22=4 tX=5 tY=6>")

        p.tX = p
        self.assertEqual(str(p), "<NSAffineTransformStruct m11=1 m12=2 m21=3 m22=4 tX=<NSAffineTransformStruct ...> tY=6>")

    def testSlice(self):
        p = NSAffineTransformStruct(1,2,3,4,5,6)
        q = p[:]

        self.assert_(isinstance(q, tuple))
        self.assertEqual(q, (1.0,2.0,3.0,4.0,5.0,6.0))

    def testDeleteSlice(self):
        p = NSAffineTransformStruct(1,2)

        def delslice(o, b, e):
            del o[b:e]

        self.assertRaises(TypeError, operator.delitem, p, 0)
        self.assertRaises(TypeError, delslice, p, 0, 3)

    def testAssignSlice(self):
        p = NSAffineTransformStruct(1,2,3,4,5,6)
        p[:] = (4,5,6,7,8,9)

        self.assert_(isinstance(p, NSAffineTransformStruct))
        self.assertEqual(p.m11, 4)
        self.assertEqual(p.m12, 5)
        self.assertEqual(p.m21, 6)
        self.assertEqual(p.m22, 7)
        self.assertEqual(p.tX, 8)
        self.assertEqual(p.tY, 9)

        p[:] = p
        self.assert_(isinstance(p, NSAffineTransformStruct))
        self.assertEqual(p.m11, 4)
        self.assertEqual(p.m12, 5)
        self.assertEqual(p.m21, 6)
        self.assertEqual(p.m22, 7)
        self.assertEqual(p.tX, 8)
        self.assertEqual(p.tY, 9)

        p[1:4] = range(3)
        self.assertEqual(p.m11, 4)
        self.assertEqual(p.m12, 0)
        self.assertEqual(p.m21, 1)
        self.assertEqual(p.m22, 2)
        self.assertEqual(p.tX, 8)
        self.assertEqual(p.tY, 9)

        def setslice(o, b, e, v):
            o[b:e] = v

        def delslice(o, b, e):
            del o[b:e]

        self.assertRaises(TypeError, setslice, p, 0, 2, [1,2,3])
        self.assertRaises(TypeError, setslice, p, 0, 2, [3])

        self.assertRaises(TypeError, delslice, p, 0, 0)
        self.assertRaises(TypeError, delslice, p, 0, 1)
        self.assertRaises(TypeError, delslice, p, 0, 2)


class TestAffineTransform (TestCase):
    def testStructReturn (self):
        transform = NSAffineTransform.transform()
        s = transform.transformStruct()
        self.assertIsInstance(s, NSAffineTransformStruct)
        s = NSAffineTransformStruct(0, 1, 2, 3, 4, 5)
        transform.setTransformStruct_(s)

        t = transform.transformStruct()
        self.assertIsInstance(t, NSAffineTransformStruct)
        self.assertEqual(s, t)



if __name__ == "__main__":
    main()
