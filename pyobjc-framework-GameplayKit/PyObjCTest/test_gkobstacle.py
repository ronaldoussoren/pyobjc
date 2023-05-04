from PyObjCTools.TestSupport import TestCase, min_os_level
import GameplayKit  # noqa: F401
from objc import simd


class TestGKObstacle(TestCase):
    def testMethods(self):
        self.assertResultHasType(
            GameplayKit.GKCircleObstacle.position, simd.vector_float2.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKCircleObstacle.setPosition_, 0, simd.vector_float2.__typestr__
        )

        self.assertArgHasType(
            GameplayKit.GKPolygonObstacle.obstacleWithPoints_count_,
            0,
            b"n^" + simd.vector_float2.__typestr__,
        )
        self.assertArgIsIn(GameplayKit.GKPolygonObstacle.obstacleWithPoints_count_, 0)
        self.assertArgSizeInArg(
            GameplayKit.GKPolygonObstacle.obstacleWithPoints_count_, 0, 1
        )

        self.assertArgHasType(
            GameplayKit.GKPolygonObstacle.initWithPoints_count_,
            0,
            b"n^" + simd.vector_float2.__typestr__,
        )
        self.assertArgIsIn(GameplayKit.GKPolygonObstacle.initWithPoints_count_, 0)
        self.assertArgSizeInArg(
            GameplayKit.GKPolygonObstacle.initWithPoints_count_, 0, 1
        )

        self.assertResultHasType(
            GameplayKit.GKPolygonObstacle.vertexAtIndex_, simd.vector_float2.__typestr__
        )

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertResultHasType(
            GameplayKit.GKSphereObstacle.position, simd.vector_float3.__typestr__
        )
        self.assertArgHasType(
            GameplayKit.GKSphereObstacle.setPosition_, 0, simd.vector_float3.__typestr__
        )
