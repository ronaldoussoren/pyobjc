from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSMatrixSum(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixSum.initWithDevice_count_rows_columns_transpose_,
            4,
        )
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSMatrixSum.transpose)
