
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *
from Quartz import *
from Foundation import NSValue

class TestCATransform3D (TestCase):

    @min_os_level('10.5')
    def testStructs(self):
        v = CATransform3D()
        self.assertIsInstance(v.m11, float)
        self.assertIsInstance(v.m12, float)
        self.assertIsInstance(v.m13, float)
        self.assertIsInstance(v.m14, float)

        self.assertIsInstance(v.m21, float)
        self.assertIsInstance(v.m22, float)
        self.assertIsInstance(v.m23, float)
        self.assertIsInstance(v.m24, float)

        self.assertIsInstance(v.m31, float)
        self.assertIsInstance(v.m32, float)
        self.assertIsInstance(v.m33, float)
        self.assertIsInstance(v.m34, float)

        self.assertIsInstance(v.m41, float)
        self.assertIsInstance(v.m42, float)
        self.assertIsInstance(v.m43, float)
        self.assertIsInstance(v.m44, float)
        

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(CATransform3DIdentity, CATransform3D)

    @min_os_level('10.5')
    def testFunctions(self):
        self.assertResultHasType(CATransform3DIsIdentity, objc._C_BOOL)
        v = CATransform3DIsIdentity(CATransform3DIdentity)
        self.assertTrue(v is True)

        self.assertResultHasType(CATransform3DEqualToTransform, objc._C_BOOL)
        v = CATransform3DEqualToTransform(CATransform3DIdentity, CATransform3DIdentity)
        self.assertTrue(v is True)

        tf1 = CATransform3DMakeTranslation(1.0, 2.0, 3.0)
        self.assertIsInstance(tf1, CATransform3D)

        tf2 = CATransform3DMakeScale(1.0, 2.0, 3.0)
        self.assertIsInstance(tf2, CATransform3D)

        tf3 = CATransform3DMakeRotation(1.0, 2.0, 3.0, 4.0)
        self.assertIsInstance(tf3, CATransform3D)

        tf4 = CATransform3DTranslate(tf1, 1.0, 2.0, 3.0)
        self.assertIsInstance(tf4, CATransform3D)

        tf5 = CATransform3DScale(tf1, 1.0, 2.0, 3.0)
        self.assertIsInstance(tf5, CATransform3D)

        tf6 = CATransform3DRotate(tf1, 1.0, 2.0, 3.0, 4.0)
        self.assertIsInstance(tf6, CATransform3D)

        v = CATransform3DConcat(tf1, tf2)
        self.assertIsInstance(v, CATransform3D)

        v = CATransform3DInvert(tf3)
        self.assertIsInstance(v, CATransform3D)

        tf7 = CATransform3DMakeAffineTransform(CGAffineTransformIdentity)
        self.assertIsInstance(tf7, CATransform3D)

        self.assertResultHasType(CATransform3DIsAffine, objc._C_BOOL)
        v = CATransform3DIsAffine(tf6)
        self.assertTrue(v is False)
        v = CATransform3DIsAffine(tf7)
        self.assertTrue(v is True)

        v = CATransform3DGetAffineTransform(tf7)
        self.assertIsInstance(v, CGAffineTransform)


        self.assertResultHasType(NSValue.CATransform3DValue, CATransform3D.__typestr__)
        self.assertArgHasType(NSValue.valueWithCATransform3D_, 0, CATransform3D.__typestr__)


if __name__ == "__main__":
    main()
