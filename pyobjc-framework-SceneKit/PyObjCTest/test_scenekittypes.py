import objc
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
    expectedFailure,
)

import SceneKit


class TestSceneKitTypes(TestCase):
    def testTypes(self):
        v = SceneKit.SCNVector3()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)

        v = SceneKit.SCNVector4()
        self.assertIsInstance(v.x, float)
        self.assertIsInstance(v.y, float)
        self.assertIsInstance(v.z, float)
        self.assertIsInstance(v.w, float)

        self.assertTrue(SceneKit.SCNQuaternion is SceneKit.SCNVector4)
        self.assertTrue(SceneKit.SCNMatrix4 is SceneKit.CATransform3D)

    def testConstants(self):
        self.assertEqual(SceneKit.SCNProgramCompilationError, 1)

        self.assertEqual(SceneKit.SCNActionTimingModeLinear, 0)
        self.assertEqual(SceneKit.SCNActionTimingModeEaseIn, 1)
        self.assertEqual(SceneKit.SCNActionTimingModeEaseOut, 2)
        self.assertEqual(SceneKit.SCNActionTimingModeEaseInEaseOut, 3)

        self.assertEqual(SceneKit.SCNColorMaskNone, 0)
        self.assertEqual(SceneKit.SCNColorMaskRed, 0x1 << 3)
        self.assertEqual(SceneKit.SCNColorMaskGreen, 0x1 << 2)
        self.assertEqual(SceneKit.SCNColorMaskBlue, 0x1 << 1)
        self.assertEqual(SceneKit.SCNColorMaskAlpha, 0x1 << 0)
        self.assertEqual(SceneKit.SCNColorMaskAll, 0xF)

    @expectedFailureIf(os_release().rsplit(".", 1)[0] == "10.10")
    @min_os_level("10.10")
    def testConstantsFail10_10(self):
        self.assertIsInstance(SceneKit.SCNErrorDomain, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(SceneKit.SCNMatrix4Identity, SceneKit.SCNMatrix4)
        self.assertIsInstance(SceneKit.SCNVector3Zero, SceneKit.SCNVector3)
        self.assertIsInstance(SceneKit.SCNVector4Zero, SceneKit.SCNVector4)

    @min_os_level("10.10")
    def testFunctions(self):
        self.assertResultHasType(SceneKit.SCNVector3EqualToVector3, objc._C_BOOL)
        self.assertResultHasType(SceneKit.SCNVector4EqualToVector4, objc._C_BOOL)

        v = SceneKit.SCNVector3Make(1, 2, 3)
        self.assertIsInstance(v, SceneKit.SCNVector3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

        v = SceneKit.SCNVector4Make(1, 2, 3, 4)
        self.assertIsInstance(v, SceneKit.SCNVector4)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)
        self.assertEqual(v.w, 4)

        v = SceneKit.SCNMatrix4MakeTranslation(1, 2, 3)
        self.assertIsInstance(v, SceneKit.SCNMatrix4)
        self.assertEqual(v.m41, 1)
        self.assertEqual(v.m42, 2)
        self.assertEqual(v.m43, 3)

        v = SceneKit.SCNMatrix4MakeScale(1, 2, 3)
        self.assertIsInstance(v, SceneKit.SCNMatrix4)
        self.assertEqual(v.m11, 1)
        self.assertEqual(v.m22, 2)
        self.assertEqual(v.m33, 3)

        w = SceneKit.SCNMatrix4Translate(v, 6, 7, 8)
        self.assertIsInstance(w, SceneKit.SCNMatrix4)

    @expectedFailure
    def testFunctions_unsupported(self):
        # XXX
        SceneKit.SCNVector3FromGLKVector3
        SceneKit.SCNVector3ToGLKVector3
        SceneKit.SCNVector4FromGLKVector4
        SceneKit.SCNVector4ToGLKVector4

    @min_os_level("10.10")
    def testFunctions10_10(self):
        v = SceneKit.SCNMatrix4MakeRotation(1, 2, 3, 4)
        self.assertIsInstance(v, SceneKit.SCNMatrix4)

        v = SceneKit.SCNMatrix4Scale(v, 1, 2, 3)
        self.assertIsInstance(v, SceneKit.SCNMatrix4)

        v = SceneKit.SCNMatrix4Rotate(v, 1, 2, 3, 4)
        self.assertIsInstance(v, SceneKit.SCNMatrix4)

        v = SceneKit.SCNMatrix4Invert(v)
        self.assertIsInstance(v, SceneKit.SCNMatrix4)

        v = SceneKit.SCNMatrix4Invert(v)
        self.assertIsInstance(v, SceneKit.SCNMatrix4)

        self.assertResultHasType(SceneKit.SCNMatrix4IsIdentity, objc._C_BOOL)
        self.assertResultHasType(SceneKit.SCNMatrix4EqualToMatrix4, objc._C_BOOL)

    @min_os_level("10.10")
    @expectedFailure
    def testFunctions10_10_unsup(self):
        # vector types
        SceneKit.SCNMatrix4ToGLKMatrix4
        SceneKit.SCNMatrix4FromGLKMatrix4

        self.assertTrue(
            SceneKit.GLKMatrix4FromCATransform3D is SceneKit.SCNMatrix4ToGLKMatrix4
        )
        self.assertTrue(
            SceneKit.GLKMatrix4ToCATransform3D is SceneKit.SCNMatrix4FromGLKMatrix4
        )
