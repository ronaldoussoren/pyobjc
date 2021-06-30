from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphLossOps(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphLossReductionTypeAxis, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphLossReductionTypeSum, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphLossReductionTypeMean, 2)
