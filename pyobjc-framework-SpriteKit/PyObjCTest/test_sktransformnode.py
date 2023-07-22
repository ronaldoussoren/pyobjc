from PyObjCTools.TestSupport import TestCase, min_os_level
from objc import simd

import SpriteKit


class TestSKTransformNode(TestCase):
    @min_os_level("10.13")
    def testMethods(self):
        self.assertResultHasType(
            SpriteKit.SKTransformNode.eulerAngles, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SKTransformNode.setEulerAngles_, 0, simd.simd_float3.__typestr__
        )

        self.assertResultHasType(
            SpriteKit.SKTransformNode.rotationMatrix, simd.simd_float3x3.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SKTransformNode.setRotationMatrix_,
            0,
            simd.simd_float3x3.__typestr__,
        )

        self.assertResultHasType(
            SpriteKit.SKTransformNode.quaternion, simd.simd_quatf.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SKTransformNode.setQuaternion_, 0, simd.simd_quatf.__typestr__
        )
