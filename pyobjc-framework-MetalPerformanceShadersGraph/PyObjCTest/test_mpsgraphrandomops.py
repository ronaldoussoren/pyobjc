from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphRandomOps(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphRandomDistribution)
        self.assertIsEnumType(
            MetalPerformanceShadersGraph.MPSGraphRandomNormalSamplingMethod
        )

    def test_constants(self):
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomDistributionUniform, 0
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomDistributionNormal, 1
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomDistributionTruncatedNormal, 2
        )

        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomNormalSamplingInvCDF, 0
        )
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRandomNormalSamplingBoxMuller, 1
        )
