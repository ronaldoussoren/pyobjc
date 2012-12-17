
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGAffineTransform (TestCase):
    def testStruct(self):
        v = CGAffineTransform()
        self.assertTrue(hasattr(v, "a"))
        self.assertTrue(hasattr(v, "b"))
        self.assertTrue(hasattr(v, "c"))
        self.assertTrue(hasattr(v, "d"))
        self.assertTrue(hasattr(v, "tx"))
        self.assertTrue(hasattr(v, "ty"))

    def testConstants(self):
        self.assertIsInstance(CGAffineTransformIdentity, CGAffineTransform)
        self.assertIsInstance(CGAffineTransformIdentity.a, float)
        self.assertIsInstance(CGAffineTransformIdentity.b, float)
        self.assertIsInstance(CGAffineTransformIdentity.c, float)
        self.assertIsInstance(CGAffineTransformIdentity.d, float)
        self.assertIsInstance(CGAffineTransformIdentity.tx, float)
        self.assertIsInstance(CGAffineTransformIdentity.ty, float)

    def testFunctions(self):
        tf = CGAffineTransformMake(1.5, 2.5, 3.5, 4.5, 5.5, 6.5)
        self.assertIsInstance(tf, CGAffineTransform)
        self.assertEqual(tf.a,  1.5)
        self.assertEqual(tf.b,  2.5)
        self.assertEqual(tf.c,  3.5)
        self.assertEqual(tf.d,  4.5)
        self.assertEqual(tf.tx, 5.5)
        self.assertEqual(tf.ty, 6.5)

        tf = CGAffineTransformMakeTranslation(2.5, 3.5)
        self.assertIsInstance(tf, CGAffineTransform)
        self.assertEqual(tf.a,  1.0)
        self.assertEqual(tf.b,  0.0)
        self.assertEqual(tf.c,  0.0)
        self.assertEqual(tf.d,  1.0)
        self.assertEqual(tf.tx, 2.5)
        self.assertEqual(tf.ty, 3.5)

        tf = CGAffineTransformMakeScale(2.5, 3.5)
        self.assertIsInstance(tf, CGAffineTransform)
        self.assertEqual(tf.a,  2.5)
        self.assertEqual(tf.b,  0.0)
        self.assertEqual(tf.c,  0.0)
        self.assertEqual(tf.d,  3.5)
        self.assertEqual(tf.tx, 0.0)
        self.assertEqual(tf.ty, 0.0)

        tf = CGAffineTransformMakeRotation(3.4)
        self.assertIsInstance(tf, CGAffineTransform)

        self.assertResultHasType(CGAffineTransformIsIdentity, objc._C_BOOL)
        self.assertTrue(CGAffineTransformIsIdentity(tf) is False)
        self.assertTrue(CGAffineTransformIsIdentity(CGAffineTransformIdentity) is True)

        tf = CGAffineTransformTranslate(tf, 2.5, 3.5)
        self.assertIsInstance(tf, CGAffineTransform)

        tf = CGAffineTransformScale(tf, 5.5, 9.5)
        self.assertIsInstance(tf, CGAffineTransform)

        tf = CGAffineTransformRotate(tf, 0.8)
        self.assertIsInstance(tf, CGAffineTransform)

        tf = CGAffineTransformInvert(tf)
        self.assertIsInstance(tf, CGAffineTransform)

        tf2 = CGAffineTransformConcat(tf,
                CGAffineTransformMake(1.0, 1.0, 1.0, 1.0, 1.0, 1.0))
        self.assertIsInstance(tf2, CGAffineTransform)

        self.assertResultHasType(CGAffineTransformEqualToTransform, objc._C_BOOL)
        self.assertTrue(CGAffineTransformEqualToTransform(tf, tf2) is False)
        self.assertTrue(CGAffineTransformEqualToTransform(tf2, tf2) is True)

        pt = CGPointApplyAffineTransform((2.5, 3.5), tf)
        self.assertIsInstance(pt, CGPoint)

        sz = CGSizeApplyAffineTransform((2.5, 3.5), tf)
        self.assertIsInstance(sz, CGSize)

        rct = CGRectApplyAffineTransform(((2.5, 3.5), (4.5, 5.5)), tf)
        self.assertIsInstance(rct, CGRect)

if __name__ == "__main__":
    main()
