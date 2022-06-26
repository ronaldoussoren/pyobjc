from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCGAffineTransform(TestCase):
    def testStruct(self):
        v = Quartz.CGAffineTransform()
        self.assertTrue(hasattr(v, "a"))
        self.assertTrue(hasattr(v, "b"))
        self.assertTrue(hasattr(v, "c"))
        self.assertTrue(hasattr(v, "d"))
        self.assertTrue(hasattr(v, "tx"))
        self.assertTrue(hasattr(v, "ty"))

        v = Quartz.CGAffineTransformComponents()
        self.assertIsInstance(v.scale, Quartz.CGSize)
        self.assertIsInstance(v.horizontalShear, float)
        self.assertIsInstance(v.rotation, float)
        self.assertIsInstance(v.translation, Quartz.CGVector)

    def testConstants(self):
        self.assertIsInstance(
            Quartz.CGAffineTransformIdentity, Quartz.CGAffineTransform
        )
        self.assertIsInstance(Quartz.CGAffineTransformIdentity.a, float)
        self.assertIsInstance(Quartz.CGAffineTransformIdentity.b, float)
        self.assertIsInstance(Quartz.CGAffineTransformIdentity.c, float)
        self.assertIsInstance(Quartz.CGAffineTransformIdentity.d, float)
        self.assertIsInstance(Quartz.CGAffineTransformIdentity.tx, float)
        self.assertIsInstance(Quartz.CGAffineTransformIdentity.ty, float)

    def testFunctions(self):
        tf = Quartz.CGAffineTransformMake(1.5, 2.5, 3.5, 4.5, 5.5, 6.5)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)
        self.assertEqual(tf.a, 1.5)
        self.assertEqual(tf.b, 2.5)
        self.assertEqual(tf.c, 3.5)
        self.assertEqual(tf.d, 4.5)
        self.assertEqual(tf.tx, 5.5)
        self.assertEqual(tf.ty, 6.5)

        tf = Quartz.CGAffineTransformMakeTranslation(2.5, 3.5)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)
        self.assertEqual(tf.a, 1.0)
        self.assertEqual(tf.b, 0.0)
        self.assertEqual(tf.c, 0.0)
        self.assertEqual(tf.d, 1.0)
        self.assertEqual(tf.tx, 2.5)
        self.assertEqual(tf.ty, 3.5)

        tf = Quartz.CGAffineTransformMakeScale(2.5, 3.5)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)
        self.assertEqual(tf.a, 2.5)
        self.assertEqual(tf.b, 0.0)
        self.assertEqual(tf.c, 0.0)
        self.assertEqual(tf.d, 3.5)
        self.assertEqual(tf.tx, 0.0)
        self.assertEqual(tf.ty, 0.0)

        tf = Quartz.CGAffineTransformMakeRotation(3.4)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)

        self.assertResultHasType(Quartz.CGAffineTransformIsIdentity, objc._C_BOOL)
        self.assertTrue(Quartz.CGAffineTransformIsIdentity(tf) is False)
        self.assertTrue(
            Quartz.CGAffineTransformIsIdentity(Quartz.CGAffineTransformIdentity) is True
        )

        tf = Quartz.CGAffineTransformTranslate(tf, 2.5, 3.5)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)

        tf = Quartz.CGAffineTransformScale(tf, 5.5, 9.5)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)

        tf = Quartz.CGAffineTransformRotate(tf, 0.8)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)

        tf = Quartz.CGAffineTransformInvert(tf)
        self.assertIsInstance(tf, Quartz.CGAffineTransform)

        tf2 = Quartz.CGAffineTransformConcat(
            tf, Quartz.CGAffineTransformMake(1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        )
        self.assertIsInstance(tf2, Quartz.CGAffineTransform)

        self.assertResultHasType(Quartz.CGAffineTransformEqualToTransform, objc._C_BOOL)
        self.assertTrue(Quartz.CGAffineTransformEqualToTransform(tf, tf2) is False)
        self.assertTrue(Quartz.CGAffineTransformEqualToTransform(tf2, tf2) is True)

        pt = Quartz.CGPointApplyAffineTransform((2.5, 3.5), tf)
        self.assertIsInstance(pt, Quartz.CGPoint)

        sz = Quartz.CGSizeApplyAffineTransform((2.5, 3.5), tf)
        self.assertIsInstance(sz, Quartz.CGSize)

        rct = Quartz.CGRectApplyAffineTransform(((2.5, 3.5), (4.5, 5.5)), tf)
        self.assertIsInstance(rct, Quartz.CGRect)

    @min_os_level("13.0")
    def test_functions13_0(self):
        Quartz.CGAffineTransformDecompose
        Quartz.CGAffineTransformMakeWithComponents
