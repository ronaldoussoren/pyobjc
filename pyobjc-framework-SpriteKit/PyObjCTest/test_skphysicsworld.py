from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit
import Quartz
from objc import simd


class TestSKPhysicsWorld(TestCase):
    @min_os_level("10.9")
    def testMethods(self):
        self.assertArgIsBlock(
            SpriteKit.SKPhysicsWorld.enumerateBodiesAtPoint_usingBlock_, 1, b"v@o^Z"
        )
        self.assertArgIsBlock(
            SpriteKit.SKPhysicsWorld.enumerateBodiesInRect_usingBlock_, 1, b"v@o^Z"
        )
        self.assertArgIsBlock(
            SpriteKit.SKPhysicsWorld.enumerateBodiesAlongRayStart_end_usingBlock_,
            2,
            b"v@" + Quartz.CGPoint.__typestr__ + Quartz.CGVector.__typestr__ + b"o^Z",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultHasType(
            SpriteKit.SKPhysicsWorld.sampleFieldsAt_, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            SpriteKit.SKPhysicsWorld.sampleFieldsAt_, 0, simd.vector_float3.__typestr__
        )

        o = SpriteKit.SKPhysicsWorld.alloc().init()
        self.assertArgHasType(o.sampleFieldsAt_, 0, simd.vector_float3.__typestr__)
        v = o.sampleFieldsAt_((9, 10, 11))
        self.assertIsInstance(v, simd.vector_float3)

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("SKPhysicsContactDelegate")
