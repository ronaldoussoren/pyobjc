from PyObjCTools.TestSupport import TestCase, min_os_level

import GameplayKit
from objc import simd


class TestGKMeshGraph(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameplayKit.GKMeshGraphTriangulationMode)

    def testConstants(self):
        self.assertEqual(GameplayKit.GKMeshGraphTriangulationModeVertices, 1 << 0)
        self.assertEqual(GameplayKit.GKMeshGraphTriangulationModeCenters, 1 << 1)
        self.assertEqual(GameplayKit.GKMeshGraphTriangulationModeEdgeMidpoints, 1 << 2)

    @min_os_level("10.12")
    def test_methods(self):
        self.assertArgHasType(
            GameplayKit.GKMeshGraph.graphWithBufferRadius_minCoordinate_maxCoordinate_nodeClass_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKMeshGraph.graphWithBufferRadius_minCoordinate_maxCoordinate_nodeClass_,
            2,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasType(
            GameplayKit.GKMeshGraph.initWithBufferRadius_minCoordinate_maxCoordinate_nodeClass_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKMeshGraph.initWithBufferRadius_minCoordinate_maxCoordinate_nodeClass_,
            2,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasType(
            GameplayKit.GKMeshGraph.graphWithBufferRadius_minCoordinate_maxCoordinate_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKMeshGraph.graphWithBufferRadius_minCoordinate_maxCoordinate_,
            2,
            simd.vector_float2.__typestr__,
        )

        self.assertArgHasType(
            GameplayKit.GKMeshGraph.initWithBufferRadius_minCoordinate_maxCoordinate_,
            1,
            simd.vector_float2.__typestr__,
        )
        self.assertArgHasType(
            GameplayKit.GKMeshGraph.initWithBufferRadius_minCoordinate_maxCoordinate_,
            2,
            simd.vector_float2.__typestr__,
        )

        self.assertResultHasType(
            GameplayKit.GKMeshGraph.triangleAtIndex_, GameplayKit.GKTriangle.__typestr__
        )
