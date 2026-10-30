from PyObjCTools.TestSupport import TestCase, min_os_level

import GameplayKit

from objc import simd


class TestGKPath(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKAgentDelegate", GameplayKit)

    def test_methods(self):
        self.assertResultIsBOOL(GameplayKit.GKPath.isCyclical)
        self.assertArgIsBOOL(GameplayKit.GKPath.setCyclical_, 0)

        # SIMD
        self.assertArgHasType(
            GameplayKit.GKPath.pathWithPoints_count_radius_cyclical_,
            0,
            b"n^" + simd.vector_float2.__typestr__,
        )
        self.assertArgIsIn(GameplayKit.GKPath.pathWithPoints_count_radius_cyclical_, 0)
        self.assertArgSizeInArg(
            GameplayKit.GKPath.pathWithPoints_count_radius_cyclical_, 0, 1
        )
        self.assertArgIsBOOL(
            GameplayKit.GKPath.pathWithPoints_count_radius_cyclical_, 3
        )

        self.assertArgHasType(
            GameplayKit.GKPath.initWithPoints_count_radius_cyclical_,
            0,
            b"n^" + simd.vector_float2.__typestr__,
        )
        self.assertArgIsIn(GameplayKit.GKPath.initWithPoints_count_radius_cyclical_, 0)
        self.assertArgSizeInArg(
            GameplayKit.GKPath.initWithPoints_count_radius_cyclical_, 0, 1
        )
        self.assertArgIsBOOL(
            GameplayKit.GKPath.initWithPoints_count_radius_cyclical_, 3
        )

        self.assertResultHasType(
            GameplayKit.GKPath.pointAtIndex_, simd.vector_float2.__typestr__
        )

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertArgHasType(
            GameplayKit.GKPath.pathWithFloat3Points_count_radius_cyclical_,
            0,
            b"n^" + simd.vector_float3.__typestr__,
        )
        self.assertArgIsIn(
            GameplayKit.GKPath.pathWithFloat3Points_count_radius_cyclical_, 0
        )
        self.assertArgSizeInArg(
            GameplayKit.GKPath.pathWithFloat3Points_count_radius_cyclical_, 0, 1
        )
        self.assertArgIsBOOL(
            GameplayKit.GKPath.pathWithFloat3Points_count_radius_cyclical_, 3
        )

        self.assertArgHasType(
            GameplayKit.GKPath.initWithFloat3Points_count_radius_cyclical_,
            0,
            b"n^" + simd.vector_float3.__typestr__,
        )
        self.assertArgIsIn(
            GameplayKit.GKPath.initWithFloat3Points_count_radius_cyclical_, 0
        )
        self.assertArgSizeInArg(
            GameplayKit.GKPath.initWithFloat3Points_count_radius_cyclical_, 0, 1
        )
        self.assertArgIsBOOL(
            GameplayKit.GKPath.initWithFloat3Points_count_radius_cyclical_, 3
        )

        self.assertResultHasType(
            GameplayKit.GKPath.float2AtIndex_, simd.vector_float2.__typestr__
        )
        self.assertResultHasType(
            GameplayKit.GKPath.float3AtIndex_, simd.vector_float3.__typestr__
        )
