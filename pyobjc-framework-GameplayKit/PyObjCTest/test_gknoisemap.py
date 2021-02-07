from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKNoiseMap(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKNoiseMap.isSeamless)
        # self.assertArgIsBOOL(GameplayKit.GKNoiseMap.setSeamless_, 0)

        # SIMD:
        # self.assertArgIsBOOL(GameplayKit.GKNoiseMap.noiseMapWithNoise_size_origin_sampleCount_seamless_, 4)
        # self.assertArgIsBOOL(GameplayKit.GKNoiseMap.initWithNoise_size_origin_sampleCount_seamless_, 4)
