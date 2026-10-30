from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphRandomOps(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphRandomDistribution)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomDistributionUniform, 0
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomDistributionNormal, 1
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomDistributionTruncatedNormal, 2
        )

        self.assertIsEnumType(
            MetalPerformanceShadersGraph.MPSGraphRandomNormalSamplingMethod
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomNormalSamplingInvCDF, 0
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomNormalSamplingBoxMuller, 1
        )
