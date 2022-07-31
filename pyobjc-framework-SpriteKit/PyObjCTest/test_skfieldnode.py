from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit
from objc import simd


class TestSKFieldNode(TestCase):
    @min_os_level("10.10")
    def testMethods(self):
        self.assertArgIsBOOL(SpriteKit.SKFieldNode.setEnabled_, 0)
        self.assertResultIsBOOL(SpriteKit.SKFieldNode.isEnabled)
        self.assertArgIsBOOL(SpriteKit.SKFieldNode.setExclusive_, 0)
        self.assertResultIsBOOL(SpriteKit.SKFieldNode.isExclusive)

        self.assertResultHasType(
            SpriteKit.SKFieldNode.direction, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SKFieldNode.setDirection_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SKFieldNode.linearGravityFieldWithVector_,
            0,
            simd.vector_float3.__typestr__,
        )
        self.assertArgHasType(
            SpriteKit.SKFieldNode.velocityFieldWithVector_,
            0,
            simd.vector_float3.__typestr__,
        )

        obj = SpriteKit.SKFieldNode.linearGravityFieldWithVector_((1, 2, 3))
        self.assertIsInstance(obj, SpriteKit.SKFieldNode)
        self.assertIsInstance(obj.direction(), simd.vector_float3)

        obj = SpriteKit.SKFieldNode.velocityFieldWithVector_((1, 2, 3))
        self.assertIsInstance(obj, SpriteKit.SKFieldNode)
        self.assertIsInstance(obj.direction(), simd.vector_float3)

        # FIXME: Requires explicit test as well.
        self.assertArgIsBlock(
            SpriteKit.SKFieldNode.customFieldWithEvaluationBlock_, 0, b"<3f><3f><3f>ffd"
        )

        obj.setDirection_((9, 10, 11))
        self.assertEqual(obj.direction(), simd.vector_float3(9, 10, 11))
