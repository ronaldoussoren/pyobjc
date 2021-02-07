from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSMatrixBatchNormalization(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSMatrixBatchNormalization.computeStatistics
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixBatchNormalization.setComputeStatistics_, 0
        )
