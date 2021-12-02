from Foundation import NSValue
from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCATransform3D(TestCase):
    @min_os_level("10.5")
    def testStructs(self):
        v = Quartz.CATransform3D()
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
        self.assertPickleRoundTrips(v)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.CATransform3DIdentity, Quartz.CATransform3D)

    @min_os_level("10.5")
    def testFunctions(self):
        self.assertResultHasType(Quartz.CATransform3DIsIdentity, objc._C_BOOL)
        v = Quartz.CATransform3DIsIdentity(Quartz.CATransform3DIdentity)
        self.assertTrue(v is True)

        self.assertResultHasType(Quartz.CATransform3DEqualToTransform, objc._C_BOOL)
        v = Quartz.CATransform3DEqualToTransform(
            Quartz.CATransform3DIdentity, Quartz.CATransform3DIdentity
        )
        self.assertTrue(v is True)

        tf1 = Quartz.CATransform3DMakeTranslation(1.0, 2.0, 3.0)
        self.assertIsInstance(tf1, Quartz.CATransform3D)

        tf2 = Quartz.CATransform3DMakeScale(1.0, 2.0, 3.0)
        self.assertIsInstance(tf2, Quartz.CATransform3D)

        tf3 = Quartz.CATransform3DMakeRotation(1.0, 2.0, 3.0, 4.0)
        self.assertIsInstance(tf3, Quartz.CATransform3D)

        tf4 = Quartz.CATransform3DTranslate(tf1, 1.0, 2.0, 3.0)
        self.assertIsInstance(tf4, Quartz.CATransform3D)

        tf5 = Quartz.CATransform3DScale(tf1, 1.0, 2.0, 3.0)
        self.assertIsInstance(tf5, Quartz.CATransform3D)

        tf6 = Quartz.CATransform3DRotate(tf1, 1.0, 2.0, 3.0, 4.0)
        self.assertIsInstance(tf6, Quartz.CATransform3D)

        v = Quartz.CATransform3DConcat(tf1, tf2)
        self.assertIsInstance(v, Quartz.CATransform3D)

        v = Quartz.CATransform3DInvert(tf3)
        self.assertIsInstance(v, Quartz.CATransform3D)

        tf7 = Quartz.CATransform3DMakeAffineTransform(Quartz.CGAffineTransformIdentity)
        self.assertIsInstance(tf7, Quartz.CATransform3D)

        self.assertResultHasType(Quartz.CATransform3DIsAffine, objc._C_BOOL)
        v = Quartz.CATransform3DIsAffine(tf6)
        self.assertTrue(v is False)
        v = Quartz.CATransform3DIsAffine(tf7)
        self.assertTrue(v is True)

        v = Quartz.CATransform3DGetAffineTransform(tf7)
        self.assertIsInstance(v, Quartz.CGAffineTransform)

        self.assertResultHasType(
            NSValue.CATransform3DValue, Quartz.CATransform3D.__typestr__
        )
        self.assertArgHasType(
            NSValue.valueWithCATransform3D_, 0, Quartz.CATransform3D.__typestr__
        )
