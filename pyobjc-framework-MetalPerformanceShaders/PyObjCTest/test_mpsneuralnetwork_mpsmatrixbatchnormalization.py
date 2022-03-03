from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSMatrixBatchNormalization(TestCase):
    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSMatrixBatchNormalization.computeStatistics
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixBatchNormalization.setComputeStatistics_, 0
        )
