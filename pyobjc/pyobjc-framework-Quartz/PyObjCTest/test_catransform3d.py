
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *
from Quartz import *
from Foundation import NSValue

class TestCATransform3D (TestCase):

    @min_os_level('10.5')
    def testStructs(self):
        v = CATransform3D()
        self.failUnlessIsInstance(v.m11, float)
        self.failUnlessIsInstance(v.m12, float)
        self.failUnlessIsInstance(v.m13, float)
        self.failUnlessIsInstance(v.m14, float)

        self.failUnlessIsInstance(v.m21, float)
        self.failUnlessIsInstance(v.m22, float)
        self.failUnlessIsInstance(v.m23, float)
        self.failUnlessIsInstance(v.m24, float)

        self.failUnlessIsInstance(v.m31, float)
        self.failUnlessIsInstance(v.m32, float)
        self.failUnlessIsInstance(v.m33, float)
        self.failUnlessIsInstance(v.m34, float)

        self.failUnlessIsInstance(v.m41, float)
        self.failUnlessIsInstance(v.m42, float)
        self.failUnlessIsInstance(v.m43, float)
        self.failUnlessIsInstance(v.m44, float)
        

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(CATransform3DIdentity, CATransform3D)

    @min_os_level('10.5')
    def testFunctions(self):
        self.failUnlessResultHasType(CATransform3DIsIdentity, objc._C_BOOL)
        v = CATransform3DIsIdentity(CATransform3DIdentity)
        self.failUnless(v is True)

        self.failUnlessResultHasType(CATransform3DEqualToTransform, objc._C_BOOL)
        v = CATransform3DEqualToTransform(CATransform3DIdentity, CATransform3DIdentity)
        self.failUnless(v is True)

        tf1 = CATransform3DMakeTranslation(1.0, 2.0, 3.0)
        self.failUnlessIsInstance(tf1, CATransform3D)

        tf2 = CATransform3DMakeScale(1.0, 2.0, 3.0)
        self.failUnlessIsInstance(tf2, CATransform3D)

        tf3 = CATransform3DMakeRotation(1.0, 2.0, 3.0, 4.0)
        self.failUnlessIsInstance(tf3, CATransform3D)

        tf4 = CATransform3DTranslate(tf1, 1.0, 2.0, 3.0)
        self.failUnlessIsInstance(tf4, CATransform3D)

        tf5 = CATransform3DScale(tf1, 1.0, 2.0, 3.0)
        self.failUnlessIsInstance(tf5, CATransform3D)

        tf6 = CATransform3DRotate(tf1, 1.0, 2.0, 3.0, 4.0)
        self.failUnlessIsInstance(tf6, CATransform3D)

        v = CATransform3DConcat(tf1, tf2)
        self.failUnlessIsInstance(v, CATransform3D)

        v = CATransform3DInvert(tf3)
        self.failUnlessIsInstance(v, CATransform3D)

        tf7 = CATransform3DMakeAffineTransform(CGAffineTransformIdentity)
        self.failUnlessIsInstance(tf7, CATransform3D)

        self.failUnlessResultHasType(CATransform3DIsAffine, objc._C_BOOL)
        v = CATransform3DIsAffine(tf6)
        self.failUnless(v is False)
        v = CATransform3DIsAffine(tf7)
        self.failUnless(v is True)

        v = CATransform3DGetAffineTransform(tf7)
        self.failUnlessIsInstance(v, CGAffineTransform)


        self.failUnlessResultHasType(NSValue.CATransform3DValue, CATransform3D.__typestr__)
        self.failUnlessArgHasType(NSValue.valueWithCATransform3D_, 0, CATransform3D.__typestr__)


if __name__ == "__main__":
    main()
