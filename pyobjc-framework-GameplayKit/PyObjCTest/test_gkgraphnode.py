from PyObjCTools.TestSupport import TestCase

import GameplayKit
from objc import simd


class TestGKGraphNode(TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(
            GameplayKit.GKGraphNode.addConnectionsToNodes_bidirectional_, 1
        )
        self.assertArgIsBOOL(
            GameplayKit.GKGraphNode.removeConnectionsToNodes_bidirectional_, 1
        )

        self.assertResultHasType(
            GameplayKit.GKGraphNode2D.position, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGraphNode2D.setPosition, 0, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGraphNode2D.nodeWithPoint_, 0, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGraphNode2D.initWithPoint_, 0, simd.vector_float2.__typestr__
        )

        self.assertResultHasType(
            GameplayKit.GKGraphNode3D.position, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGraphNode3D.setPosition, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGraphNode3D.nodeWithPoint_, 0, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGraphNode3D.initWithPoint_, 0, simd.vector_float3.__typestr__
        )

        self.assertResultHasType(
            GameplayKit.GKGridGraphNode.gridPosition, simd.vector_int2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGridGraphNode.setGridPosition, 0, simd.vector_int2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKGridGraphNode.nodeWithGridPosition,
            0,
            simd.vector_int2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKGridGraphNode.initWithGridPosition_,
            0,
            simd.vector_int2.__typestr__,
        )
