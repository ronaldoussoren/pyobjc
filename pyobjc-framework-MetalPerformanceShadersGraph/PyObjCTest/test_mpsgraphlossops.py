from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphLossOps(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphLossReductionTypeNone, 0)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphLossReductionTypeAxis,
            MetalPerformanceShadersGraph.MPSGraphLossReductionTypeNone,
        )
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphLossReductionTypeSum, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphLossReductionTypeMean, 2)
