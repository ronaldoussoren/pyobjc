
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGAffineTransform (TestCase):
    def testStruct(self):
        v = CGAffineTransform()
        self.failUnless(hasattr(v, "a"))
        self.failUnless(hasattr(v, "b"))
        self.failUnless(hasattr(v, "c"))
        self.failUnless(hasattr(v, "d"))
        self.failUnless(hasattr(v, "tx"))
        self.failUnless(hasattr(v, "ty"))

    def testConstants(self):
        self.failUnlessIsInstance(CGAffineTransformIdentity, CGAffineTransform)
        self.failUnlessIsInstance(CGAffineTransformIdentity.a, float)
        self.failUnlessIsInstance(CGAffineTransformIdentity.b, float)
        self.failUnlessIsInstance(CGAffineTransformIdentity.c, float)
        self.failUnlessIsInstance(CGAffineTransformIdentity.d, float)
        self.failUnlessIsInstance(CGAffineTransformIdentity.tx, float)
        self.failUnlessIsInstance(CGAffineTransformIdentity.ty, float)

    def testFunctions(self):
        tf = CGAffineTransformMake(1.5, 2.5, 3.5, 4.5, 5.5, 6.5)
        self.failUnlessIsInstance(tf, CGAffineTransform)
        self.failUnlessEqual(tf.a,  1.5)
        self.failUnlessEqual(tf.b,  2.5)
        self.failUnlessEqual(tf.c,  3.5)
        self.failUnlessEqual(tf.d,  4.5)
        self.failUnlessEqual(tf.tx, 5.5)
        self.failUnlessEqual(tf.ty, 6.5)

        tf = CGAffineTransformMakeTranslation(2.5, 3.5)
        self.failUnlessIsInstance(tf, CGAffineTransform)
        self.failUnlessEqual(tf.a,  1.0)
        self.failUnlessEqual(tf.b,  0.0)
        self.failUnlessEqual(tf.c,  0.0)
        self.failUnlessEqual(tf.d,  1.0)
        self.failUnlessEqual(tf.tx, 2.5)
        self.failUnlessEqual(tf.ty, 3.5)

        tf = CGAffineTransformMakeScale(2.5, 3.5)
        self.failUnlessIsInstance(tf, CGAffineTransform)
        self.failUnlessEqual(tf.a,  2.5)
        self.failUnlessEqual(tf.b,  0.0)
        self.failUnlessEqual(tf.c,  0.0)
        self.failUnlessEqual(tf.d,  3.5)
        self.failUnlessEqual(tf.tx, 0.0)
        self.failUnlessEqual(tf.ty, 0.0)

        tf = CGAffineTransformMakeRotation(3.4)
        self.failUnlessIsInstance(tf, CGAffineTransform)

        self.failUnlessResultHasType(CGAffineTransformIsIdentity, objc._C_BOOL)
        self.failUnless(CGAffineTransformIsIdentity(tf) is False)
        self.failUnless(CGAffineTransformIsIdentity(CGAffineTransformIdentity) is True)

        tf = CGAffineTransformTranslate(tf, 2.5, 3.5)
        self.failUnlessIsInstance(tf, CGAffineTransform)

        tf = CGAffineTransformScale(tf, 5.5, 9.5)
        self.failUnlessIsInstance(tf, CGAffineTransform)

        tf = CGAffineTransformRotate(tf, 0.8)
        self.failUnlessIsInstance(tf, CGAffineTransform)

        tf = CGAffineTransformInvert(tf)
        self.failUnlessIsInstance(tf, CGAffineTransform)

        tf2 = CGAffineTransformConcat(tf, 
                CGAffineTransformMake(1.0, 1.0, 1.0, 1.0, 1.0, 1.0))
        self.failUnlessIsInstance(tf2, CGAffineTransform)

        self.failUnlessResultHasType(CGAffineTransformEqualToTransform, objc._C_BOOL)
        self.failUnless(CGAffineTransformEqualToTransform(tf, tf2) is False)
        self.failUnless(CGAffineTransformEqualToTransform(tf2, tf2) is True)

        pt = CGPointApplyAffineTransform((2.5, 3.5), tf)
        self.failUnlessIsInstance(pt, CGPoint)

        sz = CGSizeApplyAffineTransform((2.5, 3.5), tf)
        self.failUnlessIsInstance(sz, CGSize)

        rct = CGRectApplyAffineTransform(((2.5, 3.5), (4.5, 5.5)), tf)
        self.failUnlessIsInstance(rct, CGRect)

if __name__ == "__main__":
    main()
