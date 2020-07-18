from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixDecomposition(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSMatrixDecompositionStatusSuccess, 0)
        self.assertEqual(
            MetalPerformanceShaders.MPSMatrixDecompositionStatusFailure, -1
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSMatrixDecompositionStatusSingular, -2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSMatrixDecompositionStatusNonPositiveDefinite, -3
        )

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixDecompositionCholesky.initWithDevice_lower_order_,
            1,
        )
