from PyObjCTools.TestSupport import TestCase, min_os_level

import GameplayKit

from objc import simd


class TestGKAgent(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKAgentDelegate")

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKAgent3D.rightHanded)
        self.assertArgIsBOOL(GameplayKit.GKAgent3D.setRightHanded_, 0)

        self.assertResultHasType(
            GameplayKit.GKAgent3D.rotation, simd.simd_float3x3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKAgent3D.setRotation_, 0, simd.simd_float3x3.__typestr__
        )

        self.assertResultHasType(
            GameplayKit.GKAgent3D.position, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKAgent3D.setPosition_, 0, simd.vector_float3.__typestr__
        )

        self.assertResultHasType(
            GameplayKit.GKAgent3D.velocity, simd.vector_float3.__typestr__
        )

        self.assertResultHasType(
            GameplayKit.GKAgent2D.position, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKAgent2D.setPosition_, 0, simd.vector_float2.__typestr__
        )

        self.assertResultHasType(
            GameplayKit.GKAgent2D.velocity, simd.vector_float2.__typestr__
        )
