from PyObjCTools.TestSupport import TestCase

import GameplayKit
from objc import simd


class TestGKNoiseMap(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKNoiseMap.isSeamless)
        # self.assertArgIsBOOL(GameplayKit.GKNoiseMap.setSeamless_, 0)

        self.assertResultIsHasType(
            GameplayKit.GKNoiseMap.size, simd.vector_double2.__typestr__
        )
        self.assertResultIsHasType(
            GameplayKit.GKNoiseMap.origin, simd.vector_double2.__typestr__
        )
        self.assertResultIsHasType(
            GameplayKit.GKNoiseMap.sampleCount, simd.vector_int2.__typestr__
        )

        self.assertArgIsHasType(
            GameplayKit.GKNoiseMap.noiseMapWithNoise_size_origin_sampleCount_seamless_,
            1,
            simd.vector_double2.__typestr__,
        )
        self.assertArgIsBOOL(
            GameplayKit.GKNoiseMap.noiseMapWithNoise_size_origin_sampleCount_seamless_,
            4,
        )

        self.assertArgIsHasType(
            GameplayKit.GKNoiseMap.initWithNoise_size_origin_sampleCount_seamless_,
            1,
            simd.vector_double2.__typestr__,
        )
        self.assertArgIsBOOL(
            GameplayKit.GKNoiseMap.initWithNoise_size_origin_sampleCount_seamless_, 4
        )

        self.assertArgIsHasType(
            GameplayKit.GKNoiseMap.valueAtPosition_, 0, simd.vector_int2.__typestr__
        )
        self.assertArgIsHasType(
            GameplayKit.GKNoiseMap.interpolatedValueAtPosition_,
            0,
            simd.vector_float2.__typestr__,
        )
        self.assertArgIsHasType(
            GameplayKit.GKNoiseMap.setValue_atPosition_, 1, simd.vector_int2.__typestr__
        )
