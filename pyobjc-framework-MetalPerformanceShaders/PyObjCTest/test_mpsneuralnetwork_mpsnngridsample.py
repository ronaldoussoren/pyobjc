from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSNNGridSample(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSNNGridSample.useGridValueAsInputCoordinate
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNNGridSample.setUseGridValueAsInputCoordinate_, 0
        )
